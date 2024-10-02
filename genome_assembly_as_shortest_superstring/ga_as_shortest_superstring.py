def handle_input(file):
    fasta = open(file, 'r')
    seq = ''
    lines = []

    line = fasta.readline()
    name = line[1:-1]

    while(line != ''):
        if (line[0] == '>'):
            if seq != '':
                lines.append(seq)
                seq = ''
                name = line[1:-1]
        else:
            seq += line.rstrip()

        line = fasta.readline()

    lines.append(seq)
    return lines 
"""
def get_overlap_strings(str1, str2):
    combined_string = []
    overlap_string = []
    for i in range(len(str1)):
        if(str1[i:] == str2[:len(str1)-i]):
            combined_string.append(str1+str2[len(str1)-i:])
            overlap_string.append(str1[i:])
            break
    
    for i in range(len(str2)):
        if(str2[i:] == str1[:len(str2)-i]):
            combined_string.append(str2+str1[len(str2)-i:])
            overlap_string.append(str2[i:])
            break

    if(not overlap_string):
        return "", ""
    
    combined_string_min = min(combined_string, key=len)
    overlap_string_max = max(overlap_string, key=len)
    return combined_string_min, overlap_string_max
        
def gs_superstring(nodes):
    temp = nodes 

    while len(temp) > 1:
        overlaping_pair = []
        overlaping_length = 0
        overlaping_string = ""
        for i in range(len(temp) - 1):
            for j in range(i+1, len(temp)):
                combined_string, overlap_string = get_overlap_strings(temp[i], temp[j])
                if(overlaping_length < len(overlap_string)):
                    overlaping_length = len(overlap_string)
                    overlap_string = combined_string
                    overlaping_pair = [temp[i], temp[j]]

        temp.remove(overlaping_pair[0])
        temp.remove(overlaping_pair[1])
        temp.append(overlaping_string)

    return temp
"""
def _get_overlap_strings(s1, s2):
    combine_strings = []
    overlap_strings = []
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1)-i]:
            overlap_strings.append(s1[i:])
            combine_strings.append(s1+s2[len(s1)-i:])
            break
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2)-i]:
            overlap_strings.append(s2[i:])
            combine_strings.append(s2+s1[len(s2)-i:])
            break
    if not overlap_strings:
        return "", ""

    combine_string = min(combine_strings, key=len)
    overlap_string = max(overlap_strings, key=len)
    return combine_string, overlap_string

def find_superstring(strings):
    temp = strings

    while len(temp) > 1:
        most_overlapping_string = ""
        most_overlapping_string_pair = []
        most_overlapping_string_length = 0

        for i in range(len(temp)-1):
            for j in range(i+1, len(temp)):
                combine_string, overlap_string = _get_overlap_strings(temp[i], temp[j])
                if len(overlap_string) > most_overlapping_string_length:
                    most_overlapping_string = combine_string
                    most_overlapping_string_pair = [temp[i], temp[j]]
                    most_overlapping_string_length = len(overlap_string)

        temp.remove(most_overlapping_string_pair[0])
        temp.remove(most_overlapping_string_pair[1])
        temp.append(most_overlapping_string)
        
    return temp 
                    

nodes = handle_input('C:\\Users\\ASUS\\Desktop\\Rosalind\\genome_assembly_as_shortest_superstring\\rosalind_long.txt')
find_superstring(nodes)