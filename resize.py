import os
import cv2

def resize_img():
    pic_num = 1
    for file_type in ['positives']:
        for img in os.listdir(file_type):
           
            if not os.path.exists("pos2"):
                os.mkdir("pos2")

            for i in file_type:
                try:
                    img = cv2.imread("positives/" + str(pic_num) + ".jpg")

                    resized_image = cv2.resize(img, (100,100))
                    cv2.imwrite("pos2/" + str(pic_num) + ".jpg", resized_image)
                    pic_num += 1

                except Exception as e:
                    print(str(pic_num) + str(e))

resize_img()
