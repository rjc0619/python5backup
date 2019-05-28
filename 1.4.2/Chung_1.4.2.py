#1-3 N/A
'''Part I: Working with a Filesystem'''
#4 N/A
#5 The relative file name is C:/
#6 the code is in windows so it will not show the c:\\

'''Part II: Rendering an Image on Screen:'''

#women_plot.png
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
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
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('women_plot')


#cat_plot.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot')


#two_women.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
# Show the figure on the screen
# fig.show()
fig.savefig('two_women')


#five_cats.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[2].imshow(img)
ax[3].imshow(img)
ax[4].imshow(img)
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats')


#lef_earing.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')


#experiment.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)
# Get the directory of this python script

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].cla()
ax[2].imshow(img)
# Show the figure on the screen
# fig.show()
fig.savefig('experiment')


# three_closeup.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
# Get the directory of this python script

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(35, 45)
ax[1].set_xlim(45, 55)
ax[2].set_xlim(55, 65)
ax[0].set_ylim(80, 70)
ax[1].set_ylim(80, 70)
ax[2].set_ylim(80, 70)
# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup')


#crazy_mice.png
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation =   'none')
ax[1].imshow(img, interpolation =   'none')
ax[1].plot (37, 48, 'ro')
ax[1].plot (116, 42, 'ro')
ax[1].plot (140, 42, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice')

#7a. It gave me an error
#7b. Yes, the code used matplotlib in a non graphical backend so it will work
#7c. 291.5, 391
#8a. fig is an instance of the class figure object and ac is an instanc of the
#class AxesSubplot object
#8b. Similarly, in line 25, the method imshow () is being called on the object
#ax. That method is being given 1 arguments. That method is a method of 
#the class AxeSubplot class.
#8c. line 30: shows figure on the screen
'''Part IV: Arrays of Objects'''
#9a. the method subplots is being called on the object (Figure, AxesSubplot).
#9b.N/A
'''Part V: Keyword = Value Pairs'''
#10 N/A
