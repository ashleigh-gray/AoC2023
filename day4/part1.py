import re

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

total_score = 0
for line in lines:
    num_won = 0
    score = 0
    add = 1
    id = re.findall("([0-9]+):", line)[0]
    numbers = re.findall("[0-9]: (.*)", line)[0]
    winning = numbers.split('|')[0]
    got = numbers.split('|')[1]
    winning = winning.split()
    got = got.split()
    for n in got:
        if n in winning:
            num_won += 1
            score += add
            if num_won > 1:
                add = add*2
    total_score += score
    print("Card", id, "had", num_won, "winning numbers, giving", score, "points")

print("total score:", total_score)
