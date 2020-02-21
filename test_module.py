import re
from copy import deepcopy

from default_data import end_statement, space_statement, standard_rules
from mongo_handler import get_mongo, set_mongo, get_mongo_param
from utils import Bug, Lexem, ExprLexem, ParentVar, tab_to_space, get_whole_line


class TestModule():

    def __init__(self, language="python", indents=True, mongo_address="mongodb://localhost:27017/", current_id=1,
                 logfile=None):
        self.language = language
        self.indents = indents
        self.mongo_address = mongo_address
        self.logfile = logfile
        self.current_id = current_id

    def start_testing_process(self, filename, version="1.0.0", author="", space_in_tab=4, db="python",
                              tokens_collection="tokens",
                              rules_collection="rules", db_bugs="bug_tracking", bugs_collection="bugs",
                              list_bad_tokens=['undefined', ], deal_rewrite={'rewrite': True}, rules='PEP8',
                              show_on_screen=False, add_to_db=True, logfile=None):
        if not logfile:
            logfile = self.logfile

        if not db:
            db = self.language

        if not deal_rewrite:
            deal_rewrite = {'rewrite': False, 'check_on_rewrite': '', 'hint_fields': ''}
        else:
            if not 'rewrite' in deal_rewrite.keys():
                deal_rewrite['rewrite'] = False
            if not 'check_on_rewrite' in deal_rewrite.keys():
                deal_rewrite['check_on_rewrite'] = ''
            if not 'hint_fields' in deal_rewrite.keys():
                deal_rewrite['hint_fields'] = ''

        if not deal_rewrite:
            self.current_id = get_mongo_param(help_fields={"program": filename})

        with open(filename) as file:
            data = file.read()
            tokenizer = Tokenizer(data, current_bug_id=self.current_id, logfile=logfile)

        self.current_tokens = get_mongo(mongo_address=self.mongo_address, mongo_db=db,
                                        mongo_collection=tokens_collection, logfile=logfile)
        self.current_tokens.sort(key=lambda x: x.prior)
        tokenizer.get_tokens(self.current_tokens)
        tokenizer.find_bad_tokens(list_bad_tokens)

        # for item in tokenizer.lexems:
        #     print('line: ' + str(item.line) + ' ; column: ' + str(item.column) + ': ' + str(
        #         item.name) + ' - ' + item.obj)

        bugs = tokenizer.bugs

        self.current_rules = get_mongo(mongo_address=self.mongo_address, mongo_db=db, mongo_collection=rules_collection,
                                       logfile=logfile)
        parser = Parser(tokenizer.lexems, self.current_rules, end_statement[self.language], self.indents,
                        space_in_tab=space_in_tab, language=self.language, current_bug_id=tokenizer.current_bug_id)
        parser.get_statements([], [], {}, {}, 0)

        # for item in parser.exprs:
        #     print("Object:" + item.lexem.obj + " on line:" + str(item.expr_line) + " on pos:" + str(item.expr_pos))
        #     print("Meaning:")
        #     if item.role:
        #         print(item.role)
        #     print("Place:" + str(item.place))
        #     print("\n\n\n")
        for item in parser.bugs:
            bugs.append(item)

        parser.append_parents()
        df = df_maker(parser.exprs, constructs=parser.constructs, logfile=logfile)
        du = du_maker(parser.exprs, df=df, logfile=logfile)
        for item in du_testing(parser.exprs, df=df, du=du, current_id=parser.current_bug_id, logfile=logfile):
            bugs.append(item)

        current_id = item.id

        for item in style_testing(exprs=parser.exprs, df=df, du=du, rule=rules, current_id=current_id, language=self.language, indents=self.indents, logfile=logfile):
            bugs.append(item)
        for bug in bugs:
            bug.author = author
            bug.program = filename
            bug.version = version
            print(bug.object, bug.line, bug.column, bug.description)

        set_mongo(self.mongo_address, db_bugs, bugs_collection, tokenizer.bugs, rewrite=deal_rewrite['rewrite'],
                  check_on_rewrite=deal_rewrite["check_on_rewrite"], hint_fields=deal_rewrite["hint_fields"],
                  logfile=logfile)


