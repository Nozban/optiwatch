import json
import pandas as pd
import numpy as np
import os

char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
nb = len(char)
ts = 6

path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'

char = sorted(char)
syn = pd.read_json(path+'syn',orient='split')

print(syn)

def calculSynergy(team):
	score = 0
	for i, c in enumerate(team):
		s=0
		for c2 in team[i+1:]:
			print(c + c2 + str(syn[c][c2]))		
			s+=syn[c][c2]
		print(s)
		score+=s
	return score

print(calculSynergy(['luc','mer','som','sym','wid','win']))
print(calculSynergy(['luc','mer','som','sym','han','win']))
