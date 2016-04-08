__author__ = 'SO'

from gc_task import read_fasta

if __name__ == "__main__":
    print "Finding a Shared Motif(LCSM task)"
    data = read_fasta("datasets/lcsm")
    min_dna = min(data, key=lambda x: len(x[1]))[1]
    dna_set = map(lambda x: x[1], data)
    length = 0
    shared_motif = ""
    for i in xrange(len(min_dna)):
        candidate = min_dna[:i][-length:] + min_dna[i]
        check = True
        for dna in dna_set:
            if candidate not in dna:
                check = False
                break
        if check is True:
            length = len(candidate)
            shared_motif = candidate
    print "Length: " + str(length)
    print "Motif: " + shared_motif
