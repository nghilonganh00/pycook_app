import math
def check(n):
    sum_digits = sum([int(digit) for digit in n])
    
    tmp = str(sum_digits)
    if tmp == tmp[::-1]:
        return True
    else:
        return False

t = int(input())
for i in range(t):
    n = input()
    if check(n): print("YES")
    else : print("NO")