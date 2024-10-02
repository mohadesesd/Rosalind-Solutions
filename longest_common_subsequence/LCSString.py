def common_substring(strings):
    substring = ''
    for i in range(len(strings[0])):
        for j in range(i, len(strings[0])):
            if len(substring) < len(strings[0][i:j+1]):
                if(all(strings[0][i:j+1] in string for string in strings)):
                    substring = strings[0][i:j+1]
    return substring

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

print(common_substring(handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\longest_common_subsequence\\rosalind_lcsm.txt')))