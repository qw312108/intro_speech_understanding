

def cancellation(list, stop_word):
    output_list=[]
    for item in list:
        if item == stop_word:
            break 
        output_list.append(item) 

    return output_list
    
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    pass

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []

    for item in input_list:
        if item != skip_word:
            output_list.append(item)

    return output_list
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    pass

def my_average(input_list):
    total = 0 
    count = 0 

    for item in input_list:
        if isinstance(item, (int, float)):
            total += item
            count += 1

    if count == 0:
        raise ValueError("输入列表中没有有效的数字元素")

    average = total / count
    return average
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    pass

