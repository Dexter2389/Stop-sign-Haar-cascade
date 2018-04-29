import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04096066"
    #neg_images_link = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03244388"
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1

    if not os.path.exists("neg"):
        os.mkdir("neg")

    for i in neg_image_urls.split('\n'):
        try:
            print(i + "  -  " + str(pic_num))
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg")

            resized_image = cv2.resize(img, (640,400))
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()
