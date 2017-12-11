""" calculate checksum, puzzle 2, http://adventofcode.com/2017/day/2 """

checksum = 0
with open("D:/DATA/Company/Werkmap/Scripting/Python/advent/2/puzzel_input.txt", 'r') as f:
    for line in f:
        print type(line), line
        line_data = map(int, line.split())
        checksum += (int(max(line_data)) - int(min(line_data)))
        print max(line_data), min(line_data), (int(max(line_data)) - int(min(line_data))), checksum, line_data
