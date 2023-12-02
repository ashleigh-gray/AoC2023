import re

testing = False

if testing == True:
    filename = "sample_input_2.txt"
elif testing == False:
    filename = "input.txt"

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

input = open(filename, 'r')
lines = input.read().splitlines()

total_sum = 0
for line in lines:
    num_first_position = 0
    word_first_position = 0
    num_last_position = len(line) - 1
    word_last_position = len(line) - 1
    # first_num = 0
    # last_num = 0

    for char in line:
        if char.isdigit():
            first_num = char
            break
        num_first_position += 1

    lowest_index = len(line) - 1
    for num in numbers:
        index = line.find(num)
        if 0 <= index < lowest_index:
            lowest_index = index
            first_num = numbers.index(num) + 1
            word_first_position = lowest_index

    if num_first_position < word_first_position:
        first_num = line[num_first_position]
    # print("first num:", first_num)
    for char in line[::-1]:
        if char.isdigit():
            last_num = char
            break
        num_last_position -= 1

    highest_index = -1
    for num in numbers:
        index = line.rfind(num)
        if index > highest_index:
            highest_index = index
            last_num = numbers.index(num) + 1
            word_last_position = highest_index

    if num_last_position > word_last_position:
        last_num = line[num_last_position]
    print(first_num, last_num)
    ans = str(first_num) + str(last_num)
    total_sum += int(ans)

print(total_sum)
# right - 54578
# wrong - 54541