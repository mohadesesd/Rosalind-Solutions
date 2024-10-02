from itertools import product
def permute1(letters, k):
    all_let = (''.join(str(x) for x in letters))
    all_perm = []
    for i in range(1,k+1):
        all_perm += [''.join(x) for x in product(all_let, repeat=i)]
    return all_perm
with open('.\\file.txt', 'w') as file:
    for i in sorted(permute1(['I', 'Z', 'L', 'S', 'J', 'N', 'X', 'C', 'O', 'D', 'K'], 3), key=lambda word: [['I', 'Z', 'L', 'S', 'J', 'N', 'X', 'C', 'O', 'D', 'K'].index(c) for c in word]):
        file.write(i)
        file.write('\n')