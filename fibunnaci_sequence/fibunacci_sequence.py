n, k = map(int, input().split())

def FC(n, k):
    fc = [0 for _ in range(n)]
    fc[0] = 1
    fc[1] = 1
    for i in range(2, n):
        fc[i] = fc[i-1] + fc[i-2]*k
    return fc[-1]

print(FC(n, k))