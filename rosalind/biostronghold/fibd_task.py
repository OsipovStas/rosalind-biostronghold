__author__ = 'SO'

if __name__ == "__main__":
    print "Wabbit Season(FIBD task)"
    n = 99
    m = 16
    mature = [0, 1]
    newborn = [1, 0]
    for i in xrange(2, n):
        live = mature[-1]
        if i >= m:
            live -= newborn[i - m]
        mature += [live + newborn[-1]]
        newborn += [mature[-2]]
    print mature[-1] + newborn[-1]
