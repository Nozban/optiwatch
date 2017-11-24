# Created By Etienne Brangbour in november 2017
#
# Detect the opponent team.
#
import json
import pandas as pd
import numpy as np
import cv2
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

def detect():		
	keyboard.wait('tab+enter')
	im = ImageGrab.grab()
	im.save('images'+os.path.sep+'sc.jpg', 'JPEG')
	res=[]
	im = cv2.imread(path+'images'+os.path.sep+'sc.jpg')

	for c in char[:6]:
		template = cv2.imread(path+'images'+os.path.sep+c+'.png')
		cv2.imshow('i',template)
		temp = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where(temp >= threshold)
		print(loc)
		if len(loc[0])>0:
			res.append(c)
			print(c)
		if len(res)==6:
			break
	if len(res)!=6:
		return 'detection error'
	return res
	
#print(str(res))
    

im = ImageGrab.grab()
im.resize(600,800)
im.save('images'+os.path.sep+'loul.jpg', 'JPEG')

keyboard.wait('x')


