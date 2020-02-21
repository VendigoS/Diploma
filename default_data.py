allow_symbols_str_left = ['\t', ' ', '\n', ',', '(', '[', '{', '=', '+', 'rb', 'br', 'rf', 'fr', 'r', 'b', 'f', 'u']
their_dict_str = {"rb": ['regular', 'byte'], "br": ['regular', 'byte'], "rf": ['regular', 'func'],
                  "fr": ['regular', 'func'], "r": ['regular'], "f": ['func'], "b": ['byte'], "u": ['unicode']}
allow_symbols_str_right = ['\t', " ", "\n", ",", ")", "]", "}", ".", "+", "%", '#', ';', ':']
allow_symbols_key_left = ['\t', ' ', '\n', ':', ',', '(', '[', '{', '=']
allow_symbols_key_right = ['\t', ' ', '\n', ':', ',', ')', ']', '}', ';', '#']
allow_symbols_number_left = ['\t', ' ', '\n', ':', ',', '(', '[', '{', '=', '+', '-', '*', '/', '%', '>', '<']
allow_symbols_number_right = ['\t', ' ', '\n', ':', ',', ')', ']', '}', ';', '#', '=', '+', '-', '*', '/', '%', '>',
                              '<']
allow_symbols_spaces_before = ['\t', ' ', '\n', ';']
allow_symbols_spaces_after = ['\t', ' ', '\n', ';', '#']
allow_symbols_spaces = ['\t', ' ', '\n']
allow_symbols_space = [' ']
allow_symbols_space_tab = ['\t', ' ']
allow_symbols_spaces_brackets = ['\t', ' ', '\n', '(', '{', '[']
allow_symbols_space_brackets_left = [' ', ')', ']', '}']
allow_symbols_space_brackets_right = [' ', '(', '{', '[']
allow_symbols_variable_left = ['\t', ' ', '=', ':', '.', '(', '[', '{', ',', '+', '%', '\n', '>', '<', '*', ';']
allow_symbols_variable_right = ['\t', ' ', '=', ':', '.', '+', '%', ')', ']', '}', ',', '\n', '#', ';', '(', '>', '<',
                                '*']
their_dict_variable = {'__': ['Class-private'], '_': ['Not imported']}

comment = {'prior': 0, 'reg': r'#[^\n]*', 'name': 'comment'}
multyStr = {'prior': 0, 'reg': r'\'\'\'[\d\D]*\'\'\'', 'name': 'multyStr',
            'leftborder': {'allow_symbols': allow_symbols_str_left, 'their_dict': their_dict_str},
            'rightborder': {'allow_symbols': allow_symbols_str_right}}
multyDoubleStr = {'prior': 0, 'reg': r'\"\"\"[\d\D]*\"\"\"', 'name': 'multyDoubleStr',
                  'leftborder': {'allow_symbols': allow_symbols_str_left, 'their_dict': their_dict_str},
                  'rightborder': {'allow_symbols': allow_symbols_str_right}}
simpleStr = {'prior': 1, 'reg': r'\'[^\n\']*\'', 'name': 'simpleStr',
             'leftborder': {'allow_symbols': allow_symbols_str_left, 'their_dict': their_dict_str},
             'rightborder': {'allow_symbols': allow_symbols_str_right}}
simpleDoubleStr = {'prior': 1, 'reg': r'\"[^\n\"]*\"', 'name': 'simpleDoubleStr',
                   'leftborder': {'allow_symbols': allow_symbols_str_left, 'their_dict': their_dict_str},
                   'rightborder': {'allow_symbols': allow_symbols_str_right}}

lambdaK = {'prior': 2, 'reg': r'lambda', 'name': 'lambdaK', 'leftborder': {'allow_symbols': allow_symbols_key_left},
           'rightborder': {'allow_symbols': ['\t', ' ']}}
false = {'prior': 2, 'reg': r'False', 'name': 'false', 'leftborder': {'allow_symbols': allow_symbols_key_left},
         'rightborder': {'allow_symbols': allow_symbols_key_right}}
true = {'prior': 2, 'reg': r'True', 'name': 'true', 'leftborder': {'allow_symbols': allow_symbols_key_left},
        'rightborder': {'allow_symbols': allow_symbols_key_right}}
none = {'prior': 2, 'reg': r'None', 'name': 'none', 'leftborder': {'allow_symbols': allow_symbols_key_left},
        'rightborder': {'allow_symbols': allow_symbols_key_right}}

cond = {'prior': 2, 'reg': r'if', 'name': 'cond', 'leftborder': {'allow_symbols': allow_symbols_spaces},
        'rightborder': {'allow_symbols': allow_symbols_spaces_brackets}}
secondcond = {'prior': 2, 'reg': r'elif', 'name': 'secondcond', 'leftborder': {'allow_symbols': allow_symbols_spaces},
              'rightborder': {'allow_symbols': allow_symbols_spaces_brackets}}
nocond = {'prior': 2, 'reg': r'else', 'name': 'nocond', 'leftborder': {'allow_symbols': allow_symbols_spaces},
          'rightborder': {'allow_symbols': ['\t', ' ', ':']}}

