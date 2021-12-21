import math

import aoc_20 as target


def test_relevant_windows():
    example_image = {0: [0, 3], 1: [0], 2: [0, 1, 4], 3: [2], 4: [2, 3, 4]}
    example_windows = {i: set(range(-1, 6)) for i in range(-1, 6)}
    example_windows[-1].discard(5)
    example_windows[0].discard(5)
    example_windows[4].discard(-1)
    example_windows[4].discard(0)
    example_windows[5].discard(-1)
    example_windows[5].discard(0)

    hole_image = {0: range(0, 5), 1: [0, 4], 2: [0, 4], 3: [0, 4],
                  4: range(0, 5)}  # 5x5 with only border lit = center pixel is not a relevant window
    hole_windows = {i: set(range(-1, 6)) for i in range(-1, 6)}
    hole_windows[2].discard(2)

    examples = [
        ({0:[0]},{i:set(range(-1,2)) for i in range(-1,2)}),
        (example_image, example_windows),
        (hole_image, hole_windows)
    ]
    for islands, windows in examples:
        assert dict(target.relevant_windows(islands)) == windows


def test_islands_to_string():
    assert target.islands_to_string(example_islands) == example_image
    assert target.islands_to_string(example_islands, (-5, 10), (-5, 10)) == example_image_0

    islands = target.string_to_islands(some_image)
    assert target.islands_to_string(islands,(0,len(some_image.splitlines()[0])),(0,len(some_image.splitlines()))) == some_image


def test_run_algorithm():
    step_1 = target.run_algorithm(example_islands, example_algorithm, 1)
    step_2 = target.run_algorithm(step_1, example_algorithm, 1)
    one_go = target.run_algorithm(example_islands, example_algorithm, 2)

    assert target.islands_to_string(step_1, (-5, 10), (-5, 10)) == example_image_1
    assert target.islands_to_string(step_2, (-5, 10), (-5, 10)) == example_image_2
    assert target.islands_to_string(one_go, (-5, 10), (-5, 10)) == example_image_2

    my_algo = example_algorithm
    my_algo[0] = '#'
    my_algo[-1] = '.'
    one_step = target.run_algorithm(example_islands,my_algo,1)
    assert target.count_lit_pixels(one_step, False) == math.inf
    two_step = target.run_algorithm(example_islands,my_algo,2)
    assert target.count_lit_pixels(two_step, False) < math.inf

def test_count_lit_pixels():
    assert target.count_lit_pixels(target.string_to_islands(example_image_2)) == 35



example_algorithm = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##\
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###\
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.\
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....\
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..\
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....\
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"

example_image = """#..#.
#....
##..#
..#..
..###"""
example_islands = {0: [0, 3], 1: [0], 2: [0, 1, 4], 3: [2], 4: [2, 3, 4]}

example_image_0 = """
...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
..............."""

example_image_1 = """...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
..............."""

example_image_2 = """...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
..............."""


some_image = """......
...##.
....#.
.#.##.
.#....
.##.#.
......"""