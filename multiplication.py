import console
from random import choice

def getAnswer(message):
	while True:
		reponse=input(message)
		try:
			if reponse != "q":
				value=int(reponse)
				return value
				break
		except ValueError:
			print("please enter an integer value.")
			continue
		return reponse

timesTable = [
	(3,0,0),
	(3,1,3),
	(3,2,6),
	(3,3,9),
	(3,4,12),
	(3,5,15),
	(3,6,18),
	(3,7,21),
	(3,8,24),
	(3,9,27),
	(3,10,30),
	(3,11,33),
	(3,12,36),
	(6,0,0),
	(6,1,6,),
	(6,2,12),
	(6,3,18),
	(6,4,24),
	(6,5,30),
	(6,6,36),
	(6,7,42),
	(6,8,48),
	(6,9,54),
	(6,10,60),
	(6,11,66),
	(6,12,72)
	]
ans = ""
minimum = 0
maximum = 23
correct = False
console.clear()

while True :
	allNumbers = list(range(minimum, maximum))
#selection = []
#for i in range(n):
	r = choice(allNumbers)

	a = timesTable[r][2]
	ans = getAnswer('what is %i x %i?' %(timesTable[r][0], timesTable[r][1]))
	console.clear()
	if ans == "q":
		break
	
	correct = (ans == a)
	print("You answered {}".format(ans))
	print("That's {}".format(correct))
	#else
	#	correct == False
	
print("exiting... thanks for playing.")	
