#!/usr/bin/python
# -*- coding: utf-8 -*-

# for the reutilisability ode the code, open cv provides  multiples classifiers, in order to not duplicate the code we will create a generic #class.

import cv2
# + d’autres imports
# list of open cv classifier used 
TRAINSET_FACE_FRONTAL = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"
TRAINSET_FACE_PROFILE = "/usr/share/opencv/haarcascades/haarcascade_profileface.xml"
TRAINSET_BODY_FULL = "/usr/share/opencv/haarcascades/haarcascade_fullbody.xml"
# Parameters of image size
DOWNSCALE = 1.1  # ratio applied to the image it must be >1

MAX_SIZE = 800 # taille maximale de l'image en pixels

class OpenCVGenericDetection:
    def __init__(self, image_path, archive_folder = "/tmp/", debug = False):
#constructor

     """ init
     @image_path :path of the image on the disk
     @archive_folder : archieve folder
     @debug : if true display images on a widows 
     """
         logging.info("Image : {0}".format(image_path))
         self.image_path = image_path
         self.archive_folder = archive_folder
         self.debug = debug
         self.items = []
         self.items_frames = []
         # initialise  a classifier
         self.set_classifier()
         # in order to groupping image we will use  a unique prefix 
         self.images_prefix = "{0}_{1}_".
         format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"), self.__class__)
         # charge an image in a frame
         # a frame in open a cv is an image object in memort, it is easy to manipluate frames in on open cv instead of loading images 
         self.frame = cv2.imread(image_path)
         logging.info("Image resolution : '{0}x{1}'".format(self.frame.shape[0], self.frame.shape[1]))

         # verify if the image is "big" if it is the case we calculate the ratio to reduce it
         ratio = 1
         if self.frame.shape[1] > MAX_SIZE or self.frame.shape[0] > MAX_SIZE:
             if self.frame.shape[1] / MAX_SIZE > self.frame.shape[0] / MAX_SIZE:
                 ratio = float(self.frame.shape[1])/ MAX_SIZE
             else:
                 ratio = float(self.frame.shape[0])/ MAX_SIZE
         # If the image is "big" we change the size
         if ratio != 1:
             newsize = (int(self.frame.shape[1]/ratio),int(self.frame.shape[0]/ratio))
             logging.info("Redimensionnement de l'imageen : {0}".format(newsize))
             self.frame = cv2.resize(self.frame,newsize)
             # Affichage de l'image originale
         if self.debug:
         
             cv2.imshow("preview", self.frame)
             cv2.waitKey()
""" 	Classifier choice """ 
    def set_classifier(self):

        self.classifier = None
""" 	Visage detection """ 
    def find_items(self):
" find the items (what we want te detect in our case is a visage) in a frame items is a list containing the coordinate of the face in format(x, y, h, w) """
"""Exemple :
[[ 483 137 47 47]
[ 357 152 46 46]
...
[ 126 167 51 51]]
"""
        logging.info("look for items...")
# apply classifier to detect items (faces)
        items = self.classifier. detectMultiScale(self.frame, scaleFactor = DOWNSCALE)
        logging.info("Nombre d'items : '{0}'".format(len(items)))
        logging.info("Items = {0}".format(items))
        self.items = ites
