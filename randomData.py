import numpy as np

f = open('features1.txt', 'w')

for _ in range(15):
	# Randomly choose either 0 or 1 and populate an array; then print with brackets removed
	f.write(str(list(np.random.choice([0,1], size = 10000, p=[0.5,0.5]))).replace('[','').replace(']',''))
	f.write("\n")

f.close()
