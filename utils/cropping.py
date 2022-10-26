import torch
import os
from shutil import copyfile,rmtree

def cropping_images(image_class="car",force=false):
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
    cwd = os.getcwd()
    path = os.path.join(cwd, "frame")
    dirs = os.listdir(path)

    try:
        if os.path.exists(os.path.join(cwd,"runs")):
            if not force:
                yn = input("You've just done before. Do you want to remove 'runs' directory?\n(if not deleted, it will be reflected in the next result)\n(y/n)[n]: ")
                if yn.lower() == 'y':
                    rmtree(os.path.join(cwd,"runs"))
                    print("runs directory is just deleted!")
                else:
                    print("it will be remained")
            else:
                rmtree(os.path.join(cwd,"runs"))
                print("runs directory is just deleted!")
    except OSError:
        print("Error: creating or removing directory")


    for d in dirs:
            imgs = []

            # Images
            for file in os.listdir(os.path.join(path,d)):
                imgs.append(os.path.join(path,d, file))

            # Images
            for img in imgs:

            # Inference
                    results = model(img)

            # Results
                    crops = results.crop(save=True)  # or .show(), .save(), .print(), .pandas(), etc.

    #copy croped image to summary directory

    summary = os.path.join(cwd, "croped_images")

    try:
        if not os.path.exists(summary):
            os.makedirs(summary)
        else:
            if not force:
                yn = input("Previous result directory exists. Do you want to remove? (y/n)[n]: ")
                if yn.lower() == 'y':
                    rmtree(summary)
                    os.makedirs(summary)
                    print("you've just deleted previous result!")
                else:
                    print("it wiil be remained")
            else:
                rmtree(summary)
                os.makedirs(summary)
                print("you've just deleted previous result!")

    except OSError:
        print("Error: Creating directory. " + summary)

    from_dirs = os.path.join(cwd,"runs","detect")

    idx = 0

    for directory in os.listdir(from_dirs):
        crop_dir = os.path.join(from_dirs, directory, "crops", image_class)

        if not os.path.exists(crop_dir):
            continue

        for name in os.listdir(crop_dir):
            print("copying "+os.path.join(crop_dir, name)+"...")
            copyfile(os.path.join(crop_dir, name), os.path.join(summary,str(idx).zfill(7))+".jpg")
            idx+=1
    print("done!")