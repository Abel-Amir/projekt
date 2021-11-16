# import re
#
# my_text = "Aman, 1998, aman@gmail.com"\
#             "Vasia, 1999, vasia@gmail.com"\
#             "Akyl, 2000, akyl@gmail.com"\
#             "Kutya, 1997, kutya@gmail.com"\
#             "Salam, 1995, salam@gmail.com"\
#             "Bishkek, 1991, bishkek@gmail.com"
#
# """
# \d = выдадает любые подряд числа [0-9]
# \D = он ищет любые не числа
# \w = любой алфавитный символ [A-Z a-z]
# \W = любой не алфавитный символ
# \s = ищет breakspace
# \S = ищет не breakspace
#
#
# [0-9]{любой порядак который вам нужен} = аналог \d
# [A-Z a-z]+ = ищем алфавитный порядок + это любая последовательность
# """
#
# searching = r"@\w+.\w+"
# results = re.findall(searching, my_text)
# print(results)

import re

file_path = "class_mock_data.txt"
results_file_path = "results.txt"
file_reader = open(file_path, mode="r", encoding="Latin_1")
results_file = open(results_file_path, mode="w", encoding="Latin_1")
my_text_1 = file_reader.read()

searching = r"[\w+_-]+@[\w+_-]+.[\w.]+"
results_all = re.findall(searching, my_text_1)
#Hyacinthie	Staines	hstainesfy@nationalgeographic.com	PedeUllamcorper.mpeg	#672239
for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total {str(len(results_all))}")