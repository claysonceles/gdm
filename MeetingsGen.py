try:
    import matplotlib.pyplot as plt
except:
    raise

import numpy.random as rd
import numpy as np

def generateGroupMeetingTimes(first_meeting_time,group_duration,beta,traceDur):	
#Parameters: <first_meeting time in hours> <period throughout which the group will meet regularly in hours> <average re-meeting period in hours>
#Generates group meeting times according to a poisson process
	group_meeting_intervals = rd.normal(beta,2,group_duration/beta)
	#group_meeting_intervals = [first_meeting_time]+group_meeting_intervals
	group_meeting_times = []
	cumsum = 0
	for i in range(len(group_meeting_intervals)):
		coin = rd.exponential(beta*(group_duration*0.1))
		if(coin > cumsum and cumsum < traceDur):
			group_meeting_times = group_meeting_times + [cumsum]
		cumsum += group_meeting_intervals[i]
	for i in range(len(group_meeting_times)):
		group_meeting_times[i] += first_meeting_time
	return group_meeting_times

def readRegularityDistro():
	f = open("RegDistro.csv")
	groupsRegDistro = []
	n_groups = 0 
	for line in f:
		pair = line.split(" ")
		i = int(pair[0])
		j = int(pair[1])
		n_groups += i
		groupsRegDistro = groupsRegDistro + [[i,j]]
	return (n_groups,groupsRegDistro)

def generateGroupSet(n_groups, groupsRegDistro, g_dur, sim_dur):
	groupSet = []
	for i in groupsRegDistro:
		for j in range(i[0]):
			beta = i[1];
			firstMeeting = np.random.randint(0,sim_dur*24)
			newGroup = generateGroupMeetingTimes(firstMeeting,g_dur*24,beta,sim_dur);
			groupSet = groupSet + [newGroup]
	return groupSet


#def generateGroupSet(n_groups,g_dur):
#	all_meetings = []
#	for i in range(n_groups):
#		beta = 24#*rd.exponential(3) #FRIENDS
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup
#	for i in range(n_groups/2):
#		beta = 7*24#*rd.exponential(3) #COLEAGES
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup

#	for i in range(n_groups/6):
#		beta = 2*24#*rd.exponential(3) #COLEAGES
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup

#	for i in range(n_groups/6):
#		beta = 3*24#*rd.exponential(3) #COLEAGES
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup

#	for i in range(n_groups/6):
#		beta = 5*24#*rd.exponential(3) #COLEAGES
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup

#	for i in range(n_groups/3):
#		beta = 24/6#*rd.exponential(3) #HOUSEMATES
#		newgroup = generateGroupMeetingTimes(0,g_dur*24,beta);
#		all_meetings = all_meetings + newgroup
#
#	return_list = []
#	for i in range(len(all_meetings)):
#		return_list = return_list + [int(all_meetings[i])]
#	for i in range(len(all_meetings)):
#		print(int(all_meetings[i]))
#	return return_list;

n_groups,groupsRegDistro = readRegularityDistro()
gSet = generateGroupSet(n_groups,groupsRegDistro,30,60)
print(len(gSet))


