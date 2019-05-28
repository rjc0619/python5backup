#13
#matplotlib.pyplot (plt) – Used for graphs and charting
#numpy (np) – used for math method
#PIL – It looks at the image (modifications)
#15a. Practice using this vocabulary by describing line 19: Line 19 calls the 
#function subplot from the plt library. The function is being called with 2
#argument(s): number of images and number of windows. The function returns 2 object(s),
#which is/are being assigned to ax.
#15b. Line 20 calls __imshow()_ on ___ax[0]____
#Line 23 calls imshow() on ax[1]
#Line 24 calls xticks on ax[1]
#Line 25 calls xlim on ax[1]
#Line 26 calls ylim on ax[1]
#Line 27 calls savefig on fig
#15c. (1162,966)
#16 (720,950)
#17a.Line 30 uses the join() method from the os.path module. It is being passed 2
#arguments. The value it returns is being assigned to the variable earth.
#17b.In line 31 the open() function of the PIL.Image module returns a new PIL.Image
#object, which is being assigned to the variable earth.img. 
#17c.In line 32 the resize() method takes only one argument: a 2-tuple because
#it needs the with and the height to get the image. 
#17d. The purpose of (89,87) is to identify the width and height of the image
#17e. Line 35 calls the function imshow from the axes1 library with 1 
#argument(s): image. The function returns resized earth object(s), which is/are being 
#assigned to earth.
#Line 33 calls the method subplots on the object fig 2 with2 1 argument(s): resize. 
#17fi. resizing
#17fii. thumbnail
#17iii. thmbnail
#17g. gives the height and width
#17h.the first one displays the length and with of the normal image. The second 
#print command displays the resized image of the orginal image, the lenght and 
#with of the resized image. and the final print coma=mand displays the 1st 
#character in the normal image which is 475
#17i.The image on the right has less pixles because the image is much smaller and 
#it cant fit as many pixels as the bigger image can.
#18. The algorithim that resize is using is 