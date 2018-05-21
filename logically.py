import sys
import logically_parser as parser


def read_file(name):
    print("Loading " + name)
    try:
        file = open(name, 'r')
        line = file.readline()
        while line:
            if '//' not in line and len(line.strip()) > 1 and 'EXIT' not in line:
                parser.do_parse(line.strip())
            line = file.readline()
    except Exception:
        print("No such file found.")
        return


if len(sys.argv) > 1:
    if sys.argv[1] == '-h':
        s = '''
logically.py filename.lly  - reads a file named \"filename\" and executes it.
                             File extension must be \".lly\"
        '''
        print(s)
        sys.exit()
    elif sys.argv[1][-4:] != '.lly':
        print("File extension must be \".lly\" ")
        sys.exit()

    print("Welcome to logically")
    print("(pre-alpha) ver. 1.0.0")
    print("")
    read_file(sys.argv[1])

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.do_parse(s)
