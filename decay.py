f = open("wt_1.txt", 'r')

ls = [i for i in range(1,13)]
today = 13
for line in f:
    l = map(int, line.rstrip().split(','))
    l = l[:12]
    for index in range(len(l)):
	if l[index] == -1:
	    l[index] = 20
    #print l
    
    print sum(0.5**(today - i) * wt for (i, wt) in zip(ls, l)),
    print sum(0.25**(today - i) * wt for (i, wt) in zip(ls, l)),
    print l[11],
    print sum(l)/12.0
