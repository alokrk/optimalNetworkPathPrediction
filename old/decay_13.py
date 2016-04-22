f = open("wt_transposed.txt", 'r')

today = 15
i = 14
for line in f:
    lx = map(int, line.rstrip().split(','))
    l = lx[13]
    if l == -1:
	l = 20
    print 0.5**(today - i) * l,
    print 0.25**(today - i) * l,
    print lx[11],
    print l
