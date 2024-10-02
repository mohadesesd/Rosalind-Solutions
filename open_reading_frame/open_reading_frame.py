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

def transcribe(dna):
    rna = dna.replace('T', 'U')
    return rna
def complement(sequence):
    complement = sequence.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')[::-1]
    return complement

dict = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L', 'AUC':'I',
    'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M',
    'GUG':'V', 'UCU':'S', 'CCU': 'P', 'ACU':'T', 'GCU': 'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 'UCA':'S',
    'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU':'Y',
    'CAU': 'H',  'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC':'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C',  'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

DNA = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\open_reading_frame\\rosalind_orf.txt')[0]
RNA = transcribe(DNA)
RNA_comp = transcribe(complement(DNA))
def translate(RNA):
    proteins = []
    for j in range(len(RNA)):
        protein = ''
        for i in range(j, len(RNA), 3):
            if(len(RNA[i:i+3]) == 3):
                if(dict[RNA[i:i+3]] != 'Stop'):
                    protein += dict[RNA[i:i+3]]
                else:
                    proteins.append(protein)
                    protein = ''
            else:
                proteins.append(protein)
                protein = ''
    return proteins

proteins = translate(RNA)
proteins_comp = translate(RNA_comp)
orfs = []
for protein in proteins:
    for i in range(len(protein)):
        if(protein[i] == 'M'):
            orfs.append(protein[i:])
            break
for protein in proteins_comp:
    for i in range(len(protein)):
        if(protein[i] == 'M'):
            orfs.append(protein[i:])

orfs = set(orfs)
for orf in orfs:
    print(orf)