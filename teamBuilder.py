# Created By Etienne Brangbour in november 2017
# 
# The actual script that give the best team to pick up. 
#
import json
import pandas as pd
import numpy as np
import os
from operator import add

char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
char = sorted(char)

def teambuilder(opp):
	path = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\'
	
	coefsyn = 0.5
	counter = pd.read_json(path+'counter',orient='split')
	scores = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

	for val in opp:
		scores = scores + counter[val].values
		#scores = scores - counter.loc[val].values

	scores = dict(zip(char, scores))
	#print(sorted(score, key=score.__getitem__))

	infile = open(path + 'teamsyn', 'r+')
	max = -99999999999999999 #dégueu
	best = []
	for line in infile:
		lineTab = line.split(" : ")
		score = int(lineTab[1])*coefsyn
		teamtab = lineTab[0].split(',')
		for c in teamtab:
			score += scores[c]
		if score>max:
			max=score
			best = []
			best.append(lineTab[0])
		elif score == max:
			best.append(lineTab[0])
	return best
	
opp = ['roa','mei','sol','tra','win','mer']
best = teambuilder(opp)

print(str(best))
	
	