import time
from threading import Thread
import urllib.request
import cv2
import numpy as np
import os
import uuid
import  threading

def sleeper(i):
    print(i)
    try:
        print(i)
        pic_num = uuid.uuid1()
        print(pic_num)

        request = urllib.request.urlopen(i, timeout=50)
        with open("neg/" + str(pic_num) + ".jpg", 'wb') as f:
            f.write(request.read())
        # urllib.request.urlretrieve(i,'neg/'+str(pic_num)+'.jpg')
        img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite('neg/' + str(pic_num) + '.jpg', resized_image)
        pic_num += 1
    except Exception as e:
        print(e)
def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    if not os.path.exists('neg'):
        os.makedirs('neg')
    activeCount = 0
    for i in neg_image_urls.split('\n'):
        t = Thread(target=sleeper, args=(i,))
        t.start()
        if  threading.active_count()>150 :
            time.sleep(20)

store_raw_images()