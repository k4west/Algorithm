def solution(str_list):
    if 'l' in str_list and 'r' in str_list:
        if str_list.index('l') < str_list.index('r'):
            a = str_list[:str_list.index('l')]
        else:
            a = str_list[str_list.index('r')+1:]
    elif 'l' in str_list:
        a = str_list[:str_list.index('l')]
    elif 'r' in str_list:
        a = str_list[str_list.index('r')+1:]
    else:
        a = []
    return a