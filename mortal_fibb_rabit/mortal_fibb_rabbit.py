n, m = map(int, input().split())

def FC(n, m):
    fc = [0 for _ in range(n)]
    fc[0] = 1
    fc[1] = 1
    for i in range(2, n):
        if(m < i):
            fc[i] = fc[i-1] + fc[i-2] - fc[i-m-1]
        elif(m == i):
            fc[i] = fc[i-1] + fc[i-2] - 1
        else:
            fc[i] = fc[i-1] + fc[i-2]

    return fc[-1]

print(FC(n, m))