class Tokenizer:
    def __init__(self, text, current_bug_id=0, logfile=None):
        self.text = text
        self.current_bug_id = current_bug_id
        self.logfile = logfile

        self.lexems = []  # results
        self.cur_pos = 0
        self.line = 1
        self.column = 1
        self.length = len(self.text)
        self.bugs = []  # lexical bugs

    def find_bad_tokens(self, list_bad_tokens):
        for item in self.lexems:
            if item.name in list_bad_tokens:
                self.bugs.append(
                    Bug(self.current_bug_id, item.obj, item.line, item.column,
                        "The unexpected symbols (name=%s)" % item.name, priority=3, important=3))
                self.current_bug_id += 1

    def get_tokens(self, token_list):

        while self.cur_pos < self.length:
            temp_lexem = Lexem()
            comparisons = 0
            for item in token_list:
                comparisons += 1
                p = re.search(item.reg, self.text[self.cur_pos:])

                if p and p.start() == 0:
                    temp_lexem = Lexem(p.group(0), item.name, [], self.cur_pos, self.line, self.column)
                    good = False
                    # CHECK PREVIOUS (LEFT) SYMBOLS OF LEXEM
                    if item.leftborder and self.cur_pos > 0:
                        for allows in item.leftborder.allow_symbols:
                            if len(allows) > self.cur_pos:
                                continue

                            if allows == self.text[self.cur_pos - len(allows):self.cur_pos]:
                                if item.leftborder.their_dict and allows in item.leftborder.their_dict.keys():
                                    temp_lexem.role = item.leftborder.their_dict[allows]
                                    temp_lexem.obj = allows + temp_lexem.obj
                                    temp_lexem.pos -= len(allows)

                                good = True
                                break
                    else:
                        good = True

                    if not good:
                        continue
                    else:
                        good = False

                    # CHECK NEXT (RIGHT) SYMBOLS AFTER LEXEM
                    if item.rightborder and self.cur_pos + len(temp_lexem.obj) < len(self.text):
                        for allows in item.rightborder.allow_symbols:

                            if allows == self.text[
                                         self.cur_pos + len(temp_lexem.obj):self.cur_pos + len(
                                             temp_lexem.obj) + len(
                                             allows)]:
                                if item.rightborder.their_dict and allows in item.rightborder.their_dict.keys():
                                    temp_lexem.role = item.rightborder.their_dict[allows]
                                    temp_lexem.obj += allows

                                good = True
                                break
                    else:
                        good = True

                    if good:
                        comparisons = 0
                        break

            if (comparisons >= len(token_list)):
                temp_lexem = Lexem(self.text[self.cur_pos:self.cur_pos + 1], "unknown", [], self.cur_pos,
                                   self.line,
                                   self.column)
                self.bugs.append(
                    Bug(self.current_bug_id, self.text[self.cur_pos:self.cur_pos + 1], self.line, self.column,
                        "The symbol with bad left or right borders", important=2, priority=2, type="bug"))
                self.current_bug_id += 1

            self.cur_pos = temp_lexem.pos + len(temp_lexem.obj)
            self.lexems.append(temp_lexem)

            for char in temp_lexem.obj:
                if char == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1

