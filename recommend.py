import csv
import sys
import numpy
import math
import warnings
from numpy import loadtxt
import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity


txt_file = r"train.txt"
csv_file = r"train.csv"
in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerows(in_txt)


result = numpy.loadtxt(open("train.csv", "rb"), delimiter=",")


lines = loadtxt("test5.txt", delimiter=" ", unpack=False)


my_dict = defaultdict(list)
rows=len(lines)
for i in range(rows):
    arr=[lines[i][1],lines[i][2]]
    my_dict[lines[i][0]].append(arr)



warnings.filterwarnings("ignore")
for key in my_dict:
    ratingmat=[[0 for i in range(201)]for i in range(5)]
    active_user=[]
    for i in range(5):
        active_user.append((my_dict.get(key))[i][1])  #contains the ranking given by the active user
        movie=((my_dict.get(key))[i][0])   #gets the movie which are predicted by the active user
        for j in range(200):
            ratingmat[i][j]=result[j][(movie-1).astype(int)]
    orig_mat=(numpy.transpose(ratingmat))   #matrix of ranking of all users from training data for the movie rated by the test user
    vict=[]   #row vector of all the weights
    for i in range(200):
        vict.append(cosine_similarity(np.array(active_user),np.array(orig_mat[i])))
        
#Calculating the weight vector
    for i in range(len(vict)):
        nonzeroind = np.nonzero(orig_mat[i])[0] #to get non zero index of the orig_matrix
    sum=0
    for index in nonzeroind:
        sum=sum+(active_user[index]*active_user[index])
    sum=math.sqrt(sum)            
    vict[i]=(vict[i]*np.linalg.norm(active_user - np.zeros(5)))/sum    #to neglect those terms which are not present in training user matrix
    
#Prediction Block
    predicted_value=0
    for i in range(5,len(my_dict.get(key))):
        total_weight=0
        total=0
        for j in range(200):
            if(((result[j][(my_dict.get(key))[i][0].astype(int)-1])!=0) and ((~numpy.isnan(vict[j])))): # rating given by jth user to ith movie
                total+=vict[j]*result[j][(my_dict.get(key))[i][0].astype(int)-1]
                total_weight+=vict[j]
        if(total_weight!=0):
            predicted_value=(numpy.round(total/total_weight)).astype(int).tolist()[0][0]
        else:
            predicted_value=1
        my_dict[key][i][1] = predicted_value
        


#output in text file
file=open('output5.txt','w')

for key in my_dict:
    for i in range(5,len(my_dict.get(key))):
        file.write(str(int(key)) + '\t'+ str(int((my_dict.get(key))[i][0])) + '\t' + str(int((my_dict.get(key))[i][1])) +'\n')

file.close()
