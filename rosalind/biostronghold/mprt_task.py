__author__ = 'stas'

import urllib2
import regex as re
from gc_task import parse_fasta


def get_protein_from_uniprot(id):
    response = urllib2.urlopen("http://www.uniprot.org/uniprot/{}.fasta".format(id)).read().split('\n')
    return parse_fasta(response)[0]


def find_motif_in_protein(motif, protein):
    """
    Numeration starts with 1 !!!!
    """
    matches = re.finditer(motif, protein, overlapped=True)
    return [m.start(0) + 1 for m in matches]


if __name__ == "__main__":
    print "Finding a Protein Motif(MPRT task)"
    with open("datasets/mprt") as f:
        proteins_id = f.readlines()
    proteins = map(lambda id: (id.strip(), get_protein_from_uniprot(id.strip())[1]), proteins_id)
    N_glycosylation_motif = "N[^P][ST][^P]"
    found_motifs = filter(lambda x: x[1],
                          map(lambda x: (x[0], find_motif_in_protein(N_glycosylation_motif, x[1])), proteins))
    for f in found_motifs:
        print f[0]
        for i in f[1]:
            print i,
        print


