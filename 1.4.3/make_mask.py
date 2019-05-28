import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 13 == 4: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [118, 200, 225, 150] # light blue
            elif (row-column)/stripe_width % 2 == 0: 
                image[row][column] = [108 , 27, 132, 168]
               
            else:
                # Odd stripe
                image[row][column] = [16, 22, 111, 245] # blue
    return image
    
if __name__ == "__main__":
    image = make_mask(100, 100, 5)
    
    fig, ax = plt.subplots(1, 2)
    ax[1].imshow(image)
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'woman.jpg')
img = plt.imread(filename)
ax[0].imshow(img, interpolation =   'none')
fig.savefig('woman_mask.png')