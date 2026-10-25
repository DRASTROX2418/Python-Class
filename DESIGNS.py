#!/usr/bin/env python
# coding: utf-8

# ## Egg Holder Design

# In[3]:


import FreeCAD
import Part 
from FreeCAD import Base

# Create Document 
doc = FreeCAD.newDocument("EasterEggHolder")

# Parameter
egg_radius = 10
egg_count = 5
spacing = 25 
base_lenght = egg_count * spacing 
base_width = 40 
base_height = 5 

# Base Platforms
base = Part.makeBox(base_lenght, base_width, base_height)

# Create holes for the eggs

for i in range (egg_count):
    x = i*spacing + spacing/2
    y = base_width / 2
    hole = Part.makeCylinder(egg_radius, base_height + 1, Base.Vector(x,y, -0.5))

# Show the object in FreeCad
Part.show(base)
doc.recompute()


# In[2]:


import FreeCAD
import Part
from FreeCAD import Base

doc = FreeCAD.newDocument("SchoolPencilHolder")

# Parameters
pencil_radius = 5
pencil_count = 25
spacing = 20
base_length = pencil_count * spacing
base_width = 25
base_height = 10

# Step 1: Create base block
base = Part.makeBox(base_length, base_width, base_height)

# Step 2: Create all holes and fuse them into one object
all_holes = None
for i in range(pencil_count):
    x = i * spacing + spacing / 2
    y = base_width / 2
    hole = Part.makeCylinder(pencil_radius, base_height + 1, Base.Vector(x, y, -0.5))
    
    if all_holes is None:
        all_holes = hole
    else:
        all_holes = all_holes.fuse(hole)

# Step 3: Subtract all holes at once
if all_holes:
    base = base.cut(all_holes)

# Step 4: Show result
Part.show(base)
doc.recompute()


# In[5]:


import FreeCAD
import Part
from FreeCAD import base

doc = FreeCAD.newDocument("Nintendo Chip Holders")

# Parameters
chip_width = 20
chip_height = 30
chip_count = 2
spacing = 8
base_length = chip_count * spacing
base_width = 20
base_height = 30

# Step 1: Create base block
base = Part.makeBox(base_length, base_width, base_height)

# Step 2: Create all holes and fuse them into one object
all_holes = None
for i in range(chip_count):
    x = i * spacing + spacing / 2
    y = base_width / 2
    hole = Part.makeCylinder(chip_width, base_height + 1, Base.Vector(x, y, -0.5))
    
    if all_holes is None:
        all_holes = hole
    else:
        all_holes = all_holes.fuse(hole)

# Step 3: Subtract all holes at once
if all_holes:
    base = base.cut(all_holes)

# Step 4: Show result
part.show(base)
doc.recompute()


# In[4]:


import FreeCAD
import Part
from FreeCAD import Base

# Create new document
doc = FreeCAD.newDocument("RubiksCube3D")

# Define colors for the Rubik's cube squares
colors = [
    ['black', 'black', 'black', 'black', 'black'],
    ['black', 'red', 'red', 'red', 'black'],
    ['black', 'red', 'blue', 'red', 'black'],
    ['black', 'red', 'red', 'red', 'black'],
    ['black', 'black', 'black', 'black', 'black'],
]

# Size settings
block_size = 10  # Each small cube size

# Draw 5x5 colored cubes
for i in range(5):       # rows
    for j in range(5):   # columns
        # Create cube
        cube = Part.makeBox(block_size, block_size, block_size, block_size, block_size)
        Part.show(cube)
        
        # Move cube to position
        obj = FreeCAD.ActiveDocument.Objects[-1]
        obj.Placement.Base = Base.Vector(j * (block_size + 1), (2-i) * (block_size + 1), 0)  # 2-i to match your original matplotlib layout
        
        # Set color
        if colors[i][j] == 'red':
            obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 0.0, 0.0)  # Red
        elif colors[i][j] == 'black':
            obj.ViewObject.ShapeColor = (0.0, 0.0, 0.0, 0.0, 0.0)  # Black
        elif colors[i][j] == 'blue':
            obj.ViewObject.ShapeColor = (0.0, 0.0, 0.0, 0.0, 1.0)  # Blue

doc.recompute()


# In[ ]:


import FreeCAD
import Part
from FreeCAD import Base

# Create new document
doc = FreeCAD.newDocument("RubiksCube3D")

# Define colors for the Rubik's cube squares
colors = [
    ['orange', 'orange', 'orange'],
    ['white', 'white', 'white'],
    ['green', 'green', 'green']
]

# Size settings
block_size = 10  # Each small cube size

# Draw 3x3 colored cubes
for i in range(3):       # rows
    for j in range(3):   # columns
        # Create cube
        cube = Part.makeBox(block_size, block_size, block_size)
        Part.show(cube)
        
        # Move cube to position
        obj = FreeCAD.ActiveDocument.Objects[-1]
        obj.Placement.Base = Base.Vector(j * (block_size + 1), (2-i) * (block_size + 1), 0)  # 2-i to match your original matplotlib layout
        
        # Set color
        if colors[i][j] == 'orange':
            obj.ViewObject.ShapeColor = (1.0, 0.5, 0.0)  # Orange
        elif colors[i][j] == 'white':
            obj.ViewObject.ShapeColor = (1.0, 1.0, 1.0)  # White
        elif colors[i][j] == 'green':
            obj.ViewObject.ShapeColor = (0.0, 1.0, 0.0)  # Green

doc.recompute()

