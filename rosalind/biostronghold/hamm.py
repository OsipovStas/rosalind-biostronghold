__author__ = 'stas'

print "Counting Point Mutations(HAMM task)"


def hamming_distance(dna1, dna2):
    return sum(map(lambda x: 1 if (x[0] != x[1]) else 0, zip(dna1, dna2)))


with open("hamm") as f:
    (dna1, dna2) = f.readlines()
    print hamming_distance(dna1, dna2)

