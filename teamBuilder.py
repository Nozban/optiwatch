# Created By Etienne Brangbour in november 2017
#
# The actual script that give the best team to pick up.
#
import json
import pandas as pd
import numpy as np
import os
import time
from operator import add
tmps1=time.clock()
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
char = sorted(char)
path = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.path.sep

def teambuilder(opp,all,battletype):
	coefsyn = 0.3
	coefbonus = 0.5
	counter = pd.read_json(path+'matrices\\counter',orient='split')
	bonus = pd.read_csv(path+'matrices\\bonus.csv',index_col=0)
	scores = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	for val in opp:
		scores = scores + counter[val].values
	scores = scores + bonus.loc[battletype].values
	maxCounter = sum(sorted(scores, reverse=True)[0:6])
	scores = dict(zip(char, scores))
	print(scores)
	infile = open(path + 'matrices\\teamsyn', 'r+')
	max = float('-inf')
	best = []
	for line in infile:
		lineTab = line.split(" : ")
		score = int(lineTab[1])*coefsyn
		teamtab = lineTab[0].split(',')
		if set(all).issubset(teamtab):
			for c in teamtab:
				score += scores[c]
			if score>max:
				max=score
				best=teamtab
			if  max > maxCounter+int(lineTab[1])*coefsyn:
				break;
	return (best, max)
# all = []
# opp = ['gen','som','luc','tra','sym','mer']
# best = teambuilder(opp,all,'attpoint')

# print(str(best))
# tmps2=time.clock()
# print(str(tmps2-tmps1))

