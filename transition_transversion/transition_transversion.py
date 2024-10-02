def transition_transversion(seq1, seq2):
    transition = 0
    transversion = 0
    for i in range(len(seq1)):
        if((seq1[i] == 'A' and seq2[i] =='G') or (seq1[i] == 'G' and seq2[i] == 'A') or (seq1[i] == 'C' and seq2[i] =='T') or (seq1[i] == 'T' and seq2[i] == 'C')):
            transition += 1
        
        if((seq1[i] == 'A' and seq2[i] =='C') or (seq1[i] == 'C' and seq2[i] == 'A') or (seq1[i] == 'G' and seq2[i] =='T') or (seq1[i] == 'T' and seq2[i] == 'G') or (seq1[i] == 'G' and seq2[i] =='C') or (seq1[i] == 'C' and seq2[i] == 'G') or (seq1[i] == 'A' and seq2[i] =='T') or (seq1[i] == 'T' and seq2[i] == 'A')):
            transversion += 1
    return transition/transversion



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

sequences = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\transition_transversion\\rosalind_tran.txt')
print(transition_transversion(sequences[0], sequences[1]))