andK = {'prior': 2, 'reg': r'and', 'name': 'andK', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
        'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
orK = {'prior': 2, 'reg': r'or', 'name': 'orK', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
       'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}

asK = {'prior': 2, 'reg': r'as', 'name': 'asK', 'leftborder': {'allow_symbols': allow_symbols_space},
       'rightborder': {'allow_symbols': allow_symbols_space}}
isK = {'prior': 2, 'reg': r'is', 'name': 'isK', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
       'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}

assertK = {'prior': 2, 'reg': r'assert', 'name': 'assertK', 'leftborder': {'allow_symbols': allow_symbols_spaces},
           'rightborder': {'allow_symbols': allow_symbols_space}}
classK = {'prior': 2, 'reg': r'class', 'name': 'classK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
          'rightborder': {'allow_symbols': allow_symbols_space}}
defK = {'prior': 2, 'reg': r'def', 'name': 'defK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
        'rightborder': {'allow_symbols': allow_symbols_space}}
fromK = {'prior': 2, 'reg': r'from', 'name': 'fromK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
         'rightborder': {'allow_symbols': allow_symbols_space}}
importK = {'prior': 2, 'reg': r'import', 'name': 'importK',
           'leftborder': {'allow_symbols': allow_symbols_spaces_before},
           'rightborder': {'allow_symbols': allow_symbols_space}}
globalK = {'prior': 2, 'reg': r'global', 'name': 'globalK',
           'leftborder': {'allow_symbols': allow_symbols_spaces_before},
           'rightborder': {'allow_symbols': allow_symbols_space}}
nonlocalK = {'prior': 2, 'reg': r'nonlocal', 'name': 'nonlocalK',
             'leftborder': {'allow_symbols': allow_symbols_spaces_before},
             'rightborder': {'allow_symbols': allow_symbols_space}}

delK = {'prior': 2, 'reg': r'del', 'name': 'delK',
        'leftborder': {'allow_symbols': allow_symbols_spaces_before},
        'rightborder': {'allow_symbols': allow_symbols_space}}

breakK = {'prior': 2, 'reg': r'break', 'name': 'breakK', 'leftborder': {'allow_symbols': allow_symbols_space_tab},
          'rightborder': {'allow_symbols': allow_symbols_spaces_after}}
continueK = {'prior': 2, 'reg': r'continue', 'name': 'continueK',
             'leftborder': {'allow_symbols': allow_symbols_space_tab},
             'rightborder': {'allow_symbols': allow_symbols_spaces_after}}
passK = {'prior': 2, 'reg': r'pass', 'name': 'passK', 'leftborder': {'allow_symbols': allow_symbols_space_tab},
         'rightborder': {'allow_symbols': allow_symbols_spaces_after}}
raiseK = {'prior': 2, 'reg': r'raise', 'name': 'raiseK', 'leftborder': {'allow_symbols': allow_symbols_space_tab},
          'rightborder': {'allow_symbols': allow_symbols_space_tab}}
returnK = {'prior': 2, 'reg': r'return', 'name': 'returnK', 'leftborder': {'allow_symbols': allow_symbols_space_tab},
           'rightborder': {'allow_symbols': [' ', '(', '[', '{', '#', ';']}}
forK = {'prior': 2, 'reg': r'for', 'name': 'forK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
        'rightborder': {'allow_symbols': [' ', '(']}}
whileK = {'prior': 2, 'reg': r'while', 'name': 'whileK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
          'rightborder': {'allow_symbols': [' ', '(']}}
tryK = {'prior': 2, 'reg': r'try', 'name': 'tryK', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
        'rightborder': {'allow_symbols': [' ', ':']}}
exceptK = {'prior': 2, 'reg': r'except', 'name': 'exceptK',
           'leftborder': {'allow_symbols': allow_symbols_spaces_before},
           'rightborder': {'allow_symbols': [' ', '(']}}
finallyK = {'prior': 2, 'reg': r'finally', 'name': 'finallyK',
            'leftborder': {'allow_symbols': allow_symbols_spaces_before},
            'rightborder': {'allow_symbols': [' ', ':']}}
notK = {'prior': 2, 'reg': r'not', 'name': 'notK',
        'leftborder': {'allow_symbols': ['\t', ' ', '(', '[', '{', '=', ':', ',', '\n']},
        'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
inK = {'prior': 2, 'reg': r'in', 'name': 'inK', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
       'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
withK = {'prior': 2, 'reg': r'with', 'name': 'withK', 'leftborder': {'allow_symbols': allow_symbols_space_tab},
         'rightborder': {'allow_symbols': allow_symbols_space}}

variable_class_private = {'prior': 2, 'reg': r'__[a-zA-Zа-яА-Яα-ωΑ-Ω]+[a-zA-Zа-яА-Яα-ωΑ-Ω0-9_]*__',
                          'name': 'variable_class_private',
                          'leftborder': {'allow_symbols': allow_symbols_variable_left},
                          'rightborder': {'allow_symbols': allow_symbols_variable_right}}

variable = {'prior': 3, 'reg': r'[a-zA-Zа-яА-Яα-ωΑ-Ω]+[a-zA-Zа-яА-Яα-ωΑ-Ω0-9_]*', 'name': 'variable',
            'leftborder': {'allow_symbols': allow_symbols_variable_left},
            'rightborder': {'allow_symbols': allow_symbols_variable_right}}

variable_not_imported = {'prior': 3, 'reg': r'_[a-zA-Zа-яА-Яα-ωΑ-Ω]+[a-zA-Zа-яА-Яα-ωΑ-Ω0-9_]*_',
                         'name': 'variable_not_imported',
                         'leftborder': {'allow_symbols': allow_symbols_variable_left},
                         'rightborder': {'allow_symbols': allow_symbols_variable_right}}

numberExp = {'prior': 3, 'reg': r'[-]?[0-9_]*[\.]?[0-9_]+[eE][\-]?[0-9_]*[jJ]?', 'name': 'numberExp',
             'leftborder': {'allow_symbols': allow_symbols_number_left},
             'rightborder': {'allow_symbols': allow_symbols_number_right}}
numberFloat = {'prior': 3, 'reg': r'[-]?[0-9_]*\.[0-9_]*[jJ]?', 'name': 'numberFloat',
               'leftborder': {'allow_symbols': allow_symbols_number_left},
               'rightborder': {'allow_symbols': allow_symbols_number_right}}
numberBin = {'prior': 3, 'reg': r'[-]?0[bB][0-1_]+', 'name': 'numberBin',
             'leftborder': {'allow_symbols': allow_symbols_number_left},
             'rightborder': {'allow_symbols': allow_symbols_number_right}}
numberOct = {'prior': 3, 'reg': r'[-]?0[oO][0-7_]+', 'name': 'numberOct',
             'leftborder': {'allow_symbols': allow_symbols_number_left},
             'rightborder': {'allow_symbols': allow_symbols_number_right}}
numberHex = {'prior': 3, 'reg': r'[-]?0[xX][0-9a-fA-F_]+', 'name': 'numberHex',
             'leftborder': {'allow_symbols': allow_symbols_number_left},
             'rightborder': {'allow_symbols': allow_symbols_number_right}}

space = {'prior': 4, 'reg': r' ', 'name': 'space', 'leftborder': None, 'rightborder': None}
newline = {'prior': 4, 'reg': r'[\n]', 'name': 'newline'}
tab = {'prior': 4, 'reg': r'[\t]', 'name': 'tab'}

number = {'prior': 4, 'reg': r'[-]?[0-9_]+[jJ]?', 'name': 'number',
          'leftborder': {'allow_symbols': allow_symbols_number_left},
          'rightborder': {'allow_symbols': allow_symbols_number_right}}

leftBracket = {'prior': 4, 'reg': r'\(', 'name': 'leftBracket'}
rightBracket = {'prior': 4, 'reg': r'\)', 'name': 'rightBracket'}
leftBraceBracket = {'prior': 4, 'reg': r'\{', 'name': 'leftBraceBracket'}
rightBraceBracket = {'prior': 4, 'reg': r'\}', 'name': 'rightBraceBracket'}
leftSquareBracket = {'prior': 4, 'reg': r'\[', 'name': 'leftSquareBracket'}
rightSquareBracket = {'prior': 4, 'reg': r'\]', 'name': 'rightSquareBracket'}
dot = {'prior': 4, 'reg': r'\.', 'name': 'dot'}
comma = {'prior': 4, 'reg': r'\,', 'name': 'comma'}
colon = {'prior': 4, 'reg': r'\:', 'name': 'colon'}
semicolon = {'prior': 4, 'reg': r'\;', 'name': 'semicolon'}

gradShort = {'prior': 4, 'reg': r'\*\*\=', 'name': 'gradShort'}
divIntShort = {'prior': 4, 'reg': r'\/\/\=', 'name': 'divIntShort'}
bitLeftShort = {'prior': 4, 'reg': r'\<\<\=', 'name': 'bitLeftShort'}
bitRightShort = {'prior': 4, 'reg': r'\>\>\=', 'name': 'bitRightShort'}

sumShort = {'prior': 5, 'reg': r'\+\=', 'name': 'sumShort'}
subShort = {'prior': 5, 'reg': r'\-\=', 'name': 'subShort'}
mulShort = {'prior': 5, 'reg': r'\*\=', 'name': 'mulShort'}
divShort = {'prior': 5, 'reg': r'\/\=', 'name': 'divShort'}
modShort = {'prior': 5, 'reg': r'\%\=', 'name': 'modShort'}
andShort = {'prior': 5, 'reg': r'\&\=', 'name': 'andShort'}
orShort = {'prior': 5, 'reg': r'\|\=', 'name': 'orShort'}
norShort = {'prior': 5, 'reg': r'\^\=', 'name': 'norShort'}

gradOp = {'prior': 5, 'reg': r'\*\*', 'name': 'gradOp'}
divIntOp = {'prior': 5, 'reg': r'\/\/', 'name': 'divIntOp'}
bitLeft = {'prior': 5, 'reg': r'\<\<', 'name': 'bitLeft'}
bitRight = {'prior': 5, 'reg': r'\>\>', 'name': 'bitRight'}
lesserEq = {'prior': 5, 'reg': r'\<\=', 'name': 'lesserEq'}
greaterEq = {'prior': 5, 'reg': r'\>\=', 'name': 'greaterEq'}
isEq = {'prior': 5, 'reg': r'\=\=', 'name': 'isEq'}
notEq = {'prior': 5, 'reg': r'\!\=', 'name': 'notEq'}

sumOp = {'prior': 6, 'reg': r'\+', 'name': 'sumOp'}
subOp = {'prior': 6, 'reg': r'\-', 'name': 'subOp'}
mulOp = {'prior': 6, 'reg': r'\*', 'name': 'mulOp'}
divOp = {'prior': 6, 'reg': r'\/', 'name': 'divOp'}
modOp = {'prior': 6, 'reg': r'\%', 'name': 'modOp'}
andOp = {'prior': 6, 'reg': r'\&', 'name': 'andOp'}
orOp = {'prior': 6, 'reg': r'\|', 'name': 'orOp'}
norOp = {'prior': 6, 'reg': r'\^', 'name': 'norOp'}
lesser = {'prior': 6, 'reg': r'\<', 'name': 'lesser'}
greater = {'prior': 6, 'reg': r'\>', 'name': 'greater'}
equal = {'prior': 6, 'reg': r'\=', 'name': 'equal'}

undefined = {'prior': 7, 'reg': r'[\$\?\`]+', 'name': 'undefined'}

pytokens = [comment, multyStr, multyDoubleStr, simpleStr, simpleDoubleStr, lambdaK, false, true, none, cond,
            secondcond, nocond, andK, orK, asK, isK, assertK, classK, defK, fromK, importK, globalK, nonlocalK, breakK,
            continueK, passK, raiseK, returnK, forK, whileK, tryK, exceptK, finallyK, notK, inK, withK, variable,
            variable_not_imported, variable_class_private, numberExp, numberFloat, numberBin, numberOct, numberHex,
            number, gradOp, divIntOp, bitLeft, bitRight, lesserEq, greaterEq, isEq, notEq, sumOp, subOp, mulOp, divOp,
            modOp, andOp, orOp, norOp, lesser, greater, equal, gradShort, divIntShort, bitLeftShort, bitRightShort,
            sumShort, subShort, mulShort, divShort, modShort, andShort, orShort, norShort, leftBracket, rightBracket,
            leftBraceBracket, rightBraceBracket, leftSquareBracket, rightSquareBracket, dot, comma, colon, semicolon,
            space, newline, tab, undefined, delK]

allow_symbols_sharp_str_left = ['\t', ' ', '\n', ',', '(', '[', '{', '=', '+']
allow_symbols_sharp_str_right = ['\t', " ", "\n", ",", ")", "]", "}", ".", "+", '/', ';', ':']
allow_symbols_sharp_key_left = ['\t', ' ', '\n', ',', '(', '[', '{', '=', '<']
allow_symbols_sharp_key_right = ['\t', ' ', '\n', ',', ')', ']', '}', '>', ';', '/']
allow_symbols_sharp_type_left = ['\t', ' ', '\n', '(', '[', '<', ')']
allow_symbols_sharp_type_right = ['\t', ' ', ')', ']', '>', '(']
allow_symbols_sharp_variable_left = ['\t', ' ', '=', ':', '.', '(', '[', '{', '<', '>', ',', '+', '/', '*', '\n', ';']
allow_symbols_sharp_variable_right = ['\t', ' ', '=', ':', '.', '+', ')', ']', '}', ',', '\n', '/', ';', '(', '>', '<',
                                      '*']

sharp_comment = {'prior': 0, 'reg': r'//[^\n]*', 'name': 'comment'}
sharp_multy_comment = {'prior': 0, 'reg': r'/\*[\Dd]*/', 'name': 'multyComment'}
sharp_char = {'prior': 1, 'reg': r'\'[^\']\'', 'name': 'char',
              'leftborder': {'allow_symbols': allow_symbols_sharp_str_left},
              'rightborder': {'allow_symbols': allow_symbols_sharp_str_right}}
sharp_str = {'prior': 1, 'reg': r'\"[^\n\"]*\"', 'name': 'string',
             'leftborder': {'allow_symbols': allow_symbols_sharp_str_left, 'their_dict': their_dict_str},
             'rightborder': {'allow_symbols': allow_symbols_sharp_str_right}}
sharp_private = {'prior': 2, 'reg': r'private', 'name': 'private',
                 'leftborder': {'allow_symbols': allow_symbols_spaces},
                 'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_public = {'prior': 2, 'reg': r'public', 'name': 'public', 'leftborder': {'allow_symbols': allow_symbols_spaces},
                'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_protected = {'prior': 2, 'reg': r'protected', 'name': 'protected',
                   'leftborder': {'allow_symbols': allow_symbols_spaces},
                   'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_void = {'prior': 2, 'reg': r'void', 'name': 'void', 'leftborder': {'allow_symbols': allow_symbols_spaces},
              'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_static = {'prior': 2, 'reg': r'static', 'name': 'static', 'leftborder': {'allow_symbols': allow_symbols_spaces},
                'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_partial = {'prior': 2, 'reg': r'partial', 'name': 'partial',
                 'leftborder': {'allow_symbols': allow_symbols_spaces},
                 'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_false = {'prior': 2, 'reg': r'false', 'name': 'false',
               'leftborder': {'allow_symbols': allow_symbols_sharp_key_left},
               'rightborder': {'allow_symbols': allow_symbols_sharp_key_right}}
sharp_true = {'prior': 2, 'reg': r'true', 'name': 'true', 'leftborder': {'allow_symbols': allow_symbols_sharp_key_left},
              'rightborder': {'allow_symbols': allow_symbols_sharp_key_right}}
sharp_null = {'prior': 2, 'reg': r'null', 'name': 'null', 'leftborder': {'allow_symbols': allow_symbols_sharp_key_left},
              'rightborder': {'allow_symbols': allow_symbols_sharp_key_right}}
sharp_int = {'prior': 2, 'reg': r'int', 'name': 'int', 'leftborder': {'allow_symbols': allow_symbols_sharp_type_left},
             'rightborder': {'allow_symbols': allow_symbols_sharp_type_right}}
sharp_string = {'prior': 2, 'reg': r'string', 'name': 'string',
                'leftborder': {'allow_symbols': allow_symbols_sharp_type_left},
                'rightborder': {'allow_symbols': allow_symbols_sharp_type_right}}
sharp_var = {'prior': 2, 'reg': r'var', 'name': 'var', 'leftborder': {'allow_symbols': allow_symbols_sharp_type_left},
             'rightborder': {'allow_symbols': allow_symbols_sharp_type_right}}
sharp_new = {'prior': 2, 'reg': r'new', 'name': 'new',
             'leftborder': {'allow_symbols': ['\t', ' ', ',', '\n', '(', '[', '<', '=', '+', '-']},
             'rightborder': {'allow_symbols': ['\t', ' ', '(']}}
sharp_out = {'prior': 2, 'reg': r'out', 'name': 'out', 'leftborder': {'allow_symbols': ['\t', ' ', '(', ',', '[', '<']},
             'rightborder': {'allow_symbols': [' ']}}
sharp_async = {'prior': 2, 'reg': r'async', 'name': 'async', 'leftborder': {'allow_symbols': allow_symbols_spaces},
               'rightborder': {'allow_symbols': allow_symbols_space_tab}}
sharp_object = {'prior': 2, 'reg': r'object', 'name': 'object',
                'leftborder': {'allow_symbols': allow_symbols_sharp_type_left},
                'rightborder': {'allow_symbols': allow_symbols_sharp_type_right}}
sharp_await = {'prior': 2, 'reg': r'await', 'name': 'await', 'leftborder': {'allow_symbols': allow_symbols_spaces},
               'rightborder': {'allow_symbols': allow_symbols_space}}
sharp_return = {'prior': 2, 'reg': r'return', 'name': 'return',
                'leftborder': {'allow_symbols': allow_symbols_space_tab},
                'rightborder': {'allow_symbols': [' ', '(', '[', '{', '<' '/', ';']}}
sharp_as = {'prior': 2, 'reg': r'as', 'name': 'as', 'leftborder': {'allow_symbols': allow_symbols_space},
            'rightborder': {'allow_symbols': allow_symbols_space}}
sharp_is = {'prior': 2, 'reg': r'is', 'name': 'is', 'leftborder': {'allow_symbols': allow_symbols_space},
            'rightborder': {'allow_symbols': allow_symbols_space}}
sharp_not = {'prior': 2, 'reg': r'not', 'name': 'not',
             'leftborder': {'allow_symbols': ['\t', ' ', '(', '[', '{', '=', '\n', ',']},
             'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
sharp_in = {'prior': 2, 'reg': r'in', 'name': 'in', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
            'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
sharp_cond = {'prior': 2, 'reg': r'if', 'name': 'cond', 'leftborder': {'allow_symbols': allow_symbols_spaces},
              'rightborder': {'allow_symbols': [' ', '(']}}
sharp_secondcond = {'prior': 2, 'reg': r'else if', 'name': 'secondcond',
                    'leftborder': {'allow_symbols': allow_symbols_spaces},
                    'rightborder': {'allow_symbols': [' ', '(']}}
sharp_nocond = {'prior': 2, 'reg': r'else', 'name': 'nocond', 'leftborder': {'allow_symbols': allow_symbols_spaces},
                'rightborder': {'allow_symbols': ['\t', ' ', '\n', '{']}}
sharp_and = {'prior': 2, 'reg': r'and', 'name': 'and',
             'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
             'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
sharp_or = {'prior': 2, 'reg': r'or', 'name': 'or', 'leftborder': {'allow_symbols': allow_symbols_space_brackets_left},
            'rightborder': {'allow_symbols': allow_symbols_space_brackets_right}}
sharp_for = {'prior': 2, 'reg': r'for', 'name': 'for', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
             'rightborder': {'allow_symbols': [' ', '(']}}
sharp_foreach = {'prior': 2, 'reg': r'foreach', 'name': 'foreach',
                 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
                 'rightborder': {'allow_symbols': [' ', '(']}}
sharp_while = {'prior': 2, 'reg': r'while', 'name': 'while',
               'leftborder': {'allow_symbols': allow_symbols_spaces_before},
               'rightborder': {'allow_symbols': [' ', '(']}}
sharp_try = {'prior': 2, 'reg': r'try', 'name': 'try', 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
             'rightborder': {'allow_symbols': [' ', '{', '\n']}}
sharp_catch = {'prior': 2, 'reg': r'catch', 'name': 'catch',
               'leftborder': {'allow_symbols': allow_symbols_spaces_before},
               'rightborder': {'allow_symbols': [' ', '(']}}
sharp_finally = {'prior': 2, 'reg': r'finally', 'name': 'finally',
                 'leftborder': {'allow_symbols': allow_symbols_spaces_before},
                 'rightborder': {'allow_symbols': [' ', '\n', '{']}}

sharp_variable = {'prior': 3, 'reg': r'[a-zA-Zа-яА-Яα-ωΑ-Ω]+[a-zA-Zа-яА-Яα-ωΑ-Ω0-9_]*', 'name': 'variable',
                  'leftborder': {'allow_symbols': allow_symbols_sharp_variable_left},
                  'rightborder': {'allow_symbols': allow_symbols_sharp_variable_right}}

sharp_numberFloat = {'prior': 3, 'reg': r'[-]?[0-9]*\.[0-9]', 'name': 'numberFloat',
                     'leftborder': {'allow_symbols': allow_symbols_sharp_variable_left},
                     'rightborder': {'allow_symbols': allow_symbols_sharp_variable_right}}

sharp_number = {'prior': 4, 'reg': r'[-]?[0-9]+', 'name': 'number',
                'leftborder': {'allow_symbols': allow_symbols_sharp_variable_left},
                'rightborder': {'allow_symbols': allow_symbols_sharp_variable_right}}

sharp_tokens = [sharp_comment, sharp_multy_comment, sharp_char, sharp_str, sharp_private, sharp_public, sharp_protected,
                sharp_void, sharp_static, sharp_partial, sharp_false, sharp_true, sharp_null, sharp_int, sharp_string,
                sharp_var, sharp_new, sharp_out, sharp_async, sharp_object, sharp_await, sharp_return, sharp_as,
                sharp_is, sharp_not, sharp_in, sharp_cond, sharp_secondcond, sharp_nocond, sharp_and, sharp_or,
                sharp_for, sharp_foreach, sharp_while, sharp_try, sharp_catch, sharp_finally, sharp_variable,
                sharp_numberFloat, sharp_number, space, tab, newline, bitLeft, bitRight, lesserEq, greaterEq, isEq,
                notEq, sumOp, subOp, mulOp, divOp, andOp, orOp, norOp, lesser, greater, equal, bitLeftShort,
                bitRightShort, sumShort, subShort, mulShort, divShort, andShort, orShort, norShort, leftBracket,
                rightBracket, leftBraceBracket, rightBraceBracket, leftSquareBracket, rightSquareBracket,
                dot, comma, colon, semicolon]

deliting = {'keyword': 'delK', 'allow_tokens': ['variable', 'space', 'comma', 'dot'], 'final_words': ['colon', 'newline'],
                 'role': ['deliting']}
parent_module = {'keyword': 'fromK', 'allow_tokens': ['variable', 'space', 'comma', 'dot'], 'final_words': ['importK'],
                 'role': ['parent_module']}
module = {'keyword': 'importK', 'allow_tokens': ['variable', 'space', 'comma', 'dot', 'mulOp'],
          'final_words': ['newline', 'semicolon', 'comment', 'multyStr', 'multyDoubleStr'], 'role': ['module']}
if_head = {'keyword': 'cond',
           'allow_tokens': ['variable', 'space', 'comma', 'dot', 'tab', 'leftBracket', 'rightBracket',
                            'leftBraceBracket',
                            'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp', 'mulOp',
                            'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK', 'notK',
                            'divIntOp', 'bitLeft', 'bitRight', 'lesserEq', 'greaterEq', 'isEq', 'notEq', 'number',
                            'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'andK', 'orK', 'none',
                            'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
           'final_words': ['colon', 'nocond'],
           'role': ['condition', 'if'], 'visa_verse': ['body', 'if']}
elif_head = {'keyword': 'secondcond',
             'allow_tokens': ['variable', 'space', 'comma', 'dot', 'tab', 'leftBracket', 'rightBracket',
                              'leftBraceBracket', 'notK',
                              'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp', 'mulOp',
                              'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK',
                              'divIntOp', 'bitLeft', 'bitRight', 'lesserEq', 'greaterEq', 'isEq', 'notEq', 'number',
                              'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'andK', 'orK', 'none',
                              'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
             'final_words': ['colon'],
             'role': ['condition', 'if']}
else_head = {'keyword': 'nocond',
             'allow_tokens': ['variable', 'space', 'comma', 'dot', 'tab', 'leftBracket', 'rightBracket',
                              'leftBraceBracket',
                              'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp', 'mulOp',
                              'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK',
                              'divIntOp', 'bitLeft', 'bitRight', 'lesserEq', 'greaterEq', 'isEq', 'notEq', 'number',
                              'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'andK', 'orK', 'none',
                              'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
             'final_words': ['colon', 'semicolon', 'newline', 'comment'],
             'role': ['condition', 'else']}
while_head = {'keyword': 'whileK',
              'allow_tokens': ['variable', 'space', 'comma', 'dot', 'tab', 'leftBracket', 'rightBracket',
                               'leftBraceBracket',
                               'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp', 'inK',
                               'mulOp', 'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser', 'greater', 'gradOp',
                               'divIntOp', 'bitLeft', 'bitRight', 'lesserEq', 'greaterEq', 'isEq', 'notEq', 'number',
                               'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'andK', 'orK', 'none',
                               'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
              'final_words': ['colon'],
              'role': ['condition', 'while']}
body = {'keyword': 'colon', 'allow_tokens': [],
        'final_words': [],
        'role': ['body'],
        'could_be_end': 'newline',
        'check_could_be_end': ['space', 'tab', 'comment']}
equation = {'keyword': 'equal',
            'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                             'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp', 'mulOp',
                             'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK',
                             'divIntOp', 'bitLeft', 'bitRight', 'number', 'numberExp', 'numberFloat', 'numberBin',
                             'numberHex', 'numberOct', 'andK', 'orK', 'none', 'multyDoubleStr', 'simpleDoubleStr',
                             'multyStr', 'simpleStr', 'true', 'false', 'lambdaK', 'lesserEq', 'greaterEq', 'isEq',
                             'notEq'],
            'final_words': ['newline', 'semicolon', 'comment', 'rightBracket'],
            'role': ['equation'], 'visa_verse': ['equation_left']}
equation_sum = {'keyword': 'sumShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'sum'], 'visa_verse': ['equation_left', 'use_equation']}
equation_sub = {'keyword': 'subShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'sub'], 'visa_verse': ['equation_left', 'use_equation']}
equation_mul = {'keyword': 'mulShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'mul'], 'visa_verse': ['equation_left', 'use_equation']}
equation_div = {'keyword': 'divShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'div'], 'visa_verse': ['equation_left', 'use_equation']}
equation_mod = {'keyword': 'modShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'mod'], 'visa_verse': ['equation_left', 'use_equation']}
equation_and = {'keyword': 'andShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'and_op'], 'visa_verse': ['equation_left', 'use_equation']}
equation_or = {'keyword': 'orShort',
               'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
               'final_words': ['newline', 'semicolon', 'comment'],
               'role': ['equation', 'or_op'], 'visa_verse': ['equation_left', 'use_equation']}
equation_nor = {'keyword': 'norShort',
                'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                 'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                'final_words': ['newline', 'semicolon', 'comment'],
                'role': ['equation', 'nor_op'], 'visa_verse': ['equation_left', 'use_equation']}
equation_grad = {'keyword': 'gradShort',
                 'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket',
                                  'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                  'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                  'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                  'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                 'final_words': ['newline', 'semicolon', 'comment'],
                 'role': ['equation', 'grad'], 'visa_verse': ['equation_left', 'use_equation']}
equation_divInt = {'keyword': 'divIntShort',
                   'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket',
                                    'leftBraceBracket',
                                    'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                    'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                    'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                    'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp', 'norOp'],
                   'final_words': ['newline', 'semicolon', 'comment'],
                   'role': ['equation', 'div_int'], 'visa_verse': ['equation_left', 'use_equation']}
equation_bitLeft = {'keyword': 'bitLeftShort',
                    'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket',
                                     'leftBraceBracket',
                                     'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                     'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                     'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                     'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp',
                                     'norOp'],
                    'final_words': ['newline', 'semicolon', 'comment'],
                    'role': ['equation', 'bit_left'], 'visa_verse': ['equation_left', 'use_equation']}
equation_bitRight = {'keyword': 'bitRightShort',
                     'allow_tokens': ['variable', 'space', 'comma', 'tab', 'leftBracket', 'rightBracket',
                                      'leftBraceBracket',
                                      'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                      'mulOp', 'divOp', 'modOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight', 'number',
                                      'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                      'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'andOp', 'orOp',
                                      'norOp'],
                     'final_words': ['newline', 'semicolon', 'comment'],
                     'role': ['equation', 'bit_right'], 'visa_verse': ['equation_left', 'use_equation']}

comparison_lesser = {'keyword': 'lesser',
                     'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                      'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                      'mulOp',
                                      'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                      'bitRight', 'inK',
                                      'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                      'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                     'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                     'use_parent_final_words': True,
                     'role': ['comparison', 'greater'], 'visa_verse': ['comparison', 'lesser']}
comparison_greater = {'keyword': 'greater',
                      'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                       'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                       'mulOp',
                                       'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                       'bitRight', 'inK',
                                       'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                       'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                      'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                      'use_parent_final_words': True,
                      'role': ['comparison', 'lesser'], 'visa_verse': ['comparison', 'greater']}
comparison_lesserEq = {'keyword': 'lesserEq',
                       'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                        'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                        'subOp', 'mulOp',
                                        'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                        'bitRight', 'inK',
                                        'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                        'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                       'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                       'use_parent_final_words': True,
                       'role': ['comparison', 'greater_eq'], 'visa_verse': ['comparison', 'lesser_eq']}
comparison_greaterEq = {'keyword': 'greaterEq',
                        'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                         'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                         'subOp', 'mulOp',
                                         'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                         'bitRight', 'inK',
                                         'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                         'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                        'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                        'use_parent_final_words': True,
                        'role': ['comparison', 'lesser_eq'], 'visa_verse': ['comparison', 'greater_eq']}
comparison_equal = {'keyword': 'isEq',
                    'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                     'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp', 'subOp',
                                     'mulOp',
                                     'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                     'bitRight',
                                     'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                     'none', 'inK',
                                     'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                    'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                    'use_parent_final_words': True,
                    'role': ['comparison', 'equal'], 'visa_verse': ['comparison', 'equal']}
comparison_notEqual = {'keyword': 'notEq',
                       'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                        'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                        'subOp', 'mulOp',
                                        'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft',
                                        'bitRight',
                                        'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                        'none', 'inK',
                                        'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false'],
                       'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                       'use_parent_final_words': True,
                       'role': ['comparison', 'not_equal'], 'visa_verse': ['comparison', 'not_equal']}

and_statement = {'keyword': 'andK',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                  'subOp', 'mulOp', 'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp',
                                  'divIntOp', 'bitLeft', 'bitRight', 'number', 'numberExp', 'numberFloat',
                                  'numberBin', 'numberHex', 'numberOct', 'none', 'inK', 'multyDoubleStr',
                                  'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false', 'lesser', 'greater',
                                  'lesserEq', 'greaterEq', 'notEq', 'isEq'],
                 'final_words': ['newline', 'semicolon', 'comment', 'andK', 'orK'],
                 'use_parent_final_words': True,
                 'role': ['and'], 'visa_verse': ['and']}

or_statement = {'keyword': 'orK',
                'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                 'subOp', 'mulOp', 'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp',
                                 'divIntOp', 'bitLeft', 'bitRight', 'number', 'numberExp', 'numberFloat',
                                 'numberBin', 'numberHex', 'numberOct', 'none', 'inK', 'multyDoubleStr', 'andK',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false', 'lesser', 'greater',
                                 'lesserEq', 'greaterEq', 'notEq', 'isEq'],
                'final_words': ['newline', 'semicolon', 'comment', 'orK'],
                'use_parent_final_words': True,
                'role': ['or'], 'visa_verse': ['or']}

def_statement = {'keyword': 'defK',
                 'allow_tokens': ['variable', 'variable_class_private', 'variable_not_imported', 'space', 'tab',
                                  'leftBracket'],
                 'final_words': ['colon'],
                 'role': ['func']}

class_statement = {'keyword': 'classK',
                   'allow_tokens': ['variable', 'space', 'tab', 'leftBracket'],
                   'final_words': ['colon'],
                   'role': ['class']}

try_statement = {'keyword': 'tryK',
                 'allow_tokens': ['space'],
                 'final_words': ['colon'],
                 'role': ['try']}

except_statement = {'keyword': 'exceptK',
                    'allow_tokens': ['variable', 'asK', 'space', 'tab'],
                    'final_words': ['colon'],
                    'role': ['except']}

finally_statement = {'keyword': 'finallyK',
                     'allow_tokens': ['space'],
                     'final_words': ['colon'],
                     'role': ['finally']}

return_statement = {'keyword': 'returnK',
                    'allow_tokens': ['space', 'comma', 'dot', 'variable', 'leftBracket', 'rightBracket',
                                     'leftBraceBracket',
                                     'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'sumOp',
                                     'subOp', 'mulOp', 'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp',
                                     'divIntOp', 'bitLeft', 'bitRight', 'number', 'numberExp', 'numberFloat',
                                     'numberBin', 'numberHex', 'numberOct', 'none', 'inK', 'multyDoubleStr',
                                     'simpleDoubleStr', 'multyStr', 'simpleStr', 'true', 'false', 'andK', 'orK'],
                    'final_words': ['newline', 'semicolon', 'comment'],
                    'role': ['return']}

raise_statement = {'keyword': 'raiseK',
                   'allow_tokens': ['space', 'dot', 'variable'],
                   'final_words': ['newline', 'semicolon', 'comment'],
                   'role': ['raise']}

lambda_statement = {'keyword': 'lambdaK',
                    'allow_tokens': ['space', 'dot', 'comma', 'variable'],
                    'final_words': ['colon'],
                    'role': ['lambda']}

with_statement = {'keyword': 'withK',
                  'allow_tokens': ['space', 'dot', 'comma', 'variable', 'leftBracket', 'rightBracket'],
                  'final_words': ['asK'],
                  'role': ['with']}

as_statement = {'keyword': 'asK',
                'allow_tokens': ['space', 'variable'],
                'final_words': ['colon'],
                'role': ['as', 'variable']}

for_statement = {'keyword': 'forK',
                 'allow_tokens': ['variable', 'space', 'comma', 'dot'], 'final_words': ['inK'],
                 'role': ['for', 'variable']}

in_statement = {'keyword': 'inK',
                'allow_tokens': ['space', 'comma', 'dot', 'variable', 'leftBracket', 'rightBracket',
                                 'leftBraceBracket', 'rightBraceBracket', 'leftSquareBracket',
                                 'rightSquareBracket', 'number', 'numberExp', 'numberFloat',
                                 'numberBin', 'numberHex', 'numberOct', 'multyDoubleStr',
                                 'simpleDoubleStr', 'multyStr', 'simpleStr'],
                'final_words': ['newline', 'semicolon', 'comment', 'colon'],
                'role': ['in', 'variable']}

dotting = {'keyword': 'dot',
           'allow_tokens': ['variable'],
           'final_words': [],
           'role': ['child'], 'visa_verse': ['parent'],
           'visa_verse_tokens': ['variable', 'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr']}

global_statement = {'keyword': 'globalK',
                    'allow_tokens': ['variable', 'space', 'tab', 'comma'],
                    'final_words': ['newline', 'semicolon', 'comment'],
                    'role': ['global']}

nonlocal_statement = {'keyword': 'nonlocalK',
                      'allow_tokens': ['variable', 'space', 'tab', 'comma'],
                      'final_words': ['newline', 'semicolon', 'comment'],
                      'role': ['global']}

left_bracket = {'keyword': 'leftBracket',
                'allow_tokens': ['variable', 'space', 'tab', 'comma', 'dot', 'true', 'false', 'none', 'leftBracket',
                                 'leftBraceBracket', 'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket',
                                 'sumOp', 'subOp', 'mulOp', 'divOp', 'modOp', 'andOp', 'orOp', 'norOp', 'lesser',
                                 'greater', 'gradOp', 'inK', 'divIntOp', 'bitLeft', 'bitRight', 'lesserEq', 'greaterEq',
                                 'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct', 'andK',
                                 'orK', 'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr', 'isEq', 'notEq',
                                 'equal', 'lambdaK', 'newline'],
                'final_words': ['rightBracket'],
                'ignore_symbols': {'newline': ['comma']},
                'inner': True,
                'role': ['bracket', 'tuple']}

left_brace_bracket = {'keyword': 'leftBraceBracket',
                      'allow_tokens': ['variable', 'space', 'tab', 'comma', 'dot', 'true', 'false', 'none', 'colon',
                                       'leftBracket', 'rightBracket', 'leftBraceBracket', 'leftSquareBracket',
                                       'rightSquareBracket', 'sumOp', 'subOp', 'mulOp', 'divOp', 'modOp', 'andOp',
                                       'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK', 'divIntOp', 'bitLeft',
                                       'bitRight', 'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex',
                                       'numberOct', 'andK', 'orK', 'multyDoubleStr', 'simpleDoubleStr', 'multyStr',
                                       'simpleStr', 'isEq', 'notEq', 'lesser', 'greater', 'lesserEq', 'greaterEq',
                                       'newline'],
                      'final_words': ['rightBraceBracket'],
                      'ignore_symbols': {'newline': ['comma', 'colon'], 'colon': None},
                      'inner': True,
                      'role': ['bracket', 'dictionary']}

left_square_bracket = {'keyword': 'leftSquareBracket',
                       'allow_tokens': ['variable', 'space', 'tab', 'comma', 'dot', 'true', 'false', 'none',
                                        'leftBracket', 'rightBracket', 'leftBraceBracket', 'rightBraceBracket',
                                        'rightSquareBracket', 'sumOp', 'subOp', 'mulOp', 'divOp', 'modOp', 'andOp',
                                        'orOp', 'norOp', 'lesser', 'greater', 'gradOp', 'inK', 'divIntOp', 'bitLeft',
                                        'bitRight', 'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex',
                                        'numberOct', 'andK', 'orK', 'multyDoubleStr', 'simpleDoubleStr', 'multyStr',
                                        'simpleStr', 'isEq', 'notEq', 'lesser', 'greater', 'lesserEq', 'greaterEq',
                                        'newline'],
                       'final_words': ['rightSquareBracket'],
                       'inner': True,
                       'ignore_symbols': {'newline': ['comma']},
                       'role': ['bracket', 'list']}

sum_statement = {'keyword': 'sumOp',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'mulOp', 'divOp',
                                  'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight',
                                  'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct',
                                  'multyDoubleStr', 'simpleDoubleStr', 'multyStr', 'simpleStr'],
                 'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'cond', 'nocond'],
                 'use_parent_final_words': True,
                 'role': ['sum'], 'visa_verse': ['sum']}

sub_statement = {'keyword': 'subOp',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'mulOp', 'divOp',
                                  'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight',
                                  'number', 'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct'],
                 'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'cond', 'nocond'],
                 'use_parent_final_words': True,
                 'role': ['sub'], 'visa_verse': ['sub']}

mul_statement = {'keyword': 'mulOp',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'number', 'numberExp',
                                  'numberFloat', 'numberBin', 'numberHex', 'numberOct'],
                 'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'mulOp', 'divOp', 'cond',
                                 'nocond',
                                 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight'],
                 'use_parent_final_words': True,
                 'role': ['mul'], 'visa_verse': ['mul']}

div_statement = {'keyword': 'divOp',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'number', 'numberExp',
                                  'numberFloat', 'numberBin', 'numberHex', 'numberOct'],
                 'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'mulOp', 'divOp', 'cond',
                                 'nocond',
                                 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight'],
                 'use_parent_final_words': True,
                 'role': ['div'], 'visa_verse': ['div']}

mod_statement = {'keyword': 'modOp',
                 'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                  'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'number', 'numberExp',
                                  'numberFloat', 'numberBin', 'numberHex', 'numberOct'],
                 'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'mulOp', 'divOp', 'cond',
                                 'nocond',
                                 'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight'],
                 'use_parent_final_words': True,
                 'role': ['mod'], 'visa_verse': ['mod']}

grad_statement = {'keyword': 'gradOp',
                  'allow_tokens': ['variable', 'space', 'tab', 'leftBracket', 'rightBracket', 'leftBraceBracket',
                                   'rightBraceBracket', 'leftSquareBracket', 'rightSquareBracket', 'number',
                                   'numberExp', 'numberFloat', 'numberBin', 'numberHex', 'numberOct'],
                  'final_words': ['newline', 'semicolon', 'comment', 'sumOp', 'subOp', 'mulOp', 'divOp', 'cond',
                                  'nocond',
                                  'modOp', 'andOp', 'orOp', 'norOp', 'gradOp', 'divIntOp', 'bitLeft', 'bitRight'],
                  'use_parent_final_words': True,
                  'role': ['grad'], 'visa_verse': ['grad']}

pyrules = [parent_module, module, if_head, elif_head, else_head, while_head, body, equation, equation_sum, equation_sub,
           equation_mul, equation_div, equation_mod, equation_bitLeft, equation_bitRight, equation_and, equation_or,
           equation_nor, equation_grad, equation_divInt, comparison_equal, comparison_greater, comparison_greaterEq,
           comparison_lesser, comparison_lesserEq, comparison_notEqual, and_statement, or_statement, class_statement,
           def_statement, try_statement, except_statement, finally_statement, return_statement, raise_statement,
           lambda_statement, with_statement, as_statement, in_statement, for_statement, sub_statement, sum_statement,
           mul_statement, div_statement, mod_statement, grad_statement, global_statement, nonlocal_statement,
           left_brace_bracket, left_bracket, left_square_bracket, dotting, deliting]

space_statement = {'python': ['space', 'tab']}
end_statement = {"python": ['semicolon', 'newline']}

PEP8_string_limit = {'name': 'The limitation of string length', 'check': 'length', 'size': 79,
                     'Description': 'The line is more than 79 symbols.'}

PEP8_names = {'name': 'Rule of class and func naming', 'check': 'var_names',
              'class': {'hint': ['class'], 'reg': '[A-ZА-ЯΑ-Ω][A-ZА-ЯΑ-ΩАa-zа-яα-ω]*',
                        'Description': 'The name of class should be with first uppercase letter and without underscores and numbers'},
              'func': {'hint': ['func'],
                       'reg': '[_]{0,2}[a-zа-яα-ω]+([a-zа-яα-ω]*_[a-zа-яα-ω]*)*[_]{0,2}',
                       'Description': 'The name of function should be lowercase without numbers and can include underscores'}}

PEP8_newlines = {'name': 'Rule of blank lines between classes and functions', 'check': 'newlines', 'hint': ['newline'],
                 'class': {'hint': ['class'], 'parent': {True: 2, False: 2}},
                 'func': {'hint': ['func'], 'parent': {True: 1, False: 2}},
                 'default': {'min': 0, 'max': 0},
                 'for': {'hint': ['for'], 'parent': {True: 0, False: 0}},
                 'Description_more': 'Too much blank lines, you should use less blank lines before. Now you has ',
                 'Description_less': 'Too few blank lines, you should use more blank lines before. Now you has '
                 }

PEP8_imports = {'name': 'Rule of imports', 'check': 'imports', 'hint': ['importK'], 'amount': 1,
                'sequence': ['importK', 'fromK'],
                'Description_sequence': 'The bad import structure. You should use all imports at the beginning of program. And you should firstly use import, then from * import, then other code',
                'Description_amount': 'You should use only one direct import'}

PEP8_oneletter_names = {'name': 'The names to avoid', 'check': 'avoid_names', 'hint': ['variable'],
                        'letters': '[oOIl]+',
                        'Description': "You shouldn't use letters O, l, I, o for naming variables. They can be misunderstood like a numbers."}

PEP8_constants = {'name': 'The names of constants', 'check': 'constants', 'hint': ['var'],
                  'look': '[A-ZА-ЯΑ-Ω]+[A-ZА-ЯΑ-Ω_0-9]*',
                  'not_should_appear': 'equation_left',
                  'Description_false_const': "You named the variable like constant, but it was changed in ",
                  'Description_const': "You named the variable like simple variable but it const because nowhere is used in left part of equation"}

PEP8_tabs_spaces = {'name': 'The tab and space in expressions', 'check': 'tabs_spaces', 'hint': {'space': 1, 'tab': 0},
                    'Description': "You shouldn't use more than one space or tab between lexems"}

PEP8_indents = {'name': 'The tab and space in start of expr', 'check': 'indents', 'space': 'space', 'tab': 'tab',
                    'Description': "You shouldn't mix tab and space in indents!"}

standard_rules = {
    'PEP8': [PEP8_string_limit, PEP8_names, PEP8_oneletter_names, PEP8_constants, PEP8_newlines, PEP8_imports,
             PEP8_tabs_spaces, PEP8_indents]}

severity = [{"id": 1, "mean": "The big failure"}, {"id": 2, "mean": "The serious problem"},
            {"id": 3, "mean": "The problem"}, {"id": 4, "mean": "Cosmetic problem"}]
priority = [{"id": 1, "mean": "High"}, {"id": 2, "mean": "Medium"},
            {"id": 3, "mean": "Low"}]

first_persons = [{'login': 'admin', 'password': '1a1dc91c907325c69271ddf0c944bc72', 'role': 'Administrator',
                  'rights': [{'db': 'bug_tracking', 'collection': 'bugs'},
                             {'db': 'bug_tracking', 'collection': 'persons'},
                             {'db': 'bug_tracking', 'collection': 'importance'},
                             {'db': 'bug_tracking', 'collection': 'severity'},
                             {'db': 'python', 'collection': 'tokens'},
                             {'db': 'python', 'collection': 'rules'}]},
                 {'login': 'someone', 'password': '202cb962ac59075b964b07152d234b70', 'role': 'Tester',
                  'rights': [{'db': 'bug_tracking', 'collection': 'bugs', 'fields': ['state']},
                             {'db': 'sharp', 'collection': 'tokens'}]}
                 ]

#for GUI
all_methods = {"Lexer": 0, "Parser": 1, "Data usage testing": 2, "Standart testing": 3, "Coverage": 2, "Coverage if": 2, "Cycle testing": 2}
lang_fits = {'.py': 'python', '.txt': 'python', '.cs': 'sharp'}
# COMM = 'comment'
# STR = 'string'
# KEY = 'keyword'
# DEF = 'definition'
# USE = 'use'
# GOTO = 'change flow'
# CYCLE = 'cycle'
# NUM = 'number'
# OP = 'operator'
# NOTUSE = 'error symbol'
# DELIM = 'delimiter'
# WHSPACE = 'whitespace'
#
# LEFTSTRBORDER = border(['\t', " ", "\n", ",", "(", "[", "=", "{", "+", "rb", "br", "rf", "fr", "r", "b", "f", "u"],
#                        {"rb": ['regular', 'byte'],
#                         "br": ['regular', 'byte'], "rf": ['regular', 'func'],
#                         "fr": ['regular', 'func'], "r": ['regular'], "b": ['byte'], "f": ['func'], "u": ['unicode']})
# RIGHTSTRBORDER = border(['\t', " ", "\n", ",", ")", "]", "}", ".", "+", "%", '#', ';', ':'])
# ALLKEYBORDER = border(['\t', ' ', '\n'])
# EXPALLKEYBORDER = border(['\t', ' ', '\n', ';'])
# RIGHTEXPALLKEYBORDER = border(['\t', ' ', '\n', ';', '#'])
# LEFTKEYVERBORDER = border(['\t',' ', '\n', ':', ',', '(', '[', '{', '='])
# RIGHTKEYVERBORDER = border(['\t',' ', '\n', ':', ',', ')', ']', '}', ';', '#'])
# LEFTVARBORDER = border(['\t',' ', '=', ':', '.', '(', '[', '{', ',', '+', '%', '\n', '__', '_'],
#                        {'__': ['Class-private'], '_': ['Not imported']})
# RIGHTVARBORDER = border(['\t', ' ', '=', ':', '.', '+', '%', ')', ']', '}', ',', '\n', '#', ';', '('])
#
# comment = Token(-1, r'#[^\n]*', 'comment', COMM)
#
# simpleStr = Token(0, r'\'[^\n\']*\'', 'simpleStr', STR, LEFTSTRBORDER, RIGHTSTRBORDER)
# simpleDoubleStr = Token(0, r'\"[^\n\"]*\"', 'simpleDoubleStr', STR, LEFTSTRBORDER, RIGHTSTRBORDER)
# multyStr = Token(-1, r'\'\'\'[\d\D]*\'\'\'', 'multyStr', STR, LEFTSTRBORDER, RIGHTSTRBORDER)
# multyDoubleStr = Token(-1, r'\"\"\"[\d\D]*\"\"\"', 'multyDoubleStr', STR, LEFTSTRBORDER, RIGHTSTRBORDER)
#
# lambdaK = Token(1, r'lambda', 'lambdaK', KEY, LEFTKEYVERBORDER, border(['\t', ' ']))
# false = Token(1, r'False', 'false', KEY, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# true = Token(1, r'True', 'true', KEY, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# none = Token(1, r'None', 'none', KEY, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# cond = Token(1, r'if', 'cond', KEY, ALLKEYBORDER,
#              border(['\t', ' ', '\n', '(', '{', '[']))
# secondcond = Token(1, r'elif', 'secondcond', KEY, ALLKEYBORDER,
#              border(['\t', ' ', '\n', '(', '{', '[']))
# nocond = Token(1, r'else', 'nocond', KEY, ALLKEYBORDER, border(['\t', ' ', '\n', ':']))
# andK = Token(1, r'and', 'andK', KEY, border([' ', ')', ']', '}']),
#              border([' ', '(', '{', '[']))
# orK = Token(1, r'or', 'orK', KEY, border([' ', ')', ']', '}']),
#             border([' ', '(', '{', '[']))
# asK = Token(1, r'as', 'asK', KEY, border([' ']), border([' ']))
# isK = Token(1, r'is', 'isK', KEY, border([' ']), border([' ']))
# assertK = Token(1, r'assert', 'assertK', KEY, ALLKEYBORDER, border([' ']))
# classK = Token(1, r'class', 'classK', DEF, EXPALLKEYBORDER, border([' ']))
# defK = Token(1, r'def', 'defK', DEF, EXPALLKEYBORDER, border([' ']))
# fromK = Token(1, r'from', 'fromK', USE, EXPALLKEYBORDER, border([' ']))
# importK = Token(1, r'import', 'importK', USE, EXPALLKEYBORDER, border([' ']))
# globalK = Token(1, r'global', 'globalK', USE, EXPALLKEYBORDER, border([' ']))
# nonlocalK = Token(1, r'nonlocal', 'nonlocalK', USE, EXPALLKEYBORDER, border([' ']))
# breakK = Token(1, r'break', 'breakK', GOTO, border(['\t', ' ']), RIGHTEXPALLKEYBORDER)
# continueK = Token(1, r'continue', 'continueK', GOTO, border(['\t', ' ']), RIGHTEXPALLKEYBORDER)
# passK = Token(1, r'pass', 'passK', GOTO, border(['\t', ' ']), RIGHTEXPALLKEYBORDER)
# raiseK = Token(1, r'raise', 'raiseK', GOTO, border(['\t', ' ']), border(['\t', ' ']))
# returnK = Token(1, r'return', 'returnK', GOTO, border(['\t', ' ']),
#                 border([' ', '(', '[', '{', '#']))
# forK = Token(1, r'for', 'forK', CYCLE, EXPALLKEYBORDER, border([' ', '(']))
# whileK = Token(1, r'while', 'whileK', CYCLE, EXPALLKEYBORDER, border([' ', '(']))
# tryK = Token(1, r'try', 'tryK', KEY, EXPALLKEYBORDER, border([' ', ':']))
# exceptK = Token(1, r'except', 'exceptK', KEY, EXPALLKEYBORDER, border([' ', '(']))
# finallyK = Token(1, r'finally', 'finallyK', KEY, EXPALLKEYBORDER, border([' ', ':']))
# notK = Token(1, r'not', 'notK', KEY, border(['\t', ' ', '(', '=', ':']),
#              border([' ', '(', '{', '[']))
# inK = Token(1, r'in', 'inK', KEY, border([' ', ')', ']', '}']),
#             border([' ', '(', '{', '[']))
# withK = Token(1, r'with', 'withK', KEY, border(['\t', ' ']), border([' ']))
# variable = Token(2, r'[a-zA-Zа-яА-Я]+[a-zA-Zа-яА-Я0-9_]*', 'variable', 'variable', LEFTVARBORDER, RIGHTVARBORDER)
# numberExp = Token(2, r'[-]?[0-9_]*[\.]?[0-9_]+[eE][\-]?[0-9_]*[jJ]?', 'numberExp', NUM, LEFTKEYVERBORDER,
#                   RIGHTKEYVERBORDER)
# numberFloat = Token(2, r'[-]?[0-9_]*\.[0-9_]*[jJ]?', 'numberFloat', NUM, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# number = Token(3, r'[-]?[0-9_]+[jJ]?', 'number', NUM, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# numberBin = Token(2, r'[-]?0[bB][0-1_]+', 'numberBin', NUM, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# numberOct = Token(2, r'[-]?0[oO][0-7_]+', 'numberOct', NUM, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# numberHex = Token(2, r'[-]?0[xX][0-9a-fA-F_]+', 'numberHex', NUM, LEFTKEYVERBORDER, RIGHTKEYVERBORDER)
# sumOp = Token(5, r'\+', 'sumOp', OP)
# subOp = Token(5, r'\-', 'subOp', OP)
# mulOp = Token(5, r'\*', 'mulOp', OP)
# gradOp = Token(4, r'\*\*', 'gradOp', OP)
# divOp = Token(5, r'\/', 'divOp', OP)
# divIntOp = Token(4, r'\/\/', 'divIntOp', OP)
# modOp = Token(5, r'\%', 'modOp', OP)
# bitLeftOp = Token(4, r'\<\<', 'bitLeftOp', OP)
# bitRightOp = Token(4, r'\>\>', 'bitRightOp', OP)
# andOp = Token(5, r'\&', 'andOp', OP)
# orOp = Token(5, r'\|', 'orOp', OP)
# norOp = Token(5, r'\^', 'norOp', OP)
# lesser = Token(5, r'\<', 'lesser', OP)
# greater = Token(5, r'\>', 'greater', OP)
# lesserEq = Token(4, r'\<\=', 'lesserEq', OP)
# greaterEq = Token(4, r'\>\=', 'greaterEq', OP)
# isEq = Token(4, r'\=\=', 'isEq', OP)
# notEq = Token(4, r'\!\=', 'notEq', OP)
# equal = Token(5, r'\=', 'equal', OP)
#
# sumShort = Token(4, r'\+\=', 'sumShort', OP)
# subShort = Token(4, r'\-\=', 'subShort', OP)
# mulShort = Token(4, r'\*\=', 'mulShort', OP)
# gradShort = Token(3, r'\*\*\=', 'gradShort', OP)
# divShort = Token(4, r'\/\=', 'divShort', OP)
# divIntShort = Token(3, r'\/\/\=', 'divIntShort', OP)
# modShort = Token(4, r'\%\=', 'modShort', OP)
# bitLeftShort = Token(3, r'\<\<\=', 'bitLeftShort', OP)
# bitRightShort = Token(3, r'\>\>\=', 'bitRightShort', OP)
# andShort = Token(4, r'\&\=', 'andShort', OP)
# orShort = Token(4, r'\|\=', 'orShort', OP)
# norShort = Token(4, r'\^\=', 'norShort', OP)
#
# leftBracket = Token(3, r'\(', 'leftBracket', DELIM)
# rightBracket = Token(3, r'\)', 'rightBracket', DELIM)
# leftBraceBracket = Token(3, r'\{', 'leftBraceBracket', DELIM)
# rightBraceBracket = Token(3, r'\}', 'rightBraceBracket', DELIM)
# leftSquareBracket = Token(3, r'\[', 'leftSquareBracket', DELIM)
# rightSquareBracket = Token(3, r'\]', 'rightSquareBracket', DELIM)
# dot = Token(3, r'\.', 'dot', DELIM)
# comma = Token(3, r'\,', 'comma', DELIM)
# colon = Token(3, r'\:', 'colon', DELIM)
# semicolon = Token(3, r'\;', 'semicolon', DELIM)
#
# space = Token(3, r'[ ]+', 'space', WHSPACE)
# newline = Token(3, r'\n', 'newline', WHSPACE)
# tab = Token(3, r'\t', 'tab', WHSPACE)
# undefined = Token(6, r'[\$\?\`]+', 'undefined', NOTUSE)
#
# python_tokens = [
#     comment, simpleStr, simpleDoubleStr, multyDoubleStr, multyStr, false, true, none,
#     cond, nocond, andK, orK, asK, isK, assertK, fromK, classK, defK, importK, globalK, nonlocalK, breakK, continueK,
#     passK, returnK, raiseK, forK, whileK, tryK, exceptK, finallyK, notK, inK, variable, numberExp, numberFloat,
#     numberBin, numberHex, numberOct, sumOp, subOp, mulOp, divOp, gradOp, divIntOp, modOp, bitLeftOp, bitRightOp, andOp,
#     orOp, norOp, lesser, greater, lesserEq, greaterEq, isEq, notEq, equal, sumShort, subShort, mulShort, divShort,
#     divIntShort, modShort, bitLeftShort, bitRightShort, andShort, orShort, norShort, leftBracket, rightBracket,
#     leftBraceBracket, rightBraceBracket, leftSquareBracket, rightSquareBracket, dot, comma, colon, semicolon, space,
#     newline, tab, undefined, lambdaK, withK, number
# ]
