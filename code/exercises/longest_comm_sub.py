def get_LCS(iv_string_1, iv_string_2):
    #for an absolutely unknown god damn reason, this declares first the columns and then the lines.
    lv_previous_results =  [ [ None for i in range(len(iv_string_2)) ] 
                                    for j in range(len(iv_string_1)) ] 

    return get_LCS_helper(iv_string_1, iv_string_2, 0, 0, lv_previous_results);


def get_LCS_helper(iv_string_1, iv_string_2, index_1, index_2, iv_previous_results):
    if (index_1 >= len(iv_string_1)  or 
        index_2 >= len(iv_string_2) ):
        return "";

    if (iv_previous_results[index_1][index_2] != None):
        return iv_previous_results[index_1][index_2];
 
    if (iv_string_1[index_1] == iv_string_2[index_2]):
        iv_previous_results[index_1][index_2] = iv_string_1[index_1] + get_LCS_helper(iv_string_1, iv_string_2, index_1 + 1, index_2 + 1, iv_previous_results);
        return iv_previous_results[index_1][index_2];

    result_1 = get_LCS_helper(iv_string_1, iv_string_2, index_1+1, index_2, iv_previous_results);
    result_2 = get_LCS_helper(iv_string_1, iv_string_2, index_1, index_2+1, iv_previous_results);

    iv_previous_results[index_1][index_2] = result_1 if len(result_1) > len(result_2) else result_2;
    return iv_previous_results[index_1][index_2];


def test():
    print(
        get_LCS(
            input("1: "),
            input("2: ")
        )
    );