import argparse

my_parser = argparse.ArgumentParser(
        prog="calculator",
        description="a simple calculator",
        usage="%(prog)s [options] operator first second",
        epilog="Thanks for using the calculator!",
        # prefix_chars='/',
        # allow_abbrev=False,
        # add_help=False
)

my_parser.add_argument("operator",
                        #type="str", 
                        help="operator to run",
                        choices=["plus","minus"])

my_parser.add_argument('-f',
                       '--first',
                       action='store',
                       type = int,
                       help='the first element in the operator',
                       required=True)

my_parser.add_argument('-s',
                       '--second',
                       action='store',
                       type = int,
                       help='the second element in the operator',
                       required=True)

my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='enable the detailed info')

# list of three elements
# my_parser.add_argument('--input', action='store', type=int, nargs=3)

args = my_parser.parse_args()

operator = args.operator
first = args.first
second = args.second
verbose = args.verbose
#print(vars(args))


result = first+second if operator=="plus" else first-second
if verbose:
    print(f"{first} {operator} {second} = {result}")
else:
    print(result)