import numpy as np

PAM_250 = [['', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'],
    ['A', '2', '-2', '0', '0', '-3', '1', '-1', '-1', '-1', '-2', '-1', '0', '1', '0', '-2', '1', '1', '0', '-6', '-3'],
    ['C', '-2', '12', '-5', '-5', '-4', '-3', '-3', '-2', '-5', '-6', '-5', '-4', '-3', '-5', '-4', '0', '-2', '-2', '-8', '0'],
    ['D', '0', '-5', '4', '3', '-6', '1', '1', '-2', '0', '-4', '-3', '2', '-1', '2', '-1', '0', '0', '-2', '-7', '-4'],
    ['E', '0', '-5', '3', '4', '-5', '0', '1', '-2', '0', '-3', '-2', '1', '-1', '2', '-1', '0', '0', '-2', '-7', '-4'],
    ['F', '-3', '-4', '-6', '-5', '9', '-5', '-2', '1', '-5', '2', '0', '-3', '-5', '-5', '-4', '-3', '-3', '-1', '0', '7'],
    ['G', '1', '-3', '1', '0', '-5', '5', '-2', '-3', '-2', '-4', '-3', '0', '0', '-1', '-3', '1', '0', '-1', '-7', '-5'],
    ['H', '-1', '-3', '1', '1', '-2', '-2', '6', '-2', '0', '-2', '-2', '2', '0', '3', '2', '-1', '-1', '-2', '-3', '0'],
    ['I', '-1', '-2', '-2', '-2', '1', '-3', '-2', '5', '-2', '2', '2', '-2', '-2', '-2', '-2', '-1', '0', '4', '-5', '-1'],
    ['K', '-1', '-5', '0', '0', '-5', '-2', '0', '-2', '5', '-3', '0', '1', '-1', '1', '3', '0', '0', '-2', '-3', '-4'],
    ['L', '-2', '-6', '-4', '-3', '2', '-4', '-2', '2', '-3', '6', '4', '-3', '-3', '-2', '-3', '-3', '-2', '2', '-2', '-1'],
    ['M', '-1', '-5', '-3', '-2', '0', '-3', '-2', '2', '0', '4', '6', '-2', '-2', '-1', '0', '-2', '-1', '2', '-4', '-2'],
    ['N', '0', '-4', '2', '1', '-3', '0', '2', '-2', '1', '-3', '-2', '2', '0', '1', '0', '1', '0', '-2', '-4', '-2'],
    ['P', '1', '-3', '-1', '-1', '-5', '0', '0', '-2', '-1', '-3', '-2', '0', '6', '0', '0', '1', '0', '-1', '-6', '-5'],
    ['Q', '0', '-5', '2', '2', '-5', '-1', '3', '-2', '1', '-2', '-1', '1', '0', '4', '1', '-1', '-1', '-2', '-5', '-4'],
    ['R', '-2', '-4', '-1', '-1', '-4', '-3', '2', '-2', '3', '-3', '0', '0', '0', '1', '6', '0', '-1', '-2', '2', '-4'],
    ['S', '1', '0', '0', '0', '-3', '1', '-1', '-1', '0', '-3', '-2', '1', '1', '-1', '0', '2', '1', '-1', '-2', '-3'],
    ['T', '1', '-2', '0', '0', '-3', '0', '-1', '0', '0', '-2', '-1', '0', '0', '-1', '-1', '1', '3', '0', '-5', '-3'],
    ['V', '0', '-2', '-2', '-2', '-1', '-1', '-2', '4', '-2', '2', '2', '-2', '-1', '-2', '-2', '-1', '0', '4', '-6', '-2'],
    ['W', '-6', '-8', '-7', '-7', '0', '-7', '-3', '-5', '-3', '-2', '-4', '-4', '-6', '-5', '2', '-2', '-5', '-6', '17', '0'],
    ['Y', '-3', '0', '-4', '-4', '7', '-5', '0', '-1', '-4', '-1', '-2', '-2', '-5', '-4', '-4', '-3', '-3', '-2', '0', '10']
]

def local_alignment(sequence1, sequence2, alignment_matrix, sigma):
    dp = [[0]*(len(sequence2)+1) for _ in range(len(sequence1)+1)]
    dir = [[0]*(len(sequence2)+1) for _ in range(len(sequence1)+1)]
    for i in range(1, len(sequence1)+1):
        for j in range(1, len(sequence2)+1):
            for k in range(len(alignment_matrix[0])):
                if(sequence1[i-1] == alignment_matrix[0][k]):
                    indx_i = k
                if(sequence2[j-1] == alignment_matrix[0][k]):
                    indx_j = k
            score = int(alignment_matrix[indx_i][indx_j])
            scores = [dp[i-1][j] + sigma, dp[i][j-1] + sigma , dp[i-1][j-1] + score, 0]
            dp[i][j] = max(scores)
            dir[i][j] = scores.index(dp[i][j])
    return np.array(dp).max(), dp, dir

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

def print_alignment(dp, dir, sequence1, sequence2):
    dp_array = np.array(dp)
    cnt_i, cnt_j = np.unravel_index(dp_array.argmax(), dp_array.shape)
    i, j = np.where(dp_array == dp_array.max())
    aligned1, aligned2 = sequence1[:cnt_i], sequence2[:cnt_j]
    while((dir[cnt_i][cnt_j] != 3) and (cnt_i*cnt_j != 0)):
        if(dir[cnt_i][cnt_j] == 2):
            cnt_i -= 1
            cnt_j -= 1
        elif(dir[cnt_i][cnt_j] == 1):
            cnt_j -= 1
        elif(dir[cnt_i][cnt_j] == 0):
            cnt_i -= 1
        else:
            break
    aligned1 = aligned1[cnt_i:]
    aligned2 = aligned2[cnt_j:]
    return aligned1, aligned2

inputs = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\local_alignment\\rosalind_local.txt')
dist, dp, dir = local_alignment(inputs[0], inputs[1], PAM_250, sigma = -5)
align1, align2 = print_alignment(dp, dir, inputs[0], inputs[1])
print(dist)
print(align1)
print(align2)