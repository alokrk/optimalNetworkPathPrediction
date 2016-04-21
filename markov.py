file = open("features.txt","r")

lists = []

for data in file:
    temp = data.rstrip()
    lists.append([int(x) for x in temp.split(",")])

#print lists

lists = map(list, zip(*lists))
print lists

def BinaryMarkov(list):
        matrix = [[0.0,0.0], [0.0,0.0]]
        list_len = len(list)
        for index in range(list_len - 1):
                matrix[list[index]][list[index+1]] += 1.0
                #print str(list[index]) + str(list[index+1])

        #Calculate probabilites with smoothing.
        denom = matrix[0][0] + matrix[0][1] + (smoothing_factor * 2)
        matrix[0][0] = (matrix[0][0] + smoothing_factor) / denom
        matrix[0][1] = (matrix[0][1] + smoothing_factor) / denom
        denom = matrix[1][0] + matrix[1][1] + (smoothing_factor * 2)
        matrix[1][0] = (matrix[1][0] + smoothing_factor) / denom
        matrix[1][1] = (matrix[1][1] + smoothing_factor) / denom

        output = [0.0,0.0,0.0,0.0,0.0]
        #Given the state of the path at time 15, whats the probability it'l be 1 at 16
        output[0] = matrix[list[-1]][1]

        for index in range(1,5):
                output[index] = (output[index-1] * matrix[1][1]) + ((1.0-output[index-1]) * matrix[0][1])

        return output


result = []

for list in lists:
    temp = BinaryMarkov(list)
    result.append(temp)
