#-*- coding: utf-8 -*-
#!/usr/bin/env python

# scipy ile matrix uygulaması

from scipy import mat
A = mat('[1 2 3; 4 5 5; 6 7 8]')
B=A*3
print B

C=A+3
print C

B*C
A**3