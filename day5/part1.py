import math
import re

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

def apply_map(x, map):
    map = sorted(map, key=lambda y: y.split(' ')[1])
    next_value = x
    for i in map:
        source = int(i.split(' ')[1])
        dest = int(i.split(' ')[0])
        range = int(i.split(' ')[2])
        if source <= x < (source + range):
            next_value = x + dest - source

    return next_value


for i in range(len(lines)):
    if re.search("seeds:", lines[i]):
        seed_list = list(filter(''.__ne__, re.split("seeds: (.*)", lines[i])))[0].split(' ')
    elif re.search("seed-to-soil map:", lines[i]):
        seed_to_soil_start = i
    elif re.search("soil-to-fertilizer map:", lines[i]):
        soil_to_fert_start = i
    elif re.search("fertilizer-to-water map:", lines[i]):
        fert_to_water_start = i
    elif re.search("water-to-light map:", lines[i]):
        water_to_light_start = i
    elif re.search("light-to-temperature map:", lines[i]):
        light_to_temp_start = i
    elif re.search("temperature-to-humidity map:", lines[i]):
        temp_to_hum_start = i
    elif re.search("humidity-to-location map:", lines[i]):
        hum_to_loc_start = i

maps = {
    'seed_to_soil': lines[seed_to_soil_start + 1:soil_to_fert_start - 1],
    'soil_to_fert': lines[soil_to_fert_start + 1:fert_to_water_start - 1],
    'fert_to_water': lines[fert_to_water_start + 1:water_to_light_start - 1],
    'water_to_light': lines[water_to_light_start + 1:light_to_temp_start - 1],
    'light_to_temp': lines[light_to_temp_start + 1:temp_to_hum_start - 1],
    'temp_to_hum': lines[temp_to_hum_start + 1:hum_to_loc_start - 1],
    'hum_to_loc': lines[hum_to_loc_start + 1:]
}

locs = []
for seed in seed_list:
    next_value = int(seed)
    for map in maps.values():
        next_value = apply_map(next_value, map)
    locs.append(next_value)
print(locs)
print(min(locs))

