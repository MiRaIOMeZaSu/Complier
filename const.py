# const.py
# token分类
TOKEN_STYLE = ['KEY_WORD', 'IDENTIFIER', 'DIGIT_CONSTANT',
               'OPERATOR', 'SEPARATOR', 'STRING_CONSTANT']

DETAIL_TOKEN_STYLE = {'abstract': 'ABSTRACT', 'assert': 'ASSERT', 'boolean': 'BOOLEAN', 'break': 'BREAK',
                      'byte': 'BYTE', 'case': 'CASE', 'catch': 'CATCH', 'char': 'CHAR', 'class': 'CLASS', 'const':
                      'CONST',
                      'continue': 'CONTINUE', 'default': 'DEFAULT', 'do': 'DO', 'double': 'DOUBLE',
                          'else': 'ELSE', 'enum': 'ENUM',
                      'extends': 'EXTENDS', 'final': 'FINAL', 'finally': 'FINALLY', 'float': 'FLOAT',
                          'for': 'FOR', 'if': 'IF',
                      'implements': 'IMPLEMENTS', 'import': 'IMPORT', 'instanceof': 'INSTANCEOF', 'interface':
                          'INTERFACE',
                      'package': 'PACKAGE', 'short': 'SHORT', 'int': 'INT', 'long': 'LONG', 'while': 'WHILE',
                          'return': 'RETURN',
                      'switch': 'SWITCH', 'native': 'NATIVE', 'private': 'PRIVATE', 'protected': 'PROTECTED',
                          'public': 'PUBLIC',
                      'static': 'STATIC', 'synchronized': 'SYNCHRONIZED', 'transient': 'TRANSIENT', 'volatile':
                      'VOLATILE',
                      'new': 'NEW', 'this': 'THIS', 'super': 'SUPER', 'void': 'VOID', 'byValue': 'BYVALUE',
                      'cast': 'CAST',
                      'false': 'FALSE', 'true': 'TRUE', 'null': 'NULL', '<': 'LT', '>': 'GT',

                      '++': 'SELF_PLUS', '--': 'SELF_MINUS', '+': 'PLUS', '-': 'MINUS', '*': 'MUL', '/': 'DIV',
                      '>=': 'GET', '<=': 'LET',
                      '(': 'LL_BRACKET', ')': 'RL_BRACKET', '{': 'LB_BRACKET', '}': 'RB_BRACKET', '!=': 'NOT_EQUAL',
                           '[': 'LM_BRACKET', ']': 'RM_BRACKET',
                      ',': 'COMMA', '\"': 'DOUBLE_QUOTE', ';': 'SEMICOLON', '#': 'SHARP', '=': 'ASSIGN'}

# 关键字
keywords = [['int', 'float', 'double', 'char', 'void'],
            ['if', 'for', 'while', 'do', 'else'],
            ['import', 'return', 'package', 'class'],
            ['public', 'private', 'protected', 'static']
            ]
# 运算符
operators = ['=', '&', '<', '>', '++', '--',
             '+', '-', '*', '/', '>=', '<=', '!=', '!']
# 分隔符
delimiters = ['(', ')', '{', '}', '[', ']', ',', '\"', ';']
