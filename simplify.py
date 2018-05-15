
# Begins the simplification process
def start(minterms, variables):
    result = decimalToBinary(minterms, len(variables))
    table = firstStep(result)
    constructDictionary(table)
    makeGroupingTable()
    makeQuantitiesTable()

    # print (" ")
    # printgroupingTable()
    # print (" ")
    # printMinsQtyTable()
    # print (" ")
    simplify()
    printStringArray()
    return


def decimalToBinary(minList, numOfVar):
    minterms = []
    string = ""

    for x in range(0, len(minList)):
        # print "x: ",x
        # print "minLis [x]: ",minList[x]
        # print
        if (minList[x] == 1):
            string = bin(x)
            string = string[2:len(string)]
            if (len(string) < numOfVar):
                for y in range(0, numOfVar - len(string)):
                    string = "0" + string
            minterms.append(string)
        # print string
        # print

    return minterms


# Verifies if the binary number 1 has the same number of 1's
# where the binary number 2 where bin1 and bin2 are strings
def equalbits(bin1, bin2):
    count1 = 0
    count2 = 0
    equal = False
    for x in bin1:
        if (x == "1"):
            count1 += 1
    for y in bin2:
        if (y == "1"):
            count2 += 1
    if (count1 == count2):
        equal = True
    return equal


# Verifies whether a given element is in the list.
# Used to avoid repetitions in groups or extra groups
def check(lists, element):
    if (len(lists) == 0):
        return False
    for x in lists:
        if (x == element):
            return True
    return False


##Creates the first table with the grouped minterms
# def firstStep(minterms)
##def firstStep(minterms,matchedPair):
def firstStep(minterms):
    group = 0
    matchedPair = {}
    checkedPairs = []
    unCheckedPairs = []
    strCPair = []
    strUcPair = []
    mins = {}

    # matchedPair = {}
    list1 = []
    for x in minterms:
        ##print("mins: "+mins)
        ##print("group: "+str(group))
        ##print mins
        ##print("run: "+str(group))
        matchedPair[group] = []
        mins[group] = []

        if (check(list1, x) == False):
            mins[group].append(x)
            matchedPair[group].append(x)
            list1.append(x)
        ##minterms.remove(mins)
        ##print (minterms)
        for y in range(group + 1, len(minterms)):
            ##print ("x: "+mins)
            if (check(list1, minterms[y]) == False):
                if (equalbits(x, minterms[y])):
                    # print ("Condition: True")
                    mins[group].append(minterms[y])
                    matchedPair[group].append(minterms[y])
                    list1.append(minterms[y])
                    ##list1.append(minterms[x])
                    ##print list1
        if (len(mins[group]) != 0):
            group = group + 1
        ##print(mins)
        ##print ("element: "+minterms[x])
        ##group = group+
    # print "First Step"
    # print"minterms:"
    # print mins
    # print "grouped minterms"
    # print matchedPair
    # print
    # secondStep(firstStep(minterms,matchedPair),cPairs, ucPairs,matchedPair)
    matchedPair = secondStep(mins, checkedPairs, unCheckedPairs, matchedPair, strCPair, strUcPair)
    # lastStep(ucPairs,ml3)

    # print
    # print ("###########")
    # print ("Last Step #")
    # print ("###########")
    # print
    # print unCheckedPairs
    # print matchedPair
    Table = lastStep(unCheckedPairs, strUcPair)
    # print "Table"
    # print Table

    return Table


