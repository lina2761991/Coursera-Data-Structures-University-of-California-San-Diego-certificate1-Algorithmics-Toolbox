import sys

def get_change(m):
    k = 1
    n = [0]*(m+1) #length of the array is m+1 and every element is set to 0 as a default value
    while k <= m:
        #where the code happens
        
        if k >= 4:
            n[k] = min(n[k-1] + 1, n[k-3] + 1, n[k-4] + 1) # this is for the 4 and up
        elif k == 3:
            n[k] = min(n[k - 1] + 1, n[k - 3] + 1) #this is for 3
        else:
            n[k] = n[k-1] + 1 # this is for the 1 and 2 
        
        ####
        k += 1 #go to the next element in the array
        
        
    return n[m] # after everything is done, return the last element of the array

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    
    # I did the dynamic programming wit the help of this video explanation 
    # https://www.youtube.com/watch?v=jgiZlGzXMBw&t=10s&ab_channel=BackToBackSWE
    # https://www.youtube.com/watch?v=WbwP4w6TpCk&ab_channel=WebDevSimplified
