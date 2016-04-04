__author__ = 'stas'

print "Rabbits and Recurrence Relations(FIB task)"

n = 36
k = 2


f_prev = 0
f_cur = 1
for i in xrange(n - 1):
    tmp = f_cur + k * f_prev
    f_prev = f_cur
    f_cur = tmp

print f_cur