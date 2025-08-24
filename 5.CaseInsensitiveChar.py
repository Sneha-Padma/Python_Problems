# Day5 Case-Insensitive Character Frequency with sorting
from collections import Counter

def solve():
    s = input().strip().lower().replace(" ", "")
    freq = Counter(ch for ch in s if ch.isalnum())
    for ch in sorted(freq.keys(), key=ord):   # ASCII order
        print(f"{ch} : {freq[ch]}")

solve()
