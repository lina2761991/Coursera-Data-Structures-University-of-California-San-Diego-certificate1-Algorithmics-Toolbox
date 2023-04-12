def fibonacci(n):
    if n<=1:
        print(n)  
        quit()
    else:
        a, b =  0, 1
        for _ in range(n-1):
            c = a + b
             
            b, a = c, b
        print(c)

if __name__ == "__main__":
    n = int(input())
    fibonacci(n)