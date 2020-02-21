import os
import subprocess
from copy import deepcopy
from datetime import datetime

import psutil


class Lexem:
    def __init__(self, obj="", name="", role=[], pos=0, line=0, column=0):
        self.obj = obj
        self.name = name
        self.pos = pos
        if role:
            self.role = deepcopy(role)
        else:
            role = []
        self.line = line
        self.column = column

    def __eq__(self, other):
        if isinstance(other, Lexem):
            return (self.obj == other.obj and self.line == other.line and self.column == other.column)
        else:
            return NotImplemented


class Token:
    def __init__(self, prior, reg, name, leftborder=None, rightborder=None):
        self.prior = prior
        self.reg = reg
        self.name = name
        if leftborder:
            self.leftborder = Border(leftborder.allow_symbols, leftborder.their_dict)
        else:
            self.leftborder = None
        if rightborder:
            self.rightborder = Border(rightborder.allow_symbols, rightborder.their_dict)
        else:
            self.rightborder = None

    def __str__(self):
        return str(self.prior) + '-' + self.name + ' -> ' + self.reg


class Border:
    def __init__(self, allow_symbols, their_dict=None):
        self.allow_symbols = deepcopy(allow_symbols)
        self.allow_symbols.sort(key=lambda s: len(s))
        if not their_dict is None:
            self.their_dict = deepcopy(their_dict)
        else:
            self.their_dict = None


class ExprLexem:
    def __init__(self, lexem, expr_line, expr_pos, place, role):
        self.lexem = lexem
        self.expr_line = expr_line
        self.expr_pos = expr_pos
        self.place = place
        if role:
            self.role = deepcopy(role)
        else:
            self.role = None


class Rule:
    def __init__(self, keyword, allow_tokens, final_words, role, ignore_symbols={}, inner=False, visa_verse=[],
                 visa_verse_tokens=[], use_parent_final=False, could_be_end=None, check_could_be_end=None):
        self.keyword = keyword
        if allow_tokens:
            self.allow_tokens = deepcopy(allow_tokens)
        else:
            self.allow_tokens = []
        if final_words:
            self.final_words = deepcopy(final_words)
        else:
            self.final_words = []
        if role:
            self.role = deepcopy(role)
        else:
            self.role = []

        if ignore_symbols:
            self.ignore_symbols = deepcopy(ignore_symbols)
        else:
            self.ignore_symbols = {}

        self.inner = inner

        if visa_verse:
            self.visa_verse = deepcopy(visa_verse)
        else:
            self.visa_verse = []
        if visa_verse_tokens:
            self.visa_verse_tokens = deepcopy(visa_verse_tokens)
        else:
            self.visa_verse_tokens = []

        self.use_parent_final = use_parent_final

        self.could_be_end = could_be_end

        if check_could_be_end:
            self.check_could_be_end = deepcopy(check_could_be_end)
        else:
            self.check_could_be_end = None


class ParentVar:
    def __init__(self, role, start, end, name=""):
        self.role = role
        self.start = start
        self.end = end
        self.name = name


class Bug:
    def __init__(self, number, object, line, column, description, priority=3, important=4, type="warning",
                 date=datetime.now(), author="", program="", version="1.0.0", state="open", manage_by="",
                 possible_decision=""):
        self.id = number
        self.object = object
        self.line = line
        self.column = column
        self.description = description
        self.priority = priority
        self.important = important
        self.type = type
        self.date = date
        self.author = author
        self.program = program
        self.version = version
        self.state = state
        self.manage_by = manage_by
        self.possible_decision = possible_decision


class Person:
    def __init__(self, id, pswd, name, role="Tester", rights=[{'db': 'bug_tracking', 'collection': 'bugs'}]):
        self.login = id
        self.password = pswd
        self.name = name
        self.role = role
        self.rights = deepcopy(rights)


def tab_to_space(old, N):
    new = ""
    for item in old:
        if item == '\t':
            for i in range(0, N):
                new += ' '
        else:
            new += ' '
    return new


def get_whole_line(exprs=[], expr=None, txt=True):
    cur_line = ""
    cur_exprs = []

    for buf_expr in exprs:
        if buf_expr.expr_line == expr.expr_line and buf_expr.lexem.obj != '\n':
            cur_line += buf_expr.lexem.obj
            cur_exprs.append(buf_expr)
        elif buf_expr.lexem.line > expr.lexem.line:
            break
    if txt:
        return cur_line
    else:
        return cur_exprs


def check_process_running(proc_name="mongod.exe"):
    return proc_name in (p.name() for p in psutil.process_iter())


def run_process(path_to_program="C:\\mongodb\\mongodb-win32-x86_64-2008plus-ssl-4.0.9\\bin", program="mongod.exe"):
    if not check_process_running(program):
        path_to_program = os.path.normpath(path_to_program)
        path_to_run = os.path.join(path_to_program, program)
        print(path_to_run)
        proc = subprocess.Popen([path_to_run])
    else:
        print("DB has already started!")
        proc = None
    return proc


if __name__ == '__main__':
    proc = run_process()
    from mongo_handler import get_mongo

    current_tokens = get_mongo()
    for token in current_tokens:
        print(token)
    subprocess.Popen.kill(proc)
