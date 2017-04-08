#-*- coding: utf-8 -*-
#!/usr/bin/env python

# matplotlib ile çizgi grafik uygulaması

import pandas as pd
import datetime
import pandas_datareader as pdr

import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 12, 31)
df = pdr.get_data_yahoo("GOOG", start, end)

style.use('fivethirtyeight')

df['High'].plot() 
plt.legend()
plt.show()