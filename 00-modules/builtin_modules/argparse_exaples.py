import argparse


# small example
def main():
    parser = argparse.ArgumentParser(prog = "echo")
    parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("-a", help="adds hi to echo", action="store_true", dest="a")
    args = parser.parse_args()

    a = args.a
    echo = args.echo

    if(a):
        print("hi", echo)
    else:
        print(echo)




# not small example
def main2():
    def directory(p):
        if(os.path.isdir(p)):
            return p
        else:
            raise argparse.ArgumentTypeError("directory does not exists")

    def path(p):
        if(os.path.isfile(p)):
            return p
        else:
            raise argparse.ArgumentTypeError("file does not exists")

    def dim(d):
        try:
            d = int(d)
            if(d > 0):
                return d
            else:
                raise argparse.ArgumentTypeError()
        except:
            raise argparse.ArgumentTypeError("invalid image dim, Ex: 1280 720")

    parser = argparse.ArgumentParser()

    # group1
    group1 = parser.add_argument_group("group1")
    group1.add_argument("-m", '--path1', dest="path1", metavar="<path>", type=directory, required=True, help='aaa')
    group1.add_argument("-n", '--path2', dest="path2", metavar="<path>", type=path, required=True, help='aaa')

    # group2
    group2 = parser.add_argument_group("group2")
    mutually_exclusive_group = group2.add_mutually_exclusive_group(required=True)
    mutually_exclusive_group.add_argument("-d", dest="path3", metavar="<path>", type=directory, help='aaa')
    mutually_exclusive_group.add_argument("-i", dest="path4", metavar="<path>", type=path, help='aaa')
    

    parser.add_argument('--resize', dest="resize", metavar="<dim>", type=dim, default=False, required=False, nargs=2, help='Resize')

    args = parser.parse_args()








# prog: program name
# usage: usage 
# description: for the text that is shown before the help text
# epilog: for the text shown after the help text
# prefix_chars: ex -a or /a 

my_parser = argparse.ArgumentParser(
prog = "name",
usage = "%(prog)s [options] path",  
description = "List the content of a folder",
epilog = "hi",
prefix_chars = "/"
)


# stores value
parser.add_argument('--foo')
# parser.add_argument('--foo', action='store')
parser.parse_args('--foo 1'.split())
# foo='1'

# stores constant
parser.add_argument('--foo', action='store_const', const=42)
parser.parse_args(['--foo'])
# foo=42

# stores constant true or false value
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
parser.parse_args('--foo --bar'.split())
# foo=True, bar=False, baz=True

# stores list of values added to the argument
parser.add_argument('--foo', action='append')
parser.parse_args('--foo 1 --foo 2'.split())
# foo=['1', '2']

# stores a list, and appends the value specified by the const keyword argument to the list
parser.add_argument('--str', dest='types', action='append_const', const=str)
parser.add_argument('--int', dest='types', action='append_const', const=int)
parser.parse_args('--str --int'.split())
# types=[<class 'str'>, <class 'int'>]

# counts argument
parser.add_argument('--verbose', '-v', action='count', default=0)
parser.parse_args(['-vvv'])
# verbose=3

# version
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.parse_args(['--version'])
# PROG 2.0

# custom help message
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

# other
parser.add_argument(
"-a",
'--argument',
dest='argument_name',
default="rock",
type=str,
help='help message for this parameter',
choices=['rock', 'paper', 'scissors'],
required=True
)


