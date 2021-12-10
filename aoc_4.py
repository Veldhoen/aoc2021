import aocd

def parse(puzzle_input):

    """Parse input"""
    lines = puzzle_input.splitlines()
    cards_data = [lines[n:n+5] for n in range(2,len(lines),6)]
    return ([int(n) for n in lines[0].split(',')], [[[int(num) for num in row.split()] for row in card_data] for card_data in cards_data])

def part1(data):
    called_numbers, cards = data
    for called_number in called_numbers:
        for h in range(len(cards)):
            cards[h], bingo = check_on_card(cards[h],called_number)
            if bingo:
                return compute_score(cards[h])*called_number

def part2(data):
    called_numbers, cards = data
    cards = {h: cards[h] for h in range(len(cards))}
    for called_number in called_numbers:
        for h in list(cards.keys()):
            cards[h], bingo = check_on_card(cards[h], called_number)
            if bingo:
                if len(cards) > 1:
                    del cards[h]
                else:
                    return compute_score(cards[h]) * called_number



def compute_score(card):
    return sum([sum([n for n in row if n > 0]) for row in card])

def check_on_card(card, called_number):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == called_number:
                card[i][j] *= -1
                if called_number == 0: card[i][j] = -100 # edge case
                if all([n < 0 for n in card[i]]) or all([row[j] < 0 for row in card]): # row or column checked
                    return card, True
                else:
                    return card, False
    return card, False # number is not on the card

    """Solve part 1"""


def solve(day=4):

    """Solve the puzzle for the given input"""

    data = aocd.get_data(day=day)
    #data = example_data


    print('part one:', part1(parse(data)))
    print('part two:', part2(parse(data)))

example_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
