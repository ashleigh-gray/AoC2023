testing = False

if testing == True:
    filename = "sample_input.txt"
elif testing == False:
    filename = "input.txt"


input = open(filename, 'r')
lines = input.read().splitlines()

total_sum = 0
for line in lines:
    for char in line:
        if char.isdigit():
            first_num = char
            break
    for char in line[::-1]:
        if char.isdigit():
            last_num = char
            break
    ans = first_num + last_num
    total_sum += int(ans)



print(total_sum)