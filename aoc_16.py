import aocd

def hex_to_bin(hex_rep):
    dic = {'0': '0000', '1': '0001','2': '0010','3': '0011','4': '0100','5': '0101','6': '0110','7': '0111',
     '8': '1000', '9': '1001','A': '1010','B': '1011','C': '1100','D': '1101','E': '1110','F': '1111'}
    return ''.join([dic[c] for c in hex_rep])

def read_header(bin_rep):
    version = int(bin_rep[:3],2)
    type_id = int(bin_rep[3:6],2)
    return version, type_id


def read_literal(bin_rep):
    groups = [bin_rep[i:i + 5] for i in range(0, len(bin_rep), 5)]
    to_interpret = ''
    for group in groups:
        to_interpret += group[1:]
        if group[0]=='0':
            break
    value = int(to_interpret,2)
    rest = bin_rep[len(to_interpret)//4*5:]
    return value, rest

def read_operator(bin_rep):
    length_type_id = bin_rep[0]
    length_of_subpackets = 0
    number_of_subpackets = 0
    if length_type_id == '0':
        length_of_subpackets = int(bin_rep[1:16],2)
        bin_rep = bin_rep[16:]
    else:
        number_of_subpackets = int(bin_rep[1:12],2)
        bin_rep = bin_rep[12:]
    version_sum = 0
    cnt = 0
    eaten = 0
    value_list = []
    while eaten < length_of_subpackets or cnt < number_of_subpackets:
        next_value, summed_versions,rest = read_packet(bin_rep)
        eaten += len(bin_rep)-len(rest)
        value_list.append(next_value)
        bin_rep = rest
        version_sum+= summed_versions
        cnt +=1
    return value_list, version_sum, bin_rep

def read_packet(bin_rep):
    if len(bin_rep)<6: return 0, bin_rep
    version, type_id = read_header(bin_rep[:6])
    if type_id == 4:
        value, rest = read_literal(bin_rep[6:])
        summed_versions = 0
    else:
        value_list, summed_versions, rest = read_operator(bin_rep[6:])
        if type_id == 0: value = sum(value_list)
        elif type_id == 1: value = functools.reduce((lambda x, y: x*y), value_list)
        elif type_id == 2: value = min(value_list)
        elif type_id == 3: value = max(value_list)
        elif type_id == 5: value =  int(value_list[0] > value_list[1])
        elif type_id == 6: value =  int(value_list[0] < value_list[1])
        elif type_id == 7: value =  int(value_list[0] == value_list[1])
    summed_versions += version
    return value, summed_versions, rest

def part1(data):
    hex = hex_to_bin(data)
    _, version_sum, _ = read_packet(hex)
    return version_sum

def part2(data):
    hex = hex_to_bin(data)
    value, _, _ = read_packet(hex)
    return value

def solve(day=16):
    data = aocd.get_data(day=day)
    print('Part one:', part1(data))
    print('Part two:', part2(data))
