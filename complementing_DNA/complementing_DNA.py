def complement(sequence):
    complement = sequence.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')[::-1]
    return complement

def read_input(file):
    with open(file, 'r') as input:
        sequence = input.readline()
        return (complement(sequence))
    
if __name__ == '__main__':
    print(read_input('c:\\Users\\ASUS\\Desktop\\Rosalind\\complementing_DNA\\rosalind_revc.txt'))