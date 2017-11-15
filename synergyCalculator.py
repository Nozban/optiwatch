# Created By Etienne Brangbour in november 2017
# 
# This file use the matrix of synergy given in 'syn' to calculate and write in 'teamsyn' the synergy score of each team possible
# This script just needs to be run when syn matrix is changed.
#
import json
import pandas as pd
import numpy as np
import os
from operator import add
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
	for char in team:
		score += sum(syn[char].values)
		score += sum(syn.loc[char].values)
	return score

i=0
outfile = open(path + 'teamsyn', 'w+')

for a in range(nb-5):
	for b in range(a+1,nb-4):
		for c in range(b+1,nb-3):
			for d in range(c+1,nb-2):
				for e in range(d+1,nb-1):
					for f in range(e+1,nb):
						team = [char[a],char[b],char[c],char[d],char[e],char[f]]
						score = calculSynergy(team)
						outfile.write(char[a]+","+char[b]+","+char[c]+","+char[d]+","+char[e]+","+char[f]+" : " + str(score) + "\n")
						i+=1;
						print (i)
						
outfile.close()	        
		
		