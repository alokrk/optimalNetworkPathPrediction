# File to see results
import csv
from sklearn import metrics

threshold_value = 0.3

filename = "./results.csv"


def calculate_auc():
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        actual_value = []
        predicted_value = []
        for line in reader:
            temp_value = float(line[17])
            temp1_value = float(line[14])
#            predicted_value.append(temp_value)
            if temp1_value == 1.0:
                actual_value.append(1)
            else:
                actual_value.append(0)
            if temp_value >= threshold_value:
                predicted_value.append(1)
            else:
                predicted_value.append(0)

        print metrics.roc_auc_score(actual_value, predicted_value)
        print metrics.precision_score(actual_value, predicted_value)

calculate_auc()
