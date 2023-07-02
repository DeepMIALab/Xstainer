import PIL.Image
import os
from os import listdir
import glob
import natsort
from natsort import natsorted
import glob
from PIL import Image



#path = "/media/fatmanur/storage/rgba/"
#output = "/media/fatmanur/storage/rgb/"
#print(path)
#png_counter = 0

#for patch in natsorted(glob.glob(path+"*.png")):
    
    #print(patch)
    #rgba_image = PIL.Image.open(patch)
    #rgb_image = rgba_image.convert('RGB')
    #rgb_image.save(output)
    #png_counter+=1
    #print("png count", png_counter)
        
        
 
files = glob.glob('/truba/home/proj3/fatmanur/STITCHING/he2trichrome_liver/case3/preds_rgba/*.png')
DESTINATION_PATH = ('/truba/home/proj3/fatmanur/STITCHING/he2trichrome_liver/case3/preds/')  # The preferred path for saving the processed image

for f in files:
    
    rgba_image = PIL.Image.open(f)
    rgb_image = rgba_image.convert('RGB')

    base_filename = os.path.basename(f)
    title, ext = os.path.splitext(base_filename)
    final_filepath = os.path.join(DESTINATION_PATH, title + '_rgb_converted' + ext)

    rgb_image.save(final_filepath)        
    
print("the images converted successfully")    
    