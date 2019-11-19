import sys

if len(sys.argv) == 1:
    print("USAGE: python command_inline_arg.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
