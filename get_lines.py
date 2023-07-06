import os
cwd = os.getcwd()

class GetLinesFromFile:
    def get_lines_to_list(cls, file_name):
        with open(file_name) as file:
            lines = [line.rstrip() for line in file]
        return lines
    
    def delete_lines(cls, file_name, array):
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            index = 0
            for line in lines:
                if index not in array:
                    line = line[19:]
                    f.write(line)
                index += 1
    