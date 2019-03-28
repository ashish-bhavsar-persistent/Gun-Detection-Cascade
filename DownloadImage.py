import time
from threading import Thread
import urllib.request
import cv2
import numpy as np
import os
import uuid
import threading


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

    except Exception as e:
        print(e)


def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00445351'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    if not os.path.exists('neg'):
        os.makedirs('neg')
    activeCount = 0
    for i in neg_image_urls.split('\n'):
        t = Thread(target=sleeper, args=(i,))
        t.start()
        if threading.active_count() > 150:
            time.sleep(20)


def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) +"/"+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(e)


def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+"/"+img+"\n"
                with open("bg.txt","a") as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type + "/" + img + " 1 0 0 50 50\n"
                with open("info.dat", "a") as f:
                    f.write(line)
create_pos_n_neg()
# find_uglies()
# store_raw_images()