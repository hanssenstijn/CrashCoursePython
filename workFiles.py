# open a text file in the directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# use file path to import the file
# file_path = 'C:\Users\stijn\Documents\GitHub\CrashCoursePython\pi_digits.txt'
# with open(file_path) as file_object:
#    contents = file_object.read()
#    print(contents)

# write to a file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")

with open('programming.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open(filename, 'a') as file_object:
    file_object.write("I also love fiding meaning in large datasets. \n")

with open('programming.txt') as file_object:
    contents = file_object.read()
    print(contents)

# store data in Json file
# import json
# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#  json.dump(numbers, f_obj)

