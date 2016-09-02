from random import random
from time import time

NUMTEAMS = 30
REPEAT_ROOM = False

tic = time()

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

for i in range(NUMTEAMS):
	for j in range(len(ans)):
		if j < (len(ans)-1):
			tmp = assign[i][j+1]
			text = ""
			if ans[j] > tmp: #handle differently for greater than or less than answer
				a = int(ans[j])/int(tmp)
				b = int(ans[j])/a - tmp
				text = "Take your answer, divide by " + str(a) + " and throw away the remainder, and subtract " + str(b) + ". This is your next room number."
			else if ans[j] < tmp:
				a = int(tmp)/int(ans[j])
				b = tmp - a*ans[j]
				text = "Take your answer, multiply by " + str(a) + ", and add " + str(b) + ". This is your next room number."
			else: #if equal just go there
				text = "Your answer is your next room number."
			assign[i][j] = (assign[i][j],text,tmp)
		else:
			assign[i][j] = (assign[i][j],"Return to the cafeteria.","Cafeteria")

fout = open("out.txt","w")
for i in range(NUMTEAMS):
	fout.write("TEAM " + str(i+1) + "\n")
	for j in range(len(ans)):
		fout.write("Question " + str(j) + " - CURRENT ROOM NUMBER: " + str(assign[i][j][0]) + " DIRECTION: " + str(assign[i][j][1]) + " NEXT ROOM NUMBER: " + str(assign[i][j][2]) + "\n")
fout.close()

toc = time()

print "Done!"
print "Time Elapsed: " + str(toc-tic)
