import networkx as nx 
import matplotlib.pyplot as plt
import random

def partial_duplication_model(G,p,q,s,max_score):
    #G = nx.Graph()
    #for i in range(s):
    #        G.add_node(i,name = "u")
    # for i in range(0,10):
	
	node = random.choice(G.nodes())
	v = max_score + 1
	G.add_node(v)
        
	G.add_edge(v,node,weight = q)
	k=G.number_of_nodes()
        #for j in range(k):
	for i in G.neighbors(node):
		if not i==v:
			G.add_edge(i,node,weight = p)
	
	#print("drawing the graph")
	#nx.draw(G)
	#plt.show()
	for node in G.nodes():
		x=degree(node)

	
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
	s = 2
	partial_duplication_model(G,p,q,s,max_score)

	
