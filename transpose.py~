f = open("wt_1000.txt","r")

lists = []

for data in f:
    temp = data.rstrip().lstrip()
    #print len(temp)
    lists.append([int(x) for x in temp.split(",")])

#print lists

lists = map(list, zip(*lists))

for list_ in lists:
    string = ''
    for item in list_:
        string += str(item) + ','
    print string[:-1]

