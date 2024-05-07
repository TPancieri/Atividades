#You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
#Return the score of s.
class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_value = []
        for ch in s:
            ascii_value.append(ord(ch))
        ascii_abs = []
        for index, value in enumerate(ascii_value):
            if index < (len(s)-1):
                absolute = abs(ascii_value[index] - ascii_value[index+1])
                ascii_abs.append(absolute)
        return sum(ascii_abs)
