from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
height = len(img)
width = len(img[0])
for row in range(420, 480):
    for column in range(120, 160):
        img[row][column] = [0, 255, 0] # red + green = yellow
        
height = len(img)
width = len(img[1])
for row in range(440, 500):
    for column in range(430, 480):
        img[row][column] = [0, 255, 0]
ax.imshow(img, interpolation='none')
# Saves the figure

###
# Make a rectangle of pixels yellow
###


 
fig.savefig('women_sky_earing')

'''#5 The image height = the number of rows of pixels = 960
	the image width = the number of columns = 584
	the green intensity at (5,9) = img[5][9][1]
the red intensity at (4,10) = 62
the red intensity of the 25th pixel in the 50th row = 75
'''

