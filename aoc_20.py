import math
import pathlib
import aocd
from collections import defaultdict
import sys


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    algorithm = lines[0]
    islands = string_to_islands('\n'.join(lines[2:]))
    return algorithm, islands

def islands_to_string(islands, x_range = None, y_range = None):
    if x_range:
        x_0, x_n = x_range
    else:
        x_values = [val for row in islands.values() for val in row]
        x_0 = min(x_values)
        x_n = max(x_values)+1
    if y_range:
        y_0, y_n = y_range
    else:
        y_0 = min(islands.keys())
        y_n = max(islands.keys())+1
    return '\n'.join([''.join(['#' if y in islands and x in islands[y] else '.' for x in range(x_0, x_n)]) for y in range(y_0, y_n)])

def string_to_islands(image_string):
    return {i: [j for j, c in enumerate(row) if c == '#'] for i, row in enumerate(image_string.splitlines())}

def run_algorithm(islands, algorithm, nsteps):
    cnt = 0
    new_islands_light = True
    while cnt < nsteps:
        islands, new_islands_light = compute_new_islands(islands, algorithm, new_islands_light)
        cnt+=1
    return islands, new_islands_light


def count_lit_pixels(islands, islands_light):
    if not islands_light: return math.inf
    else:
        return sum([len(pixels) for pixels in islands.values()])

def compute_new_islands(islands, algorithm, existing_islands_light = True):
    if existing_islands_light: # sea == 0: what does sea become? Look at first character of algorithm
        new_islands_light = algorithm[0] == '.'
    else: # sea == 1: what does sea become? Look at last character of algorithm
        new_islands_light = algorithm[-1] == '.'
    windows = relevant_windows(islands)
    new_islands = defaultdict(list)
    for row_index, col_indices in windows.items():
        for col_index in col_indices:
            new_value = algorithm[get_window_value((row_index,col_index), islands, existing_islands_light)]
            if (new_islands_light and (new_value =='#')) or (not new_islands_light and (new_value == '.')):
                new_islands[row_index].append(col_index)
    return new_islands, new_islands_light




def get_window_value(coordinates, islands, islands_light):
    window = ''
    for delta_i in range(-1,2):
        for delta_j in range(-1, 2):
            i = coordinates[0]+delta_i
            if i in islands.keys() and coordinates[1]+delta_j in islands[i]:
                window += '1' if islands_light else '0'
            else:
                window += '0' if islands_light else '1'
    return int(window,2)

def relevant_windows(islands):
    """
    :param islands: a dictionary of row_index: col_indices (list) that specifies per row the column indices that are islands (either light or dark pixels)
    :return: windows: a dictionary of row_index: col_indices (set) that specify 3x3 windows that contain at least one island pixel
    """
    windows = defaultdict(set)
    for row_index, col_indices in islands.items():
        for delta_i in range(-1,2):
            for delta_j in range(-1, 2):
                windows[row_index+delta_i].update([col_index+delta_j for col_index in col_indices])
    return windows

def part1(data):

    algoritm, islands = parse(data)
    islands, islands_light = run_algorithm(islands,algoritm, 2)
    return count_lit_pixels(islands, islands_light)


def part2(data):
    algoritm, islands = parse(data)
    islands, islands_light = run_algorithm(islands,algoritm, 50)
    return count_lit_pixels(islands, islands_light)


def solve(day=20):
    data = aocd.get_data(day=day)

    print('Part one:', part1(data))
    print('Part two:', part2(data))
