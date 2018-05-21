from matplotlib_venn import *
from matplotlib import pyplot as plt

Constants = ['a', 'b', 'c']

Letters = []

def clearLettersArray():
    del Letters[:]

def constantExpression(be):
    newString = ""
    counter = 0
    length = len(be.split())
    for tokens in be.split():
        if len(tokens) != 1 or tokens == '(' or tokens == ')':
            newString = newString + tokens
            length = length - 1
        else:
            newString = newString + Constants[counter]
            counter = counter + 1
            length = length - 1
        if length != 0:
            newString = newString + " "
    return newString

def venn(be):

    set1 = " "
    set2 = " "
    set3 = " "

    set = be.split()

    for token in set:
       if len(token) == 1 and token != '(' and token != ')':
           Letters.append(token)

    if len(Letters) == 1:
        set1 = Letters[0]
        vd = venn2(subsets={'10': 1, '11': 0, '01': 0}, set_labels=(set1, set2))
    elif len(Letters) == 2:
        set1 = Letters[0]
        set2 = Letters[1]
        vd = venn2(subsets={'10':1, '11':1, '01':1}, set_labels=(set1, set2))
    elif len(Letters) == 3:
        set1 = Letters[0]
        set2 = Letters[1]
        set3 = Letters[2]
        vd = venn3(subsets={'111': 1, '001': 1, '010': 1, '011': 1, '100': 1, '101': 1, '110': 1},
                   set_labels=(set1, set2, set3))

    newString = constantExpression(be)

    if (newString == "a"):

        vd.get_patch_by_id('10').set_color('orange')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')

    elif (newString == "not a"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')

    elif (newString == "a and ( b and c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a or ( b or c )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a or b"):

        vd.get_patch_by_id('10').set_color('orange')
        vd.get_patch_by_id('11').set_color('orange')
        vd.get_patch_by_id('01').set_color('orange')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( a or b ) and ( not c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a or b ) or ( not c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and b"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('orange')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "a or ( b and c )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( not b )"):

        vd.get_patch_by_id('10').set_color('orange')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "a and ( ( not b ) or ( a and b ) )"):

        vd.get_patch_by_id('10').set_color('orange')
        vd.get_patch_by_id('11').set_color('orange')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( not a ) and b"):

        vd.get_patch_by_id('10').set_color('orange')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( not a ) and ( b or ( a and b ) )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('orange')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( not a ) and ( b or ( a and ( not b ) ) )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('orange')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')


    elif (newString == "( not a ) and ( not b )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( not a ) and ( ( not b ) or ( a and b ) )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "( not a ) and ( ( not b ) or ( a and ( not b ) ) )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('black')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')


    elif (newString == "( not a ) and ( ( not b ) or ( ( not a ) and b ) )"):

        vd.get_patch_by_id('10').set_color('black')
        vd.get_patch_by_id('11').set_color('black')
        vd.get_patch_by_id('01').set_color('orange')
        vd.get_label_by_id('10').set_text('')
        vd.get_label_by_id('01').set_text('')
        vd.get_label_by_id('11').set_text('')

    elif (newString == "a and ( b and c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( b and ( not c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( b and ( not c ) ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( ( not b ) and c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( ( not b ) and c ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "a and ( ( not b ) and ( not c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or ( ( a and ( b and ( not c ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or ( a and ( ( not b ) and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or  ( ( a and ( ( not b ) and c ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( a and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and c ) )  or ( a and ( b and ( not c ) ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( b and c )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( not a ) and ( b and c ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and c ) ) or ( a and ( b and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and c ) ) or ( ( a and ( b and ( not c ) ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and c ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and c ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "(( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( b and ( not c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( a and ( b and ( not c ) ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( a and ( ( not b ) and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( a and ( ( not b ) and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and ( not c ) ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( ( not b ) and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( not a ) and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( ( not a ) and ( b and c ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and c ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( b and ( not c ) ) ) or ( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( ( not b ) and c )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( a and ( b and c ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( a and ( b and ( not c ) ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( a and ( ( not b ) and c ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and c ) ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) ) )"):

        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( a and ( ( not b ) and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a ) and ( b and c ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a) and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( ( not b ) and ( not c ) ) ) "):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( ( not b ) and c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and c ) ) or ( ( not a ) and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( not a ) and ( ( not b ) and ( not c ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( a and ( b and c ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( a and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( b and ( not c ) ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( a and ( ( not b ) and c ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and c ) ) or ( a and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( a and ( ( not b ) and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( a and ( ( not b ) and ( not c ) ) ) or ( a and ( ( not b ) and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( not a ) and ( b and c ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and c ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and c ) ) or ( a and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and c ) ) or ( a and ( ( not b ) and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( not a ) and ( b and ( not c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and ( not c ) ) ) or ( a and ( ( not b ) and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( b and ( not c ) ) ) or ( ( not a ) and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( not a ) and ( ( not b ) and c ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not b ) and c ) ) or ( a and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not  b ) and c ) ) or ( a and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('orange')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not b ) and c ) ) or ( a and ( ( not b ) and c ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('orange')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not b ) and c ) ) or ( a and ( ( not b ) and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('orange')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not b ) and c ) ) ) or ( ( not a ) and ( b and c ) ) )"):
        vd.get_patch_by_id('001').set_color('black')
        vd.get_patch_by_id('010').set_color('black')
        vd.get_patch_by_id('011').set_color('orange')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('orange')

    elif (newString == "( ( not a ) and ( ( not b ) and ( not c ) ) ) or ( ( ( not a ) and ( ( not b ) and c ) ) ) or ( ( not a ) and ( b and ( not c ) ) ) )"):
        vd.get_patch_by_id('001').set_color('orange')
        vd.get_patch_by_id('010').set_color('orange')
        vd.get_patch_by_id('011').set_color('black')
        vd.get_patch_by_id('100').set_color('black')
        vd.get_patch_by_id('101').set_color('black')
        vd.get_patch_by_id('110').set_color('black')
        vd.get_patch_by_id('111').set_color('black')

    else:
        clearLettersArray()
        return
    plt.title("Venn Diagram: " + be, fontsize=14)
    plt.show()

    clearLettersArray()
