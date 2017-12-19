# Created By Etienne Brangbour in november 2017
# 
# This file use the matrix of synergy given in 'syn' to calculate and write in 'teamsyn' the synergy score of each team possible
# This script just needs to be run when syn matrix is changed.
#
import json
import pandas as pd
import numpy as np
import os
import time
from operator import add
tmps1=time.clock()
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
nb = len(char)
ts = 6

char = sorted(char)
syn = pd.read_json(path+'syn',orient='split')

#for i, val in enumerate(char):
#	for j, val2 in enumerate(char):
#		if(j<=i):
#			temp = syn[j][i]
#			syn[i][j] = temp

def calculSynergy(team):
	score = 0
	for i, c in enumerate(team):
		for c2 in team[i+1:]:
			score+=syn[c][c2]
	return score

i=0
outfile = open(path + 'teamsyn', 'w+')

tabtemp = []

for a in range(nb-5):
	for b in range(a+1,nb-4):
		for c in range(b+1,nb-3):
			for d in range(c+1,nb-2):
				for e in range(d+1,nb-1):
					for f in range(e+1,nb):
						team = [char[a],char[b],char[c],char[d],char[e],char[f]]
						score = calculSynergy(team)
						tabtemp.append((char[a]+","+char[b]+","+char[c]+","+char[d]+","+char[e]+","+char[f], score))
						i+=1;
						print (i)

						
tabtemp = sorted(tabtemp, key=lambda colonnes: colonnes[1], reverse=True)
for l in tabtemp:
	outfile.write(l[0]+" : " + str(l[1]) + "\n")						
outfile.close()	

		
tmps2=time.clock()
print(str(tmps2-tmps1))