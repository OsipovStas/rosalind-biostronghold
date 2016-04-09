__author__ = 'stas'


def count_gc(dna):
    count = 0
    for n in dna:
        if n is 'C' or n is 'G':
            count += 1
    return count / float(len(dna))


def parse_fasta(f):
    data_set = []
    name = ""
    dna = ""
    for line in f:
        if line.startswith(">"):
            data_set.append((name, dna))
            name = line.strip()[1:]
            dna = ""
        else:
            dna += line.strip()
    data_set.append((name, dna))
    return data_set[1:]


def read_fasta(file_name):
    with open(file_name) as f:
        data_set = parse_fasta(f)
    return data_set


if __name__ == "__main__":
    print "Computing GC Content(GC Task)"
    gc_counters = map(lambda x: (x[0], count_gc(x[1])), read_fasta("gc"))
    print max(gc_counters, key=lambda x: x[1])

