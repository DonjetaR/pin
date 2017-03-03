import networkx as nx 
import matplotlib.pyplot as plt
import random
from networkx.generators.classic import empty_graph, path_graph, complete_graph

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
	
	size_of_G=3000
	
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

	s = 5
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
	
	size_of_G=3000
	
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
	
def experiments(G):
        print("drawing the loglog-plot")
        y=sorted(nx.degree(G).values())
        x=range(G.number_of_nodes())
        plt.loglog(x,y)
        plt.show()
        plt.savefig("loglog-plot.png")

        isolate = nx.isolates(G)
        for i in isolate:
                G.remove_node(i)
        
        print("Average shortest path: ")
        connected_G=nx.connected_component_subgraphs(G)
        #print(connected_G)
        p=0
        j=0

        
        for i in connected_G:
                #print("degree : ",len(i))
                p=p+nx.average_shortest_path_length(i)
                j=j+1
                        
        
        average_p=p/j
        #print(average_p)
        print(average_p)
        print("Clustering coefficient: ")
        print(nx.average_clustering(G))
        print("Number of nodes : ")
        print(nx.number_of_nodes(G))
        #print("drawing the graph")
        #nx.draw(G)
        #plt.show()

def random_attack(G,num_remove):
        for i in range(1,num_remove):
                #list_of_nodes = G.nodes()
                node = random.choice(G.nodes())
                #random_nodes = random.sample(list_of_nodes,2)
                #G.remove_nodes_from(random_nodes)
                G.remove_node(node)
                
        return(G)
	
if __name__ == '__main__':
        f=open("4932.protein.links.v10.txt","r").readlines()
        #f.readline()
        #for x in f:
        #f.split("\n")
        G=nx.Graph()
        #max_score=0
        #min_score=1000

        for x in f[1:]:
                y=x.split(" ")
                for node in y[:1]:
                        if int(y[2])>=990:
                                G.add_node(node)
                if int(y[2])>=990:
                        G.add_edge(y[0], y[1], weight=int(y[2]))
        p = 0.99
        q = 0.3
        r = 0.6
        s = 1
        #print(nx.number_of_nodes(G))
        G1 = partial_duplication_model(p,q,s)
        #G2 = duplication_divergence_model(p,q,r,s)
        #nodes = G.number_of_nodes()
        #G3 = nx.fast_gnp_random_graph(nodes, 0.01)
        #degree_sequence_random = nx.degree_histogram(random_graph)
        #print(degree_sequence_random)
        #experiments(G3)
        num_remove = [100,100,100,100,100]
        for i in num_remove:
                print(i)
                random_attack(G1,i)
                experiments(G1)
	
