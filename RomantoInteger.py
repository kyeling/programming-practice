class Solution(object):
    def romanToInt(self, s):
        sum = 0
        prev = 0
        val = 0
        for c in s:
            val = self.getValue(c)
            sum += val
            if prev < val: sum -= 2*prev
            prev = val
        return sum
    
    def getValue(self, c):
        if c == 'I': return 1 
        if c == 'V': return 5 
        if c == 'X': return 10 
        if c == 'L': return 50 
        if c == 'C': return 100 
        if c == 'D': return 500 
        if c == 'M': return 1000 

# define values
# parse string and get each value
# sum values, if value is greater than previous, subtract 2*previous (to make up for adding it)
#     instead of storing values in array to compare previous value, just store previous value

# test cases:
    # empty string, numbers with subtraction, numbers that weren't valid roman numerals (e.g. VIIIII)
