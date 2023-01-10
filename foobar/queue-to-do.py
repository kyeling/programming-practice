# Google Foobar Level 3a

# auxiliary function for visualizing queue based on input
def print_q(start, length):
    for i in range(length, 0, -1):
        for j in range(i):
            print(start, end=' ')
            start += 1
        print('/', end=' ')
        for j in range(i+1, length+1):
            print(start, end=' ')
            start += 1
        print('')
    return


# return result of taking the xor of all numbers in the range 
# 1 to n (inclusive) in constant time
def xor_one_to_n(n):
    if n % 4 == 0: return n
    if n % 4 == 1: return 1
    if n % 4 == 2: return n + 1
    if n % 4 == 3: return 0

def solution(start, length):
    checksum = start + length * (length - 1)
    for i, l in zip(range(length-1), range(length,1,-1)):
        row_start = start + (i * length) - 1
        checksum = checksum ^ xor_one_to_n(row_start) ^ xor_one_to_n(row_start + l)
    return checksum

if __name__ == '__main__':
    res = solution(3,1)
    print(res)
