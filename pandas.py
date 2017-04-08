#-*- coding: utf-8 -*-
#!/usr/bin/env python

# pandas ile veri alma uygulaması

import pandas as pd
import datetime
import pandas_datareader as pdr

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 12, 31)
df = pdr.get_data_yahoo("GOOG", start, end)

print df
print df['Close'].max()
print df['Close'].idxmax()