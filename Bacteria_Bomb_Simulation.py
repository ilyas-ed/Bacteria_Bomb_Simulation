

#* ---------------------------------------------------
#*
#*     Created by Ilyas: edd.ilyas@gmail.com, December 2021
#* 
#* ---------------------------------------------------



from matplotlib import pyplot as plt 
import rasterio
import pandas as pd
import numpy as np

from scipy.stats import kde
import scipy
import random 


print(scipy.__version__)
print(rasterio.__version__)

#! ----------------- Variables initialization -----------------

FILE_PATH = "./wind.gif"
# file path

OUTPUT_PATH = '.' # Output path

PARTICLES_NUM = 5000 # Amount of bacteria to be simulated

IMAGE_SIZE_x = 300
IMAGE_SIZE_y = 300

SAME_STARTING_POINT = True # set to True so as to all the bacteria start their movement from the same bombing point. If False the Bacteria will start from random places (apart the first one which will start from the bombing point)

SAVE_DENSITY_MAP = False # set to True in order to save the density map figure

COLOR_MAP = plt.cm.BuGn_r # Choose the colormap of preference

#? Probabilities of movements' directions
WEST = 0.5
NORTH = 0.10
SOUTH = 0.10
EAST = 0.75
#? Probabilities of movements' directions

#! ----------------- Variables initialization -----------------


#* ----------------- file reading -----------------

raster = rasterio.open(FILE_PATH)
src = raster.read(1)
PARTICLES_NUM_ = PARTICLES_NUM

#* ----------------- file reading -----------------


#? Finding out the bombing point from the data file

for i in range(len(src)):
    for j in range(len(src[0])):
        if src[i][j] != 0: 
            bomb_src = src[i][j]
            bomb_x = j
            bomb_y = i

#? Finding out the bombing point from the data file


#? Bacteria movements simulation

list_of_particles = list()
positions = list()
GROUND_HITTING_LOCATIONS = []

val_x = bomb_x
val_y = bomb_y

while(PARTICLES_NUM > 0):
    
    val = random.choices([1, 2, 3, 4], weights=(EAST, WEST, NORTH, SOUTH), k=1)[0]

    if val == 1:
        val_x += 1
        val_y += 0

    elif val == 2:
        val_x -= 1
        val_y += 0

    elif val == 3:
        val_x += 0
        val_y += 1
        
    else:
        val_x += 0
        val_y -= 1
        
    if val_y > 75:

        odds = random.choices([1, 2], weights=(0.2, 0.70), k=1)[0]

        if odds == 1: 
            val_y += 1

        if odds == 2: 
            val_y = 0
    else:
        val_y -= 1

    pos = (val_x, val_y)
    positions.append(pos)

    if val_y <= 0: 
        val_y = 0
        list_of_particles.append(positions)
        positions = list()
        
        GROUND_HITTING_LOCATIONS.append(positions)

        PARTICLES_NUM -=1

        if SAME_STARTING_POINT:
            val_x = bomb_x
            val_y = bomb_y
        else:
            val_x = random.choices(range(IMAGE_SIZE_x), k=1)[0]
            val_y = random.choices(range(IMAGE_SIZE_y), k=1)[0]


#? Bacteria movements simulation


#* Creating lists of X-coordinates and Y coordinates of all bacteria positions during the whole simulation

XX = []
YY = []

for i in range(PARTICLES_NUM_): 
    for a in list_of_particles[i]:
        XX.append(a[0])
        YY.append(a[1])

#* Creating lists of X-coordinates and Y coordinates of all bacteria positions during the whole simulation


#! Plooting 

plt.figure()
plt.scatter(XX, YY)
plt.xlim(0, IMAGE_SIZE_x)
plt.ylim(0, IMAGE_SIZE_y)


plt.figure()
data = np.array([XX, YY])
k = kde.gaussian_kde(data)
xi, yi = np.mgrid[min(XX):max(XX):100*1j, min(YY):max(YY):100*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=COLOR_MAP)
plt.contour(xi, yi, zi.reshape(xi.shape))

#! Plooting 


#* Saving the txt files

with open(OUTPUT_PATH + "/GROUND_HITTING_LOCATIONS.txt", 'w') as output:
    for row in GROUND_HITTING_LOCATIONS:
        output.write(str(row) + '\n')

with open(OUTPUT_PATH + '/density.dat', 'w') as outf:
    for lat in yi[:,0]:
        for long in xi[0]:
            outf.write("{:+.1f} {:.1f}\n".format(long, lat))

#* Saving the txt files


#? Saving the density heatmap

if SAVE_DENSITY_MAP:
    plt.savefig(OUTPUT_PATH + '/Density_heatmap.png')

#? Saving the density heatmap


plt.show()

