from itertools import product



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

def product1(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]

def k_mer_compposition(seq, k):
    counter = {}
    k_mers = product1(k)
    k_mers.sort()

    for k_mer in k_mers:
        counter[k_mer] = 0
    
    for i in range(len(seq)-k+1):
        k_mer = seq[i:i+k]
        counter[k_mer] += 1

    return list(counter.values())

inputs = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\k_mer_composition\\rosalind_kmer.txt')
result = str(k_mer_compposition(inputs[0], 4))
print(result.replace(',', '')[1:-1])