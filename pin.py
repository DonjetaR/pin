import networkx as nx 
import matplotlib.pyplot as plt

def duplicatin_duplication_model():
	pass
		
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
			#print(node)
			G.add_node(node)
		if int(y[2])>=500:
			G.add_edge(y[0], y[1], weight=int(y[2]))
		#temp=int(y[2])
		#print(type(temp))
		#max_score=max(max_score,temp)
		#min_score=min(min_score,temp)
	#print(max_score)
	#print(min_score)
	
	#nx.draw(G)
	#plt.show()
	#plt.savefig("graph.png")
		
	
	duplicatin_duplication_model()

print("hello")
	
