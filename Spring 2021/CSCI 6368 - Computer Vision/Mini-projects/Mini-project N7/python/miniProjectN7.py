import os
import cv2
import numpy as np
import pandas as pd
import sys
import time
import math
import datetime
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

def predict_image(samples_to_predict):

    if len(samples_to_predict) != 0:
        available_classes = ['airplane', 'automobile', 'bird',
                             'cat', 'deer' ,'dog','frog',
                             'horse','ship','truck']
        print("\n\n\n\n")
        print("Available_classes are:")
        print()
        print(available_classes)
        print()
        print()
        
        samples_to_predict = np.array(samples_to_predict)
        
    
        
        predictions = model.predict(samples_to_predict)
        
        
        print("\n\n\n\nProbability Predictions are:")
        print()
        print(predictions)
    
        results = np.argmax(predictions, axis = 1)
        
        final_results = []
        
        for the_result in results:
            final_results.append(available_classes[the_result])
        print("\n\n\n\nFinal Classes are:")
        print()
        print(final_results)

def file_list_to_process(folder_path_to_process):
    return list((image_file for image_file in os.listdir(folder_path_to_process) \
    if (image_file.endswith('.' + 'jpg') 
    or image_file.endswith('.' + 'jpeg') \
    or image_file.endswith('.' + 'bmp') \
    or image_file.endswith('.' + 'gif') \
    or image_file.endswith('.' + 'png'))))

if __name__ == "__main__":


    filepath = './saved_model_for_project'
    
    model = load_model(filepath, compile = True)
    
    folder_path = os.path.dirname(os.getcwd()) + os.path.sep
    
    folder_path_to_write_image = folder_path + "resultsOfProcessing" + os.path.sep + "Images_written"
    
    if not os.path.exists(folder_path_to_write_image):
        os.makedirs(folder_path_to_write_image)
    
    folder_path_to_write_resized_image = folder_path + "resultsOfProcessing" + os.path.sep + "Resized_Images"
    
    if not os.path.exists(folder_path_to_write_resized_image):
        os.makedirs(folder_path_to_write_resized_image)
    
    folder_path_to_write_pyramid = folder_path + "resultsOfProcessing" + os.path.sep + "Pyramids"
    
    if not os.path.exists(folder_path_to_write_pyramid):
        os.makedirs(folder_path_to_write_pyramid)
    
    picture_value=0
    

    cap = cv2.VideoCapture(0)
    
    
    samples_to_predict = []
    
    while(True):
        
        place_to_write_image = folder_path_to_write_image + os.path.sep + 'frame' + str(picture_value) + '.png'
        place_to_write_image_resized = folder_path_to_write_resized_image + os.path.sep + 'frame' + str(picture_value) + '.png'
        place_to_write_image_pyramid = folder_path_to_write_pyramid + os.path.sep + 'frame' + str(picture_value) + '.png'
    
        
        ret, frame = cap.read()
        success, img2 = cap.read()
        imgOriginal = img2.copy()
    
        img_resized = cv2.resize(img2, (256,256))
        
        img_32x32 = img_resized.copy()
        
        for i in range(3):
            img_32x32 = cv2.pyrDown(img_32x32)
    
        cv2.imshow('frame',imgOriginal)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == 27:
            break
        elif k == ord('f'):
            images_list = file_list_to_process(folder_path_to_write_pyramid)
            samples_to_predict = []
            for image in images_list:
                image_path = folder_path_to_write_pyramid + os.sep + image
                image_to_add = cv2.imread(image_path)
                image_to_add = cv2.cvtColor(image_to_add, cv2.COLOR_BGR2RGB)
                samples_to_predict.append(image_to_add)
        elif k == ord('r'):
            cv2.imwrite(place_to_write_image, imgOriginal)
            cv2.imwrite(place_to_write_image_resized, img_resized)
            cv2.imwrite(place_to_write_image_pyramid, img_32x32)
            picture_value += 1
            samples_to_predict.append(img_32x32)
        elif k == ord('z'):
            picture_value = 0
            samples_to_predict = []
        elif k == ord('p'):
            predict_image(samples_to_predict)
    

    cap.release()
    cv2.destroyAllWindows()
    
    if len(samples_to_predict) != 0:
        predict_image(samples_to_predict)


