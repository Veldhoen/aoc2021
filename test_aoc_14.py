import collections

import aoc_14 as target


def test_parse():
    template, rules = target.parse(example_data)
    assert template == example_template
    assert rules == example_rules


def test_apply_step():
    step_1 = target.apply_step(example_template, example_rules)
    assert step_1 == example_step_1
    step_2 = target.apply_step(step_1, example_rules)
    assert step_2 == example_step_2
    step_3 = target.apply_step(step_2, example_rules)
    assert step_3 == example_step_3
    step_4 = target.apply_step(step_3, example_rules)
    assert step_4 == example_step_4


def test_apply_steps():
    step_4 = target.apply_steps(example_template, example_rules, 4)
    assert step_4 == example_step_4


def test_compute_score():
    step_10 = target.apply_steps(example_template, example_rules, 10)
    assert target.compute_score(step_10) == 1588


def test_part1():
    assert False


def test_part2():
    assert False


example_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

example_rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H',
                 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}

example_template = """NNCB"""
example_step_1 = "NCNBCHB"
example_step_2 = "NBCCNBBBCBHCB"
example_step_3 = "NBBBCNCCNBBNBNBBCHBHHBCHB"
example_step_4 = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

example_counter_10 = collections.Counter({'B': 1749, 'C': 298, 'H': 161, 'N': 865})


def test_compute_score_counter():
    assert target.compute_score_counter(example_counter_10) == 1588


def test_apply_steps_for_pairs():
    cat_rules = target.categorize_rules(example_rules)
    example_steps = [example_step_1, example_step_2, example_step_3, example_step_4]
    # for i, example in enumerate(example_steps):
    #     c, s = target.apply_steps_for_pairs(example_template, cat_rules, i+1)
    #     assert s == example
    #     assert c == collections.Counter(example)

    c, s = target.apply_steps_for_pairs(example_steps[0], cat_rules, 3)
    assert s == example_steps[3]
    assert c == collections.Counter(example_steps[3])


def test_apply_steps_pair():
    cat_rules = target.categorize_rules(example_rules)
    parents = 'CN'
    depth, expansion = 3, 'CCNBCNCCN'
    # depth, expansion = 2, 'CNCCN'

    # parents = 'CC'
    # depth, expansion = 1, 'CNC'
    c, s = target.apply_steps_pair(parents, cat_rules, depth)
    assert parents[0] + s + parents[1] == expansion
    assert c + collections.Counter(parents) == collections.Counter(expansion)


def test_all_pair_counts():
    example_steps = [example_template,example_step_1, example_step_2, example_step_3, example_step_4]
    for depth, example in enumerate(example_steps):
        counts = target.all_pair_counts(example_rules, depth)
        score = collections.Counter()
        for i in range(len(example_template)-1):
            score += counts[depth][example_template[i:i+2]]
            score[example_template[i+1]]-=1
        score[example_template[-1]]+=1
        assert score==collections.Counter(example)



