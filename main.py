from PIL import Image
from numba import jit
from math import ceil
import numpy as np
from numpy import random
import os
import matplotlib.pyplot as plt
import glob
import time
from time import sleep

# Configuration:
FPS = 30                #Frames per second
duration = 2            #Duration in seconds
total = FPS*duration

loading="\|/-"
start_time = time.time()

def savetooutput(input, outputindex):
    input = np.reshape(input, (resx, resy, 3))
    input = input.astype(np.uint8)
    Image.fromarray(input).save("output/output" + str(outputindex).zfill(6) + ".jpg")


def drawdata(input):
    input = np.reshape(input, (resx, resy, 3))
    input = input.astype(np.uint8)
    plt.imshow(input)
    plt.show()


def randomize(data, ind):

    position = ind*(pixc//(duration*FPS))

    for i in range(pixc//(duration*FPS)):
        randindex = random.randint(pixc-1)
        tempr = data[0][position][0]
        tempg = data[0][position][1]
        tempb = data[0][position][2]
        data[0][position] = data[0][randindex]
        data[0][randindex][0] = tempr
        data[0][randindex][1] = tempg
        data[0][randindex][2] = tempb
        position += 1

@jit(nopython=True)
def jit_randomize(data, ind):

    position = ind * (pixc // (duration * FPS))

    for i in range(pixc // (duration * FPS)):
        randindex = random.randint(pixc - 1)
        tempr = data[0][position][0]
        tempg = data[0][position][1]
        tempb = data[0][position][2]
        data[0][position] = data[0][randindex]
        data[0][randindex][0] = tempr
        data[0][randindex][1] = tempg
        data[0][randindex][2] = tempb
        position += 1



image = Image.open('input.jpg')
data = np.asarray(image)
data = data.copy()
data.setflags(write=True)
data = data.astype(np.uint32)


resx = data.shape[0]
resy = data.shape[1]
pixc = resx*resy
outputindex = 0
startshape = data.shape
starttype = data.dtype

data = np.reshape(data, (1, pixc, 3))

if(pixc<62500):
    print("JIT mode: OFF")
    for i in range(total):
        randomize(data, i)
        savetooutput(data, outputindex)
        outputindex += 1
        print("Status: " + str(ceil((i + 1) / total * 100)) + "% " + loading[i % 4], end='\r')

else:
    print("JIT mode: ON")

    for i in range(total):
        randomize(data, i)
        savetooutput(data, outputindex)
        outputindex += 1
        print("Status: " + str(ceil((i + 1) / total * 100)) + "% " + loading[i % 4], end='\r')



frames = []


sleep(0.05)
imgs = sorted(glob.glob("output/*.jpg"), key=os.path.basename)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('output/output.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=(1000//FPS), loop=0)

print("Finished in %s seconds" % (round(time.time() - start_time, 4)))
