"""
A binary gap within a positive integer N is any maximal sequence of
 consecutive zeros that is surrounded by ones at both ends in the binary
 representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap
 of length 2. The number 529 has binary representation 1000010001 and contains
 two binary gaps: one of length 4 and one of length 3. The number 20 has binary
 representation 10100 and contains one binary gap of length 1.
 The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
 The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
 representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
"""


def solution(N):
    # convert number to binary
    binary_rep = bin(N)[2:]

    # define variable that holds max value
    max_gap_length = 0
    current_gap_length = 0
    # iterate digits on binary
    for i in range(len(binary_rep)):
        if binary_rep[i] == '0' and i is not len(binary_rep)-1:
            # increase current gap length if its zero
            current_gap_length += 1
        else:
            if binary_rep[i] == '0' and i is len(binary_rep)-1:
                current_gap_length+=1
            # if its 1 or latest digit as zero, check the current gap length
            max_gap_length = max(max_gap_length, current_gap_length)
            current_gap_length = 0
    return max_gap_length

# Example
number=257
print(bin(number)[2:])
print(solution(number)) 
