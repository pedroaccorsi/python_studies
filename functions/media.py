# to create functions, the syntax is: def name_of_func(parameters):

def get_mean(iv_list):
    return sum(iv_list) / len(iv_list);
      
lv_mean = get_mean([10,3,4,5,6,7,7,4,4,5,6,6,]);

print(lv_mean);