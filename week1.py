import numpy as np
import csv
reader = csv.reader(open("d.csv"), delimiter="\t", skiprows=1)
x = list(reader)
result = np.array(x)
print(result)