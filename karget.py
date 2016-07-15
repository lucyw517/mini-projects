'''
Algorithms - design and analysis (Stanford), Part I.
Programming Question 3:
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6 155 56 52 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
'''


import random
import copy
def karget(graph):
	v1=random.choice(list(graph.keys()))
	v2=random.choice(list(graph[v1]))
	graph[v1].extend(graph[v2])
	for v in graph[v2]:
		graph[v].remove(v2)
		graph[v].append(v1)
	while v1 in graph[v1]:
		graph[v1].remove(v1)
	del graph[v2]
	
def cut(graph):
	length=[]
	while len(graph)>2:
		karget(graph)
	for key in graph.keys():
		length.append(len(graph[key]))
	return length[0]

def mincut(graph):
	mincut=100
	i=0
	while i<100:
	  data = copy.deepcopy(graph)
		if mincut>cut(data):
			mincut=cut(data)
		i=i+1
	return mincut
