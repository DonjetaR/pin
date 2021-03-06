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
	
	size_of_G=100
	
	for v in range(s,size_of_G):
		prob=random.uniform(0,1)
		#print("prob=",prob)
		node = random.choice(G.nodes())
		if prob>=q:
			G.add_node(v)
			G.add_edge(v,node)
		prob=random.uniform(0,1)
		
		for j in G.neighbors(node):
			if not j==v and prob<=p:			
				G.add_edge(j,v)
	print("Number of nodes after",G.number_of_nodes())
	print("Is it connected after: ",nx.is_connected(G))
	return(G)
	
	
	
def duplication_divergence_model(p,q,r,s):
    #G = nx.Graph()
    #for i in range(s):
    #        G.add_node(i,name = "u")
    # for i in range(0,10):
	
	#list=[]
	
	G=nx.Graph()
	
	for i in range(s):
		G.add_node(i)
			
		if i>0:
			
			list_of_nodes=G.nodes()	
			
			del list_of_nodes[-1]
			#print(list_of_nodes)
			node = random.choice(list_of_nodes)
			#print(node)
			#if not node==i:
			G.add_edge(i,node)
		#if s>2:
		#	node = random.choice(G.nodes(s<2))
		#	if not node==i:
		#		G.add_edge(i,node)
				
	print("Number of nodes before",G.number_of_nodes())
	print("Is it connected before: ",nx.is_connected(G))
	
	#nx.draw(G)
	#plt.show()
	
	size_of_G=10
	
	for v in range(s,size_of_G):

		node_u = random.choice(G.nodes())
		G.add_node(v)
		prob=random.uniform(0,1)
		if prob>=q:
			G.add_edge(v,node)
		
		
		#print(node_w)
		for i in G.neighbors(node_u):
			#node_w = random.choice(G.neighbors(node_u))
		#if (node_w,node_u) in G.edges():
		#	print("true")
			G.add_edge(v,i)			
			prob=random.uniform(0,1)
			if prob>=p:
				continue
			else:
				prob=random.uniform(0,1)
				if prob>=r:					
					G.remove_edge(node_u,i)
				elif prob>=(r-1):
					G.remove_edge(v,i)
				
		
	#	for j in G.neighbors(node):
	#		if not j==v and prob<=p:			
	#			G.add_edge(j,v)
	print("Number of nodes after",G.number_of_nodes())
	print("Is it connected after: ",nx.is_connected(G))
	#nx.draw(G)
	#plt.show()
	return(G)
	
def eksperiments(G):
	print("drawing the loglog-plot")
	y=sorted(nx.degree(G).values())
	x=range(G.number_of_nodes())
	plt.loglog(x,y)
	plt.show()
	#plt.savefig("loglog-plot.png")
	
	print("Average shortest path: ")
	connected_G=nx.connected_component_subgraphs(G)
	#print(connected_G)
	for i in connected_G:
		p=nx.average_shortest_path_length(i)
		print(p)
	
	print("Clustering coefficient: ")
	print(nx.average_clustering(G))
	
	#print("drawing the graph")
	#nx.draw(G)
	#plt.show()
	
	
if __name__ == '__main__':
	#f=open("4932.protein.links.v10.txt","r").readlines()
	#f.readline()
	#for x in f:
	#f.split("\n")
	#G=nx.Graph()
	#max_score=0
	#min_score=1000
	
	
	# x in f[1:]:
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
	r = 0.6
	s = 1
	#print(s)
	#node = random.choice(G.nodes())
	#print(node)
	#print("before: ",nx.is_connected(G))
	G1=partial_duplication_model(p,q,s)
	#G2=duplication_divergence_model(p,q,r,s)
	#print("after: ",nx.is_connected(G))
	eksperiments(G1)

	
