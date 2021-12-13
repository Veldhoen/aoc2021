import pathlib
import aocd

import sys


def parse(puzzle_input):
    lines = puzzle_input.splitlines()

    coordinates = []
    folds = []
    for line in lines:
        try:
            assert line[0].isnumeric()
            coordinates.append([int(num) for num in line.split(',')])
        except IndexError:
            continue
        except AssertionError:
            horizontal = line.split('=')[0][-1]=='y'
            position = int(line.split('=')[1])
            folds.append((horizontal,position))

    return turn_to_grid(coordinates), folds
    """Parse input"""

def turn_to_grid(points):
    max_x = max([coord[0] for coord in points])
    max_y = max([coord[1] for coord in points])

    grid = [[0 for i in range(max_x+1)] for i in range(max_y+1)]
    for (x,y) in points:
        grid[y][x] = 1
    return grid

def fold_paper(grid, horizontal, position):
    if horizontal:
        max = len(grid)
        for i in range(0,max-position):
            grid[position-i] = [sum(x) for x in zip(grid[position-i],grid[position+i])]
        grid = grid[:position]
        return grid
    else:
        max = len(grid[0])
        for i in range(1,max-position):
            for j in range(len(grid)):
                grid[j][position-i] += grid[j][position+i]
        grid = [line[:position] for line in grid]
    return grid

def count_the_dots(grid):
    return sum([sum([int(c>0) for c in line]) for line in grid])

def part1(data):
    grid, folds = parse(puzzle_input=data)
    first_fold = fold_paper(grid, folds[0][0], folds[0][1])
    return count_the_dots(first_fold)

    """Solve part 1"""


def part2(data):
    grid, folds = parse(puzzle_input=data)
    for fold in folds:
        grid = fold_paper(grid, fold[0], fold[1])
    print('\n'.join([''.join(['#' if c>0 else '.' for c in line]) for line in grid]))

    """Solve part 2"""


def solve(day=13):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)

    print('Part one:', part1(data))
    print('Part two:', part2(data))
