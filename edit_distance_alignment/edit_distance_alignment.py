import numpy as np

def edit_distance_alignment(sequence1, sequence2):
    dp = [[0]*(len(sequence2)) for _ in range(len(sequence1))]
    dir = [[0]*(len(sequence2)) for _ in range(len(sequence1))]
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
                if(dp[i][j] == (dp[i][j-1] + 1)):
                    dir[i][j] = 'L'
                elif(dp[i][j] == (dp[i-1][j] + 1)):
                    dir[i][j] = 'U'
                else:
                    dir[i][j] = 'D'
            else:
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
                if(dp[i][j] == (dp[i-1][j-1] + 1)):
                    dir[i][j] = 'D'
                elif(dp[i][j] == (dp[i-1][j] + 1)):
                    dir[i][j] = 'U'
                else:
                    dir[i][j] = 'L'
    return dp[len(sequence1)-1][len(sequence2)-1], dir

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

def print_alignment(dir, sequence1, sequence2):
    align1 = ''
    align2 = ''
    cnt_i = len(sequence1) - 1
    cnt_j = len(sequence2) - 1
    while(cnt_i >= 0 and cnt_j >= 0): 
            if (dir[cnt_i][cnt_j] == 'L'):
                align2 = sequence2[cnt_j] + align2
                cnt_j -= 1
                align1 = '-' + align1
            elif(dir[cnt_i][cnt_j] == 'U'):
                align1 = sequence1[cnt_i] + align1
                cnt_i -= 1
                align2 = '-' + align2
            elif(dir[cnt_i][cnt_j] == 'D'):
                align1 = sequence1[cnt_i] + align1
                align2 = sequence2[cnt_j] + align2
                cnt_i -= 1
                cnt_j -= 1
            else:
                align1 = sequence1[cnt_i] + align1
                align2 = sequence2[cnt_j] + align2
                cnt_i -= 1
                cnt_j -= 1
    while(cnt_i >= 0):
        align1 = sequence1[cnt_i] + align1
        cnt_i -= 1
    while(cnt_j >= 0):
        align2 = sequence2[cnt_j] + align2
        cnt_j -= 1
    return align1, align2

inputs = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\edit_distance_alignment\\rosalind_edta.txt')
dist, dir = edit_distance_alignment(inputs[0], inputs[1])
align1, align2 = print_alignment(dir, inputs[0], inputs[1])
print(dist)
print(align1)
print(align2)