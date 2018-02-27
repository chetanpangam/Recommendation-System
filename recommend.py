import csv
import sys
import numpy
from numpy import loadtxt
from collections import defaultdict 


text_file = r"train.txt"
csv_file = r"train.csv"

in_txt = csv.reader(open(text_file, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)

result=numpy.loadtxt(open("train.csv", "rb"), delimiter=",")

lines = loadtxt("test5.txt", delimiter=" ",unpack=False)

my_dict = defaultdict(list)
rows = len(lines)
for i in range(rows):
    arr=lines[i][1],lines[i][2]
    my_dict[lines[i][0]].append(arr)