import re

sequence1 = input()
sequence2 = input()

positions = []
for i in range(len(sequence1)-len(sequence2) + 1):
    if(sequence1[i:i+len(sequence2)] == sequence2):
        positions.append(i+1)

for i in range(len(positions)):
    if(i == (len(positions) - 1)):
        print(positions[i])
    else:
        print(positions[i], end=' ')

