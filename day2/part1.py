import re

testing = False

if testing == True:
    filename = "sample_input.txt"

elif testing == False:
    filename = "input.txt"

red_limit = 12
green_limit = 13
blue_limit = 14

input = open(filename, 'r')
lines = input.read().splitlines()

good_ids = []
for line in lines:
    limit_reached = False
    id = re.findall("([0-9]+):", line)[0]
    result = re.findall("[0-9]: (.*)", line)[0]
    a_result = result.split('; ')
    for games in a_result:
        draws = games.split(', ')
        for draw in draws:
            number = re.findall(r'\d+', draw)[0]
            colour = re.findall(r'\d+ (.*)', draw)[0]
            if colour == 'red':
                if int(number) > red_limit:
                    limit_reached = True
            if colour == 'blue':
                if int(number) > blue_limit:
                    limit_reached = True
            if colour == 'green':
                if int(number) > green_limit:
                    limit_reached = True
    if not limit_reached:
        good_ids.append(int(id))

print(good_ids)
print(sum(good_ids))



