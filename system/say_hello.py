import os
import sys

def hello(name):
    print(f'Hello, {name}!')
def usage():
    print('USAGE python say_hello.py --name <name>') 
if(__name__ == '__main__'):
    name_arg = '--name'
    if '--help' in sys.argv:
        usage()
        exit(0)
    if name_arg in sys.argv:
        name_index = sys.argv.index(name_arg)
        if name_index >= len(sys.argv) or name_index + 1 >= len(sys.argv):
            usage()
            exit(1)
        hello(sys.argv[name_index+1])
    else:
        hello(os.getlogin())
