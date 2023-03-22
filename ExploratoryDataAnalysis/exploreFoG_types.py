"""
Quick thoughts: time series data -- need to classify runs of data
Try a shaplett based classification (brute force?)
Or maybe try mlpclassifier
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
from sklearn.neural_network import MLPClassifier

fileIn = sys.argv[1] 

# Read in data
data = np.loadtxt(fileIn, delimiter=",", skiprows=1)

boolStartHes = data[:,4] #Is there a start hesitation?  1 if yes 0 if no
boolTurn = data[:,5]     #Is turning? 1 if yes 0 if no
boolWalking = data[:,6]  #Is walking? 1 if yes 0 if no


print "Total Time Steps with Start Hesitations: ", np.sum(boolStartHes)
print "Total Time Steps with Turning Events: ", np.sum(boolTurn)
print "Total Time Steps with Walking Events: ", np.sum(boolWalking)


