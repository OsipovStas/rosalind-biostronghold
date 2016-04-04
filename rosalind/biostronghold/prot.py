__author__ = 'stas'

print "Translating RNA into Protein(PROT task)"

with open("resources/codons") as f:
    lines = map(lambda x: x.strip(), f.readlines())

lines = map(lambda l: filter(lambda x: x is not "", l.split(" ")), lines)
lines = sum(lines, [])
cod_table = dict(zip(lines[::2], lines[1::2]))

with open("datasets/prot") as f:
    rna = f.readlines()[0].strip()

data_set = [rna[i:i + 3] for i in xrange(0, len(rna), 3)]
print ''.join(map(lambda x: cod_table[x], data_set))