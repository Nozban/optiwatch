from detector import detect
from teamBuilder import teambuilder
import keyboard

oppteam = detect()
if oppteam == 'detection error':
	print(oppteam)
else:
	print('detected opponent team : '+str(oppteam) )
	team = teambuilder(oppteam,'attescort')
	print(str(team))
	keyboard.write(str(team))