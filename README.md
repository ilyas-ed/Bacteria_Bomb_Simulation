# Bacteria_Bomb_Simulation

Code by Ilyas Ed-daoui


This script simulates the movements of bacteria in a given environment. The movements are affected by the position of the bacteria (especially the height). 


This program does the following:


1. Pull in the data file and finds out the bombing point. (i already have the data file that has the bombing point)
2. Calculates where 5000 bacteria will end up.
3. Draws a density map of where all the bacteria end up as an image and displays it on the screen.
4. Saves the density map to a file as text.
The basic algorithm is, for each particle, to move the particle up and along in a loop that picks randomly the way it will go. When it hits the ground, you make a note of where it hit by incrementing a 2D array by one, and start with the next particle.
5. Allow the user to set the number of particles and windspeed-based probabilities


As instance, this version is implementing this example:


From a given location, there is a 5% chance that in any given second, given the current wind, that a particle will blow west, a 10% chance of blowing north or south, and a 75% chance of blowing east. One model iteration is one second, and each model iteration the longest potential movement is one pixel on screen, which is 1 meter's length. 


The building is 75m high. If the particle is above the height of the building there is a 20% chance each second it will rise by a meter in turbulence, a 10% chance it will stay at the same level, and an 70% chance it will fall. Below the height of the building there is no turbulence, and the particles will drop by a meter a second


**Python/libraries versions:**


Python 3.8.5


numpy: 1.19.2


pandas: 1.1.3


matplotlib: 3.3.2


scipy: 1.6.2
raterio: 1.2.10


