import numpy as np
import cv2
from shutil import copyfile,rmtree
import os

def filtering_image(image_size=(300,300),force=False):
    cwd = os.getcwd()
    path = os.path.join(cwd, "croped_images")
    dest_path = os.path.join(cwd,'filtered')
    files = os.listdir(path)

    height , weight = image_size

    print("Copying all images with a minimum resolution of "+str(height)+"x"+str(weight)+"or higher")

    try: 
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        else:
            if not force:    
                yn = input("You've just done before. Do you want to remove 'filtered' directory?\n(if not deleted, it will be reflected in the next result)\n(y/n)[n]: ")
                if yn.lower() == 'y':
                    rmtree(dest_path)
                    os.makedirs(dest_path)
                    print("filtered directory is just deleted!")
                else:
                    print("it will be remained")
            else:
                rmtree(dest_path)
                os.makedirs(dest_path)
                print("filtered directory is just deleted!")
                
    except OSError:
        print("Error: creating or removing directory")

        
    for f in files:
        file_path = os.path.join(path, f)
        dest_file = os.path.join(dest_path, f)
        
    

        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        h, w, c = img.shape
        
        if h >= 300 and w >= 300:
            print("copying "+file_path+"...")
            copyfile(file_path, dest_file)
            
