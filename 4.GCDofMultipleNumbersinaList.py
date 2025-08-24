# Day4 GCD of Multiple Numbers in a List 
import math
def gcd(a):
    if not a:
        return 0
    result = a[0]
    for i in range(1, len(a)):
        result = math.gcd(result, a[i])
    return result
n = int(input())
a = list(map(int, input().split()))
final_gcd = gcd(a)
print(final_gcd)