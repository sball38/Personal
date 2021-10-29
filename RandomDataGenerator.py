import random

positions = ['QB', 'RB', 'WR']
Entry = []
EntryTemplate = ""
namesub = 'Joe' 
TeamName = 'Razorbacks'
global entrylist
entrylist = []

#print(namesub + str(random_int))
#print(PlayerID)
#print(TeamName)
#print(positions[random_position])
#print(random_touchdowns)
#print(random_totalyards)
#print(random_salary)
PlayerID = 5

def WriteToFile():
	file_text = open('100k.txt', 'w')
	for x in entrylist:
		file_text.write(x + '\n')

for num in range (1,10):
	random_int = random.randint(1,10)
	random_position = random.randint(0,2)
	random_touchdowns = random.randint(0,50)
	random_totalyards = random.randint(0,2000)
	random_salary = random.randint(100000, 100000000)
	random_entry = '\"' + namesub + str(num) + '\", ' + str(PlayerID) + ', \"' + TeamName + '\", \"' + positions[random_position] + '\", ' + str(random_touchdowns) + ', ' + str(random_totalyards) + ', ' + str(random_salary)
	#print(random_entry + '\n')
	entrylist.append(random_entry)
	PlayerID += 1
	
WriteToFile()


