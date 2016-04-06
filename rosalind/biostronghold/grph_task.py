__author__ = 'SO'

from gc_task import read_fasta

if __name__ == "__main__":
    print "Overlap Graphs(GRPH task)"
    data = read_fasta("datasets/grph")
    overlap_graph = [(x[0], y[0]) for x in data for y in data if x[1][-3:] == y[1][:3] and x[0] != y[0]]
    for e in overlap_graph:
        print e[0] + " " + e[1]
