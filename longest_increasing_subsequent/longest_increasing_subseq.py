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
    final = []
    while(cnt_i > 0 and cnt_j > 0): 
            if (dir[cnt_i][cnt_j] == 'L'):
                cnt_j -= 1
            elif(dir[cnt_i][cnt_j] == 'U'):
                cnt_i -= 1
            elif(dir[cnt_i][cnt_j] == 'D'):
                final = [sequence1[cnt_i - 1]] + final
                cnt_i -= 1
                cnt_j -= 1
    return final
with open('C:\\Users\\ASUS\\Desktop\\Rosalind\\longest_increasing_subsequent\\rosalind_lgis.txt', 'r') as file:
    number = int(file.readline())
    input = list(map(int, file.readline().split()))
dp, dir = LCS(input, range(1, number+1))
inc = print_LCS(dp, dir, input)
for i in inc:
    print(i, end =' ')
print()
dp, dir = LCS(input, range(number+1, 1, -1))
dec = print_LCS(dp, dir, input)
for i in dec:
    print(i, end =' ')
print()