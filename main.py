import keyboard
import random
import time
import os
max = 80 * 20
nam = 40
lp = ""
y = 0
n1 = nam
cols = 80
lines = 20
jump = 0
timesleep = 0.005
player = 'p'
fire1 = False
fire = False
live2 = 100
live1 = 100
namy = 0
bot = "b"
timefire = 0.0
timefire1 = 0.0
score1 = 0
score2 = 0


def print_hi(place,entiti):


	global y
	global lp
	while place > y:
		y += 1
		lp += "."
	lp += entiti
	y += 1


def bot1():


	global namy
	global max
	global timefire1
	global nam
	global live1
	global fire1
	global bot
	time.sleep(0.002)
	bot = "b"
	ran = random.randrange(0,4)
	if ran == 1:
		if not namy + 1 == max:
			namy += 1
	elif ran == 0:
		if not namy - 1 == 0:
			namy -= 1
	elif ran == 2 and not timefire1 > 0 and False:
		bot += ">>>>"
		if namy + 3 > nam:
			live1 -= 10
		timefire1 = 0.1
		max -= 4
		fire = True		


def main(nam):


	global lp
	global y
	y = 0
	lp = ""
	time.sleep(timesleep)
	if nam < namy:
		time.sleep(0.0001)

		print_hi(nam,player)

		print_hi(namy,bot)
	else:
		time.sleep(0.0001)

		print_hi(namy,bot)

		print_hi(nam,player)	
	print_hi(max,"")
	# print x, y
	if nam < 79:
		ox = nam
	else:
		we = int(nam / 80)
		qw = 1
		ox = nam - 80
		while qw < we:
			qw += 1
			ox -= 80
		if ox == -1:
			ox = 79
	qip = ('y:' + str(int((nam / 80) + 1)) + ', x:' + str(ox + 1) + ", live1: " + str(live1) + ", live2: " + str(live2) + ", timefire: " + str(timefire) + "\nscore1: " + str(score1) + ", score2:" + str(score2))
	lp += qip
	os.system("cls")
	print(lp)
	# ............................................................
os.system("mode con:cols=80 lines=23")
os.system("cls")
print("press any button")
os.system("pause >nul")
main(nam)
while 2>1:
	if not timefire1 < 0.02:
		time.sleep(0.001)
		timefire1 -= 0.001
	else:
		timefire1 = 0.0
	max = 80 * 20
	#bot1()
	if live2 == 0:
		score1 += 1
		live2 = 100
		namy = 0
	if live1 == 0:
		score2 += 1
		live1 = 100
		nam = 1
	if not timefire < 0.02:
		time.sleep(0.001)
		timefire -= 0.001
	else:
		timefire = 0.0
	if fire:
		time.sleep(0.02)
		player = "p"
		max += 4
		fire = False
	if keyboard.is_pressed("e") and not timefire > 0 and False:
		# fire
		if player == "p":
			player += ">>>>"
			if nam + 3 > namy:
				live2 -= 10
		if player == "q":
			player = "<<<<" + player
			if nam - 3 < namy:
				live2 -= 10
			nam -= 4
		timefire = 0.1
		max -= 4
		fire = True
	if nam > max - 1:
		nam = n1

	if nam < 0:
		nam = n1

	if keyboard.is_pressed('a'):
		n1 = nam
		nam -= 1
		player = 'q'

	if keyboard.is_pressed('d'):
		n1 = nam
		nam += 1
		player = 'p'
		
	if keyboard.is_pressed('w') and not nam - 80 < 0:
		n1 = nam
		nam = nam - 80
	if keyboard.is_pressed('s') and not nam + 80 > max - 1:
		n1 = nam
		nam = nam + 80

	x = range(79, 1841, 80)
	for x in x:
		if nam == x:
			if player == 'q':
				nam = n1

		if nam == x + 1:
			if player == 'p':
				nam = n1
	if keyboard.is_pressed('space'):
		if jump == 0:
			jump = 1
	if jump == 1:
		if not nam < cols * (lines - 6):
			nam -= cols
		else:
			jump = 2
	if jump == 2:
		if not nam > cols * (lines - 1):
			nam += cols
		else:
			jump = 0
	main(nam)