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

def common_ancester(seqs):
    dict = {'A':[0 for _ in range(len(seqs[0]))], 'T':[0 for _ in range(len(seqs[0]))], 'C':[0 for _ in range(len(seqs[0]))], 'G':[0 for _ in range(len(seqs[0]))]}
    for seq in seqs:
        for i, s in enumerate(seq):
            dict[s][i] += 1
    consensus = ''
    for j in range(len(seqs[0])):
        max = 0
        chra = ''
        if(dict['A'][j] > max):
            max = dict['A'][j]
            chra = 'A'
        if(dict['T'][j] > max):
            max = dict['T'][j]
            chra = 'T'
        if(dict['C'][j] > max):
            max = dict['C'][j]
            chra = 'C'
        if(dict['G'][j] > max):
            max = dict['G'][j]
            chra = 'G'
        consensus += chra
    return consensus, dict

consensus, dict = common_ancester(handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\common_ancester\\rosalind_cons.txt'))
print(consensus)
print('A: ', end='')
for i in range(len(dict['A'])-1):
    print(dict['A'][i], end=' ')
print(dict['A'][len(dict['A'])-1])
print('C: ', end='')
for i in range(len(dict['C'])-1):
    print(dict['C'][i], end=' ')
print(dict['C'][len(dict['C'])-1])
print('G: ', end='')
for i in range(len(dict['G'])-1):
    print(dict['G'][i], end=' ')
print(dict['G'][len(dict['G'])-1])
print('T: ', end='')
for i in range(len(dict['T'])-1):
    print(dict['T'][i], end=' ')
print(dict['T'][len(dict['T'])-1])