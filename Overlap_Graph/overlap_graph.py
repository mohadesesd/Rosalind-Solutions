def handle_input(file):
    fasta = open(file, 'r')
    seq = ''
    lines = []

    line = fasta.readline()
    name = line[1:-1]

    while(line != ''):
        if (line[0] == '>'):
            if seq != '':
                lines.append([name, seq])
                seq = ''
                name = line[1:-1]
        else:
            seq += line.rstrip()

        line = fasta.readline()

    lines.append([name, seq])
    return lines 

def connected(seq1, seq2):
    """print(seq1)
    print(seq2)
    print(seq1[1][-3:])
    print(seq2[1][:3])"""
    if(seq1[1][-3:] == seq2[1][:3]):
        return f'{seq1[0]} {seq2[0]}'
    else:
        return ''

nodes = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\Overlap_Graph\\rosalind_grph.txt')
for seq1 in nodes:
    for seq2 in nodes:
        if(seq1 != seq2):
            if(connected(seq1, seq2) != ''):
                print(connected(seq1, seq2))
