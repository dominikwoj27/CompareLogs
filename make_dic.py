CDC_INDEX = 4
SERIAL_NUMBER_INDEX = 5

def fill_dic(input_list):
    filled_dic = {'cdc': input_list[CDC_INDEX], 'sn': input_list[SERIAL_NUMBER_INDEX] } 
    return filled_dic