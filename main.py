from detector import detect
from teamBuilder import teambuilder
import keyboard

def main():
	while True:
		print('------Select Battletype------')
		print('1:attaque escort')
		print('2:defence escort')
		print('3:attaque point')
		print('4:defence point')
		print('5:double attaque')
		print('x:Exit')
		k = keyboard.read_key()
		battletype = None
		while battletype == None:
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
			elif str(k)=='KeyboardEvent(x down)':
				return

		oppteam = 'detection error'

		while oppteam == 'detection error':
			print('press tab + enter')
			oppteam = detect()
			if oppteam == 'detection error':
				print(oppteam)
				keyboard.write(oppteam)

		print('detected opponent team : '+str(oppteam) )
		team = teambuilder(oppteam,battletype)
		print(str(team))
		keyboard.write(str(team))

main()