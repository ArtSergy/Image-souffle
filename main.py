from PIL import Image
import numpy as np
import os
from random import randint
import matplotlib.pyplot as plt
import glob
from time import sleep


def savetooutput(input):
    input = np.reshape(input, (resx, resy, 3))
    input = input.astype(np.uint8)
    sleep(0.01)
    Image.fromarray(input).save("/home/linux77/PycharmProjects/imagesort/output/output" + str(outputindex) + ".jpg")


def drawdata(input):
    input = np.reshape(input, (resx, resy, 3))
    input = input.astype(np.uint8)
    plt.imshow(input)
    plt.show()


image = Image.open('input.jpg')
data = np.asarray(image)
data = data.copy()
data.setflags(write=True)
data = data.astype(np.uint32)


resx = data.shape[0]
resy = data.shape[1]
pixc = resx*resy
startshape = data.shape
starttype = data.dtype
framescout = 40         #number of frames
duration = 1            #duration
outputindex = 0

#data = np.insert(data,data.shape[2],255,axis=2)
#data = np.insert(data,data.shape[2],0,axis=2)
data = np.reshape(data, (1, pixc, 3))

#for i in range(pixc):
    #data[0][i][4] = i

for j in range(pixc):
    randindex = randint(j,pixc-1)
    tempr = data[0][j][0]
    tempg = data[0][j][1]
    tempb = data[0][j][2]
    data[0][j] = data[0][randindex]
    data[0][randindex][0] = tempr
    data[0][randindex][1] = tempg
    data[0][randindex][2] = tempb

    if (j%(pixc//framescout//duration)==0):
        savetooutput(data)
        outputindex += 1

frames = []
imgs = sorted(glob.glob("/home/linux77/PycharmProjects/imagesort/output/*.jpg"), key=os.path.getmtime)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('/home/linux77/PycharmProjects/imagesort/output/output.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=framescout//duration//2, loop=0)

outputgif = Image.open("/home/linux77/PycharmProjects/imagesort/output/output.gif").show()
