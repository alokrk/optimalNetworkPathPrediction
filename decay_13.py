f = open("wt_1.txt", 'r')

today = 14
i = 13
for line in f:
    lx = map(int, line.rstrip().split(','))
    l = lx[12]
    if l == -1:
	l = 20
    print 0.5**(today - i) * l,
    print 0.25**(today - i) * l,
    print lx[11],
    print l
