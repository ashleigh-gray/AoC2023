import re

testing = False

if testing == True:
    filename = "sample_input.txt"

elif testing == False:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

powers = []
for line in lines:
    red_draw = 0
    blue_draw = 0
    green_draw = 0
    id = re.findall("([0-9]+):", line)[0]
    result = re.findall("[0-9]: (.*)", line)[0]
    a_result = result.split('; ')
    for games in a_result:
        draws = games.split(', ')
        for draw in draws:
            number = re.findall(r'\d+', draw)[0]
            colour = re.findall(r'\d+ (.*)', draw)[0]
            if colour == 'red' and int(number) > red_draw:
                red_draw = int(number)
            elif colour == 'blue' and int(number) > blue_draw:
                blue_draw = int(number)
            elif colour == 'green' and int(number) > green_draw:
                green_draw = int(number)

    power = red_draw * blue_draw * green_draw
    powers.append(power)

print(powers)
print(sum(powers))



