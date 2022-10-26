from pytube import YouTube
import os

import cv2

def downloading(txt_list):
    for txt in txt_list:
        file_name = os.path.basename(txt)
        cls = file_name.split(".")[0]
        
        save_dir = os.path.join(file_dir,"src")
        
        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)

        print(f"Downloading videos is started")
        
        with open(txt, "r") as f:
            urllines = f.readlines()

            for idx ,url in enumerate(urllines):
                yt = YouTube(url)
                try:
                    print(f"Video {yt.title} is downloading...")
                    stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first() #가장 화질 좋도록
                    stream.download(save_dir)
                except:
                    print(">>> Something is wrong, stop downloading current file...\n")
                
                
            print(f"< Downloading videos is finished >\n")

    print("Done!")
