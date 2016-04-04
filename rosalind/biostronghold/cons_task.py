__author__ = 'stas'

from gc_task import read_fasta
from dna_task import base_counter


if __name__ == "__main__":
    print "Finding a Most Likely Common Ancestor(CONS task)"
    data_set = read_fasta("datasets/cons")
    print data_set
    profile_length = len(data_set[0][1])
    data_set = map(lambda x: x[1], data_set)
    join_dna = ''.join(data_set)
    profiles = [base_counter(join_dna[i::profile_length]) for i in xrange(profile_length)]
    consensus = map(lambda p: max(p, key=lambda k: p[k]), profiles)
    print ''.join(consensus)
    for n in ['A', 'C', 'G', 'T']:
        print n + ": ",
        for p in profiles:
            print str(p[n]) + " ",
        print





