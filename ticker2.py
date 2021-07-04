#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:37:37 2021

@author: timothyperez
"""
import requests
import simplejson as json
import pandas as pd
import numpy as np
import datetime
from bokeh.plotting import curdoc, figure, show
from bokeh.models.widgets import TextInput, Button
from bokeh.layouts import row, column



#%%
#Extract API key
#key=
#file = open('Desktop/avkey.txt', 'r') #change desktop directory once this is rady to be devployed
#for line in file.readlines(): 
#    key.append(line)
#key=key[0]   

#Set up default textbox values
text_input = TextInput(value="GME", title="Label:")

#set up call back 
def update_ticker():
    text_input.value = text_input.value#
    return 
  
    
TICKER=text_input.value
#extract stock data and format
url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}".format(TICKER, key)
r = requests.get(url)
data = r.json()
df=pd.DataFrame.from_dict(data["Time Series (5min)"]) #select data of interest
df2=df.T #transfrom data
df2.index=pd.to_datetime(df2.index, format="%Y-%m-%d %H:%M:%S") #format date/time
    #return df2

#Title
y_title=text_input.value     

#plotting
p = figure(height=600, width=800, title=y_title, x_axis_type='datetime')#, tools='pan,box_zoom,hover,reset') #kw=A subclass of Plot that simplifies plot creation with default axes, grids, tools, etc. 
    #p.circle(x=df2.index y=df2["3. low"], color="black", size=1 line_color="black") #, alpha=0.6, hover_color='white', hover_alpha=0.5)
p.line(df2.index, df2["3. low"], color="red", legend_label="low")
p.line(df2.index, df2["2. high"], color="blue", legend_label="high")
p.line(df2.index, df2["4. close"], color="black", legend_label="close")

#widgets callbacks
update = Button(label="Update")
update.on_click(update_ticker)
#text_input.on_change("value", update_ticker)
inputs = column(text_input, update)

# render on the web page
curdoc().add_root(column(p, row(inputs), width=1600))


#show(column(p, row(inputs)))