class Parser:
    def __init__(self, lexems, expr_list, ends, indents=True, space_in_tab=4, language='python', current_bug_id=0,
                 logfile=None):
        self.lexems = deepcopy(lexems)  # All lexems gotten from tokenizer
        self.current_bug_id = current_bug_id

        self.exprs = []  # All combined by rules lexems gotten from this parser
        self.cur_pos = 0  # Counter of current lexem
        self.expr_line = 1  # Counter of expressions
        self.expr_pos = 0  # Counter of expression position
        self.special_cond = None
        self.special_item = None
        self.cur_line = 0

        self.indents = indents
        self.prev_indent = [""]
        self.cur_indent = ""
        self.start_indent = True

        if expr_list:
            self.expr_list = deepcopy(expr_list)
        else:
            self.expr_list = []

        if ends:
            self.ends = ends
        else:
            self.ends = []

        self.ignore = False

        self.space_in_tab = space_in_tab
        self.language = language
        self.logfile = logfile

        self.bugs = []
        self.constructs = []

    def check_cond(self):
        if self.lexems[self.cur_pos].name in self.ends:
            self.expr_line += 1
            self.expr_pos = 0
            return True

    def append_parents(self, keywords=['func', 'class', 'for', 'while', 'if', 'else']):
        for expr in self.exprs:
            if expr.role:
                for pos_role, role in expr.role.items():
                    buf_role = None
                    for item in keywords:
                        if item in role:
                            buf_role = item
                            break
                    if buf_role:
                        for construct in self.constructs:
                            if construct.start == expr.expr_line + 1:
                                construct.role = buf_role
                                break
                        break

    def get_statements(self, allow_tokens, final_words, role={}, ignores=None, level=0, could_be_end=None,
                       check_could_be_end=None):
        '''
        allow_tokens - tokens which could be found in current expressions. If we meet token not from this list, then
        we should leave out current expression.
        final_words - tokens which should be final in current expressions.
        level - the nesting level.
        role - role of tokens of current expression.
        '''
        ignore_final = False

        while self.cur_pos < len(self.lexems) and (
                (level == 0 or not allow_tokens or self.lexems[self.cur_pos].name in allow_tokens) and (
                not final_words or not self.lexems[self.cur_pos].name in final_words) or ignore_final):
            self.cur_line = self.lexems[self.cur_pos].line
            ignore_final = False
            should_ignore = False
            result = False

            if could_be_end:
                if check_could_be_end:
                    if self.lexems[self.cur_pos].name in check_could_be_end:
                        pass
                    elif self.lexems[self.cur_pos].name == could_be_end:
                        if self.indents:
                            could_be_end = False  # if the end of expression depends on indents then we avoid condition on "If could_be_end is None"
                        else:
                            could_be_end = None
                    else:
                        self.expr_line += 1
                        self.expr_pos = 0
                        check_could_be_end = False
                else:
                    if self.lexems[self.cur_pos].name == could_be_end:
                        could_be_end = None

            # If we are not in inner statement (like (,[,{ etc) and meet some token of the end then we should firstly check special property of this token and add count of expressions
            if ignores and self.lexems[self.cur_pos].name in ignores.keys():
                buf_length = self.cur_pos - 1
                while buf_length > 1 and self.lexems[buf_length].name in space_statement[self.language]:
                    buf_length -= 1
                if self.lexems[buf_length].name in ignores[self.lexems[self.cur_pos].name]:
                    should_ignore = True

            if not should_ignore:
                # if language with indents then we should check every line
                if self.indents:
                    if self.lexems[self.cur_pos].name == 'newline':
                        self.start_indent = True
                    elif self.start_indent and self.lexems[self.cur_pos].name in space_statement[self.language]:
                        self.cur_indent += self.lexems[self.cur_pos].obj
                    elif self.start_indent:
                        if len(tab_to_space(self.cur_indent, self.space_in_tab)) % self.space_in_tab != 0:
                            self.bugs.append(
                                Bug(self.current_bug_id, "",
                                    self.lexems[self.cur_pos].line,
                                    self.lexems[self.cur_pos].column,
                                    "Bad amount of blank symbols of indent", important=3, priority=3,
                                    type="warning"))
                            self.current_bug_id += 1

                        if len(tab_to_space(self.cur_indent, self.space_in_tab)) < len(
                                tab_to_space(self.prev_indent[len(self.prev_indent) - 1],
                                             self.space_in_tab)) and level > 0:

                            if len(self.prev_indent) > 1:
                                self.prev_indent.pop(len(self.prev_indent) - 1)

                            # Here is some code for changing places and roles of old lexems
                            verse_pos = self.cur_pos - 1
                            while (verse_pos >= 0 and self.exprs[verse_pos].expr_line == self.expr_line):
                                self.exprs[verse_pos].place -= 1

                                self.exprs[verse_pos].role.pop(1)
                                buf_dict = {}
                                for k in self.exprs[verse_pos].role.keys():
                                    buf_dict[k - 1] = self.exprs[verse_pos].role[k]

                                self.exprs[verse_pos].role = deepcopy(buf_dict)
                                verse_pos -= 1
                            ##############
                            break
                        else:
                            if len(tab_to_space(self.cur_indent, self.space_in_tab)) > len(
                                    tab_to_space(self.prev_indent[len(self.prev_indent) - 1],
                                                 self.space_in_tab)) and level > 0:
                                self.prev_indent.append("")
                            elif len(tab_to_space(self.cur_indent, self.space_in_tab)) > len(
                                    tab_to_space(self.prev_indent[len(self.prev_indent) - 1],
                                                 self.space_in_tab)):
                                self.bugs.append(
                                    Bug(self.current_bug_id, "",
                                        self.lexems[self.cur_pos].line,
                                        self.lexems[self.cur_pos].column,
                                        "Bad indent", important=3, priority=3,
                                        type="bug"))
                                self.current_bug_id += 1
                            self.prev_indent[len(self.prev_indent) - 1] = self.cur_indent
                            self.cur_indent = ""
                            self.start_indent = False

            self.expr_pos += 1

            for item in self.expr_list:
                if should_ignore:
                    continue

                if self.lexems[self.cur_pos].name in item.keyword:
                    self.exprs.append(
                        ExprLexem(self.lexems[self.cur_pos], self.expr_line, self.expr_pos, level, role))

                    result = self.check_cond()

                    # Here is some code for item which roles affect on previous items
                    if item.visa_verse:
                        verse_pos = self.cur_pos - 1
                        was_verse = False
                        special_end = ""
                        if self.exprs[verse_pos].role:
                            for placing, roling in self.exprs[verse_pos].role.items():
                                if 'bracket' in roling:
                                    special_end = ","
                                    break

                        while (verse_pos >= 0 and self.exprs[verse_pos].expr_line == self.expr_line and self.exprs[
                            verse_pos].place >= self.exprs[self.cur_pos].place and (
                                       not special_end or self.exprs[verse_pos].lexem.obj != special_end)):
                            if not self.exprs[verse_pos].lexem.name in space_statement[self.language]:
                                was_verse = True
                            if item.visa_verse_tokens and not self.exprs[
                                                                  verse_pos].lexem.name in item.visa_verse_tokens:
                                self.bugs.append(
                                    Bug(self.current_bug_id, self.exprs[verse_pos].lexem.obj,
                                        self.exprs[verse_pos].lexem.line,
                                        self.exprs[verse_pos].lexem.column,
                                        "Left right of expression doesn't correspond to rule", important=3, priority=3,
                                        type="warning"))
                                self.current_bug_id += 1
                            elif not item.visa_verse_tokens and allow_tokens and not self.exprs[
                                                                                         verse_pos].lexem.name in allow_tokens:
                                self.bugs.append(
                                    Bug(self.current_bug_id, self.exprs[verse_pos].lexem.obj,
                                        self.exprs[verse_pos].lexem.line,
                                        self.exprs[verse_pos].lexem.column,
                                        "Left right of expression doesn't correspond to rule", important=3, priority=3,
                                        type="warning"))
                                self.current_bug_id += 1
                            verse_pos -= 1

                        if was_verse:
                            buf_counter = 1
                            verse_pos += 1
                            # print(self.lexems[self.cur_pos].name, self.lexems[self.cur_pos].obj, self.lexems[self.cur_pos].line)

                            while self.cur_pos > verse_pos:
                                if not self.exprs[verse_pos].role:
                                    self.exprs[verse_pos].role = {}
                                buf_level = self.exprs[verse_pos].place + 1
                                self.exprs[verse_pos].role[buf_level] = deepcopy(item.visa_verse)
                                self.exprs[verse_pos].place = buf_level
                                buf_counter += 1
                                verse_pos += 1
                    #########

                    # Do new nodes
                    role_buf = deepcopy(role)
                    if not role_buf:
                        role_buf = {}
                    if item.role:
                        role_buf[level + 1] = deepcopy(item.role)

                    final_words_buf_list = deepcopy(item.final_words)
                    if item.use_parent_final:
                        if item.final_words:
                            for word in final_words:
                                if not word in final_words_buf_list:
                                    final_words_buf_list.append(word)
                        else:
                            final_words_buf_list = deepcopy(final_words)

                    self.cur_pos += 1

                    #Get expression number for inner structures
                    buf_construct = None
                    if 'body' in item.role:
                        buf_construct = ParentVar("", self.expr_line + 1, 0, "")

                    #Go deeper
                    self.get_statements(item.allow_tokens, final_words_buf_list, role_buf, item.ignore_symbols,
                                        level + 1, item.could_be_end, item.check_could_be_end)

                    if buf_construct:
                        buf_construct.end = self.expr_line - 1
                        self.constructs.append(buf_construct)
                    ##############

                    if item.inner and self.lexems[self.cur_pos].name in item.final_words:
                        ignore_final = True

                    break
            else:

                self.exprs.append(ExprLexem(self.lexems[self.cur_pos], self.expr_line, self.expr_pos, level, role))

                if not should_ignore:
                    result = self.check_cond()

                self.cur_pos += 1

            if result and level > 0 and could_be_end is None:
                break

        if final_words and self.cur_pos < len(self.lexems):
            if not self.lexems[self.cur_pos].name in final_words:
                self.bugs.append(
                    Bug(self.current_bug_id, self.lexems[self.cur_pos].obj,
                        self.lexems[self.cur_pos].line,
                        self.lexems[self.cur_pos].column,
                        "The end of expression doesn't correspond to rule", important=3, priority=3,
                        type="Warning"))
                self.current_bug_id += 1

