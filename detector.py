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
from PIL import Image
from operator import add
tmps1=time.clock()
char = ['doo','rea','gen','mcc','pha','sol','som','tra','roa','dva','ori','rei','win','zar','bas','jun','wid','han','mei','tor','ana','mer','luc','moi','sym','zen']
char = sorted(char)
path = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.path.sep

def detect(teamsize):		
	keyboard.wait('tab+enter')
	im = ImageGrab.grab()
	basewidth = 800
	wpercent = (basewidth / float(im.size[0]))
	hsize = int((float(im.size[1]) * float(wpercent)))
	im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	im1=im.crop((0,0,basewidth,hsize/2))
	im2=im.crop((160+80*teamsize,hsize/2,basewidth,hsize))
	im1.save('images'+os.path.sep+'sc.jpg', 'JPEG')
	im2.save('images'+os.path.sep+'sc2.jpg', 'JPEG')
	enemies=[]
	allies = []
	im1 = cv2.imread(path+'images'+os.path.sep+'sc.jpg')
	im2 = cv2.imread(path+'images'+os.path.sep+'sc2.jpg')

	for c in char:
		template = cv2.imread(path+'images'+os.path.sep+c+'.jpg')
		temp = cv2.matchTemplate(im1, template, cv2.TM_CCOEFF_NORMED)
		temp2 = cv2.matchTemplate(im2, template, cv2.TM_CCOEFF_NORMED)

		threshold = 0.8
		loc = np.where(temp >= threshold)
		loc2 = np.where(temp2 >= threshold)
		if len(loc[0])>0:
			enemies.append(c)
		if len(loc2[0])>0:
			allies.append(c)
		if len(enemies)==6 and len(allies)==6-teamsize:
			break
	if len(enemies)!=6 or len(allies)!=6-teamsize:
		return 'detection error'
	return (enemies,allies)
	
#print(str(res))
 

# keyboard.wait('x') 




