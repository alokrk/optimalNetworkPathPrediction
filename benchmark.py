from sklearn import metrics
# import pandas as pd
# from ggplot import *

# Taking 'Mode' of the list as the feature
def benchmark(list1):
	list_len = len(list1)
	no_of_ones = sum(list1)
	no_of_zeroes = list_len - no_of_ones
	if(no_of_ones > no_of_zeroes):
		return 1
	else: return 0

def transpose(l):
	return list(map(list, zip(*l)))

file = open("features.txt","r")

data = []
for line in file:
    temp = line.rstrip()
    data.append([int(x) for x in temp.split(",")])
# print(len(data))

# First 12 to train, rest 3 to test
train0 = data[0:12]
test0 = data[12:]
train = transpose(train0)
test = transpose(test0)

auc = 0
for i in range(3):						# range(3) as predicting for 3 graphs
	temp = []
	for entry in train:
		temp.append(benchmark(entry))
	train0.append(temp)					# Append the newly predicted results to train, so that they can be used for next prediction
	train = transpose(train0)

	fpr, tpr, _ = metrics.roc_curve(transpose(test)[i], temp)
	auc += metrics.auc(fpr,tpr)

pred = transpose(train0[12:])
print(auc/3)							# Division by 3 as avg value for 3 predictions

file.close()


# df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
# ggplot(df, aes(x='fpr', y='tpr')), geom_line(), geom_abline(linetype='dashed')

'''
ggplot(df, aes(x='fpr', ymin=0, ymax='tpr')) +\
    geom_area(alpha=0.2) +\
    geom_line(aes(y='tpr')) +\
    ggtitle("ROC Curve w/ AUC=%s" % str(auc))
'''
