from indic_numtowords.hin.data.nums import exceptions_dict
from indic_numtowords.hin.data.nums import direct_dict
from indic_numtowords.hin.data.nums import higher_dict
from indic_numtowords.hin.data.nums import variations_dict
from indic_numtowords.hin.data.nums import symbols_dict

from indic_numtowords.hin.utils import combine

def convert(num):
    final_word_list = []
    word_list1=[""]
    word_list = [""]

    if str(num)[0]=='-':
        word_list = combine(word_list, symbols_dict['-'])
        word_list1 = combine(word_list1, symbols_dict['-'])
        num_str = str(num)[1:].strip()
    else:
        num_str = str(num).strip()
        
    if num_str in exceptions_dict:
        return exceptions_dict[num_str]
    
    
    for i in num_str:
        new_list = direct_dict[i]
        word_list1 = combine(word_list1, new_list)
    final_word_list.extend(word_list1)

    num_str = num_str.lstrip('0')
    n = len(num_str)


    if n == 9 or n == 8:
        #crore case
        temp_num = num_str[:-7]
        lis1 = direct_dict[temp_num]
        lis2 = higher_dict[7]
        inter_list = combine(lis1, lis2)
        word_list = combine(word_list, inter_list)
        num_str = num_str[len(temp_num):]
        num_str = num_str.lstrip('0')
        n = len(num_str)

    if n == 7 or n == 6:
        #lakh case
        temp_num = num_str[:-5]
        lis1 = direct_dict[temp_num]
        lis2 = higher_dict[5]
        inter_list = combine(lis1, lis2)
        word_list = combine(word_list, inter_list)
        num_str = num_str[len(temp_num):]
        num_str = num_str.lstrip('0')
        n = len(num_str)

    if n == 5 or n == 4:
        #thousands case
        temp_num = num_str[:-3]

        if len(temp_num)==1:                             
            word_list_alt = word_list.copy()
            word_list_alt = combine(word_list_alt, direct_dict[num_str[:-2]])
            word_list_alt = combine(word_list_alt, higher_dict[2]+[''])

        lis1 = direct_dict[temp_num]
        lis2 = higher_dict[3]
        inter_list = combine(lis1, lis2)
        word_list = combine(word_list, inter_list)
        num_str = num_str[len(temp_num):]
        num_str = num_str.lstrip('0')
        n = len(num_str)

    if n == 3:
        #hundreds case
        temp_num = num_str[0]
        lis1 = direct_dict[temp_num]
        lis2 = higher_dict[2]
        inter_list = combine(lis1, lis2)
        inter_list.extend(direct_dict[temp_num])
        if num_str in variations_dict:
            final_word_list.extend(combine(word_list, variations_dict[num_str]))
        word_list = combine(word_list, inter_list)
        num_str = num_str[1:]
        num_str = num_str.lstrip('0')
        n = len(num_str)
    
    if n == 2 or n == 1:
        #tens case
        lis2 = direct_dict[num_str]
        lis1 = word_list
        word_list = combine(lis1, lis2)

        if 'word_list_alt' in locals():                      
            lis2 = direct_dict[num_str]
            lis1 = word_list_alt
            word_list_alt = combine(lis1, lis2)
            word_list.extend(word_list_alt)

    final_word_list = word_list + final_word_list
    return [l.strip() for l in final_word_list]
