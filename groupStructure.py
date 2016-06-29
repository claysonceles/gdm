try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
import numpy.random as rd
import random
import sys
import socialNet as soc
import MeetingsGen as mg

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

	nx.draw_networkx_nodes(G,pos,nodelist=snowball,node_color="red")

	nx.draw_networkx_edges(G,pos,width=1)
			# labels
	nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

	plt.axis('off')
	plt.savefig("snowball"+str(num)+".png") # save as png
	plt.close()

def snowBallTest():			
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

def defineGroupLeaders(n_nodes,n_groups): #selects group leaders with uniform distribution
	leaderSet = []
	for i in range(n_groups):
		leaderSet = leaderSet + [random.randint(0, n_nodes)]
	return leaderSet

def defineGroupSizes(n_groups, beta):
	sizes = []
	i = 0
	while i < n_groups:
		sample = int(rd.exponential(beta))+2
		sizes = sizes + [sample]
		i+=1
	return sizes

def defineGroups(n_nodes, group_size_beta, socialGraph):
	n_groups,groupsRegDistro = mg.readRegularityDistro()
	meetings = mg.generateGroupSet(n_groups,groupsRegDistro,30,60)
	endMeeting = mg.generateMeetingDur(n_groups,meetings);
	#print(teste)
	leaders = defineGroupLeaders(n_nodes, n_groups)
	sizes = defineGroupSizes(n_groups, group_size_beta)
	groupsList = []
	for i in range(n_groups):
		leader = leaders[i]
		size = sizes[i]
		structure = snowball(leader,socialGraph,size)
		probabilities = []
		for j in range(len(structure)):
			probabilities = probabilities + [willIGo(structure[j],structure,socialGraph)]
		
		encounters = meetings[i]
		endEncounter = endMeeting[i]
		groupsList = groupsList + [[leader,structure,probabilities,encounters,endEncounter]]
		
	return groupsList

def willIGo(node_id, group_struct, graph):
	neighbors = graph.neighbors(node_id)
	intersection = 1.0*len(list(set(neighbors).intersection(group_struct)))
	return intersection/(len(group_struct)-1)

def printGroups(groups):
	for i in groups:
		print("Leader: " +str(i[0])+"\n")
		print("Structure: " +str(i[1])+"\n")
		print("Probabilities: " +str(i[2])+"\n")		
		print("Encounters: " +str(i[3])+"\n")
		print("End of Encounters: " +str(i[4])+"\n")
		print("Duration:")
		test = []
		for j in range(len(i[4])):
			test = test+[(i[4][j]-i[3][j])]
		print(test)
		print("")


def printDurations(groups):
	for i in groups:
		for j in range(len(i[2])):
			print(int(i[3][j]-i[2][j]))

socialGraph = soc.generateGaussian(1201,20, 10,0.5,0.002);
#socialGraph = soc.readSocialGraph("../../mestrado/datasets2/dartmouth/1200_sample.csv",1200, 2*388800/(9))
#print("graph reading done!")


groups = defineGroups(1200,10,socialGraph)

printGroups(groups)


