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

path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\'

for j in range(0,1):
	im = Image.open(path+"ScreenShot"+str(j)+".jpg")
	basewidth = 800
	wpercent = (basewidth / float(im.size[0]))
	hsize = int((float(im.size[1]) * float(wpercent)))
	im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	#im=im.crop((0,0,basewidth,hsize/2))
	#im.save('images'+os.path.sep+'loul.jpg', 'JPEG')
	#114
	for i in range(6):
		base = 184
		ah=im.crop((base+i*80,241,base+i*80+32,241+32))
		ah.save('loul'+str(j)+str(i)+'.jpg', 'JPEG')