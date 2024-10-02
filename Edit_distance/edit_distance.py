import numpy as np

def edit_distance(sequence1, sequence2):
    dp = [[0]*(len(sequence2)) for _ in range(len(sequence1))]
    for i in range(len(sequence1)):
        for j in range(len(sequence2)):
            if(i == 0):
                if(sequence1[i] == sequence2[j]):
                    if((j-1) >= 0):
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                else:
                    if((j-1) >= 0):
                        dp[i][j] = dp[i][j-1] + 1
                    else:
                        dp[i][j] = 1
            elif(j == 0):
                if(sequence1[i] == sequence2[j]):
                    if((i-1) >= 0):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = 0
                else:
                    if((i-1) >= 0):
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = 1
            elif(sequence1[i] == sequence2[j]):
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
    return dp[len(sequence1)-1][len(sequence2)-1]

def handle_input(file):
    fasta = open(file, 'r')
    seq = ''
    lines = []

    line = fasta.readline()
    while(line != ''):
        if (line[0] == '>'):
            if seq != '':
                lines.append(seq)
                seq = ''
        else:
            seq += line.rstrip()

        line = fasta.readline()

    lines.append(seq)
    return lines 

inputs = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\Edit_distance\\rosalind_edit.txt')
print(edit_distance(inputs[1], inputs[0]))