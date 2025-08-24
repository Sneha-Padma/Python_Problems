#Day30 Monsters vs Heros
import sys
class BIT:
    def __init__(self, n):
        self.n = n
        self.ft = [0] * (n + 5)

    def _add(self, i, delta):
        while i <= self.n:
            self.ft[i] += delta
            i += i & -i

    def range_add(self, l, r, delta):
        if l > r:
            return
        self._add(l, delta)
        self._add(r + 1, -delta)

    def point_query(self, i):
        s = 0
        while i > 0:
            s += self.ft[i]
            i -= i & -i
        return s

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    N = next(it); Q = next(it)

    intervals = []      
    total_monsters = 0
    max_coord = 0

    for _ in range(N):
        L = next(it); R = next(it); S = next(it)
        intervals.append((S, L, R))
        total_monsters += (R - L + 1)
        if R > max_coord: max_coord = R
        if L > max_coord: max_coord = L

    pos = [0] * Q
    power = [0] * Q
    for i in range(Q):
        x = next(it); P = next(it)
        pos[i] = x
        power[i] = P
        if x > max_coord: max_coord = x
    intervals.sort(key=lambda t: t[0])
    queries = sorted([(power[i], pos[i], i) for i in range(Q)])

    bit = BIT(max_coord + 2)
    c_less = [0] * Q  

    p = 0
    for P, x, idx in queries:
        while p < N and intervals[p][0] < P:
            _, L, R = intervals[p]
            bit.range_add(L, R, 1)
            p += 1
        c_less[idx] = bit.point_query(x)
    last_max_power = [0] * (max_coord + 3)   
    last_count     = [0] * (max_coord + 3)
    remaining = total_monsters
    out = [0] * Q
    for i in range(Q):
        x = pos[i]
        P = power[i]
        if P > last_max_power[x]:
            delta = c_less[i] - last_count[x]
            if delta > 0:
                remaining -= delta
                last_count[x] = c_less[i]
            last_max_power[x] = P
        out[i] = remaining
    print(" ".join(map(str, out)))
if __name__ == "__main__":
    solve()
