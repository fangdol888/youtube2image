
import os
import glob
import cv2

def extract_frame(file_dir ,file_name, sec=1000):
    
    filepath = os.path.join(file_dir,"src", file_name)
    video = cv2.VideoCapture(filepath) #'' 사이에 사용할 비디오 파일의 경로 및 이름을 넣어주도록 함
    
    if not video.isOpened():
        print("Could not Open :", filepath)
        exit(0)


    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("length :", length)
    print("width :", width)
    print("height :", height)
    print("fps :", fps)
    
    frame_dir = os.path.join(file_dir,"frame")
    frame_path = os.path.join(frame_dir, file_name[:-4])
    
    try:
        if not os.path.exists(frame_path):
            os.makedirs(frame_path)
        
    except OSError:
        print ('Error: Creating directory. ' +  frame_path)

    count = 0
    success, image = video.read()
    print("Read a new frame : ", success)
        
    while success:
            print('Saved frame number :', count)
            cv2.imwrite(frame_path + "/frame%d.jpg" % count, image)
            video.set(cv2.CAP_PROP_POS_MSEC,(count*sec)) #sec초 마다 추출
            success, image = video.read()
            print("Read a new frame : ", success)
            count += 1

    video.release()
    
def execute_extraction(file_dir):
    filepath = os.path.join(file_dir, "src")
    file_list = []

    for file in os.listdir(filepath):
        if file.endswith((".webm",".mp4")):
            file_list.append(file)

    for file in file_list:
        extract_frame(file_dir, file)