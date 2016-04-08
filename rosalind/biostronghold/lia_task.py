__author__ = 'SO'


def mult(xs, f):
    return map(lambda x: x * f, xs)


from math import factorial


def c(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


k = 5
N = 9

if __name__ == "__main__":
    print "Independent Alleles(LIA task)"
    p = 0.25
    q = 1 - p
    amount = (2 ** k)
    print amount
    fail_probability = map(lambda x: c(amount, x) * (p ** x) * (q ** (amount - x)), range(N))
    print 1 - sum(fail_probability)
