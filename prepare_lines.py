import re_module
import make_dic
import get_lines

def keep_line(line, cdc):
    return_regex = re_module.re_find_numbers(line)
    if len(return_regex) < 6:
        return False
    
    return_dic = make_dic.fill_dic(return_regex)

    #delete line with wrong CDC
    if int(return_dic['cdc']) != cdc:
        return False
        
    #delete lines with commands etc.
    if 'cdc' not in return_dic:
        return False
        
    return True 

def format_file(file_name, cdc):
    getLinesFromFile = get_lines.GetLinesFromFile()
    lines = getLinesFromFile.get_lines_to_list(file_name)
    
    i = 0
    line_indexes_to_remove = []
    
    for line in lines:
        if keep_line(line, cdc) is False:
            line_indexes_to_remove.append(i)
        i += 1
    print(line_indexes_to_remove)

    getLinesFromFile.delete_lines(file_name, line_indexes_to_remove)