# mPair = Prime Implicants
# mInv = Minterms Involved
# def secondStep(mPair,cPair,ucPair):
def secondStep(minterms, cPair, ucPair, groupedMinterms, strCPair, strUcPair):
    # print ("###############")
    # print ("# Second Step #")
    # print ("###############")
    # print "Second Step"
    # print"minterms/mPair:"
    # print minterms
    # print "grouped minterms/mInv"
    # print groupedMinterms
    # print "checked:"
    # print cPair
    # print "unchecked"
    # print ucPair
    # print "Str checked:"
    # print strCPair
    # print "Str unchecked"
    # print strUcPair
    # print

    key = 0
    minPair = {}
    minInv = {}
    group = 0

    pointer1 = 0
    pointer2 = 0

    while (group < len(minterms) - 1):

        minPair[group] = []
        minInv[group] = []
        # print "key: ",group
        for mins1 in minterms[group]:

            for mins2 in minterms[group + 1]:
                # print "mins1: ",mins1
                # print "mins2: ",mins2
                # compare minterm1 and minterm2 for a change in a single bit.
                # Construct al tables in the process
                # compMinterm(mins1,mins2,groupedMinterms[group][pointer1],groupedMinterms[group+1][pointer2],minPair[group],cPair,ucPair,strCPair,strUcPair)
                compMinterm(mins1, mins2, groupedMinterms[group][pointer1], groupedMinterms[group + 1][pointer2],
                            minPair[group], minInv[group], cPair, ucPair, strCPair, strUcPair)
                # minInv[group].append(groupedMinterms[group][pointer1]+"-"+groupedMinterms[group+1][pointer2])

                # print "group: ",minPair[group]
                # print
                pointer2 += 1
            pointer1 += 1
            pointer2 = 0

        pointer1 = 0
        pointer2 = 0
        if (len(minPair[group]) == 0):
            del (minPair[group])
        if (len(minInv[group]) == 0):
            del (minInv[group])
        group = group + 1

    if (len(minPair) == 0):
        if (len(minterms) == 1):
            pointer3 = 1
            gPointer = 1
            ucPair.append(minterms[0][0])
            # print"Hello",groupedMinterms[0][0]
            strUcPair.append(groupedMinterms[0][0])

            while (pointer3 < len(minterms[0]) - 1):
                if (minterms[0][pointer3] != minterms[0][pointer3 + 1]):
                    ucPair.append(minterms[0][pointer3 + 1])
                pointer3 += 1

            while (gPointer < len(groupedMinterms[0]) - 1):
                if (groupedMinterms[0][gPointer] != groupedMinterms[0][gPointer + 1]):
                    strUcPair.append(groupedMinterms[0][gPointer + 1])
                gPointer += 1

        removeChecked(cPair, ucPair)
        removeChecked(strCPair, strUcPair)

        # print ("##########")
        # print ("# RETURN #")
        # print ("##########")
        # print
        # print"minterms/mPair:"
        # print minterms
        # print
        # print "grouped minterms/mInv"
        # print groupedMinterms
        # print
        # print "checked:"
        # print cPair
        # print
        # print "unchecked"
        # print ucPair
        # print
        # print "Str checked:"
        # print strCPair
        # print
        # print "Str unchecked"
        # print strUcPair
        # print
        return minterms

    return secondStep(minPair, cPair, ucPair, minInv, strCPair, strUcPair)


def compMinterm(minterm1, minterm2, grminterm1, grminterm2, minterms, groupedMinterms, cPair, ucPair, strCPair,
                strUcPair):
    # print "compMinterm"

    count = 0
    pointer = 0
    groupMins = False
    for bit in range(0, len(minterm1)):
        if (minterm1[bit] != minterm2[bit]):
            count += 1
            pointer = bit

    # print count
    # print "minterm1",minterm1
    # print "minterm2",minterm2
    if (count == 1):
        # Making a list of all the minterms that paired together.
        # Making a list of all the grouped minterms that paired together
        # Verifies always that minterm 1 is on checked list to avoid repetitions.
        if (check(cPair, minterm1) == False):
            cPair.append(minterm1)
        if (check(strCPair, grminterm1) == False):
            strCPair.append(grminterm1)
            # Listing all of the groped minterms together
        # strCPair.append(minterm2)

        strCPair.append(grminterm2)

        cPair.append(minterm2)

        # Changes the bit position for underscore
        x = list(minterm2)
        x[pointer] = "_"
        minterm2 = "".join(x)

        # Appending the modified minterm
        minterms.append(minterm2)
        groupedMinterms.append(grminterm1 + "-" + grminterm2)

        return True
    else:
        # Making a list of all unchecked Minterms that couldn't make a group
        if (check(ucPair, minterm1) == False):
            ucPair.append(minterm1)
            # strUcPair.append(grminterm1)
        if (check(ucPair, minterm2) == False):
            ucPair.append(minterm2)
            # strUcPair.append(grminterm2)
        if (check(strUcPair, grminterm1) == False):
            strUcPair.append(grminterm1)
            # strUcPair.append(grminterm1)
        if (check(strUcPair, grminterm2) == False):
            strUcPair.append(grminterm2)

    return False

    # print minterm2
    # return minterm2
    ##if(check(cPair,minterm2)==False):
    ##cPair.append(minterm2)


def removeChecked(cPair, ucPair):
    counter1 = 0
    counter2 = 0
    while (counter1 < len(cPair)):

        while (counter2 < len(ucPair)):
            if (cPair[counter1] == ucPair[counter2]):
                ucPair.remove(ucPair[counter2])
            else:
                counter2 = counter2 + 1
        counter1 = counter1 + 1
        counter2 = 0


