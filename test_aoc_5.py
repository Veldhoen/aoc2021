import aoc_5 as target


def test_parse():
    assert target.parse(example_data) == example_lines


def test_turn_to_grid():
    assert target.turn_to_grid(target.omit_diagnal(example_lines)) == example_grid_1
    assert target.turn_to_grid(example_lines) == example_grid_2


def test_count_dangerous():
    assert target.count_dangerous(example_grid_1) == 5
    assert target.count_dangerous(example_grid_2) == 12


def test_part1():
    assert target.part1(example_data) == 5

def test_part2():
    assert target.part2(example_data) == 12

example_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

example_lines = [
    [(0, 9), (5, 9)],
    [(8, 0), (0, 8)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(6, 4), (2, 0)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
    [(0, 0), (8, 8)],
    [(5, 5), (8, 2)],
]

example_grid_1_string = """.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111...."""

example_grid_2_string = """1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."""


def turn_to_int(c):
    if c == '.':
        return 0
    else:
        return int(c)


example_grid_1 = [[turn_to_int(c) for c in line] for line in example_grid_1_string.splitlines()]
example_grid_2 = [[turn_to_int(c) for c in line] for line in example_grid_2_string.splitlines()]
