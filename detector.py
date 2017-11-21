# Created By Etienne Brangbour in november 2017
#
# Detect the opponent team.
#
import json
import pandas as pd
import numpy as np
import os
import time
import keyboard
import PIL
from PIL import ImageGrab
from operator import add
tmps1=time.clock()
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
char = sorted(char)
path = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.path.sep
needle = []

for c in char:
    needle.append(PIL.Image.open(path+'images'+os.path.sep+c+'.png'))

im=ImageGrab.grab()
im.show()

while True:
    if keyboard.is_pressed('q'):
        break
    else:
        pass


