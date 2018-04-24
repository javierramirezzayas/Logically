import ply.lex as lex
import sys

# Implementation of lexical analyzer

# Create Tokens

tokens = [

    'AND',
    'NAND',
    'OR',
    'NOR',
    'XOR',
    'XNOR',
    'NAME',
    'EQUALS',
    'TABLE',
    'VENN',
    'CKT',
    'HELP',
    'NOT',
    'BUFFER',
    'EXIT'

]


t_AND = r'\AND'
t_NAND = r'\NAND'
t_OR = r'\OR'
t_NOR = r'\NOR'
t_XOR = r'\XOR'
t_XNOR = r'\XNOR'
t_EQUALS = r'\='
t_TABLE = r'\TABLE'
t_VENN = r'\VENN'
t_CKT = r'\CKT'
t_HELP = r'\HELP'
t_NOT = r'\NOT'
t_BUFFER = r'\BUFFER'
t_EXIT = r'\EXIT'
t_ignore = r' '


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal Character(s)")
    t.lexer.skip(1)

lexer = lex.lex()

