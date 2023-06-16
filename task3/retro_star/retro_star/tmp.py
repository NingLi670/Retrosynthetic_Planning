import torch
import numpy as np


data1 = np.load('dataset1/starting_mols.pkl', allow_pickle=True)
data2 = np.load('dataset1/test_mols.pkl', allow_pickle=True)

data3 = np.load('dataset/routes_possible_test_hard.pkl', allow_pickle=True)
num = 0

# print(data2[2])
# print(data3[2][0].split('>')[0])

for i, item in enumerate(data2):
    if item == data3[i][0].split('>')[0]:
        num = num + 1


print(num)

# print(data)
