import numpy as np

def LCS(sequence1, sequence2):
    dp = [[0]*(len(sequence2) + 1) for _ in range(len(sequence1) + 1)]
    dir = [[0]*(len(sequence2) + 1) for _ in range(len(sequence1) + 1)]
    for i in range(1, (len(sequence1)+1)):
        for j in range(1, len(sequence2)+1):
            if(sequence1[i-1] == sequence2[j-1]):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+1)
                if(dp[i][j] == dp[i][j-1]):
                    dir[i][j] = 'L'
                elif(dp[i][j] == dp[i-1][j]):
                    dir[i][j] = 'U'
                else:
                    dir[i][j] = 'D'
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if(dp[i][j] == dp[i][j-1]):
                    dir[i][j] = 'L'
                elif(dp[i][j] == dp[i-1][j]):
                    dir[i][j] = 'U'
    return dp, dir

def print_LCS(dp, dir, sequence1):
    dp_array = np.array(dp)
    i, j = np.where(dp_array == dp_array.max())
    cnt_i = i[0]
    cnt_j = j[0]
    str = ''
    while(cnt_i > 0 and cnt_j > 0): 
            if (dir[cnt_i][cnt_j] == 'L'):
                cnt_j -= 1
            elif(dir[cnt_i][cnt_j] == 'U'):
                cnt_i -= 1
            elif(dir[cnt_i][cnt_j] == 'D'):
                str = sequence1[cnt_i - 1] + str
                cnt_i -= 1
                cnt_j -= 1
    return str

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

inputs = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\longest_common_subsequence\\rosalind_lcsq.txt')
dp, dir = LCS(inputs[0], inputs[1])
print(print_LCS(dp, dir, inputs[0]))