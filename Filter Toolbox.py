# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:40:53 2026

@author: aarus
"""

#The Filter Toolbox (ImageFilter)
These are "one-click" effects. You apply them using image.filter(ImageFilter.NAME).

BLUR: Like looking at the image through and steamy shower door. 
It averages the colors of nearby pixels so everything looks soft.

GaussianBlur(radius): A "smarter" blur. Instead of just averaging everything equally, it gives more importance to the center pixel. 
It’s the "Photoshop-style" blur. You can pick how blurry it is with the radius (higher number = more blur).

SHARPEN: The opposite of blur. It looks for tiny differences in color and makes them more extreme,
making details "pop" out.

FIND_EDGES: Turns the image black and draws white lines 

where the colors change quickly (like the outline of a person).

CONTOUR: Similar to finding edges, but it looks more like a sketch or a 3D map. 
It keeps the "flow" of the shapes.

EMBOSS: Makes the image look like it was pressed into a sheet of metal.
 It creates a 3D "raised" effect by adding fake shadows and highlights