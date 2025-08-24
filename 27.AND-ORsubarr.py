# Day27 AND OR subarray
def solve():
    T = int(input().strip()) 
    for _ in range(T):
        N = int(input().strip())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        max_len = 0
        for i in range(N):
            or_val = 0
            and_val = B[i]
            for j in range(i, N):
                or_val |= A[j]
                and_val &= B[j]
                if or_val == and_val:
                    max_len = max(max_len, j - i + 1)
                if or_val > and_val:
                    break

        print(max_len)
if __name__ == "__main__":
    solve()
