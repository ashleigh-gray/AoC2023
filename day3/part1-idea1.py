import pandas as pd
import itertools

testing = True

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
        self.number_adj = False
        self.char_adj = False
        self.part = False

    def __repr__(self):
        return self.char_adj.__str__()
    def __str__(self):
        return str(self.char_adj)


df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
x_length = len(df.columns) - 1
y_length = len(df.index) - 1

print(df.to_string())


def has_number_adj(xy, df):
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_adjs = get_adjs(xy.x, x_max)
    y_adjs = get_adjs(xy.y, y_max)
    all_adjs = list(itertools.product(x_adjs,y_adjs))
    all_adjs.remove((xy.x, xy.y))

    for x,y in all_adjs:
        if df[x][y].isdigit():
            return True

def has_char_adj(xy, df):
    char_list = []
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_adjs = get_adjs(xy.x, x_max)
    y_adjs = get_adjs(xy.y, y_max)
    all_adjs = list(itertools.product(x_adjs,y_adjs))
    all_adjs.remove((xy.x, xy.y))

    for x,y in all_adjs:
        if (not df[x][y].isalnum()) and (df[x][y] != '.'):
            return True

def get_adjs(i, max):
    adjs = [i]
    if i == 0:
        adjs.append(i+1)
    elif i == max:
        adjs.append(i-1)
    else:
        adjs.append(i-1)
        adjs.append(i+1)
    return adjs

df_details = []
for y in range(y_length):
    row_details = []
    for x in range(x_length):
        xy = number(df[x][y], x, y)
        if df[x][y].isdigit():
            if has_number_adj(xy, df):
                xy.number_adj = True
            if has_char_adj(xy, df):
                xy.char_adj = True
        row_details.append(xy)
    df_details.append(row_details)


df2 = pd.DataFrame(data=df_details)
print(df2.to_string())




