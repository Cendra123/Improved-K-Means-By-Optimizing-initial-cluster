import math

import pandas as pd

import sys
# Example points in 3-dimensional space...
# x = (5, 6, 7,1)
# y = (8, 9, 9,4)

df = pd.read_excel('TF-IDF_01.xlsx')

print(df)
sys.exit()

# print(type(x))
# print(df.ix[1][:])

for i in range(5):
    for j in range(i,5):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(df.ix[i][:], df.ix[j][:])]))
        print("Euclidean distance from ",i," to ",j,": ",distance)


# distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
# print("Euclidean distance from x to y: ",distance)