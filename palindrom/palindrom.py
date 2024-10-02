def complement(sequence):
    complement = sequence.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')[::-1]
    return complement

def is_reverse_palindrom(sequence):
    if(complement(sequence) == sequence):
        return True 
    else:
        return False 
    
def all_subseqs(sequence):
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            subseq = sequence[i:j+1]
            if ((4 <= len(subseq)) and (len(subseq) <= 12)):
                if(is_reverse_palindrom(subseq)):
                    print(i+1, len(subseq))
            
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

all_subseqs(handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\palindrom\\rosalind_revp.txt')[0])
