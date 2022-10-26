import random
import os
from shutil import copyfile,rmtree

def sampling(n=5000,force=False):
    cwd = os.getcwd()
    path = os.path.join(cwd,'filtered')
    files = os.listdir(path)
    dest_path = os.path.join(cwd,'sampled')

    sampled_img = random.sample(files,n)

    try: 
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        else:
            if not force:
                yn = input("You've just done before. Do you want to remove 'sampled' directory?\n(if not deleted, it will be reflected in the next result)\n(y/n)[n]: ")
                if yn.lower() == 'y':
                    rmtree(dest_path)
                    os.makedirs(dest_path)
                    print("sampled directory is just deleted!")
                else:
                    print("it will be remained")
            else:
                rmtree(dest_path)
                os.makedirs(dest_path)
                print("sampled directory is just deleted!")
                
    except OSError:
        print("Error: creating or removing directory")
        
    for img in sampled_img:
        file_path = os.path.join(path, img)
        dest_file = os.path.join(dest_path, img)
        print("copying "+file_path+"...")
        copyfile(file_path, dest_file)

