import os
import prepare_lines

first_log_name = input('please enter first log file name: \n')
second_log_name = input('please enter secosdnd log file name: \n')
cdc_date = input('please enter cdc date of logs to compare: \n')

cwd = os.getcwd()
first_log_name = cwd + "\\" + first_log_name + ".txt"
second_log_name = cwd + "\\" + second_log_name + ".txt"

prepare_lines.format_file(first_log_name, int(cdc_date))
prepare_lines.format_file(second_log_name, int(cdc_date))

#calculate the difference with git diff, and save to file diff-cdc_number.txt
command = "git diff --no-index " + first_log_name +" --no-index " + second_log_name + " > dif-" + cdc_date + ".txt"
os.system(command)