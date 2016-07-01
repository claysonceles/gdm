try:
    import matplotlib.pyplot as plt
except:
    raise

import numpy.random as rd
import numpy as np
import HeavyTail as pl

def generateGroupMeetingTimes(first_meeting_time,group_duration,beta,traceDur):	
#Parameters: <first_meeting time in hours> <period throughout which the group will meet regularly in hours> <average re-meeting period in hours>
#Generates group meeting times according to a poisson process
	group_meeting_intervals = rd.normal(beta,2,group_duration/beta)
	for i in range(len(group_meeting_intervals)):
		if group_meeting_intervals[i] < 0:
			group_meeting_intervals[i] = 0;
	#group_meeting_intervals = [first_meeting_time]+group_meeting_intervals
	group_meeting_times = []
	cumsum = 0
	for i in range(len(group_meeting_intervals)):
		coin = rd.exponential(beta*(group_duration*0.1))
		if(coin > cumsum and cumsum < traceDur):
			group_meeting_times = group_meeting_times + [cumsum]
		cumsum += group_meeting_intervals[i]
	for i in range(len(group_meeting_times)):
		group_meeting_times[i] = (first_meeting_time + group_meeting_times[i])*3600 #converting to seconds
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

def generateMeetingDur(n_groups,meetingTimes):
	meetingsAvgDur = pl.randht(n_groups,'cutoff',600,2,1.0/(30*24*3600));	#duration in seconds
	#meetingsAvgDur = pl.randht(n_groups,'powerlaw',600,3);	#duration in seconds
	endTimes = []
	for groupEnc in range(len(meetingTimes)):
		endTime = []
		durations = rd.normal(meetingsAvgDur[groupEnc],600,len(meetingTimes[groupEnc]))
		for i in range(len(durations)):
			if durations[i] < 0:
				durations[i] = 0
		for i in range(len(durations)-1):
			if durations[i] + meetingTimes[groupEnc][i] > meetingTimes[groupEnc][i+1]:
				durations[i] = meetingTimes[groupEnc][i+1] - meetingTimes[groupEnc][i]
		for i in range(len(durations)):
			endTime = endTime + [meetingTimes[groupEnc][i] + durations[i]]
		endTimes = endTimes+[endTime]
	return endTimes
		

