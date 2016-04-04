__author__ = 'stas'

print "Complementing a Strand of DNA(REVC task)"

dna = "TGGCCTCCTTTCATTAAAATTTTGTAACATGTACGAGATTTGATCCCAGCAAAAATAATTCTTCGCCCGTGCTGACGACGTTGCTTAATACACATCCGTAGAATACACGAATAACTCCATGCATATTTCGGTTATGGTATCTAGACAGGGGCACGGGCTATTATGCCAAGTAGAACTTATGTCGTTACCGGGGAAGGGCCTTGGTCTGGTATGGTAAGTTGCTGTTGACCCAAGTCTACCGCCCAAAACACAAGCTCCACCGGTCTAACTAGCGAATGGGTATCGGAGGATATCGCTTGAATGTAGTATCTGTGAAGTGAGGCTTTAGTCCATTAAACCGCTACGGTAAAACTGTGTAGTAAGGGCTTCCTAGAACTCTATCCTACCAAGTCCCTTGAGAACACCGGCATAGGTGGGGCGAAAGCCTAATCCGTTCACAACGACTAGACTGGTCTCATACCAATGAAATGTGGATTTCGCGTGCCAGAGAGACGAGACTGAGATACTGCCACAGGCTCAGACTAAAGCCGTTTTCATTCGTATGAACCCAGCGTGATGCCTATTTTCTTTGTAAGATGACTTGTCCCCGGGGAGGCGAAGTGCACCCGGCGATTATGCGCACCCAAGTTTCTTCGGCCAAGAAGCCCGAACACGTTTCCCGCAGAGAGCCACTCCACTGACATGTTCACGTGTAACGGGCGACTCGGTTCTTATGCGGGGGCACGAGAACCTAAAGATAATTTGAGCGTACTAGTGAGTCCCTATCATGTATCTTTATAACCTGCATCTATTGATGCCCTCGGTCGTCGTAACTGTCCACGTTTGCGAAAGGCAGAATTCAATCTCAAATCACAACAACAGCTTCAAACCGGGCGGATACGGACTCTTATAAGCGGGTTTGAA"

dna_complement = ""

nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

for n in dna:
    dna_complement += nucleotides[n]

print(dna_complement[::-1])