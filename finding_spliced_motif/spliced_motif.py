def motif(sequence1, sequence2):
    positions = []
    for i in range(len(sequence1)-len(sequence2) + 1):
        if(sequence1[i:i+len(sequence2)] == sequence2):
            positions.append(i+1)
    return positions

def spliced_motif(s, t):
    indices = []
    for i in t:
        indx = motif(s, i)
        if(indices):
            for i in indx:
                if(i > indices[-1]):
                    indices.append(i)
                    break
        else:
            indices.append(indx[0])
    return indices

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
input = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\finding_spliced_motif\\rosalind_sseq.txt')
output = spliced_motif(input[0], input[1])
for i in range(len(output)):
    if(i == (len(output)-1)):
        print(output[i])
    else:
        print(output[i], end =' ')