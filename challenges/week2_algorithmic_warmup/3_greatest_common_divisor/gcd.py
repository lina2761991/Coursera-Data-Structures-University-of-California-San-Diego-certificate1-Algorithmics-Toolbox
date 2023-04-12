# Uses python3
import sys

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)#!!!!!!

if __name__ == "__main__":
    l = list(map(int,input().split()))
    a = l[0]
    b = l[1]
    print(gcd(a,b))