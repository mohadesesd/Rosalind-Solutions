def permutation(k, array, result):
    if k == len(array):
        result.append(array.copy())
        for i in range(len(array)):
            if(i == (len(array)-1)):
                print(array[i])
            else:
                print(array[i], end = ' ')
    else:
        for i in range(k, len(array)):
           array[i], array[k] = array[k], array[i]
           permutation(k+1, array, result)
           array[i], array[k] = array[k], array[i]

result = []
permutation(0, list(range(1, 7)), result)
print(len(result))