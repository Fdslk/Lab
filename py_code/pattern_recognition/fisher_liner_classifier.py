import os  
import sys  
import numpy as np  
from numpy import *  
import operator  
import matplotlib  
import matplotlib.pyplot as plt  
  
def createDataSet():  
    group1=mat(random.random((2,8))*5+20)  
    group2=mat(random.random((2,8))*5+2)  
    return group1, group2  
  
def draw(group):  
    fig=plt.figure()  
    plt.ylim(0, 30)  
    plt.xlim(0, 30)  
    ax=fig.add_subplot(111)  
    ax.scatter(list(group[0,:]), list(group[1,:]))  
    plt.show()  
  
def compute_mean(samples):  
    mean_mat=mean(samples, axis=1)  
    return mean_mat  
  
def compute_withinclass_scatter(samples, mean):  
    dimens,nums=samples.shape[:2]  
    samples_mean=samples-mean  
    s_in=0    
    for i in range(nums):  
        x=samples_mean[:,i]  
        s_in+=dot(x,x.T)  
    return s_in    
  
if __name__=='__main__':  
	# group1 is class1
	# group2 is class2
    group1,group2=createDataSet()  
    print "group1 :\n",group1  
    print "group2 :\n",group2  
    draw(hstack((group1, group2)))  
    mean1=compute_mean(group1)  
    print "mean1 :\n",mean1  
    mean2=compute_mean(group2)  
    print "mean2 :\n",mean2  
	# compute the interclass 
    s_in1=compute_withinclass_scatter(group1, mean1)  
    print "s_in1 :\n",s_in1  
    s_in2=compute_withinclass_scatter(group2, mean2)  
    print "s_in2 :\n",s_in2  
    s=s_in1+s_in2  
    print "s :\n",s   
    s_t=s.I  
    print "s_t :\n",s_t  
    w=dot(s_t, mean1-mean2)  
    print "w :\n",w  
    test1=mat([1,1])  
    g=dot(w.T, test1.T-0.5*(mean1-mean2))  
    print "g(x) :",g  
    test2=mat([10,10])  
    g=dot(w.T, test2.T-0.5*(mean1-mean2))  
    print "g(x) :",g  