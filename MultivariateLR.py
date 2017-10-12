
# coding: utf-8

# In[33]:


import numpy as np
import csv

maxy=0;


def univariateXfetcher():
    mylist = []
    with open("ex1data2.txt") as csvfile:
        reader = csv.reader(csvfile)
        mylist = list(reader)
    
    data = np.array(mylist,dtype='float64')
    x1,x2,y = data.T
    x1=x1/np.max(x1)
    x2=x2/np.max(x2)    
    maxy=np.max(y)
    y=y/np.max(y)
    
    x1 = x1.reshape(47)
    x2 = x2.reshape(47)
    onesvector = np.ones(47)
    X = np.empty([3,47])
    X[0] = onesvector
    X[1] = x1
    X[2] = x2
   
    return X,y


       
theta = np.empty ([1,3])
X,y = univariateXfetcher()
y = y.reshape(47)
m = X.shape[1]
print X.shape
i = 0
while i < 100000:
    
    hyp = np.dot(theta,X)
    
    hyp = hyp.reshape(47)
    diff = np.subtract(hyp,y)
    diff = diff.reshape(1,47)
    core = np.dot(diff,X.T)  
    core = core * 0.01/m
    theta = theta - core
    i+=1
    cost = np.sum(np.square(diff))/(2*m)
    print cost
    
print theta


# In[6]:

univariateXfetcher()

