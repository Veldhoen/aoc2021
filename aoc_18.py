import math
import pathlib
import aocd
import copy

import sys


class NoExplosiveError(Exception):
    pass

class NoSplitError(Exception):
    pass

def parse(puzzle_input):
    return [eval(line) for line in puzzle_input.splitlines()]
    """Parse input"""

def get_magnitude(tree):
    if type(tree) is int: return tree
    else:
        return 3 * get_magnitude(tree[0]) + 2* get_magnitude(tree[1])


def biggest_sum_in_list_of_numbers(list_of_numbers):
    list_of_numbers = [reduce(number) for number in list_of_numbers]
    biggest_magnitude = 0

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if i ==j: continue
            magnitude_0 = get_magnitude(reduce([copy.deepcopy(list_of_numbers[i]),copy.deepcopy(list_of_numbers[j])]))
            magnitude_1 = get_magnitude(reduce([copy.deepcopy(list_of_numbers[j]),copy.deepcopy(list_of_numbers[i])]))
            biggest_magnitude=max([biggest_magnitude,magnitude_0,magnitude_1])
    return biggest_magnitude


def sum_list_of_numbers(list_of_numbers):
    if len(list_of_numbers) ==1:
        return list_of_numbers[0]
    else:
        first_sum = reduce([list_of_numbers[0],list_of_numbers[1]])
        return reduce(sum_list_of_numbers([first_sum]+ list_of_numbers[2:]))

def reduce(tree):
    """

    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.

    :param tree:
    :return:
    """
    reduced = False
    last_explosion = ''
    while not reduced:
        #breakpoint()
        try:
            explosive_position = find_first_explosive(tree, last_explosion)
            tree = explode(tree,explosive_position)
            last_explosion = explosive_position
        except NoExplosiveError:
            try:
                split_position = find_first_splittingpoint(tree)
                tree = split(tree, split_position)
                if len(split_position)>3:
                    # we already know we'll have to explode this node
                    tree = explode(tree, split_position)
            except NoSplitError:
                reduced = True
    return tree

def find_first_splittingpoint(tree):
    if type(tree) is int:
        if tree>9:
            to_return =  ''
        else:
            raise NoSplitError
    else:
        try:
            to_return = '0'+find_first_splittingpoint(tree[0])
        except NoSplitError:
                to_return = '1'+find_first_splittingpoint(tree[1])
    return to_return

def find_first_explosive(tree, last_explosion, depth = 0):
    if type(tree) is int:
        raise NoExplosiveError
    if type(tree[0]) is int and type(tree[1]) is int:
        if depth >3:
            path =  ''
        else:
            raise NoExplosiveError
    else:
        skip_left = False
        path = ''
        if last_explosion:  # we already scouted the left branch for explosives and didn't find them
            skip_left = last_explosion[0] == '1'
        if not skip_left:
            try:
                path = '0' + find_first_explosive(tree[0], last_explosion[1:], depth +1)
            except NoExplosiveError:
                    True
        if not path:
            path = '1' + find_first_explosive(tree[1], '', depth + 1)
    return path

def split(tree, splitting_point):
    node = traverse_tree(tree,splitting_point)
    half = node/2
    tree = replace_tree_bit(tree, splitting_point, [math.floor(half),math.ceil(half)])
    return tree

def add_to_descendant(tree, to_add, leftmost):
    if type(tree) == int:
        return tree+to_add
    else:
        tree[int(leftmost)] = add_to_descendant(tree[int(leftmost)], to_add, leftmost)
        return tree

def traverse_tree(tree, node_position):
    i = int(node_position[0])
    if len(node_position)>1:
        return traverse_tree(tree[i], node_position[1:])
    else:
        return tree[i]


def replace_tree_bit(tree, node_position, replacement):
    i = int(node_position[0])
    if len(node_position)>1:
        tree[i] = replace_tree_bit(tree[i],node_position[1:],replacement)
    else:
        tree[i] = replacement
    return tree




def ancestor_position(node_position, for_left):
    before, sep, _ = node_position.rpartition('1' if for_left else '0')
    if sep == '1': before += '0'
    if sep == '0': before += '1'
    return before

def addition_position(tree, for_left):
    if type(tree) == int:
        addition_position =  ''
    else:
        if for_left:
            addition_position = '0'+addition_position(tree[0], for_left)
        else:
            addition_position = '1'+addition_position(tree[1], for_left)
    return addition_position


def explode(tree, node_position):
    left,right = traverse_tree(tree, node_position)
    ancestor_left_position = ancestor_position(node_position, True)
    if ancestor_left_position: # if there is no such ancester, don't bother replacing anything
        tree = replace_tree_bit(tree,ancestor_left_position, add_to_descendant(traverse_tree(tree, ancestor_left_position),left,True))
    ancestor_right_position = ancestor_position(node_position, False)
    if ancestor_right_position: # if there is no such ancester, don't bother replacing anything
        tree = replace_tree_bit(tree, ancestor_right_position,
                         add_to_descendant(traverse_tree(tree, ancestor_right_position), right, False))
    tree = replace_tree_bit(tree,node_position, 0)
    return tree

def part1(data):
    list_of_numbers = parse(data)
    sum = sum_list_of_numbers(list_of_numbers)
    magnitude = get_magnitude(sum)
    return magnitude

    """Solve part 1"""


def part2(data):
    list_of_numbers = parse(data)
    magnitude = biggest_sum_in_list_of_numbers(list_of_numbers)
    return magnitude
    """Solve part 2"""


def solve(day=18):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)

    print('Part one:', part1(data))
    print('Part two:', part2(data))
