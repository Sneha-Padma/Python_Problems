#Day14 Sum of Elements in a Subarray (Prefix Sum)
def solve():
    import sys
    input = sys.stdin.readline   
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]
    for _ in range(q):
        L, R = map(int, input().split())
        print(prefix[R] - prefix[L - 1])
if __name__ == "__main__":
    solve()
