def get_module(iv_script):
    if  (iv_script == 'flatten_list'    ): from exercises.flatten_list     import test 
    elif(iv_script == 'longest_comm_sub'): from exercises.longest_comm_sub import test 
    else: raise Exception ("module %s not found" % (iv_script))
    return test
    