import networkx as nx 
import matplotlib.pyplot as plt
import random

def partial_duplication_model(p,q,s):
    #G = nx.Graph()
    #for i in range(s):
    #        G.add_node(i,name = "u")
    # for i in range(0,10):
	
	#list=[]
	
	G=nx.Graph()
	for i in range(s):
		G.add_node(i)
	print("Number of nodes before",G.number_of_nodes())
	print("Is it connected before: ",nx.is_connected(G))
	
	size_of_G=500
	
	for v in range(s,size_of_G):
		prob=random.uniform(0,1)
		print("prob=",prob)
		node = random.choice(G.nodes())
		if prob>=q:
			G.add_node(v)
			G.add_edge(v,node)
		#prob=random.rand(0,1)
		
		for j in G.neighbors(node):
			if not j==v and prob<=p:			
				G.add_edge(j,v)
	print("Number of nodes after",G.number_of_nodes())
	print("Is it connected after: ",nx.is_connected(G))
	return(G)
	
def eksperiments(G):
	print("drawing the loglog-plot")
	#W=nx.degree_histogram(G)
	#plt.loglog(W)
	#plt.show()
	#nx.draw(G)
	#plt.show()
	y=[]
	x=[]
	i=0
	for node in G.nodes():
		t=G.degree(node)
		x.append(i)
		y.append(t)
		i=i+1
	
	#W=G.degree()
	#x=range(k)
	sorted(y)
	#print("y=",y)
	#print("x=",x)
	plt.loglog(x,y)
	plt.show()
	#plt.savefig("loglog-plot.png")
	print("Average shortest path: ")
	
	p=nx.average_shortest_path_length(G)
	print(p)
	
	print("Clustering coefficient: ")
	print(nx.average_clustering(G))
	
	print("drawing the graph")
	nx.draw(G)
	plt.show()
	
	
if __name__ == '__main__':
	#f=open("4932.protein.links.v10.txt","r").readlines()
	#f.readline()
	#for x in f:
	#f.split("\n")
	#G=nx.Graph()
	#max_score=0
	#min_score=1000
	
	
	#for x in f[1:]:
	#	y=x.split(" ")		
	#	for node in y[:1]:
	#		if int(y[2])>=990:
	#			G.add_node(node)
	#	if int(y[2])>=990:
	#		G.add_edge(y[0], y[1], weight=int(y[2]))
	#	temp=int(y[2])
		#print(type(temp))
	#	max_score=max(max_score,temp)
		#min_score=min(min_score,temp)
	#print(max_score)
	#print(min_score)
	
	#nx.draw(G)
	#plt.show()
	#plt.savefig("graph.png")
		
	p = 0.3
	q = 0.7
	s = 1
	#print(s)
	#node = random.choice(G.nodes())
	#print(node)
	#print("before: ",nx.is_connected(G))
	G1=partial_duplication_model(p,q,s)
	#print("after: ",nx.is_connected(G))
	eksperiments(G1)

	
