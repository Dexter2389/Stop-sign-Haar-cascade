import os
import cv2

def create_neg():
    for file_type in ["positives", "negatives"]:
        for img in os.listdir(file_type):
            if file_type == "negatives":
                line = file_type+"/"+img+"\n"
                with open("bg.txt", "a") as f:
                    f.write(line)
            elif file_type == 'positives':
                line = img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)

create_neg()
