import sys
from   util import *

if __name__ == '__main__':

    try:
        test = get_module( sys.argv[1] )
        test()
    except Exception as e:
        print(e)