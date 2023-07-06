import re

def use_regex(input_text):
    pattern = re.compile(r"<DEBU> \(04:15:48\)> Przeczytano obiekt typu 5 CDC=[0-9]+, sn=[0-9]+, date=16-CZE-2023:04:09:54, dateUTC=16-CZE-2023:02:09:54, dateCDC=3690", re.IGNORECASE)
    return pattern.match(input_text)

def re_find_numbers(input_text):
    return_info = re.findall(r'\b\d+\b', input_text)
    return return_info