import pathlib
import aocd

import sys


def parse(puzzle_input):
    return puzzle_input.splitlines()
    """Parse input"""


class CorruptedException(Exception):
    def __init__(self, character):
        self.character = character


def complete_line(line):
    legal_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line:
        if c in legal_pairs.keys():
            stack.append(c)
        else:
            if c != legal_pairs[stack.pop()]:
                raise CorruptedException(c)
    return [legal_pairs[stack.pop()] for i in range(len(stack))]


def part1(data):
    scores = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    for line in parse(data):
        try:
            complete_line(line)
        except CorruptedException as e:
            score += scores[e.character]

    return score

    """Solve part 1"""

def score_completion(completion):
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for c in completion:
        score *= 5
        score += scores[c]
    return score

def determine_middle_number(number_list):
    number_list.sort()
    return number_list[len(number_list)//2]


def part2(data):

    scores = []
    for line in parse(data):
        try:
            completion = complete_line(line)
        except CorruptedException as e:
            continue
        scores.append(score_completion(completion))
    return determine_middle_number(scores)

    """Solve part 2"""


def solve(day=10):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)

    print('Part one:', part1(data))
    print('Part two:', part2(data))
