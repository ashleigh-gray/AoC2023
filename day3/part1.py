import pandas as pd
import itertools

testing = False

if testing == True:
    filename = "sample_input.txt"

elif testing == False:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()


class number():
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y


df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
x_length = len(df.columns)
y_length = len(df.index)

# print(df.to_string())

def has_char_adj(xy, df):
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_adjs = get_adjs(xy.x, x_max)
    y_adjs = get_adjs(xy.y, y_max)
    all_adjs = list(itertools.product(x_adjs, y_adjs))
    all_adjs.remove((xy.x, xy.y))

    for x, y in all_adjs:
        if (not df[x][y].isalnum()) and (df[x][y] != '.'):
            return True


def get_adjs(i, max):
    adjs = [i]
    if i == 0:
        adjs.append(i + 1)
    elif i == max:
        adjs.append(i - 1)
    else:
        adjs.append(i - 1)
        adjs.append(i + 1)
    return adjs


df_details = []
running_num = ''
valid_parts = []
invalid_parts = []
prev_valid = False
for y in range(y_length):
    row_details = []
    for x in range(x_length):
        xy = number(df[x][y], x, y)
        if df[x][y].isdigit():
            running_num += str(df[x][y])
            if has_char_adj(xy, df):
                prev_valid = True
            if x == x_length - 1 and prev_valid:
                if running_num != '':
                    valid_parts.append(running_num)
                    prev_valid = False
                    running_num = ''
        else:
            if prev_valid:
                if running_num != '':
                    valid_parts.append(running_num)
                    prev_valid = False
                    running_num = ''
            else:
                if running_num != '':
                    invalid_parts.append(running_num)
                    running_num = ''

        row_details.append(xy)
    running_num = ''
    prev_valid = False
    df_details.append(row_details)

print("valid:", valid_parts)
print(sum(list(map(int, valid_parts))))
