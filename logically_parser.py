import ply.yacc as yacc
import logically_lex

tokens = logically_lex.tokens
env = [list()]


def p_assign(p):
    '''
    assign : NAME EQUALS expr term
           | func
    '''
    # print(p[1])
    expression = env.pop()
    # print(expression)
    expression.insert(0, p[1])
    # print(expression)
    env.append(expression)
    env.append(list())
    print(env)


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
    expr = env.pop()
    expr.insert(0, p[1])
    env.append(expr)

def p_term(p):
    '''
    term : NAME term
         | NAME
    '''
    expr = env.pop()
    expr.append(p[1])
    env.append(expr)


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
