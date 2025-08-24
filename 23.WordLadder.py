#Day23 Word Ladder
from collections import deque
def wordLadder(beginWord, endWord, wordList):
    wordSet, L = set(wordList), len(beginWord)
    if endWord not in wordSet: return 0
    q, vis = deque([(beginWord,1)]), {beginWord}
    while q:
        w,d = q.popleft()
        if w == endWord: return d
        for i in range(L):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != w[i]:
                    nxt = w[:i]+c+w[i+1:]
                    if nxt in wordSet and nxt not in vis:
                        vis.add(nxt); q.append((nxt,d+1))
    return 0
bw = input().strip()
ew = input().strip()
n  = int(input().strip())
wl = [input().strip() for _ in range(n)]
print(wordLadder(bw, ew, wl))
