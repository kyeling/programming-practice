def solution(M, A): # M is highest bound for array elements
    N = len(A) # length of array A
    count = [0] * (M + 1) # map for counts (index as key) for 0 to M
    maxOccurence = 1 # there is at least 1 integer that occurs 1 time
    index = -1
    for i in range(N): # iterate through array in linear time
        count[A[i]] += 1
        if count[A[i]] > 0: # if number has already been seen before
            tmp = count[A[i]]
            if tmp > maxOccurence: # if number of times seen before greater than maxOccurence # should be tmp + 1
                maxOccurence = tmp
                index = i
        #     count[A[i]] = tmp + 1
        # else:
        #     count[A[i]] = 1
    return A[index]

# didn't pass performance tests
from collections import Counter
def solution(S):
    # write your code in Python 3.6

    # even case: 1 operation (rightmost/least significant bit is 0, shift right to divide by 2)
    # odd case: 2 operations (least significant bit is 1, subtract 1 then divide to get rid of digit)

    # leading 0s case: 0 operations (strip these from input)
    # single 1 case: 1 operation (subtract 1 and it becomes 0)


    # strip leading zeroes
    s = str(int(S))

    # edge case: s = "0"
    if s == "0": return 0

    # initialize a map to count the number of occurences of 0s and 1s (linear time)
    counts = Counter(s)

    # add 1 operation for each "0" and 2 operations for each "1"
    # subtract 1 because the leading "1" will only need 1 operation instead of 2 to become 0
    # (we're guaranteed that s has a leading 1 because all leading 0s were stripped and s is not 0)
    num_operations = counts["0"] + 2 * counts["1"] - 1

    return num_operations