def style_testing(exprs=[], df=[], du=[], rule='PEP8', current_id=0, language='python', indents=True, logfile=None):
    current_rules = standard_rules[rule]
    bugs = []
    for item in current_rules:

        if item['check'] == 'length':
            all_length = 0
            temp_obj = ""
            temp_line = 1
            for expr in exprs:
                for char in expr.lexem.obj:
                    all_length += 1
                    temp_obj += char
                    if char == '\n':
                        if all_length > item['size']:
                            bugs.append(Bug(current_id, temp_obj, temp_line, all_length,
                                            item['Description'] + ' The current length is %s' % all_length))
                            current_id += 1
                        all_length = 0
                        temp_line += 1
                        temp_obj = ""
        elif item['check'] == 'var_names':
            cur_level_class = 0
            cur_level_func = 0
            was_class = False
            was_func = False

            for var in df:
                if var['mean'] in item['class']['hint'] and (not re.search(item['class']['reg'], var['expr'].lexem.obj) or len(
                            re.search(item['class']['reg'], var['expr'].lexem.obj).group(0)) != len(var['expr'].lexem.obj)):
                    bugs.append(Bug(current_id, var['expr'].lexem.obj, var['expr'].lexem.line, var['expr'].lexem.column,
                                    item['class']['Description']))
                    current_id += 1
                if var['mean'] in item['func']['hint'] and (not re.search(item['func']['reg'], var['expr'].lexem.obj) or len(
                            re.search(item['func']['reg'], var['expr'].lexem.obj).group(0)) != len(var['expr'].lexem.obj)):
                    bugs.append(Bug(current_id, var['expr'].lexem.obj, var['expr'].lexem.line, var['expr'].lexem.column,
                                    item['func']['Description']))
                    current_id += 1
        elif item['check'] == 'avoid_names':
            for expr in exprs:
                if expr.lexem.name in item['hint']:
                    if re.search(item['letters'], expr.lexem.obj) and len(
                            re.search(item['letters'], expr.lexem.obj).group(0)) == len(expr.lexem.obj):
                        bugs.append(Bug(current_id, expr.lexem.obj, expr.lexem.line, expr.lexem.column,
                                        item['Description']))
                        current_id += 1
        elif item['check'] == 'constants':
            consts = []
            not_consts = {}
            not_consts_list = []
            for var in df:
                if var['mean'] in item['hint'] and not var['parent']:
                    if re.search(item['look'], var['expr'].lexem.obj) and len(re.search(item['look'], var['expr'].lexem.obj).group(0)) == len(var['expr'].lexem.obj):
                        for const in consts:
                            if var['expr'].lexem.obj == const.lexem.obj:
                                bugs.append(Bug(current_id, var['expr'].lexem.obj, const.lexem.line, const.lexem.column,
                                                item['Description_false_const'] + "line: " + str(
                                                    var['expr'].lexem.line) + " column " + str(var['expr'].lexem.column)))
                                current_id += 1
                                break
                        else:
                            consts.append(var['expr'])
                    else:
                        if var['expr'].lexem.obj in not_consts.keys():
                            not_consts[var['expr'].lexem.obj] += 1
                        else:
                            not_consts[var['expr'].lexem.obj] = 0
                            not_consts_list.append(var['expr'])

            for key, value in not_consts.items():
                if value == 0:
                    for not_const in not_consts_list:
                        if not_const.lexem.obj == key:
                            bugs.append(Bug(current_id, key, not_const.lexem.line, not_const.lexem.column, item['Description_const']))
                            current_id += 1
                            break
        elif item['check'] == 'newlines':
            newlines = 0
            was = True
            for expr in exprs:
                if expr.lexem.name in item['hint']:
                    newlines += 1
                    was = True
                elif expr.lexem.name in space_statement:
                    pass
                elif was:
                    buf_expr_line = expr.expr_line

                    cur_line = get_whole_line(exprs, expr)

                    for var in df:
                        if var['expr'].expr_line == buf_expr_line and var['mean'] in item.keys():
                            has_parent = False
                            if var['parent']:
                                has_parent = True

                            if 'parent' in item[var['mean']].keys():

                                if item[var['mean']]['parent'][has_parent] < newlines:
                                    bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column, item['Description_more'] + str(newlines) + " lines."))
                                    current_id += 1
                                    break
                                elif item[var['mean']]['parent'][has_parent] > newlines:
                                    bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column, item['Description_less'] + str(newlines) + " lines."))
                                    current_id += 1
                                    break
                            else:
                                if 'parent_min' in item[var['mean']].keys() and item[var['mean']]['parent_min'][has_parent] > newlines:
                                    bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column,
                                                    item['Description_less'] + str(newlines) + " lines."))
                                    current_id += 1
                                    break
                                if 'parent_max' in item[var['mean']].keys() and item[var['mean']]['parent_max'][has_parent] < newlines:
                                    bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column,
                                                    item['Description_more'] + str(newlines) + " lines."))
                                    current_id += 1
                                    break
                    else:
                        if 'default' in item.keys():
                            if 'min' in item['default'].keys() and item['default']['min'] > newlines:
                                bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column,
                                                item['Description_less'] + str(newlines) + " lines."))
                                current_id += 1
                            if 'max' in item['default'].keys() and item['default']['max'] > newlines:
                                bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column,
                                                item['Description_more'] + str(newlines) + " lines."))
                                current_id += 1
                    was = False
                    newlines = -1
        elif item['check'] == 'imports':
            whois_pos = None
            newline = False
            importing = False
            importKs = []

            for expr in exprs:
                if expr.lexem.name in space_statement[language]:
                    pass
                elif expr.lexem.name in item['sequence']:
                    if not importing:
                        if expr.lexem.name in item['hint']:
                            importKs.append(expr.expr_line)

                        importing = True
                        newline = False
                        buf_index = item['sequence'].index(expr.lexem.name)
                        if whois_pos is None:
                            whois_pos = buf_index
                        else:
                            if buf_index > whois_pos:
                                whois_pos = buf_index
                            elif buf_index < whois_pos:
                                cur_line = get_whole_line(exprs, expr)
                                bugs.append(Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column,
                                                item['Description_sequence']))
                                current_id += 1
                elif expr.lexem.name in end_statement[language]:
                    newline = True
                    importing = False
                elif newline:
                    whois_pos = len(item['sequence']) + 1

            buf_amount = 0
            buf_expr = None
            for importK in importKs:
                for var in df:
                    if var['mean'] == 'module' and var['expr'].expr_line == importK:
                        buf_amount += 1
                        buf_expr = var['expr']
                    elif not buf_expr is None and var['expr'].expr_line > importK:
                        if buf_amount > item['amount']:
                            bugs.append(
                                Bug(current_id, buf_expr.lexem.obj, buf_expr.lexem.line, buf_expr.lexem.column,
                                    item['Description_amount']))
                            current_id += 1
                        buf_amount = 0
                        buf_expr = None
                        break
        elif item['check'] == 'tabs_spaces':
            not_space = False
            amounts = {}
            for expr in exprs:
                buf_name = expr.lexem.name
                if buf_name in end_statement[language]:
                    not_space = False
                elif buf_name in space_statement[language]:
                    if not_space:
                        if buf_name in amounts.keys():
                            amounts[buf_name] += 1
                        else:
                            amounts[buf_name] = 1
                        if amounts[buf_name] > item['hint'][buf_name]:
                            cur_line = get_whole_line(exprs, expr)
                            bugs.append(
                                Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column, item['Description']))
                            current_id += 1
                else:
                    for key, value in amounts.items():
                        amounts[key] = 0
                    not_space = True
        elif item['check'] == 'indents' and indents:
            was_space = False
            was_tab = False
            for expr in exprs:
                if expr.lexem.name in end_statement[language]:
                    was_space = False
                    was_tab = False
                elif expr.lexem.name in space_statement[language]:
                    if expr.lexem.name == item['space']:
                        was_space = True
                    elif expr.lexem.name == item['tab']:
                        was_tab = True
                    if was_tab and was_space:
                        cur_line = get_whole_line(exprs, expr)
                        bugs.append(
                            Bug(current_id, cur_line, expr.lexem.line, expr.lexem.column, item['Description']))
                        current_id += 1
                else:
                    pass

    return bugs


