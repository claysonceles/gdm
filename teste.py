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

lista = [9,15,1,7,200,4,7,2,8,1]
print lista
print sort(lista)
