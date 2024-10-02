def transcribe(dna):
    rna = dna.replace('T', 'U')
    return rna

def translate(rna):
    dict = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L', 'AUC':'I',
    'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M',
    'GUG':'V', 'UCU':'S', 'CCU': 'P', 'ACU':'T', 'GCU': 'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 'UCA':'S',
    'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU':'Y',
    'CAU': 'H',  'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC':'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C',  'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

    protein = ''
    for i in range(0, len(rna), 3):
        protein += dict[rna[i:i+3]]
    return protein

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

def splicing(seqs):
    DNA = seqs[0]
    introns = seqs[1:]
    for intron in introns:
        indx = DNA.find(intron)
        DNA = DNA[:indx] + DNA[indx+len(intron):]
    return translate(transcribe(DNA))[:-4]

print(splicing(handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\RNA_splicing\\rosalind_splc.txt')))