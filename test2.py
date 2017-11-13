import json
import pandas as pd
import numpy as np
import os
from operator import add
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '/'
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']

char = sorted(char)
counter = pd.read_json(path+'counter',orient='split')

opp = ['roa','mei','sol','tra','win','mer']
score = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for val in opp:
    score = score + counter[val].values
    score = score - counter.loc[val].values

score = dict(zip(char, score))

print(sorted(score, key=score.__getitem__))
