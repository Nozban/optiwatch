import os
import glob
path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + '\\'
files = glob.glob(path+'ScreenShot*')
i = 0

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'ScreenShot'+str(i)+'.jpg'))
    i = i+1
