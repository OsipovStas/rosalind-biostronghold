__author__ = 'stas'


def base_counter(dna):
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in dna:
        nucleotides[n] += 1
    return nucleotides


if __name__ == "__main__":
    print "Counting DNA Nucleotides(DNA task)"
    dna = "TCGGCATGGATACAAAACGCACTGGCCAGTCTAGTATAGGGTCTATAGCACGTGTTACCTTTCCAAACAAGTTGGTAGTCACTGTTACATTCGGAGTCGTTCTCTGGGATGTGACTGAGGCGAAATGCAATTCTGAGAGTATTCCCAGTATAAATGTAATATAGCGGGTGAACCTTCTCAGATCTTGCATACGGGTCGTTTTTCCCCACAATATGAACGTGGAGGTTTCAGCAGGCCCGTGGAAAGATGCCCCGAGAGGTACGTTGGCGGGGGCGGGGGCCGATGACATCTTGTGCGATATACCGCTCGTATCCATGTCATGACAAAGACTGGTGGATGTTTTAAGTCGTCGGTCGAGGTAGATCGATCTCGATTGTTTTACCAGTAGGAATGAGGATCTTGTTACGACACAGGGCTAGGTTAGTTACAATTGCAAGTTGTCCACTCTTGCACTCCGTAATGTTGCGAGACCTTACCCCTTTACGAGCGTCTCAGTCTTCCCTGACGTCGACGGATAGTATTCGCATGCCGCGCTCGATGGTACCCGTTCGATCCGGGCAGGGGTGGAGTAATTTGCACCTAGACCAAAGCTGAAATGCCATCAAGAGCCCTGGGGAATTAAGCGCCGTGTAGCAATGGCAACTGGTCTATACGCCGATTATACTGGTCCGAGCAATTTTTACTCAGAACGGTGATTCGCACGGTTGCCGCGACGCCATAGCGCAGAATCCGTCGTCCTCAGGCAGCCCTTCTTACCGTTGGTCTCGTCCGGCGTCATCGATTCGATGACCATAGGACGAAAAGCCCAATGTCGGTCACTCGAAGGCCTTTAGACGCAGTGTTGGAGGGGGGATGTTTCATATGTATTTCCCCCCTAGGATTAAACCCGTCTAAAAGCTCTAGTTTGGGAGAGTGTAATTCACACGCGTCACTG"
    print base_counter(dna)