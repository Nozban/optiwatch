# Created By Etienne Brangbour in november 2017
#
# manualy input the matrices, just used for test.

import json
import pandas as pd
import os
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
battletype = ['attescort','defescort','attpoint','defpoint','dual']

counter = []
bonus = []
char = sorted(char)

for i in battletype:
	row = []
	for j in char:
		row.append(0)
	bonus.append(row)

bonusframe = pd.DataFrame(bonus, index=battletype, columns=char)
outfile = open(path + 'bonus', 'w+')
outfile.write(bonusframe.to_json(orient="split"))
outfile.close()

for i, val in enumerate(char):
    counter.append([])
    for j, val2 in enumerate(char):
        counter[i].append(input(val + '-->' + val2 + ': '))

counterframe = pd.DataFrame(counter, index=char, columns=char)

outfile = open(path + 'counter', 'w+')
outfile.write(counterframe.to_json(orient="split"))
outfile.close()

syn = []

for i, val in enumerate(char):
    syn.append([])
    for j, val2 in enumerate(char):
        if(j<=i):
            syn[i].append(0)
        else:
            syn[i].append(input(val + ' and ' + val2 + ': '))


synframe = pd.DataFrame(syn, index=char, columns=char)

outfile = open(path + 'syn', 'w+')
outfile.write(synframe.to_json(orient="split"))
outfile.close()
