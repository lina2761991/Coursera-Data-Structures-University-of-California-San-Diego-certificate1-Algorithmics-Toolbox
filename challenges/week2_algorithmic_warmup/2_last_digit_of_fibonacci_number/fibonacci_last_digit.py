def fibonacci(n):
    a , b = 0,1
    for _ in range(n):
        a,b = b % 10, a+b % 10
    return a

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))