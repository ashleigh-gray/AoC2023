import re
import time

t = time.time()
testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

cards_won = {}
for line in lines:
    num_won = 0
    id = re.findall("([0-9]+):", line)[0]
    if int(id) not in cards_won:
        cards_won[int(id)] = 1
    else:
        cards_won[int(id)] += 1
    numbers = re.findall("[0-9]: (.*)", line)[0]
    winning = numbers.split('|')[0]
    got = numbers.split('|')[1]
    winning = winning.split()
    got = got.split()
    for n in got:
        if n in winning:
            num_won += 1
    for cards in range(cards_won[int(id)]):
        for i in range(1, (num_won+1)):
            if int(id)+i <= len(lines):
                if int(id)+i not in cards_won:
                    cards_won[int(id)+i] = 1
                else:
                    cards_won[int(id)+i] += 1
    # print("Card", id, "had", num_won, "winning numbers")
    # print(cards_won)

print(sum(cards_won.values()))
elapsed = time.time() - t
print(elapsed)
