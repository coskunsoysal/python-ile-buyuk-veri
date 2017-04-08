#-*- coding: utf-8 -*-
#!/usr/bin/env python

# scipy ve matplotlib ile image uygulamasi

from scipy import signal, misc
import matplotlib.pyplot as plt
image = misc.ascent()
w = signal.gaussian(50, 10.0)
image_new = signal.sepfir2d(image, w, w)

plt.figure()
plt.imshow(image)
plt.title('Original image')
plt.show()

plt.figure()
plt.imshow(image_new)
plt.gray()
plt.title('Filtered image')
plt.show()