def du_testing(exprs=[], df=[], du=[], current_id=0, ignores=['parent_module'], banned=["system"], logfile=None):
    bugs = []
    for item in df:
        for item2 in df:
            if item2['expr'].lexem.obj == item['expr'].lexem.obj and item2['expr'].expr_line == item['expr'].expr_line and item2['allow'] == item['allow']:
                is_use = False
                delete = []
                for use in du:
                    if use['expr'].expr_line > item['allow'][0] and use['expr'].expr_line < item['allow'][len(item['allow']) - 1]:
                        if use['expr'].lexem.obj == item['expr'].lexem.obj:
                            if delete:
                                bugs.append(Bug(current_id, use['expr'].lexem.obj, use['expr'].lexem.line,
                                        use['expr'].lexem.column, "The variable was removed at {0}:{1} and wasn't initialized".format(delete[0], delete[1])))
                                break
                            if use['mean'] == 'deliting':
                                delete = [use['expr'].lexem.line, use['expr'].lexem.column]
                                continue
                            is_use = True
                            break
                    elif use['expr'].expr_line > item['allow'][len(item['allow']) - 1]:
                        break
                if not is_use:
                    bugs.append(
                        Bug(current_id, item['expr'].lexem.obj, item['expr'].lexem.line, item['expr'].lexem.column,
                            'The variable has not used'))
                    current_id += 1
                break

    for use in du:
        ignore = False
        if use['expr'].role:
            for key, value in use['expr'].role.items():
                for val in value:
                    if val in ignores:
                        ignore = True
                else:
                    continue
                break
        if not ignore:
            was_define = False
            was_define_after = []
            for define in df:

                if use['expr'].expr_line > define['expr'].expr_line:
                    if use['expr'].lexem.obj == define['expr'].lexem.obj:
                        was_define = True
                else:
                    if was_define:
                        break
                    else:
                        if use['mean'] == 'func':
                            if not use['expr'].lexem.obj in banned:
                                was_problem = False
                                try:
                                    eval("{0}()".format(use['expr'].lexem.obj))
                                except NameError as er:
                                    was_problem = True
                                except Exception:
                                    pass

                                if not was_problem:
                                    was_define = True
                                    break

                        if use['expr'].lexem.obj == define['expr'].lexem.obj and use['expr'].expr_line < define['expr'].expr_line:
                            was_define_after = [define['expr'].lexem.line, define['expr'].lexem.column]
                            break
            if not was_define:
                if not was_define_after:
                    bugs.append(
                        Bug(current_id, use['expr'].lexem.obj, use['expr'].lexem.line, use['expr'].lexem.column,
                            'The variable was not defined before usage and nowhere in program!'))
                    current_id += 1
                else:
                    bugs.append(
                        Bug(current_id, use['expr'].lexem.obj, use['expr'].lexem.line, use['expr'].lexem.column,
                            'The variable was not defined before, but was defined at {0}:{1}'.format(was_define_after[0], was_define_after[1])))
                    current_id += 1

    return bugs


