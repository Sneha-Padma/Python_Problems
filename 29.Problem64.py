#Day29 Problem 64
N = int(input().strip())
numbers = input().strip().split()
total_sum = 0
for num in numbers:
    min_digit = min(int(d) for d in num)
    total_sum += min_digit
print(total_sum)
