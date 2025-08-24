# Day26 Chocolate game
a,b=map(int,input().split())
s=0
while a and b:
    if a>=b:a,s=a%b,s+a//b
    else:b,s=b%a,s+b//a
print(s)
