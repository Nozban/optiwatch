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

def detect():		
	keyboard.wait('tab+enter')
	im = ImageGrab.grab()
	basewidth = 800
	wpercent = (basewidth / float(im.size[0]))
	hsize = int((float(im.size[1]) * float(wpercent)))
	im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	im=im.crop((0,0,basewidth,hsize/2))
	im.save('images'+os.path.sep+'sc.jpg', 'JPEG')
	res=[]
	im = cv2.imread(path+'images'+os.path.sep+'sc.jpg')

	for c in char:
		template = cv2.imread(path+'images'+os.path.sep+c+'.jpg')
		temp = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where(temp >= threshold)
		if len(loc[0])>0:
			res.append(c)
		if len(res)==6:
			break
	if len(res)!=6:
		return 'detection error'
	return res
	
#print(str(res))
 

# keyboard.wait('x') 
# for j in range(1,13):
	# im = Image.open(path+'images'+os.path.sep+"screenshot"+str(j)+".jpg")
	# basewidth = 800
	# wpercent = (basewidth / float(im.size[0]))
	# hsize = int((float(im.size[1]) * float(wpercent)))
	# im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	# #im=im.crop((0,0,basewidth,hsize/2))
	# im.save('images'+os.path.sep+'loul.jpg', 'JPEG')
	# #114
	# for i in range(6):
		# base = 184
		# ah=im.crop((base+i*80,241,base+i*80+32,241+32))
		# ah.save('images'+os.path.sep+'loul'+str(j)+str(i)+'.jpg', 'JPEG')



