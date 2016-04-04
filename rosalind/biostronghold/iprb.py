__author__ = 'stas'

print "Mendel's First Law(IPRB task)"

homo_dom = 19
hetero = 26
homo_rec = 22


k = float(homo_dom)
m = float(hetero)
n = float(homo_rec)
a = float(k + m + n)

prob = ((2 * k * (m + n)) + (k * k - k) + (0.75 * (m * m - m)) + (m * n)) / (a * (a - 1))
print prob
