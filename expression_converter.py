from itertools import product
import re


# Function to exchange all operators with those evaluated by python.
def replace_operators(expr):
    REPLACEMENTS = {
        'NOT': ' not ',
        'OR': ' or ',
        'AND': ' and ',
        'XOR': ' ^ ',
        'NAND': ' and ',
        'NOR': ' or ',
        'XNOR': ' ^ ',
    }
    return re.sub('|'.join(re.escape(sym) for sym in REPLACEMENTS.keys()),
                  lambda sym: REPLACEMENTS[sym.group(0)],
                  expr).strip()


# Function to find all variables in a logic expression.
def extract_variables(expr):
    ops = ['not', 'or', 'and', '^']
    vars = sorted(set(re.findall(r'[a-z]+', expr)))

    for op in ops:
        while op in vars:
            vars.remove(op)

    return vars


# Auxiliary function for replacing all negated gates to an equivalent expression
# which python can evaluate.
def replace_negations(expr):
    NEGATIONS = ['NAND', 'NOR', 'XNOR']
    vars = extract_variables(expr)
    op = replace_operators(expr.split()[0])
    newexpr = ""

    for v in vars[0:-1]:
        newexpr = newexpr + v + " " + op + " "

    if len(vars) == 1:
        newexpr = op + " " + vars[0]
    else:
        newexpr = newexpr + vars[-1]

    for op in NEGATIONS:
        if op in expr.split():
            newexpr = "not( " + newexpr + " )"

    return newexpr


# Function to generate the truth table of the logical function
def generate_table(expr):
    vars = extract_variables(expr)
    NO_GLOBALS = {'__builtins__': {}}

    # Print header
    print('\t'.join(vars + [expr]))

    # Print body
    for vals in product(range(2), repeat=len(vars)):
        locals = dict(zip(vars, vals))
        result = int(eval(expr, NO_GLOBALS, locals))
        print('\t'.join([str(v) for v in vals] + [str(result)]))


def get_minterms(expr):
    vars = extract_variables(expr)
    NO_GLOBALS = {'__builtins__': {}}
    minterms = []
    for vals in product(range(2), repeat=len(vars)):
        locals = dict(zip(vars, vals))
        minterms.append(int(eval(expr, NO_GLOBALS, locals)))
    return vars, minterms


def tree_to_string(env):
    expr_list = [list()]
    expr = [str(env[0])]
    string = str(env[1])
    for i in range(len(env[2])):
        node = env[2][i]
        if len(node) < 3:
            string = string + " " + str(node[0])
        else:
            string = string + " " + str(node[0])
            next_strings = tree_to_string(node)
            expr_list = expr_list + next_strings

    expr.append(string)
    expr_list[0] = expr
    return expr_list


# Function to convert the current environment into one equivalent logical expression.
def env_to_expr(env):
    expression_list = tree_to_string(env)
    expression = replace_negations(expression_list[0][1])

    for i in range(1, len(expression_list)):
        if expression_list[i][0] in expression.split():
            temp_expr = replace_negations(expression_list[i][1])
            temp_expr = '( ' + temp_expr + ' )'
            expression = expression.replace(expression_list[i][0], temp_expr)

    return expression