def coverage_operator_testing(exprs=[], inputs={}, outputs={}, banned=[".system"], logfile=None):
    current_line = -1
    for expr in exprs:
        if expr.expr_line > current_line:
            
            current_expr = get_whole_line(expr, exprs)
            current_line = expr.expr_line

            was_banned = False
            for item in banned:
                if item in current_line:
                    was_banned = True
            if not was_banned:
                for item in inputs.keys():
                    if item in current_expr:
                        current_expr = current_expr.replace(item, str(inputs[item]))
                print(current_expr)


def df_maker(exprs=[], hints=['variable', 'variable_class_private', 'variable_not_imported'],
             roles_in_many={'var': ['func', 'bracket']},
             roles={'var': ['equation_left', 'as'], 'for': ['for'], 'class': ['class'], 'func': ['func'],
                    'module': ['module']}, keywords=['class', 'func', 'for'], constructs=[], logfile=None):
    df = []
    for expr in exprs:

        if expr.lexem.name in hints and expr.role:  # expr.role will be everytime because of equation role

            for pos_role, role in expr.role.items():
                for key, values in roles.items():
                    for value in values:
                        if value in role and pos_role >= expr.place:

                            for construct in constructs:
                                if construct.start == expr.expr_line + 1 and construct.role == value:
                                    construct.name = expr.lexem
                                    break

                            df.append({'expr': expr, 'mean': key})
                            break

                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                buf_key = None
                buf_counter = 0
                for pos_role, role in expr.role.items():
                    for key, values in roles_in_many.items():
                        for value in values:
                            if value in role:
                                buf_key = key
                                buf_counter += 1
                                break
                        else:
                            continue
                        break
                    else:
                        buf_key = None
                        buf_counter = 0
                if buf_key and buf_counter == len(roles_in_many[buf_key]):
                    df.append({'expr': expr, 'mean': buf_key})

    last_expr = exprs[len(exprs) - 1].expr_line
    all_exprs = []
    all_outer_exprs = []
    for i in range(0, last_expr + 1):
        all_exprs.append(i)
        for construct in constructs:
            if i >= construct.start and i <= construct.end:
                break
        else:
            all_outer_exprs.append(i)

    #Add parent and place of usage
    for item in df:
        if item['expr'].expr_line in all_outer_exprs:
            item['allow'] = all_exprs
            item['parent'] = None
        else:
            for construct in constructs:
                if not construct.role in keywords:
                    continue

                buf_expr_line = item['expr'].expr_line
                if not item['mean'] in keywords and construct.role in keywords:
                    buf_expr_line += 1

                if buf_expr_line >= construct.start and buf_expr_line <= construct.end:
                    item['allow'] = [i for i in range(construct.start, construct.end + 1)]
                    item['parent'] = construct.name
                    break
            if not 'allow' in item.keys():
                item['allow'] = all_exprs
                item['parent'] = None

    # for i in range(0, len(df)):
    #     for k in range(i + 1, len(df)):
    #         if df[k]['expr'].lexem.obj == df[i]['expr'].lexem.obj and ((df[k]['parent'] == df[i]['expr']) or (df[k]['parent'] is None and df[i]['parent'] is None)):
    #             cur_line = df[k]['expr'].expr_line
    #             buf_allow = [line for line in df[i]['allow'] if line < cur_line]
    #             df[i]['allow'] = deepcopy(buf_allow)
    #             buf_allow = [line for line in df[k]['allow'] if line >= cur_line]
    #             df[k]['allow'] = deepcopy(buf_allow)
    #
    #             break

    return df

