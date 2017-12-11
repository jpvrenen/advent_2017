#!/usr/bin/python

import sys
import re
import base64
import time
import pprint
import xmltodict
import puzzle_input

#pinput = puzzle_input.input
pinput = puzzle_input.input_bj

#Rules
"""
Part One
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
    1221 produces 0, because every comparison is between a 1 and a 2.
    123425 produces 4, because both 2s match each other, but no other digit has a match.
    123123 produces 12.
    12131415 produces 4.

"""

input_list = [ entry for entry in pinput ]
input_len = len(input_list)
skip_steps = input_len/2

def sum_string(data_str):
    result = 0
    for n in data_str:
        result = result + int(n)
    return result

def part_one(input_list, input_len):
    result = str()
    for index, entry in enumerate(input_list):
        if index == (input_len - 1):
            if entry == input_list[0]:
                result = result+entry
        elif entry == input_list[index+1]:
            result = result+entry

    return sum_string(result)

def part_two(input_list, input_len, skip_steps):
    result = str()
    for index, entry in enumerate(input_list):
        if (index+skip_steps) > (input_len-1):
            if entry == input_list[index-skip_steps]:
                result = result+entry
        elif entry == input_list[index+skip_steps]:
            result = result+entry

    return sum_string(result)

print part_one(input_list, input_len)
print part_two(input_list, input_len, skip_steps)
