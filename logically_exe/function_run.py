import sys
from logically_exe import logic_gates_drawer as lgd, venn_drawer as venn, expression_converter as conv, simplify as simp


def function_parser(func, expression=None):
    if func == "TABLE":
        generate_table(expression)
    elif func == "VENN":
        generate_venn(expression)
    elif func == "CKT":
        generate_circuit(expression)
    elif func == "SIMPLIFY":
        simplify_expression(expression)
    elif func == "DISPLAY":
        generate_display(expression)
    elif func == "HELP":
        show_help()
    elif func == "EXIT":
        exit_case()
    else:
        print("Invalid function.")


def generate_table(env):
    print("Generating truth table:\n")
    expression = conv.env_to_expr(env)
    conv.generate_table(expression, env[0])


def simplify_expression(env):
    print("Simplifying " + str(env[0]))
    expression = conv.env_to_expr(env)
    print(expression)
    variables, minterms = conv.get_minterms(expression)
    print(str(variables))
    print(str(minterms))
    simp.start(minterms, variables)


def generate_circuit(env):
    print("Generating circuit diagram")
    try:
        s = lgd.initDrawSchematic()
        lgd.rec_draw(s, env)
        lgd.drawSchematic(s)
    except Exception:
        return


def generate_venn(env):
    print("Generating venn diagram")
    expr = conv.env_to_expr(env)
    if len(conv.extract_variables(expr)) > 3:
        print("Expression can't have more than 3 variables.")
        return
    else:
        try:
            expression = conv.env_to_expr(env)
            print(str(expression))
            venn.venn(expression)
        except Exception:
            return


def generate_display(env):
    print("Displaying expression:")
    expression = conv.env_to_expr(env)
    print(str(expression))


def show_help():
    str = '''
    To declare an expression:
    out = OP input input ...
    
    Available Operators:
    AND OR NOT XOR NOR NAND XNOR
    
    Available functions:
    TABLE name - generate the truth table for the specified expression.
    SIMPLIFY name - obtain a simplified version of the specified expression.
    DISPLAY name - display in the console the specified expression
    CKT name - draw the logic circuits for the specified expression.
    VENN name - create a Venn diagram for the specified expression.
    DEL name - remove created expression.
    EXIT - close the program.
          '''
    print(str)


def exit_case():
    sys.exit(0)