def du_maker(exprs=[], df=[], hints=['variable', 'variable_class_private', 'variable_not_imported'], roles={'func': ['leftBracket']}, ignores=['use_equation'], add_always=['deliting'], logfile=None):
    du = []
    for i in range(0, len(exprs) - 1):
        if exprs[i].lexem.name in hints:
            for item in df:
                if exprs[i].lexem.obj == item['expr'].lexem.obj and exprs[i].expr_line == item['expr'].expr_line and exprs[i].expr_pos == item['expr'].expr_pos:
                    for key, value in exprs[i].role.items():
                        for ignore in ignores:
                            if ignore in value:
                                break
                        else:
                            continue
                        break
                    else:
                        break
                    du.append({'expr': exprs[i], 'mean': ""})
                    break
            else:

                buf_expr = exprs[i]
                buf_mean = ""

                if exprs[i].role:
                    for key, value in exprs[i].role.items():
                        for other_value in value:
                            if other_value in add_always:
                                buf_mean = other_value
                                break
                        else:
                            continue
                        break

                i += 1
                while exprs[i].lexem.name in space_statement:
                    i += 1
                for key, value in roles.items():
                    if exprs[i].lexem.name in value:
                        buf_mean = key
                        break
                du.append({'expr': buf_expr, 'mean': buf_mean})

    # for item in du:
    #     print(item['expr'].lexem.obj, item['expr'].lexem.line, item['mean'])
    return du

if __name__ == '__main__':
    test = TestModule()
    test.start_testing_process('test.py')