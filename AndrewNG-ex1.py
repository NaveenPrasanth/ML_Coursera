
# coding: utf-8

# In[2]:

import numpy as np
import csv




def univariateXfetcher():
    mylist = []
    with open("ex1data1.txt") as csvfile:
        reader = csv.reader(csvfile)
        mylist = list(reader)
    
    data = np.array(mylist,dtype='float64')
    x,y = data.T
   
    x = x.reshape(97)
    onesvector = np.ones(97)

    X = np.empty([2,97])
    X[0] = onesvector
    X[1] = x
    return X,y


       
theta = np.empty ([1,2])
X,y = univariateXfetcher()
y = y.reshape(97)
m = X.shape[1]

i = 0
while i < 5000 :
    
    hyp = np.dot(theta,X)
    hyp = hyp.reshape(97)
    diff = np.subtract(hyp,y)
    diff = diff.reshape(1,97)
    core = np.dot(diff,X.T)/m   
    core = core * 0.01
    theta = theta - core
    i+=1
    cost = np.sum(np.square(diff))/(2*m)
    print cost
    
print theta





