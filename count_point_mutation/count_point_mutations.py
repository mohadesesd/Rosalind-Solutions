first_sequence = input()
second_sequence = input()
cnt = 0
for i in range(len(first_sequence)):
    if(first_sequence[i] != second_sequence[i]):
        cnt += 1
print(cnt)