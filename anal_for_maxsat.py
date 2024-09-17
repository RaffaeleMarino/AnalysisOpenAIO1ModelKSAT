import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("output_maxsatK=2.txt")
x=data[:,0]
y=data[:,1]
z=data[:,2]

mean=np.mean(y/z)
std=np.std(y/z)/np.sqrt(y.shape[0])
print(mean, std)