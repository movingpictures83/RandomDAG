#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #### Start Java VM

# In[2]:

import PyIO

class RandomDAGPlugin:
 def input(self, inputfile):
   self.parameters = PyIO.readParameters(inputfile)

 def run(self):
   pass

 def output(self, outputfile):
   from pycausal.pycausal import pycausal as pc
   pc = pc()
   pc.start_vm()


   # #### Load causal algorithms from the py-causal library and Run RandomDag

   # In[3]:


   from pycausal import search as s
   randomDag = s.randomDag(seed = 123, numNodes = int(self.parameters["numnodes"]), numEdges = int(self.parameters["numedges"]))


   # #### RandomDag's Result's Nodes

   # In[4]:


   randomDag.getNodes()


   # #### RandomDag's Result's Edges

   # In[5]:


   randomDag.getEdges()


   # #### Plot The Result's Graph

   # In[6]:


   import pydot
   #from IPython.display import SVG
   dot_str = pc.tetradGraphToDot(randomDag.getTetradGraph())
   outf = open(outputfile+".txt", 'w')
   outf.write(dot_str)
   graphs = pydot.graph_from_dot_data(dot_str)
   graphs[0].write_png(outputfile)
   #svg_str = graphs[0].create_svg()
   #SVG(svg_str)


   # #### Stop Java VM

   # In[7]:


   pc.stop_vm()


   # In[ ]:




