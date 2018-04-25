import ply.yacc as yacc
import logically_lex

tokens = logically_lex.tokens


def p_assign(p):
    '''
    assign : NAME EQUALS expr term
           | func
    '''
    # print(p[0])


def p_expr(p):
    '''
    expr : OR
         | AND
         | NOT
         | XNOR
         | XOR
         | NAND
         | NOR
         | BUFFER
     '''
    print(p[1])


def p_term(p):
    '''
    term : NAME term
         | NAME
    '''
    print(p[1])


def p_func(p):
    '''
    func : TABLE
         | VENN
         | CKT
         | HELP
         | EXIT
    '''


def p_error(p):
    print(p)
    print("Syntax error.")


parser = yacc.yacc()

while True:
    try:
        s = input('>>>')
    except EOFError:
        break
    parser.parse(s)
