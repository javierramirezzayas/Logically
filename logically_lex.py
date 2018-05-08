import ply.lex as lex
import sys

# Implementation of lexical analyzer

# Create Tokens

tokens = [

    'NAND',
    'AND',
    'OR',
    'NOR',
    'XOR',
    'XNOR',
    'NOT',
    'BUFFER',
    'NAME',
    'EQUALS',
    'TABLE',
    'VENN',
    'CKT',
    'HELP',
    'EXIT'
]

reserved = {
    'AND': 'AND',
    'OR': 'OR',
    'NOR': 'NOR',
    'XOR': 'XOR',
    'XNOR': 'XNOR',
    'NOT': 'NOT',
    'TABLE': 'TABLE',
    'VENN': 'VENN',
    'CKT': 'CKT',
    'HELP': 'HELP',
    'EXIT': 'EXIT'
}



# t_NAND = r'\NAND'
# t_AND = r'\AND'
# t_OR = r'\OR'
# t_NOR = r'\NOR'
# t_XOR = r'\XOR'
# t_XNOR = r'\XNOR'
# t_NOT = r'\NOT'
t_EQUALS = r'\='
# t_TABLE = r'\TABLE'
# t_VENN = r'\VENN'
# t_CKT = r'\CKT'
# t_HELP = r'\HELP'
# t_EXIT = r'\EXIT'
t_ignore = r' '


def t_NAME(t):
    r'[a-zA-Z][0-9a-zA-Z]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t


def t_error(t):
    print("Unrecognized Character(s)")
    # print(t)
    t.lexer.skip(1)

lexer = lex.lex()



