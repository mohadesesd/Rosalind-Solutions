n, k = map(int, input().split())

def comb(n, k):
    pi = 1
    for i in range(n-k+1, n+1):
        pi *= i
    return pi    

print(comb(n, k)%1000000)