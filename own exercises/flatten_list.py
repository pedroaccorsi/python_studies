def flatten_list(iv_list):

    if(iv_list): 
        return __flatten_list(iv_list, [])
          
    raise Exception ("Invalid input: %s" % iv_list)

def __flatten_list(iv_list, cv_ret_list):

    if( type(iv_list) != list ):
        cv_ret_list.append(iv_list)
    else:
        for element in iv_list:
            cv_ret_list = __flatten_list(element, cv_ret_list)

    return cv_ret_list     

list_a = [ 1, 3, [ [4, 5, [6] ], [[[[[[[[[[[7,[[]]]]]]]]]]]]] ] ]
list_b = None

try:
    print( flatten_list( list_a ) )
    print( flatten_list( list_b ) )
except Exception as e:
    print(e)

