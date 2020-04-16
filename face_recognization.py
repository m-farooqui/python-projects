#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:01:50 2020

@author: mawais
"""

import face_recognition
import docopt
from sklearn import svm
import os

def face_recognize(dir, test):
    
    
    
    
    encodings = []
    names = []
    
    if dir[-1] != '/' :
        dir += '/'
    train_dir = os.listdir(dir)
    
    for person in train_dir:
        pix = os.listdir(dir + person)
        
    for person_img in pix:
        
        face = face_recognition.load_image_file(
            dir + person + "/" + person_img)
        face_bounding_boxes = face_recognition.face_locations(face)
        
    if len(face_bounding_boxes) == 1:
        face_enc = face_recognition.face_encodings(face)[0]
        encodings.append(face_enc)
        names.append(person)
        
    else:
        print(person + "/" + person_img + "can't be used for training")
        
clf = svm.SVC(gamma = 'scale')
clf.fit(encodings, names)

test_image = face_recognition.load_image_file(test)

face_locations = face_recognition.face_locations(test_image)
no = len(face_locations)
print("Number of faces detected: ", no)

print(" Found: ")
for i in range(no):
    test_image_enc = face_recognition.face_encodings(test_image)[i]
    name = clf.predict([test_image_enc])
    print(*name)
    
def main():
    args = docopt.docopt(__doc__)
    train_dir = args["--train_dir"]
    test_image = args["--test_image"]
    face_recognize(train_dir, test_image)
    
if __name__ =="__main__":
    main()
    
      
    
