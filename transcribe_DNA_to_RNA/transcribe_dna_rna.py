def transcribe(dna):
    rna = dna.replace('T', 'U')
    return rna

def read_input(file):
    with open(file, 'r') as input:
        sequence = input.readline()
        return (transcribe(sequence))
    
if __name__ == '__main__':
    print(read_input('c:\\Users\\ASUS\\Desktop\\Rosalind\\transcribe_DNA_to_RNA\\rosalind_rna.txt'))