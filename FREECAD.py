#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1 is to make a shape
# make.box

# Step 2 is to move the shape 
# translate()

# Step 3 is to join or cut
# fuse()

# Step 4 is to add a function to Freecad
# addObject()+Shape

# Step 4 is to recomput and view
# doc.recompute()


# In[ ]:


import FreeCAD as App, FreeCADGui as Gui
import Part

# ---------------------------
# Parameters (mm)
# ---------------------------
block_len  = 60   # X
block_wid  = 30   # Y
block_ht   = 10   # Z
hole_r     = 6
peg_r      = 4
peg_ht     = 15

# New doc
doc = App.newDocument("SimplePart")

# 1) Make shapes
box  = Part.makeBox(block_len, block_wid, block_ht)         # base block
hole = Part.makeCylinder(hole_r, block_ht + 2)              # a bit taller than block for clean cut
peg  = Part.makeCylinder(peg_r, peg_ht)                     # top peg

# 2) Move them (translate)
# center hole in X,Y; drop it 1 mm below so it cuts fully through
hole.translate(App.Vector(block_len/2, block_wid/2, -1))
# place peg near one end, sitting on the top surface (z = block_ht)
peg.translate(App.Vector(10, block_wid/2, block_ht))

# 3) Join or cut
part_with_hole = box.cut(hole)       # subtract cylinder -> through-hole
final_shape    = part_with_hole.fuse(peg)  # add the peg on top

# 4) Add to FreeCAD (model tree)
obj = doc.addObject("Part::Feature", "DemoPart")
obj.Shape = final_shape

# 5) Recompute & View
doc.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")

App.Console.PrintMessage("Made a block with a through-hole and a top peg.\n")
App.Console.PrintMessage("Tip: File → Export → STL for 3D printing.\n")

