import re

def find_number_test(string):
    regex_num = re.compile('\d+')
    return regex_num.findall(string)[0]

def find_number_flow(string):
    regex_num = re.compile('\d{3}')
    return regex_num.findall(string)[1]

def find_number_user(string):
    regex_num = re.compile('\d+')
    return regex_num.findall(string)[3]

def find_type_flow(string):
    regex_word = re.compile('\D+')
    r = regex_word.findall(string)
    return re.sub(' |_', '', r[3])

def replace_character(string):
    replace_list1 = ["-", ')', '(']
    for i in replace_list1:
        string = string.replace(i, '')
    replace_list2 = ['/', '-', ' ' ]
    for i in replace_list2:
        string = string.replace(i, '_')
    return string