def binaryToDecimal(num):
    # print num
    exp = len(num)
    decimal = 0
    for bit in num:
        # print bit
        if (bit == "1"):
            decimal = decimal + pow(2, exp - 1)
        exp = exp - 1
    # print decimal
    return decimal


# Prime Implicants = unchecked Pairs
# Minterms Involved = grouped minters
def compareList(list1, list2):
    counter = 0
    equalList = False
    for lists in list2:
        # print "lists: ",lists
        # print "list1: ",list1
        for x in lists:
            for y in list1:
                if (x == y):
                    counter += 1
        if (counter == len(list1)):
            return True
        counter = 0
    return False


def lastStep(uncheckedPairs, GroupedMinterms):
    # print("unchecked Pairs: ", uncheckedPairs)
    # print "length UP",len(uncheckedPairs)
    # print("Grouped Minterms", GroupedMinterms)
    # print "length GM",len(GroupedMinterms)
    # print

    listOfMins = []
    list1 = []
    list2 = []

    decimal = 0

    binary = []
    strDecimal = ""
    PrimeImplicants = {}
    pointer = 0  # Minterm Pointer

    dictionary = {}
    table = []

    gpPointer = 0  # grouped minterm Pointer
    for minterms in GroupedMinterms:

        # print "minterms: ",minterms
        # print "Lenght: ",len(minterms)
        # print "bit2: ",minterms[8]

        for bit in minterms:
            # print bit

            if (bit != "-" and pointer != (len(minterms))):
                # strDecimal = strDecimal+bit
                binary.append(bit)
                # print "binary: ",binary
                # print
            else:
                decimal = binaryToDecimal(binary)
                # print "decimal: ",decimal

                strDecimal = strDecimal + str(decimal) + ","
                list1.append(decimal)

                binary = []

            pointer += 1

        decimal = binaryToDecimal(binary)

        list1.append(decimal)
        # print "list1: ", list1
        # print "list2: ", list2
        # print (compareList(list1,list2))
        # print

        if ((compareList(list1, list2)) == False and gpPointer < len(uncheckedPairs)):
            list2.append(list1)
            strDecimal += str(decimal)
            dictionary[uncheckedPairs[gpPointer]] = strDecimal
            table.append(dictionary)
            gpPointer += 1

        # print "decimal: ",binaryToDecimal(binary)
        # print "strDecimal: ",strDecimal
        # print "list1: ", list1
        # print "list2: ", list2

        strDecimal = ""
        list1 = []
        pointer = 0
        binary = []
        dictionary = {}

        # print
        # print "table: ",table
        # print "strDecimal: ",strDecimal
        # print "Binary: ",binary
    return table


############################################################################
#                              YORKIS PART                                 #
############################################################################
import re

# ============================================================================== #
Letters = {

    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k"

}

# ============================================================================== #
#                                  METHODS                                       #
# ============================================================================== #

minternsTable = []
quantitiesTable = {}
groupingTable = {}
stringArray = []


# Constructs array of dictionaries that will be used to construct the table
def constructDictionary(Dict):
    for dict in Dict:
        dummyDict = {}
        for k, v in dict.items():
            dummyDict["min"] = v
            dummyDict["binary"] = k
        minternsTable.append(dummyDict)


# Constructs table that saves the quantity of each minterm on the equation
def makeQuantitiesTable():
    numbersArray = []
    for row in minternsTable:
        positions = re.findall(r"(\d+\.?\d*)", row["min"])
        for digit in positions:
            numbersArray.append(int(digit))
        numbersArray.sort()
    for num in numbersArray:
        if num not in quantitiesTable:
            quantitiesTable[num] = 1
        else:
            quantitiesTable[num] = quantitiesTable[num] + 1


# Constructs the X's table
def makeGroupingTable():
    for row in minternsTable:
        array = re.findall(r"(\d+\.?\d*)", row["min"])
        group = getRepresentation(row["binary"])
        if group not in groupingTable:
            groupingTable[group] = []
            for digit in array:
                groupingTable[group].append(int(digit))
        else:
            groupingTable[group].append(int(digit))


# Main method that simplifies the boolean expression
def simplify():
    checkForTermsWithOneX()
    lookForBestCandidate()


# First step : Save groups that have unique minterms
def checkForTermsWithOneX():
    for k, v in quantitiesTable.items():
        if v == 1:
            findTerm(k)


# Finds the alphabetic term to which the minterm corresponds
def findTerm(key):
    for k, v in groupingTable.items():
        for digit in v:
            if digit == key and k not in stringArray:
                stringArray.append(k)
                for iter in v:
                    changeMinQtyToCero(iter)


