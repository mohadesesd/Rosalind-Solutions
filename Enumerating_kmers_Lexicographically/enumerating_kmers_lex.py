import itertools

result = []
inputs = list(input().split())
length = int(input())
result = list(itertools.product(inputs, repeat = length))
result.sort()
for array in result:
    for i in range(len(array[:length])):
        if(i == (len(array[:length])-1)):
            print(array[:length][i])
        else:
            print(array[i], end = '')