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
    'DEL',
    'SIMPLIFY',
    'DISPLAY',
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
    'NAND': 'NAND',
    'TABLE': 'TABLE',
    'VENN': 'VENN',
    'CKT': 'CKT',
    'DEL': 'DEL',
    'HELP': 'HELP',
    'SIMPLIFY': 'SIMPLIFY',
    'DISPLAY': 'DISPLAY',
    'EXIT': 'EXIT'
}

t_EQUALS = r'\='
t_ignore = r' '


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
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



