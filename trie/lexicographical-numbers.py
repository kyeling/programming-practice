class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if 1 <= n <= 9:
            return [i for i in range(1, n+1)]
        
        result = []
        current_num = 1
        while current_num > 0:
            if current_num in result: 
                break
            else:
                result.append(current_num)
            
            if current_num * 10 <= n:
                # go down one level
                current_num = current_num * 10
            elif current_num % 10 < 9 and current_num + 1 <= n:
                # travel sideways across level
                current_num += 1
            else:
                # go up one or more levels
                parent_num = current_num // 10
                while parent_num % 10 >= 9:
                    parent_num //= 10
                current_num = parent_num + 1
        
        return result

"""
example 1: n=13
- starting with 1: 1, 10, 11, 12, 13 (14 > 13 so not included)
- starting with 2: 2, (20 > 13 so not included)
- starting with 3: 3, etc

example 2: n=2
- starting with 1: 1 (10 > 2)
- starting with 2: 2 (20 > 2) etc

example 3: n=224
- 1, 10..19, 100..109, 110..119, 120..129, ..., 190..199, (1000 > 224)
- 2, 20..29, 200..209, 210..219, 220..224 (225 > 224)
- 3, 30..39, (300 > 224)

approach:
iterate from starting digits 1 through 10:
for each digit, try appending 0 through 9 and see if it exceeds n
for each of those digits, try appending 0 through 9 and see if it exceeds 0 through 9

[""]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], ...
[100, 101, 102, 103, 104, 105, 106, 107, 108, 109], ...

depth first search: 1 --> 10 --> 100 (backtrack) ---> 10 -> 11 -> 12 -> 13 -> 14 ---> 1 -> 2 -> 3 ...
"""
