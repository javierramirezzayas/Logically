import sys
import expression_converter as conv


def function_parser(func, env):
    if func == "TABLE":
        generate_table(env)
    elif func == "VENN":
        generate_venn(env)
    elif func == "CKT":
        generate_circuit(env)
    elif func == "HELP":
        show_help()
    elif func == "EXIT":
        exit_case()
    else:
        print("Invalid function.")


def generate_table(env):
    print("The truth table is: ")
    env.pop()
    expression = conv.env_to_expr(env)
    print(expression)
    conv.generate_table(expression)
    env.append(list())


def generate_circuit(env):
    print("Generate circuit diagram")


def generate_venn(env):
    print("Generate venn diagram")


def show_help():
    print("Here goes help with function descriptions.")


def exit_case():
    sys.exit(0)
