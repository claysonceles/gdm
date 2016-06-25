try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
import random
import sys
import socialNet as soc


def selectGroupLeaders(n_nodes,n_groups): #selects group leaders with uniform distribution
	leaderSet = []
	for i in range(n_groups):
		leaderSet = leaderSet + [random.randint(0, n_nodes)]
	return leaderSet

def snowball(center,graph, maxNodes):
	members = [center]
	iterator = 0
	while len(members) < maxNodes and iterator < len(members):
		for i in graph.neighbors(members[iterator]):
			if not (i in members):
				members = members + [i]
		if len(members) > maxNodes:
			return members[0:maxNodes]
		iterator+=1
	return members
	
def plotSnowball(G, snowball,num):

	pos=nx.graphviz_layout(G) # positions for all nodes

	plt.figure(figsize=(12,12))

	#colors = ["green","yellow","red","blue","pink","orange","gray","brown","black","white","purple","green","yellow","red","blue","pink","orange","gray","brown","black","white","purple"]

#	colors = ["#ff0000","#ff8000","#ffbf00","#ffff00","#bfff00","#80ff00","#40ff00","#00ff00", "#00ff40", "#00ff80", "#00ffbf", "#00ffff", "#00bfff", "#0080ff", "#0040ff", "#0000ff", "#4000ff", "#8000ff", "#bf00ff", "#ff00ff", "#ff00bf", "#ff0080", "#ff0040","#ff0000","#ff8000","#ffbf00","#ffff00","#bfff00","#80ff00","#40ff00","#00ff00", "#00ff40", "#00ff80", "#00ffbf", "#00ffff", "#00bfff", "#0080ff", "#0040ff", "#0000ff", "#4000ff", "#8000ff", "#bf00ff", "#ff00ff", "#ff00bf", "#ff0080", "#ff0040"]

	nx.draw_networkx_nodes(G,pos,nodelist=snowball,node_color="red")

	nx.draw_networkx_edges(G,pos,width=1)
			# labels
	nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

	plt.axis('off')
	plt.savefig("snowball"+str(num)+".png") # save as png
	plt.close()
			
leaders = selectGroupLeaders(40,10)

socialGraph = soc.generateGaussian(100,20, 10,0.5,0.002);

sb = snowball(20,socialGraph, 5)
plotSnowball(socialGraph,sb,1)

sb = snowball(20,socialGraph, 10)
plotSnowball(socialGraph,sb,2)

sb = snowball(20,socialGraph, 20)
plotSnowball(socialGraph,sb,3)

sb = snowball(20,socialGraph, 40)
plotSnowball(socialGraph,sb,4)

sb = snowball(20,socialGraph, 80)
plotSnowball(socialGraph,sb,5)
#members = sbs.snowballsampling(socialGraph,20,20)

#print members
