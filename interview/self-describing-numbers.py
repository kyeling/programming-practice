import sys 

n = sys.argv[1]
arrlen = len(n)

if int(max(n)) > arrlen: # edge case
    print(0)

else:
    freq = [0] * arrlen # array with indices 0 to N-1

    # iterate through input by digit and count occurrences of each number
    for digit in n:
        freq[int(digit)] += 1

    res = ''.join(map(str, freq)) # convert freq to array of strings, then convert to string
    if n == res:
        print(1)
    else:
        print(0)


## solution 2
# iterate through input again and check that number of each position value occurs with the frequency of the digit in that position
# for pos in range(len(n)):
#     occur = int(n[pos])
#     if occur != freq[pos]:
#         print(0)
#         break
# if occur == 0:
#     print(1)


## solution 1
# for pos in range(len(n)):
#     occur = int(n[pos])
#     for dig in n:
#         if pos == int(dig):
#             occur -= 1
#     if occur != 0:
#         print(0)
#         break
# if occur == 0:
#     print(1)
