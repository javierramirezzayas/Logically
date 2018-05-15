import ply.yacc as yacc
import logically_lex
import function_helper
import logic_gates_drawer

tokens = logically_lex.tokens
env = [list()]
forest = []


def p_assign(p):
    '''
    assign : NAME EQUALS expr term
           | func
    '''
    global forest
    # Create node from expression
    if len(p) > 2:
        p[0] = [p[1], p[3], p[4]]
        count = 0

        if forest is None:  # If there are no expression trees, create one
            forest.append(p[0])
            count = 1
        else:  # Check existing trees to see if one has the expression as an input.
            for i in range(len(forest)):
                forest[i], check = add_node(forest[i], p[0])
                # print(str())
                if check is 1:
                    count = count + 1

        # If expression is not input of any tree then create it as a new expression tree.
        if count is 0:
            forest.append(p[0])
        print(forest)


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
    p[0] = p[1]


def p_term(p):
    '''
    term : NAME term
         | NAME
    '''
    p[0] = list()
    p[0].append(p[1])

    if len(p) is 3:
        p[0] = p[0] + p[2]


def p_func(p):
    '''
    func : TABLE NAME
         | DEL NAME
         | VENN NAME
         | CKT NAME
         | SIMPLIFY NAME
         | HELP
         | EXIT
    '''
    if str(p[1]) == "HELP" or str(p[1]) == "EXIT":
        function_helper.function_parser(p[1])
    else:
        expression = get_node(str(p[2]))
        if expression is None:
            print(p[2] + " is not a declared expression.")
        elif len(expression) < 3:
            print(p[2] + " is an input signal, not an expression.")
        else:
            if p[1] == "DEL":
                delete_node(p[2])
                global forest
                # print(forest)
            else:
                function_helper.function_parser(p[1], expression)


def p_error(p):
    print(p)
    print("Syntax error.")


def add_node(t, p):
    # If tree is empty add expression.
    if t[0] is None:
        t = list(p)
        return t, 1

    # Check if current tree is input of new expression.
    for i in range(len(p[2])):
        if t[0] == p[2][i]:
            p[2][i] = t
            return p, 1

    check = 0

    if len(t) > 2:
        for i in range(len(t[2])):
            # If node has same name as the one inserted replace it.
            if t[2][i][0] is p[0]:
                t[2][i] = p
                check = 1
            # If node is another expression, search that expression
            elif len(t[2][i]) > 1:
                t[2][i], check = add_node(t[2][i], p)

    return t, check


# Function to get an expression from the tree
def get_node(name, t=None):
    global forest
    if t is not None:

        if len(t) > 2:

            for node in t[2]:
                if node[0] == name:
                    return node
                elif len(node) > 2:  # Check if node is part of a child's tree.
                    result = get_node(name, node)
                    if result is not None:
                        return result
        else:
            return None

    else:  # Search every tree for the node
        for tree in forest:

            # If its the first node, return the whole tree
            if tree[0] == name:
                return tree

            elif len(tree) > 2:  # Check every child
                for node in tree[2]:
                    if node[0] == name:
                        return node
                    elif len(node) > 2:  # Check if node is part of a child's tree.
                        result = get_node(name, node)
                        if result is not None:
                            return result

    return None


# Function to delete expression from tree
def delete_node(name, t=None):
    global forest

    if t is not None:
        if len(t) > 2:
            for i in range(len(t[2])):
                if t[2][i][0] == name:
                    t[2][i] = name
                    return t
                elif len(t[2][i]) > 2:  # Check if node is part of a child's tree.
                    t = delete_node(name, t[2][i])
                    return t
        else:
            return t

    else:  # Search every tree for the node
        for i in range(len(forest)):
            # If its the first node, remove the tree
            if forest[i][0] == name:
                forest.remove(forest[i])
                return
            elif len(forest[i]) > 2:  # If tree has children search them
                children = forest[i][2]
                for j in range(len(forest[i][2])):
                    if children[j][0] == name:
                        children[j] = name
                        forest[i][2] = children
                    elif len(children[j]) > 2:  # Check if node is part of a child's tree.
                        children[j] = delete_node(name, children[j])
                        forest[i][2] = children

    return


parser = yacc.yacc()
while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.parse(s)
