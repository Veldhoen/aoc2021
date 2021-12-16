import aoc_16 as target


def test_part1():
    examples = [
        ('8A004A801A8002F478', 16),
        ('620080001611562C8802118E34', 12),
        ('C0015000016115A2E0802F182340', 23),
        ('A0016C880162017C3686B18A3D4780', 31)
    ]
    for hex, version_sum in examples:
        assert target.part1(hex) == version_sum


def test_hex_to_bin():
    assert target.hex_to_bin('D2FE28') == '110100101111111000101000'


def test_read_literal():
    literal, unused = target.read_literal('110100101111111000101000'[6:])
    assert literal == 2021
    assert unused == '000'


def test_read_operator():
    operator_content = '00000000000110111101000101001010010001001000000000'
    value, summed_values, rest = target.read_operator(operator_content)
    assert summed_values == int('110', 2) + int('010', 2)
    assert rest == '0000000'

    operator_content = '10000000001101010000001100100000100011000001100000'
    value, summed_values, rest = target.read_operator(operator_content)
    assert summed_values == int('010', 2) + int('100', 2) + int('001', 2)
    assert rest == '00000'


def test_read_packet():
    value, sum, rest = target.read_packet('110100101111111000101000')
    assert sum == 6

    value, sum, rest = target.read_packet('00111000000000000110111101000101001010010001001000000000')
    assert sum == int('001', 2) + int('110', 2) + int('010', 2)


def test_part2():
    examples = [
        ('C200B40A82',3),
        ('04005AC33890',54),
        ('880086C3E88112', 7),
        ('CE00C43D881120', 9),
        ('D8005AC2A8F0',1),
        ('F600BC2D8F',0),
        ('9C005AC2F8F0', 0),
        ('9C0141080250320F1802104A08',1)]
    for example, value in examples:
        assert target.part2(example) == value

