from math import comb
k, m, n = map(int, input().split())

dominant_pairs = comb(k, 2) + comb(k, 1)*comb(m, 1) + comb(k, 1)*comb(n, 1) +\
    comb(m, 2)*0.75 + comb(m, 1)*comb(n, 1)*0.5

all_pairs = comb((k + m + n), 2)

print(dominant_pairs/all_pairs)