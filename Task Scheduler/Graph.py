#!/usr/bin/python

from Task import Task

class Graph(object):
	graph = {}	 
	def __init__(self,gr={}):
		self.graph = gr
			
	def find_all_paths(self, start, end, path=[]):
        	path = path + [start]
        	if start == end:
            		return [path]
        	if not self.graph.has_key(start):
            		return []
        	paths = []
        	for node in self.graph[start]:
            		if node not in path:
                		
                		newpaths = self.find_all_paths( node, end, path)
               			for newpath in newpaths:
                    			paths.append(newpath)
        	return paths



"""ta = Task(1)
tb = Task(2)
tc = Task(3)
td = Task(4)
te = Task(5)
tf = Task(6)
gr1 = {ta.id : [tb.id, tc.id],
       tb.id : [tc.id, td.id],	
       tc.id : [td.id],
       td.id : [tc.id],
       te.id : [tf.id],	
       tf.id : [tc.id]}
#for key in gr1.keys():
#	print key
g = Graph(gr1)

paths = g.find_all_paths(ta.id,td.id)
print(paths)
#for path in paths:
#	print path
	#print "\n"
"""
