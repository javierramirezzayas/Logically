import ply.yacc as yacc
import logically_lex
import function_helper

tokens = logically_lex.tokens
env = [list()]


def p_assign(p):
    '''
    assign : NAME EQUALS expr term
           | func
    '''
    expression = env.pop()
    expression.insert(0, p[1])
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
    expr.insert(1, p[1])
    env.append(expr)


def p_term(p):
    '''
    term : NAME term
         | NAME
    '''
    expr = env.pop()
    expr[0] = expr[0] + " " + p[1]
    env.append(expr)


def p_func(p):
    '''
    func : TABLE
         | VENN
         | CKT
         | HELP
         | EXIT
    '''
    function_helper.function_parser(p[1], env)


def p_error(p):
    print(p)
    print("Syntax error.")


parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.parse(s)
