#Day19 N-Queens Problem
def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    cols = set()
    diag1 = set() 
    diag2 = set() 
    
    solution = []

    def backtrack(row):
        if row == N:
            for r in board:
                solution.append(" ".join(map(str, r)))
            return True

        for col in range(N):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            board[row][col] = 1
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            if backtrack(row + 1):
                return True
            
            board[row][col] = 0
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
        return False
    
    if backtrack(0):
        print("\n".join(solution))
    else:
        print(-1)
N = int(input().strip())
solve_nqueens(N)
