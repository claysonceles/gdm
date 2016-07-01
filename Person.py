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
import groupStructure as gs

LEADER = 0
STRUCTURE = 1
PROB = 2
ENC = 3
END_ENC = 4

def scheduleConflict(schedule, newMeeting):
	flag = False
	for i in range(len(schedule)):
		to1 = newMeeting[0]
		tf1 = newMeeting[1]
		to2 = schedule[i][1][0]
		tf2 = schedule[i][1][1]
		case1 = to1 >= to2 and to1 <= tf2
		case2 = tf1 >= to2 and tf1 <= tf2
		case3 = to2 >= to1 and to2 <= tf1
		case4 = tf2 >= to1 and tf2 <= tf1
		if(case1 or case2 or case3 or case4):
			flag = True
			break;
	return flag

def insOrdSchedule(schedule,newMeeting):
	if schedule == []:
		return [newMeeting]
	if newMeeting[1][0] < schedule[0][1][0]:
		return [newMeeting] + schedule
	else:
		return [schedule[0]] + insOrdSchedule(schedule[1:],newMeeting)
		

def mySchedule(node_id, groups):	#TODO: Efficiency may be improved here
	schedule = []
	index = -1
	for i in range(len(groups)):
		if not(node_id in groups[i][STRUCTURE]):
			continue;
		else:
			for j in range(len(groups[i][STRUCTURE])):
				if(groups[i][STRUCTURE][j] == node_id):
					index = j
					break;
			prob = groups[i][PROB][index]
			for k in range(len(groups[i][ENC])):
				coin = (rd.randint(0,100000000)*1.0)/100000000
				if prob > coin and not(scheduleConflict(schedule,[groups[i][ENC][k],groups[i][END_ENC][k]])) :
					schedule = insOrdSchedule(schedule,[i,[groups[i][ENC][k],groups[i][END_ENC][k]]])
					#TODO: modificar tempo de permanencia individual no encontro.	
	return schedule

def allNodesSchedule(n_nodes,groups):
	nodesSchedule = []
	for i in range(n_nodes):
		a =  mySchedule(i,groups)
		nodesSchedule =  nodesSchedule + [a]
	return nodesSchedule		

def printNodesSchedule(nodesSchedule):
	for i in range(len(nodesSchedule)):
		for j in range(len(nodesSchedule[i])):
			print(str(i)+" "+str(nodesSchedule[i][j][0])+" "+str(int(nodesSchedule[i][j][1][0]))+" "+str(int(nodesSchedule[i][j][1][1])))

def insOrd(schedule,newMeeting):
	if schedule == []:
		return [newMeeting]
	if newMeeting < schedule[0]:
		return [newMeeting] + schedule
	else:
		return [schedule[0]] + insOrd(schedule[1:],newMeeting)

def sort(lista):
	listaOrd = []
	for i in lista:
		listaOrd = insOrd(listaOrd,i)
	return listaOrd



#socialGraph = soc.generateGaussian(1201,20, 10,0.5,0.002);
#socialGraph = soc.readSocialGraph("../../mestrado/datasets2/dartmouth/1200_sample.csv",1200, 2*388800/(9))

#groups = gs.defineGroups(1199,10,socialGraph)

#nodesSchedule = allNodesSchedule(1200,groups)

#printNodesSchedule(nodesSchedule)

#printNodesSchedule(nodesSchedule)
