# Created By Etienne Brangbour in november 2017
#

import json
import pandas as pd
import os
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
battletype = ['attescort','defescort','attpoint','defpoint','dual']

counter = []
char = sorted(char)

tempcounter = pd.read_csv(path+'contre.csv',index_col=0)
c=[]
for i, val in enumerate(char):
    c.append([])
    for j, val2 in enumerate(char):
        if(j<=i):
            c[i].append(tempcounter[val2][val])
        else:
            c[i].append(-tempcounter[val][val2])

cframe = pd.DataFrame(c, index=char, columns=char)
print(cframe)
outfile = open(path + 'counter', 'w+')
outfile.write(cframe.to_json(orient="split"))
outfile.close()

tempsyn = pd.read_csv(path+'synergy.csv',index_col=0)
s=[]
for i, val in enumerate(char):
    s.append([])
    for j, val2 in enumerate(char):
        if(j<=i):
            s[i].append(tempsyn[val2][val])
        else:
            s[i].append(tempsyn[val][val2])

sframe = pd.DataFrame(s, index=char, columns=char)
print(sframe)
outfile = open(path + 'syn', 'w+')
outfile.write(sframe.to_json(orient="split"))
outfile.close()
