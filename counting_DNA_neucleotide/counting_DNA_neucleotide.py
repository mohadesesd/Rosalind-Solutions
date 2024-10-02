def count_base(sequence):
    base = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    base['A'] = sequence.count('A')
    base['T'] = sequence.count('T')
    base['C'] = sequence.count('C')
    base['G'] = sequence.count('G')
    return base 

def read_input(file):
    with open(file, 'r') as input:
        sequence = input.readline()
        return (count_base(sequence))
    
if __name__ == '__main__':
    print(read_input('c:\\Users\\ASUS\\Desktop\\Rosalind\\counting_DNA_neucleotide\\rosalind_dna.txt'))