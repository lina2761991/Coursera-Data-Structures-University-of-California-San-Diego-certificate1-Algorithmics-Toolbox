# Uses python3
import sys



def gcd(x, y):
    if y == 0:
        return x 
    else:
        return gcd(y, x%y)

def LCM(x, y):
    lcm = (x*y)//gcd(x,y) # the // in pyhton returns the closest int to the division 
    return lcm



if __name__ == "__main__":
    l = list(map(int,input().split()))
    a = l[0]
    b = l[1]
    print(LCM(a,b))