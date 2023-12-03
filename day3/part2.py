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
        self.gear_adj = []


df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
x_length = len(df.columns)
y_length = len(df.index)


# print(df.to_string())

def has_gear_adj(xy, df):
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_adjs = get_adjs(xy.x, x_max)
    y_adjs = get_adjs(xy.y, y_max)
    all_adjs = list(itertools.product(x_adjs, y_adjs))
    all_adjs.remove((xy.x, xy.y))

    for x, y in all_adjs:
        if (df[x][y] == '*') and (df[x][y] != '.'):
            xy.gear_adj = (x, y)
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
prev_gear = []
prev_valid = False

for y in range(y_length):
    row_details = []
    for x in range(x_length):
        xy = number(df[x][y], x, y)
        if df[x][y].isdigit():
            running_num += str(df[x][y])
            if has_gear_adj(xy, df):
                prev_valid = True
                prev_gear = xy.gear_adj

            if x == x_length - 1 and prev_valid:
                if running_num != '':
                    valid_parts.append((running_num, prev_gear))
                    prev_valid = False
                    prev_gear = []
                    running_num = ''
        else:
            if prev_valid:
                if running_num != '':
                    valid_parts.append((running_num, prev_gear))
                    prev_valid = False
                    prev_gear = []
                    running_num = ''
            else:
                if running_num != '':
                    invalid_parts.append((running_num, prev_gear))
                    running_num = ''
                    prev_gear = []

        row_details.append(xy)
    running_num = ''
    prev_valid = False
    df_details.append(row_details)

dfgears = pd.DataFrame(data=valid_parts)
dfgears = dfgears.sort_values([1])
gb = dfgears.groupby([1])

pairs = gb.filter(lambda x: len(x) > 1)
pairs = pairs.sort_values([1])
pl = pairs.values.tolist()
products = []
for i in range(0, len(pl), 2):
    first = pl[i]
    second = pl[i + 1]
    first_part_no = first[0]
    second_part_no = second[0]
    if first[1] == second[1]:
        product = int(first_part_no) * int(second_part_no)
        products.append(product)

print(sum(products))
