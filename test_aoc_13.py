import aoc_13 as target


def test_parse():
    grid, folds = target.parse(puzzle_input=example)
    assert grid_to_paper(grid) == example_paper
    assert folds == example_folds


def test_count_the_dots():
    assert target.count_the_dots(target.turn_to_grid(example_dots)) == example_paper.count('#')
    fold_1 = target.fold_paper(target.turn_to_grid(example_dots), example_folds[0][0], example_folds[0][1])
    assert target.count_the_dots(fold_1) == 17
    fold_2 = target.fold_paper(fold_1, example_folds[1][0], example_folds[1][1])
    assert target.count_the_dots(fold_2) == example_fold_2.count('#')

def test_fold_paper():
    fold_1 = target.fold_paper(target.turn_to_grid(example_dots),example_folds[0][0],example_folds[0][1])
    assert grid_to_paper(fold_1) == example_fold_1
    fold_2 = target.fold_paper(fold_1,example_folds[1][0],example_folds[1][1])
    assert grid_to_paper(fold_2) == example_fold_2


def grid_to_paper(grid):
    return '\n'.join([''.join(['#' if c>0 else '.' for c in line]) for line in grid])

def test_turn_to_grid():
    assert grid_to_paper(target.turn_to_grid(example_dots)) == example_paper

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

example_dots = [(6,10),(0,14),(9,10),(0,3),(10,4),(4,11),(6,0),(6,12),(4,1),(0,13),(10,12),(3,4),(3,0),(8,4),(1,10),(2,14),(8,10),(9,0)]
example_folds = [(True,7),(False,5)]

example_paper = """...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........"""

example_fold_1 = """#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
..........."""

example_fold_2 = """#####
#...#
#...#
#...#
#####
.....
....."""
