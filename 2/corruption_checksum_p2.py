""" calculate checksum, puzzle 2, http://adventofcode.com/2017/day/2 """

import itertools

checksum = 0
with open("D:/DATA/Company/Werkmap/Scripting/Python/advent/2/puzzel_input.txt", 'r') as f:
    for line in f:
        line_data = sorted((map(int, line.split())), reverse=True)
        for a, b in itertools.combinations(line_data, 2):
            if not a%b:
                checksum += a/b

print checksum
