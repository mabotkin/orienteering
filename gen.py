from random import random

NUMTEAMS = 30
REPEAT_ROOM = False

rooms = []
ans = []
fin = open("rooms.txt").read().splitlines()
for i in fin:
	rooms.append(int(i))
fin = open("ans.txt").read().splitlines()
for i in fin:
	ans.append(int(i))
#initially distribute rooms in so that no room is overused or underused
assign = [[0 for i in range(len(ans))] for i in range(NUMTEAMS)]
cur = 0
for i in range(NUMTEAMS):
	for j in range(len(ans)):
		assign[i][j] = rooms[cur]
		cur += 1
		if cur >= len(rooms):
			cur = 0
#swap a lot of times
for i in range(NUMTEAMS*NUMTEAMS*len(ans)):
	#choose horizontal or vertical swap
	if random() < 0.3:
		#horizontal swap
		team = int(random()*NUMTEAMS)
		x = int(random()*len(ans))
		y = int(random()*len(ans))
		tmp = assign[team][x]
		assign[team][x] = assign[team][y]
		assign[team][y] = tmp
	else:
		#vertical swap
		x = int(random()*len(ans))
		team1 = int(random()*NUMTEAMS)
		team2 = int(random()*NUMTEAMS)
		if not REPEAT_ROOM and (assign[team2][x] in assign[team1] or assign[team1][x] in assign[team2]):
			#dont let teams repeat rooms
			i -= 1
			#skip iteration
		else:
			tmp = assign[team1][x]
			assign[team1][x] = assign[team2][x]
			assign[team2][x] = tmp

print assign

