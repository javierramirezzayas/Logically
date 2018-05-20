from matplotlib_venn import *
from matplotlib import pyplot as plt

Constants = ['a', 'b', 'c']

Letters = []


def clearLettersArray():
    del Letters[:]


def constantExpression(be):
    newString = be
    counter = 0
    for count in Letters:
        newString = newString.replace(count, Constants[counter])
        counter = counter + 1
    return newString


def venn(be):
    set1 = " "
    set2 = " "
    set3 = " "

    set = be.split()

    for token in set:
        if token != 'and' and token != 'or' and token != '(' and token != ')' and token != 'not':
                Letters.append(token)

    if len(Letters) == 1:
        set1 = Letters[0]
    elif len(Letters) == 2:
        set1 = Letters[0]
        set2 = Letters[1]
    elif len(Letters) == 3:
        set1 = Letters[0]
        set2 = Letters[1]
        set3 = Letters[2]

    newString = constantExpression(be)
    print ("NEW STRING " + newString)

    vd = venn3(subsets={'111': 1, '001': 1, '010': 1, '011': 1, '100': 1, '101': 1, '110': 1},
               set_labels=(set1, set2, set3))

    if (newString == "a"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( not a )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "a and b and c"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a or b or c"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a or b"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a or ( b and c )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(a or b) and ( not c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "b"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')


    elif (newString == "( not b )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "c"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( not c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "a and b"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( not b )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "a or ( not b )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b )) or (a and b)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( not a ) and b"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b) or (a and b)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and b) or ( a and ( not b))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')


    elif (newString == "( not a ) and ( not b )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b )) or (a and b)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b )) or (a and ( not b ))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b )) or ( not a ) and b)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and b and c"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and b and ( not c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and b and ( not c )) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( not b ) and c"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b ) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(a and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b) and c) or (a and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( not b) and ( not c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b ) and ( not c )) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(a and ( not b) and ( not c)) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b) and ( not c)) or (a and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(a and ( not b) and ( not c)) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(a and ( not b) and ( not c)) or (a and ( not b) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(a and ( not b) and ( not c)) or (a and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and b and c"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and ( not c)) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and c) or (a and ( not b) and ( not c)) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and b and ( not c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and ( not c)) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and ( not c)) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (a and ( not b) and ( not c)) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (( not a ) and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (( not a ) and b and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and b and ( not c)) or (( not a ) and b and c) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and b and ( not c)) or (( not a ) and b and c) or (a and ( not b) and ( not c))"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( not b) and c"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and b and ( not c)) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and c)"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and c) or (a and b and c)"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and c) or (a and b and ( not c))"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and ( not c)) or (a and b and c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and ( not c)) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (a and ( not b) and ( not c)) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and c) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and c) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and c) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c)) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c)) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c)) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c)) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and c) or (( not a ) and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( not b) and ( not c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and b and ( not c)) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and c) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and c) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and ( not c)) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and ( not c)) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (a and ( not b) and ( not c)) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and c) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and c) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and c) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and c) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and ( not c)) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and ( not c)) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and ( not c)) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and b and ( not c)) or (( not a ) and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (a and b and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (a and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (a and ( not b) and c)"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (a and ( not b) and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (( not a ) and b and c)"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "(( not a ) and ( not b) and ( not c)) or (( not a ) and ( not b) and c) or (( not a ) and b and ( not c))"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    else:
        print("Unable to draw expression.")

    plt.title("Venn Diagram: " + be, fontsize=14)
    plt.show()

    clearLettersArray()


# venn("x")
# venn("f")
# venn("a and ( not v)")
# venn("a and b and ( not c)")
