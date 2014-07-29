"""
generate_cordinates.py
Writes the Bounds of the US States .
author: Hashir Haris - hashir.haris@gmail.com

"""

import shapefile
import os

sf = shapefile.Reader(os.getcwd() + "/us_states/states.shp")
shapes = sf.shapes()
co_ordinate_list=[]
for states in shapes:
  co_ordinate_list.append(states.bbox)
print co_ordinate_list