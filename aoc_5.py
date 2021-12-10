import aocd


def parse(puzzle_input):
    """Parse input"""
    return [[tuple([int(c) for c in point.split(',')]) for point in line.split(' -> ')] for line in puzzle_input.splitlines()]

def omit_diagnal(lines):
    return [line for line in lines if line[0][0]==line[1][0] or line[0][1] == line[1][1]]

def turn_to_grid(lines):
    max_point = max([coord for line in lines for point in line for coord in point])

    grid = [[0 for i in range(max_point+1)] for i in range(max_point+1)]
    for (x1,y1),(x2,y2) in lines:
        if x1==x2:
            highest,lowest = max(y1,y2), min(y1,y2)
            for y in range(lowest,highest+1):
                grid[y][x1]+=1
        elif y1==y2:
            highest,lowest = max(x1,x2), min(x1,x2)
            for x in range(lowest,highest+1):
                grid[y1][x]+=1
        else:
            for i in range(abs(x1-x2)+1):
                grid[y1+i if y1<y2 else y1-i][x1+i if x1<x2 else x1-i] += 1
    return grid

def count_dangerous(grid):
    return sum([sum([int(p>1) for p in line]) for line in grid])

def part1(data):
    return count_dangerous(turn_to_grid(omit_diagnal(parse(data))))

def part2(data):
    return count_dangerous(turn_to_grid(parse(data)))

def solve(day=5):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)
    #data = example_data


    print('part one:', part1(data))
    print('part two:', part2(data))
