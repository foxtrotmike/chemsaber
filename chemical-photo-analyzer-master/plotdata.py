# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:00:00 2019
Code for plotting data
Put it in the same directory as the data
@author: afsar
"""
from __future__ import print_function
import numpy as np
import os
import matplotlib.pyplot as plt
L = list(os.walk("./"))
c = 'rgbcmy'
cname = []
rgb = None
Z = []
seed = 7
for d,_,flist in L[1:]:
    print(d)    
    for f in flist:
        if f.split('#')[1]==str(seed)+'.spv':
            name = d.split('/')[1]
            cname.append(name)            
            D = np.loadtxt(os.path.join(d,f))            
            if rgb is not None:
                assert np.all(rgb == np.array(D[:,:3]))
            else:
                rgb = np.array(D[:,:3])
            x = np.array(D[:,3:]).T
            assert x.shape[0]==4
            assert x.shape[1]==len(rgb)
            Z.append(x)
            #plt.plot((D[:,5]-mZ)/sZ,c[i]+'+-')
Z = np.array(Z)
cname = np.array(cname)
dA = {}
for n in set(cname):
    dA[n]=np.mean(Z[cname==n],axis=0)
A = np.array(list(dA.values()))
anames = np.array(list(dA.keys()))
idx = np.argsort(anames)
A = A [idx]
anames = anames[idx]
for i in range(A.shape[1]):
    plt.figure()
    plt.plot(A[:,i,:].T,'o-')
    plt.legend(anames)
    plt.title('Avraged Reading'+str(i))
    plt.grid()