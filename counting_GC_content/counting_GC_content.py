def calculate_GC_content(sequence):
    C = sequence.count('C')
    G = sequence.count('G')
    return ((C+G)*100)/len(sequence)

def max_CG_content(lines):
    max_GC = 0
    name_max = ''
    for name, seq in lines:
        GC_content = calculate_GC_content(seq)
        if(max_GC < GC_content):
            max_GC = GC_content
            name_max = name
    return name_max, max_GC

def handle_input(file):
    fasta = open(file, 'r')
    seq = ''
    lines = []
    name = ''
    line = fasta.readline()
    while(line != ''):
        if (line[0] == '>'):
            if seq != '':
                lines.append([name, seq])
                seq = ''
            name = line[1:]
        else:
            seq += line.rstrip()

        line = fasta.readline()

    lines.append([name, seq])
    return lines 

name, max_content = max_CG_content(handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\counting_GC_content\\rosalind_gc.txt'))
print(name)
print(max_content)