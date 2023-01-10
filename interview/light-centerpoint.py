# from Roblox CodeSignal assessment

import sys


# approach 1: time complexity O(max - min + r) ???
def get_center1(objects, r):
    # edge case: only one object, 
    # for minimal center, object is on rightmost edge
    if len(objects) == 1: 
        return objects[0]-r

    min_idx, max_idx = objects[0]-2*r, objects[-1]+1
    line = [1 if i in objects else 0 for i in range(min_idx, max_idx)] # number line

    ## debugging output
    debug = False
    if debug:
        print([i for i in range(min_idx, max_idx)])
        print(line)
        print([i for i in range(len(line))])

    best_c = r
    max_objs = sum(line[:2*r+1]) # first window index c-r=0 to c+r (exclude end index)
    num_objs = sum(line[:2*r+1])

    for c in range(r+1, len(line)-r):
        num_objs += line[c+r] - line[c-r-1]
        if debug: print(c, num_objs)
        if num_objs > max_objs:
            best_c = c
            max_objs = num_objs

    res = best_c + min_idx
    return res


# approach 2: O(n) time hopefully
def get_center2(objects, r):

    # same edge case as above
    n = len(objects)
    if n == 1: return objects[0]-r

    span = 2*r + 1
    i, best_j, curr_i = 0, 0, 0
    max_objs, curr_objs = 1, 1

    for i in range(1, n):
        if objects[i] - objects[curr_i] > span:
            if curr_objs > max_objs: best_j = i - 1  
            curr_i += 1
            curr_objs = 1
        else: 
            curr_objs += 1
            
    # account for last object 
    if curr_objs > max_objs: best_j = i 

    return objects[best_j] - r



# parse user input and print result
if __name__ == '__main__':

    # convert input (space-separated sequence of numbers in ascending order) to array
    objects = list(map(int, input().split()))

    # radius of light (total span of light is 2r + 1 ticks on number line)
    r = int(input())

    print(get_center2(objects, r))