from detector import detect
from teamBuilder import teambuilder
import keyboard
import os
def main():
	teamsize = 0
	while True:
		print('------Welcome to optiwatch ------')
		print('Enter the size of your team:')
		k = keyboard.read_key()
		teamsize = int(str(k)[14])
		print(teamsize)
		if(teamsize>0 or teamsize<7):			
			break
		else:
			print('error : size out of range')
	os.system('cls')	
	while True:
		print('------Select Battletype------')
		print('1:attaque escort')
		print('2:defence escort')
		print('3:attaque point')
		print('4:defence point')
		print('5:double attaque')
		print('9:Exit')
		battletype = None
		while battletype == None:
			k = keyboard.read_key()
			if str(k)=='KeyboardEvent(1 down)':
				print('1:attaque escort')
				battletype='attescort'
			elif str(k)=='KeyboardEvent(2 down)':
				print('2:defence escort')
				battletype='defescort'
			elif str(k)=='KeyboardEvent(3 down)':
				print('3:attaque point')
				battletype='attpoint'
			elif str(k)=='KeyboardEvent(4 down)':
				print('4:defence point')
				battletype='defpoint'
			elif str(k)=='KeyboardEvent(5 down)':
				print('5:double attaque')
				battletype='double'
			elif str(k)=='KeyboardEvent(9 down)':
				return

		teams = 'detection error'

		while teams == 'detection error':
			print('press tab + enter')
			teams = detect(teamsize)
			if teams == 'detection error':
				print(teams)
				keyboard.write(teams)
		os.system('cls')
		print('detected opponent team : '+str(teams[0]) )
		print('detected allied team : '+str(teams[1]) )
		(team, score) = teambuilder(teams[0],teams[1],battletype)
		print('opptimal teams calculated : '+str(team)+':'+str(score))
		esq = list(set(team)-set(teams[1]))
		print('esquade : '+str(esq))
		keyboard.write(str(team))
		keyboard.wait('enter')
		os.system('cls')

main()
