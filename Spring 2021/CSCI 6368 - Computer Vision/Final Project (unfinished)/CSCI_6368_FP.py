# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:05:48 2021

@author: mathe
"""

import tkinter as tk
from PIL import Image, ImageTk
import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import time
import queue
import threading as th
import sys
#For file commands
import os
import shutil
from tkinter import filedialog

class MainWindow():
    def __init__(self, window):
        self.window = window
        self.window.geometry("900x900")
        self.window.minsize(900, 900)
        
        self.frame_image_mode_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_image_mode_button.grid(sticky="W", row=0, column=0, padx=0, pady=0)
        
        self.frame_video_mode_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_video_mode_button.grid(sticky="W", row=0, column=1, padx=0, pady=0)
        
        self.frame_turn_on_the_camera_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_turn_on_the_camera_button.grid(sticky="W", row=0, column=2, padx=0, pady=0)
        
        self.frame_turn_off_the_camera_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_turn_off_the_camera_button.grid(sticky="W", row=0, column=3, padx=0, pady=0)
        
        self.frame_process_the_image_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_process_the_image_button.grid(sticky="W", row=0, column=4, padx=0, pady=0)
        
        self.frame_upload_new_image_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.frame_upload_new_image_button.grid(sticky="W", row=0, column=5, padx=0, pady=0)
        
        
        self.label_image_mode_button = tk.Button(master=self.frame_image_mode_button, text="Image Mode", relief=tk.RAISED, command = self.Image_mode_switcher)
        self.label_image_mode_button.pack(padx=0, pady=0)
        
        self.label_video_mode_button = tk.Button(master=self.frame_video_mode_button, text="Video Mode", relief=tk.RAISED, command = self.Video_mode_switcher)
        self.label_video_mode_button.pack(padx=0, pady=0)
        
        self.label_turn_on_the_camera_button = tk.Button(master=self.frame_turn_on_the_camera_button, text="Turn on the camera", relief=tk.RAISED, state=tk.DISABLED, command = self.Camera_turn_on)
        self.label_turn_on_the_camera_button.pack(padx=0, pady=0)
        
        self.label_turn_off_the_camera_button = tk.Button(master=self.frame_turn_off_the_camera_button, text="Turn off the camera", relief=tk.RAISED, state=tk.DISABLED, command = self.Camera_turn_off)
        self.label_turn_off_the_camera_button.pack(padx=0, pady=0)
        
        self.label_process_the_image_button = tk.Button(master=self.frame_process_the_image_button, text="Process the image", relief=tk.RAISED, state=tk.DISABLED, command = self.process_images)
        self.label_process_the_image_button.pack(padx=0, pady=0)
        
        self.label_upload_new_image_button = tk.Button(master=self.frame_upload_new_image_button, text="Upload new image", relief=tk.RAISED, state=tk.DISABLED, command = self.uploadIMG)
        self.label_upload_new_image_button.pack(padx=0, pady=0)
        
    
    def Image_mode_switcher(self):
        self.label_process_the_image_button['state'] = tk.NORMAL
        self.label_upload_new_image_button['state'] = tk.NORMAL
        self.label_turn_on_the_camera_button['state'] = tk.DISABLED
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=640, height=480)
        
        self.image2 = cv2.imread("black_img.jpg")
        self.image2 = cv2.cvtColor(self.image2, cv2.COLOR_BGR2RGB)
        self.image2 = Image.fromarray(self.image2)
        self.image2 = ImageTk.PhotoImage(image = self.image2)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image2)
        
        self.label_image_mode_button.configure(bg = "red", fg="white")
        self.label_video_mode_button.configure(fg = "black", bg="SystemButtonFace")
    
    def Video_mode_switcher(self):
        self.label_process_the_image_button['state'] = tk.DISABLED
        self.label_upload_new_image_button['state'] = tk.DISABLED
        self.label_turn_on_the_camera_button['state'] = tk.NORMAL
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        
        #Set Canvas
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=640, height=480)
        
        #Display Black Image
        self.image3 = cv2.imread("black_img.jpg")
        self.image3 = cv2.cvtColor(self.image3, cv2.COLOR_BGR2RGB)
        self.image3 = Image.fromarray(self.image3)
        self.image3 = ImageTk.PhotoImage(image = self.image3)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image3)
        
        self.label_video_mode_button.configure(bg = "red", fg="white")
        self.label_image_mode_button.configure(fg = "black", bg="SystemButtonFace")
        
    def uploadIMG(self):
        #Open File Menu
        self.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpeg files","*.jpg"),("xml files","*.xml"),("all files","*.*")))
        self.cv2_current_frame = cv2.imread(self.filename)
                
        frame = self.cv2_current_frame
        dim = (640,480)
        #Resize Image
        self.resizeIMG = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        
        self.cv2image_for_image_process = cv2.cvtColor(self.resizeIMG, cv2.COLOR_BGR2RGB)
        self.cv2image = cv2.cvtColor(self.resizeIMG, cv2.COLOR_BGR2RGBA)
        self.fixed_image = Image.fromarray(self.cv2image)  
        self.image4 = ImageTk.PhotoImage(image = self.fixed_image)
        
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=640, height=480)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image4)
        
        
        
        #IMPORTANT#
        #####Image that is displayed is saved under self.image4#####
    
    def Camera_turn_on(self):
#        self.cap = cv2.VideoCapture(0)
        self.label_turn_on_the_camera_button['state'] = tk.DISABLED
        self.label_turn_off_the_camera_button['state'] = tk.NORMAL
        
        thread = th.Thread(target=self.process_frames)
        thread.start()

    
    def Camera_turn_off(self):
        self.label_turn_off_the_camera_button['state'] = tk.DISABLED
        self.label_turn_on_the_camera_button['state'] = tk.NORMAL
        
        #Release Camera
        self.cap.release()
        cv2.destroyAllWindows()
        
        #Create Canvas
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=640, height=480)

        
        #Display Black Image
        self.image5 = cv2.imread("black_img.jpg")
        self.image5 = cv2.cvtColor(self.image5, cv2.COLOR_BGR2RGB)
        self.image5 = Image.fromarray(self.image5)
        self.image5 = ImageTk.PhotoImage(image = self.image5)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image5)
        
    def setBlankIMG(self):
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=640, height=480)
        self.image7 = cv2.imread("black_img.jpg")
        self.image7 = cv2.cvtColor(self.image7, cv2.COLOR_BGR2RGB)
        self.image7 = Image.fromarray(self.image7)
        self.image7 = ImageTk.PhotoImage(image = self.image7)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image7)
        
    def process_frames(self):
        ap = argparse.ArgumentParser()
#        ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
#        ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
        ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections")
        args = vars(ap.parse_args())
        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat","bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
        COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
        
        #Create path variables for config file and model file
        proto = "MobileNetSSD_deploy.prototxt"
        model = "MobileNetSSD_deploy.caffemodel"
        
        
        # load our serialized model from disk
        print("[INFO] loading model...")
        net = cv2.dnn.readNetFromCaffe(proto, model)
        # initialize the video stream, allow the cammera sensor to warmup,
        # and initialize the FPS counter
        print("[INFO] starting video stream...")
        
        self.cap = cv2.VideoCapture(0)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        print(self.width)
        print(self.height)
        
        self.interval = 20

        
        time.sleep(2.0)
        fps = FPS().start()
        
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.place(x=0, y=50, bordermode=tk.INSIDE, width=self.width, height=self.height)
        

        # loop over the frames from the video stream
        while True:
	       # grab the frame from the threaded video stream and resize it
	       # to have a maximum width of 400 pixels
          
           __, frame2 = self.cap.read()
           
           

           
           #Check if frame is empty
           if (frame2 is None):
              self.image6 = cv2.imread("black_img.jpg")
              self.image6 = cv2.cvtColor(self.image6, cv2.COLOR_BGR2RGB)
              self.image6 = Image.fromarray(self.image6)
              self.image6 = ImageTk.PhotoImage(image = self.image6)
              self.canvas.create_image(0, 0, anchor="nw", image=self.image6)

              
              
           self.frame = cv2.resize(frame2 , (640, 400))
           
	       # grab the frame dimensions and convert it to a blob
           (self.h, self.w) = self.frame.shape[:2]
           blob = cv2.dnn.blobFromImage(cv2.resize(self.frame, (300, 300)),
                                        0.007843, (300, 300), 127.5)
	       # pass the blob through the network and obtain the detections and
	       # predictions
           net.setInput(blob)
           detections = net.forward()
           	# loop over the detections
           for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
            confidence = detections[0, 0, i, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
            if confidence > args["confidence"]:
			# extract the index of the class label from the
			# `detections`, then compute the (x, y)-coordinates of
			# the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([self.w, self.h, self.w, self.h])
                (startX, startY, endX, endY) = box.astype("int")
			# draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
                
                cv2.rectangle(self.frame, (startX, startY), (endX, endY),
				COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(self.frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
           
            
           self.key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
           if cv2.waitKey(10) &  0xFF == ord("q"):
               break
          
#           self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
#           self.image = Image.fromarray(self.image)
#           self.image = ImageTk.PhotoImage(image = self.image)
           #image_frame = cv2.imshow("Live Feed", frame)

        #Check if Frame is empty, if yes then display black screen

           self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
           self.image = Image.fromarray(self.image)
           self.image = ImageTk.PhotoImage(image = self.image)
           self.canvas.create_image(0, 0, anchor="nw", image=self.image)

           

	# update the FPS counter
           fps.update()
           
    
    # stop the timer and display FPS information
        #self.update_image(frame)
        fps.stop()
        print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
        # do a bit of cleanup
        cv2.destroyAllWindows()
        
    def process_images(self):
        ap = argparse.ArgumentParser()
#        ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
#        ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
        ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections")
        args = vars(ap.parse_args())
        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat","bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
        COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
        
        #Create path variables for config file and model file
        proto = "MobileNetSSD_deploy.prototxt"
        model = "MobileNetSSD_deploy.caffemodel"
        
        
        # load our serialized model from disk
        print("[INFO] loading model...")
        net = cv2.dnn.readNetFromCaffe(proto, model)
        # initialize the video stream, allow the cammera sensor to warmup,
        # and initialize the FPS counter


           


        blob = cv2.dnn.blobFromImage(cv2.resize(self.cv2image_for_image_process, (300, 300)),
                                        0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()
        

        self.idxs = np.argsort(detections[0])[::-1][:5]


        for (i, idx) in enumerate(self.idxs):
            print(np.shape(detections))
            print(i)
            print(idx[0])
            if i == 0:
                text = "Label: {}, {:.2f}%".format(CLASSES[idx],
        			detections[0][idx] * 100)
                cv2.putText(self.cv2image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,
        			0.7, (0, 0, 255), 2)
        	# display the predicted label + associated probability to the
        	# console	
            print("[INFO] {}. label: {}, probability: {:.5}".format(i + 1,
        		CLASSES[idx], detections[0][idx]))
        # display the output image

        self.image = cv2.cvtColor(self.cv2image_for_image_process, cv2.COLOR_BGR2RGB)
        self.image = Image.fromarray(self.image)
        self.image = ImageTk.PhotoImage(image = self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)


    cv2.destroyAllWindows()

        
            
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()