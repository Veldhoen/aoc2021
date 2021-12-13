import aoc_10 as target


def test_parse():
    assert target.parse(example_data) == example_lines


def test_complete_line():
    for line in example_lines:
        try:
            completion = target.complete_line(line)
        except target.CorruptedException:
            assert line in example_corrupted
        else:
            assert line not in example_corrupted
            assert ''.join(completion) == example_incomplete[line][0]


example_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

example_lines = example_data.splitlines()

example_corrupted = [
    "{([(<{}[<>[]}>{[]{[(<()>",  # Expected ], but found } instead.
    "[[<[([]))<([[{}[[()]]]",  # Expected ], but found ) instead.
    "[{[{({}]{}}([{[{{{}}([]",  # Expected ), but found ] instead.
    "[<(<(<(<{}))><([]([]()",  # Expected >, but found ) instead.
    "<{([([[(<>()){}]>(<<{{"]

example_incomplete = {
    "[({(<(())[]>[[{[]{<()<>>": ("}}]])})]", 288957),
    "[(()[<>])]({[<{<<[]>>(": (")}>]})", 5566),
    "(((({<>}<{<{<>}{[]{[]{}": ("}}>}>))))", 1480781),
    "{<[[]]>}<{[{[{[]{()[[[]": ("]]}}]}]}>", 995444),
    "<{([{{}}[<[[[<>{}]]]>[]]": ("])}>", 294)}


def test_part1():
    assert target.part1(example_data) == 26397


def test_score_completion():
    for completion, score in example_incomplete.values():
        assert target.score_completion(completion) == score


def test_determine_middle_number():
    scores = [score for (_,score) in example_incomplete.values()]
    assert target.determine_middle_number(scores) == 288957
