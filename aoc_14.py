import pathlib
import aocd
from collections import Counter
import sys


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    template = lines[0]
    rules = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in lines[2:]}
    return template, rules
    """Parse input"""

def compute_score_counter(counter):
    c = counter.most_common()
    return c[0][1] - c[-1][1]

def apply_steps_for_pairs(template,cat_rules, n):
    cnt = Counter(template)
    polymer = ''
    for i in range(len(template) - 1):
        polymer += template[i]
        c, s = apply_steps_pair(template[i:i+2],cat_rules, n)
        cnt += c
        polymer += s
    polymer += template[-1]
    return cnt, polymer


def expand(parents, rules, n):
    # we know that every right branch will always expend the same, so focus on the left expansions only
    child = rules[parents]
    if n>1:
        left = parents[0]+child
        if left == parents:
            True# don't go into this again, we're already working this out for one level higher
        else:
            expand(left, rules, n-1)
        right = child+parents[1]
        if right == parents:
            True
            # don't go into this again, we're already working this out for one level higher
        else:
            expand(right,rules,n-1)




def apply_steps_pair(parents, cat_rules, n):
    polymer = ''
    case = 'left' if parents in cat_rules['left'] else 'right' if parents in cat_rules['right'] else 'other'
    #breakpoint()
    if parents in cat_rules['left']:
        child = cat_rules['left'][parents]
        descendants = Counter({child:n})
        polymer+= n*child
        if n>1:
            c, s = apply_steps_pair(child+parents[1], cat_rules,n-1)
            descendants += c
            polymer += s
    elif parents in cat_rules['right']:
        child = cat_rules['right'][parents]
        descendants = Counter({child: n})
        if n>1:
            c, s = apply_steps_pair(parents[0]+child,cat_rules,n-1)
            descendants +=c
            polymer += s
        polymer += n * child
    else:
        child = cat_rules['other'][parents]
        descendants = Counter({child:1})
        if n>1:
            c, s = apply_steps_pair(parents[0] + child, cat_rules, n - 1)
            descendants += c
            polymer += s
            polymer += child
            c, s = apply_steps_pair(child + parents[1], cat_rules, n - 1)
            descendants += c
            polymer += s
        else:
            polymer += child
    return descendants, polymer


def null_expansions(rules):
    return {0:{key: key[0]+value+key[1] for key, value in rules.items}}




def apply_step(template, rules):
    polymer = ''
    for i in range(len(template)-1):
        polymer+=template[i] + rules[template[i:i+2]]
    polymer += template[i+1]
    return polymer

def apply_steps(polymer, rules, n):
    for i in range(n):
        polymer = apply_step(polymer,rules)
    return polymer


def pair_counts(pair, rules, known_counts, depth):
    if depth not in known_counts:
        known_counts[depth]={}
    if depth-1 not in known_counts:
            known_counts[depth-1] = {}
    if depth > 0:
        child = rules[pair]
        left = pair[0]+child
        if left not in known_counts[depth-1]:
            known_counts = pair_counts(left, rules, known_counts, depth-1)
            assert left in known_counts[depth-1]
        right = child+pair[1]
        if right not in known_counts[depth - 1]:
            known_counts = pair_counts(right, rules, known_counts, depth-1)
            assert right in known_counts[depth - 1]
        known_counts[depth][pair] = known_counts[depth-1][left]+known_counts[depth-1][right]
        known_counts[depth][pair][child] -= 1 # ugly way to make sure child is only counted once
    else:
        if pair not in known_counts[depth]:
            known_counts[depth][pair] = Counter(pair)
    return known_counts

def all_pair_counts(rules, to_depth):
    counts = {0:{pair:Counter(pair) for pair in rules.keys()}}
    for pair in rules.keys():
        counts = pair_counts(pair,rules,counts,to_depth)
    return counts

def count_based_on_counts(template, rules, depth):
    counts = all_pair_counts(rules, depth)
    score = Counter()
    for i in range(len(template) - 1):
        score += counts[depth][template[i:i + 2]]
        score[template[i + 1]] -= 1
    score[template[-1]] += 1
    return score


def compute_score_polymer(polymer):
    c = Counter(polymer).most_common()
    return c[0][1] - c[-1][1]

def part1(data):
    template, rules = parse(data)
    #return compute_score_polymer(apply_steps(template,rules,10))
    #return compute_score_counter(apply_steps_for_pairs(template, rules, 10))
    return compute_score_counter(count_based_on_counts(template, rules, 10))

    """Solve part 1"""



def part2(data):
    template, rules = parse(data)

    return compute_score_counter(count_based_on_counts(template, rules, 40))


"""Solve part 2"""

def solve(day=14):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)

    print('Part one:', part1(data))
    print('Part two:', part2(data))

