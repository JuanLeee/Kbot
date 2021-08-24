import numpy as np
import json
import string, re

dict_text = {}
series_number_list = {}

count = 0
print("\nUsing readline()")
 
with open("import.txt") as fp:
    while True:
        count += 1
        line = fp.readline()
        space_index  = line.find(' ')+1
        opening_index  = line.find('(')
        closing_index  = line.find(')')
        opening_sq = line.find('[')
        closing_sq = line.find(']')
        if len(line)>4:
            char_name = line[space_index:opening_index-1].lower()
            series_name = line[opening_index+1:closing_index].lower()
            char_name = re.sub('[^0123456789abcdefghijklmnopqrstuvwxyz QWERTYUIOPLKJHGFDSAZXCVBNM\']','', char_name)
            series_name = re.sub('[^0123456789abcdefghijklmnopqrstuvwxyz QWERTYUIOPLKJHGFDSAZXCVBNM\']','', series_name)
            dict_text[char_name] = series_name
            series_number = line[opening_sq+1:closing_sq]
            series_list = series_number.split(", ")
            series_numbers = []
            for i in series_list:
                series_numbers.append(int(i))
            if series_numbers[0] == 2:
                series_number_list[char_name] = 2

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))

with open('export_char.py', 'w') as file:
     file.write(json.dumps(dict_text))
with open('export_numbers.py', 'w') as file:
     file.write(json.dumps(series_number_list))