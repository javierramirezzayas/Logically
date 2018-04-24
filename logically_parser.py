import ply.yacc as yacc
import logically_lex
tokens = logically_lex.tokens

def p_assign(p):
    '''assign : NAME EQUALS
              | func'''
    print(p[1] + '=')

def p_expr(p):
    '''expr : AND term
            | OR NAME
            | NOT NAME
            | XNOR term
            | XOR term
            | NAND term
            | NOR term
            | BUFFER NAME'''
    print(p[2])

def p_term(p):
    '''term : NAME term
            | NAME'''

def p_func(p):
    '''func : TABLE
            | VENN
            | CKT
            | HELP
            | EXIT'''

def p_error(p):
    print("Syntax error.")

parser = yacc.yacc()

while True:
    try:
        s = input('>>>')
    except EOFError:
        break
    parser.parse(s)