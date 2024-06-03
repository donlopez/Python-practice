import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('coordinates.csv')

BBox = (df.longitude.min(),   df.longitude.max(),      
         df.latitude.min(), df.latitude.max())
(-81.3512,-81.2847, 28.3936, 28.4636)

ruh_m = plt.imread('"C:\Users\welve\Desktop\MCO.png"')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')