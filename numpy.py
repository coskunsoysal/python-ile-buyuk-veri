#-*- coding: utf-8 -*-
#!/usr/bin/env python

# numpy ile random ve dosya islemleri

import numpy as np 

a = np.random.random((1000,1000)) 
np.savetxt('sample.txt',a) 
b = np.loadtxt('sample.txt') 
print b