# Changed the quantity to zero in the quantity table of a minterm that is being groupd
def changeMinQtyToCero(min):
    if min in quantitiesTable:
        quantitiesTable[min] = 0


# Second Step : Look for the alphabetic term that impacts the most minterms.
# This one is the one that would be grouped next
def lookForBestCandidate():
    while checkForRemainingMins() == False:
        maxTerm = selectCandidate()
        if maxTerm not in stringArray:
            stringArray.append(maxTerm)
        mins = returnMinsOfThisTerm(maxTerm)
        for min in mins:
            changeMinQtyToCero(min)


# Helper method to the lookForBestCandidate method which selects the best candidate to group next
def selectCandidate():
    max = 0
    candidate = "null"
    for term in groupingTable:
        values = returnMinTermsImpacted(term)
        if values > max:
            max = values
            candidate = term
    return candidate


# Returns an array of the minterms corresponding to a specific alphabetic term
def returnMinsOfThisTerm(term):
    mins = []
    if term in groupingTable:
        for digit in groupingTable.get(term):
            if quantitiesTable.get(digit) > 0:
                mins.append(digit)
    return mins


# Helper method of the lookForBestCandidate method which returns the the quantity of minterms impacted
# by grouping a specific term
def returnMinTermsImpacted(term):
    max = 0
    if term in groupingTable:
        sum = 0
        for digit in groupingTable.get(term):
            quantityLeft = quantitiesTable.get(digit)
            if quantityLeft > 0:
                sum = sum + quantityLeft
        if sum > max:
            max = sum
    return max


# Method that checks if there are minterms ungrouped.
# Returns true when all minterms were grouped.
def checkForRemainingMins():
    for k, v in quantitiesTable.items():
        if v != 0:
            return False
    return True


# Changes the binary representation of a term of the boolean expression to its alphabetic representation
def getRepresentation(element):
    counter = 0
    result = ""
    for char in element:
        if char == "_":
            counter += 1
        elif char == "0":
            result = result + "-" + Letters[counter]
            counter += 1
        elif char == "1":
            result += Letters[counter]
            counter += 1
    return result


# ============================================================================== #
#                           HELPER METHODS                                       #
# ============================================================================== #


def printMinsQtyTable():
    print("Quantity Table: ")
    for k, v in quantitiesTable.items():
        print(str(k) + ":   \t\t " + str(v))


def printgroupingTable():
    print("Grouping Table: ")
    for k, v in groupingTable.items():
        print(str(k) + ":   \t\t " + str(v))


def printStringArray():
    count = len(stringArray)
    counter = 1
    result = " "
    for term in stringArray:
        result = result + term
        if counter != count:
            result = result + " + "
        counter = counter + 1
    print("Result: ")
    print(result)


# ============================================================================== #
#                             TESTING                                            #
# ============================================================================== #


# testArray = [{'_00_' : '0,1,8,9'}, {'_0_1' : '1, 3, 9, 11'}, {'__11': '3, 7, 11, 15'}]
# minterms = ["0000", "0001", "0011", "0111", "1000", "1001", "1011", "1111"]
#
# minterms = ["0000", "0001", "0011", "0111", "1000", "1001", "1011", "1111"]
# minterms2 = ["0100", "1000", "1010", "1011", "1100", "1111"]
# minterms3 = ["00000", "00001", "00010", "01000", "00011", "00110", "01001", "01010", "10001", "10100", "01011", "10101",
#              "11001", "11100", "10111", "11110", "11111"]
# minterms4 = ['001', '010', '011', '100', '101', '110', '111']
# minterms5 = ['000001', '000010', '000011', '000100', '000111', '100000', '010000', '001000']

# var = ['a','b','c']
# print "var",len(var)
# st = "abc"
# print "st",len(st)
# variables1 = ['a', 'b', 'c', 'd']
# variables2 = ['a', 'b', 'c']
# variables3 = ['a', 'b', 'c', 'd', 'e']
# mins = [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
# mins2 = [0, 1, 1, 1, 1, 1, 1, 1]
# mins3 = [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]
# start(mins,variables1)
# start(mins2,variables2)
# start(mins3,variables3)
# start(mins3, variables3)
# constructDictionary(start(mins2,variables2))
# start(mins,variables1)
# makeGroupingTable()
# makeQuantitiesTable()

# print (" ")
# printgroupingTable()
# print (" ")
# printMinsQtyTable()
# print (" ")

# simplify()
# printStringArray()

############################################################################
#                              END PART                                 #
############################################################################



