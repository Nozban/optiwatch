import json
import pandas as pd
import os
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']

counter = []

char = sorted(char)

# for i, val in enumerate(char):
#     counter.append([])
#     for j, val2 in enumerate(char):
#         counter[i].append(input(val + '-->' + val2 + ': '))
#
# counterframe = pd.DataFrame(counter, index=char, columns=char)
#
# outfile = open(path + 'counter', 'w+')
# outfile.write(counterframe.to_json(orient="split"))
# outfile.close()

cyn = []

for i, val in enumerate(char):
    cyn.append([])
    for j, val2 in enumerate(char):
        if(j<=i):
            cyn[i].append(0)
        else:
            cyn[i].append(input(val + ' and ' + val2 + ': '))


cynframe = pd.DataFrame(cyn, index=char, columns=char)

outfile = open(path + 'cyn', 'w+')
outfile.write(cynframe.to_json(orient="split"))
outfile.close()
