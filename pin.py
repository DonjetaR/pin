import networkx as nx 
import matplotlib.pyplot as plt
import random

def partial_duplication_model(G,p,q,s,max_score):
    #G = nx.Graph()
    #for i in range(s):
    #        G.add_node(i,name = "u")
    # for i in range(0,10):
	k=G.number_of_nodes()
	list=[]
	
	for i in range(s):
		#random.randint(1,k)
		node = random.choice(G.nodes())
		if node not in list:
			v = max_score + i
			G.add_node(v)
			list.append(node)
        
			G.add_edge(v,node,weight = q)
	
        #for j in range(k):
			for j in G.neighbors(node):
				if not j==v:
					G.add_edge(j,node,weight = p)
		
	
	print(G.number_of_nodes())
	
	return(G)
	
def eksperiments(G):
	print("drawing the graph/loglog-plot")
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
	#print("Average shortest path: ")
	
	#p=nx.average_shortest_path_length(G)
	#print(p)
	
	print("Clustering coefficient: ")
	print(nx.average_clustering(G))
	
	
if __name__ == '__main__':
	f=open("4932.protein.links.v10.txt","r").readlines()
	#f.readline()
	#for x in f:
	#f.split("\n")
	G=nx.Graph()
	max_score=0
	#min_score=1000
	
	
	for x in f[1:]:
		y=x.split(" ")		
		for node in y[:1]:
			if int(y[2])>=990:
				G.add_node(node)
		if int(y[2])>=990:
			G.add_edge(y[0], y[1], weight=int(y[2]))
		temp=int(y[2])
		#print(type(temp))
		max_score=max(max_score,temp)
		#min_score=min(min_score,temp)
	#print(max_score)
	#print(min_score)
	
	#nx.draw(G)
	#plt.show()
	#plt.savefig("graph.png")
		
	p = 0.3
	q = 0.7
	s = G.number_of_nodes()
	print(s)
	#node = random.choice(G.nodes())
	#print(node)
	print("before: ",nx.is_connected(G))
	G1=partial_duplication_model(G,p,q,s,max_score)
	print("after: ",nx.is_connected(G))
	eksperiments(G1)

	
