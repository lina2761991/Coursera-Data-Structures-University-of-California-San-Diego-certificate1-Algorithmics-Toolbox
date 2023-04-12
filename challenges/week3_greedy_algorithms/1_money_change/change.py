# Uses python3
import sys

def change(money):
    # write your code here
    # we have change of 10,5 and 1
    # in order to have the 10 we do money %10
    # in order to have the 5 we have to have the rest of money %5
    # in order to have the 1 we have to %1
  

    d = money//10 # this is the result of the division  by 10 
    f = (money-(money//10)*10)//5 # this is the result of the division of the rest  by 5 
    o = (money - (d*10 +f *5))//1 # this is the result of the division of the rest  by 1
    #print(d)
    #print(f)
    #print(o)
    return d + f + o

if __name__ == '__main__':
    m = int(input())
    print(change(m))
