from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw      
import Image, ImageOps
import Image, ImageDraw, ImageFont
import Image



    #returns the canvas with the right size, color, and width for the image that is going to be edited
 #Removes all the unwanted files from the directory, So that there's more space to run code
   
def new_create_border(image, color, width):
#The image the border is being applied to MUST be in the Project_Images folder
    new_size = int(image.size[0] * (1 + width * 2)), int(image.size[1] * (1 + width * 2))
    
    paste_location = (int(image.size[0] * width), int(image.size[1] * width))
    #This is the location the border is going to be paste on 
    
    background_canvas = PIL.Image.new('RGBA', new_size, color)
    #creates a plain background canvas
    background_canvas.paste(image, paste_location)
    #this will be where the image the user wants to edit will be, with the border on the image
    
    return background_canvas
def main():
    img = Image.open('family (1).jpg')
    img = img.resize((6240,4160)) 
    img = new_create_border(img, (184, 131, 11, 255), 0.1)
    img = new_create_border(img, (255, 215, 0, 255), 0.2)
    img = img.save('familyborder.jpg')#<---- To delete/insert a border either delete this line of code or insert another one
        #if you change the code be sure to replace the color, and ratio
        #makes 2 borders which later is going to be applied to the image the user wants to edit
        #The numbers in the brakets represents the RGBA value of the border, and the 0.1/0.2 reprent the size of the canvas
        
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''Family-Text'''
    #Every code from now onwards adds extensions to the border, EX: Geomatrical Shapes, Sillhotes, and corner lines
        
    paste_img = Image.open(os.path.join('Project_Images','text.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize((1700,1100))#resizes the img so that it fits perfectly on the border
    
    
    img = Image.open('familyborder.jpg')
    img.paste(paste_img, (4260, 0), mask = paste_img)
    img = img.save('familytext.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
       
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Top-Left Border'''
        
    paste_img = Image.open(os.path.join('Project_Images', 'vinezz.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (2700, 2700))#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('familytext.jpg')
    img.paste(paste_img, (100, 50), mask = paste_img)
    img = img.save('familyborder.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
    
        
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
        
    '''Bottom-Right Border'''
            
    paste_img = Image.open(os.path.join('Project_Images','vinezz.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (2700, 2700))#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.rotate( 180, expand = paste_img)
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
        
    img = Image.open('familyborder.jpg')
    img.paste(paste_img, (7555, 4200), mask = paste_img)
    img = img.save('familyborder1.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
    
     
        
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Top-Right Border'''
        
    paste_img = Image.open(os.path.join('Project_Images', 'vinezz.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (2700, 2700))#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.rotate( 270, expand = paste_img)#rotates the image 270 degrees so that it lines up on the top right
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('familyborder1.jpg')
    img.paste(paste_img, (7555, 50), mask = paste_img)
    img =img.save('border2.jpg')# finally pastes the image that has been opened, resized, converted on to  
    #the border 
       
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Bottom-Left Border'''
            
    paste_img = Image.open(os.path.join('Project_Images','vinezz.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (2700, 2700))#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.rotate( 90, expand = paste_img)#rotates the image 270 degrees so that it lines up on the top right
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('border2.jpg')
    img.paste(paste_img, (100, 4200), mask = paste_img)
    img = img.save('border3.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
      
        
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Left-Logo'''
            
    paste_img = Image.open(os.path.join('Project_Images','goldencircle.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (700, 700) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('border3.jpg')
    img.paste(paste_img, (2915, 50), mask = paste_img)
    img = img.save('logo.jpg')# finally pastes the image that has been opened, resized, converted on to  
    #the border 
    img = img.convert("RGBA")
      
            
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
    '''Right-Logo'''
            
    paste_img = Image.open(os.path.join('Project_Images','goldencircle.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (700,700) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('logo.jpg')
    img.paste(paste_img, (6666, 50), mask = paste_img)
    img = img.save('logo2.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
    
       
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Bottom Left-Logo'''
        
        
    paste_img = Image.open(os.path.join('Project_Images','goldencircle.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (700,700) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
    
    img = Image.open('logo2.jpg')
    img.paste(paste_img, (2915, 6100), mask = paste_img)
    img = img.save('logo3.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
    
        
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Bottom Right-Logo'''
        
    paste_img = Image.open(os.path.join('Project_Images','goldencircle.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (700,700) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('logo3.jpg')
    img.paste(paste_img, (6666, 6100), mask = paste_img)
    img = img.save('logo4.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
     
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Football-Sillothe'''
        
    paste_img = Image.open(os.path.join('Project_Images','football.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (750,750) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('logo4.jpg')
    img.paste(paste_img, (150, 3075), mask = paste_img)
    img = img.save('football.jpg')# finally pastes the image that has been opened, resized, converted on to  
        #the border 
       
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    '''Basketball-Sillothe'''
        
    paste_img = Image.open(os.path.join('Project_Images','basketball.png'))# opens the image that is going to be inserted on the border
    paste_img = paste_img.resize( (700,700) )#resizes the img so that it fits perfectly on the border
    paste_img = paste_img.convert("RGBA")#converts the pixels in the img to RGBA
            
    img = Image.open('football.jpg')
    img.paste(paste_img, (9450, 3075), mask = paste_img)# finally pastes the image that has been opened, resized, converted on to  
        #the border 
    img = Image.save(os.path.join('finalpicture.jpg'))#saves the image, So that the user can look at the final product
        
        

    
main()#delete's all the unuseful files