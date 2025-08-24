#Day 12 Find First Non-Repeating Character in a String
from collections import Counter
def first_non_repeating_char(S):
    freq = Counter(S)  
    for ch in S:
        if freq[ch] == 1:
            return ch
    return "NO"
S = input().strip()
print(first_non_repeating_char(S))
