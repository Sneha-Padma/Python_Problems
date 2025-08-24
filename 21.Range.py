#Day21 Range Sum Query and Point Update using Segment Tree
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  

    def update(self, i, delta):
        """Add delta to element at index i (1-based)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        """Prefix sum up to index i (1-based)."""
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        """Sum from index l to r (inclusive)."""
        return self.query(r) - self.query(l - 1)
n, q = map(int, input().split())
arr = list(map(int, input().split()))

fenwick = FenwickTree(n)
for i, val in enumerate(arr, 1):
    fenwick.update(i, val)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        
        i, x = query[1], query[2]
        delta = x - arr[i - 1]
        arr[i - 1] = x
        fenwick.update(i, delta)
    else:
        l, r = query[1], query[2]
        print(fenwick.range_sum(l, r))
