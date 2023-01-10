# foobar.withgoogle.com Level 2
# also LeetCode 1363: Largest Multiple of Three

from collections import Counter    

# remove smallest remainder (fewest digits, then lowest values)
def solution(l):
    digit_freqs = dict(Counter(l))
    sum_digits = sum([k * v for k, v in digit_freqs.items()])

    r1_combinations = [[1], [4], [7], [2,2], [5,2], [5,5], [8,2], [8,5], [8,8]]
    r2_combinations = [[2], [5], [8], [1,1], [4,1], [4,4], [7,1], [7,4], [7,7]]
    r_combinations = {1 : r1_combinations, 2 : r2_combinations}
    r = sum_digits % 3 # either 1 or 2

    if r:
        # remove the fewest digits and smallest number(s) possible to subtract mod remainder
        combination_found = False
        for fst, *snd in r_combinations[r]:
            if snd: 
                snd = snd[0]
                if (fst == snd and digit_freqs.get(fst, 0) >= 2) or (fst != snd and digit_freqs.get(fst, 0) and digit_freqs.get(snd, 0)):
                    digit_freqs[fst] -= 1
                    digit_freqs[snd] -= 1
                    sum_digits -= (fst + snd)
                    combination_found = True
                    break
            elif digit_freqs.get(fst, 0):
                digit_freqs[fst] -= 1
                sum_digits -= fst
                combination_found = True
                break
        if not combination_found: return 0

    res = []
    for k, v in digit_freqs.items():
        res += [k] * v 
    
    if not res: return 0
    res = sorted(res, reverse=True)
    res_str = ''.join(list(map(str, res)))
    return res_str


if __name__ == '__main__':
    input = [5,2,3]
    # [1,1,1,1,8,8]
    # [1,2,3,4,5,6,7,8,9]
    # [3, 1, 4, 1]
    # [3, 1, 4, 1, 5, 9]
    # [8,5,4,8,4]
    print(input)
    print(solution(input))