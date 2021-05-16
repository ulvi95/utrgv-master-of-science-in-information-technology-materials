import os
import cv2
import numpy as np
import pandas as pd
import sys
import time
import math
import datetime
import matplotlib.pyplot as plt



def file_list_to_process(folder_path_to_process):
    return list((image_file for image_file in os.listdir(folder_path_to_process) \
    if (image_file.endswith('.' + 'jpg') 
    or image_file.endswith('.' + 'jpeg') \
    or image_file.endswith('.' + 'bmp') \
    or image_file.endswith('.' + 'gif') \
    or image_file.endswith('.' + 'png'))))

def orb_list_to_process(folder_path_to_process_orb):
    return list((image_file for image_file in os.listdir(folder_path_to_process_orb) \
    if (image_file.endswith('.' + 'orb'))))

def get_class_names_from_descriptors(image_descriptions_list):
    class_descriptors = []
    if len(image_descriptions_list) != 0:
        for names in image_descriptions_list:
            class_descriptors.append(os.path.splitext(names)[0])  
    return class_descriptors

def get_class_values_from_descriptors(image_descriptions_list, folder_path_to_process_orb):
    class_descriptors_values = []
    if len(image_descriptions_list) != 0:
        for orb_names in image_descriptions_list:
            file_to_read = folder_path_to_process_orb + os.path.sep + orb_names
            to_write = pd.read_csv(file_to_read,header=None)
            class_descriptors_values.append(pd.DataFrame(to_write).to_numpy(copy=False, dtype=np.uint8))
    return class_descriptors_values

def calculateAndWriteDescriptors(image_files_list, folder_path_to_process, folder_path_to_write_orb):
    files = os.listdir(folder_path_to_write_orb)
    for file in files:
        os.remove(folder_path_to_write_orb+os.sep+file)
    if len(image_files_list) != 0:
        for images in image_files_list:
            file_to_read = folder_path_to_process + os.path.sep + images
            file_to_write = folder_path_to_write_orb + os.path.sep + os.path.splitext(images)[0] + '.orb'
            image_to_compute = cv2.imread(file_to_read)
            orb = cv2.ORB_create()
            kp, des = orb.detectAndCompute(image_to_compute,None)
            if os.path.exists(file_to_write):
                os.remove(file_to_write)
                pd.DataFrame(des).to_csv(file_to_write, header=None, index=None)
            else:
                pd.DataFrame(des).to_csv(file_to_write, header=None, index=None)
    else:
        pass

def findTheProperClass(image_to_check, class_descriptors_values):
    orb = cv2.ORB_create()
    kp2, des2 = orb.detectAndCompute(image_to_check, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    finalIndexValue = -1
    matchingElementsList = []
    matchingElementsListMean = []
    
    try:
        for descriptor in class_descriptors_values:
            matches = bf.match(des2, descriptor)
            
            matchList = []
            for m in matches:
                matchList.append(m.distance)
            matchingElementsList.append(len(matchList))
            matchingElementsListMean.append(np.mean(matchList))
            
    except:
        print('None')
    if len(matchingElementsList) !=0:
        if np.min(matchingElementsListMean) < 50:
            finalIndexValue = matchingElementsListMean.index(np.min(matchingElementsListMean))
        else:
            pass
    else:
        pass
    return finalIndexValue


def main():
    folder_path = os.path.dirname(os.getcwd()) + os.path.sep
    textfile_log = folder_path + "logFile.txt"

    if os.path.exists(textfile_log):
        file_results_log = open("logFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    folder_path_to_process = folder_path + "imagesToProcess"
    if not os.path.exists(folder_path_to_process):
        print("Error: There is no '/imagesToProcess' folder. The program is ended.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: There is no '/imagesToProcess' folder. The program is ended.\n")
        file_results_log.close()
        sys.exit(0)
    
    folder_path_to_write_orb = folder_path + "imageORBfiles"
    
    if not os.path.exists(folder_path_to_write_orb):
        os.makedirs(folder_path_to_write_orb)
    
    folder_path_to_write_results = folder_path + "resultsOfProcessing"
    
    if not os.path.exists(folder_path_to_write_results):
        os.makedirs(folder_path_to_write_results)
    
    image_files_list = file_list_to_process(folder_path_to_process)
    calculateAndWriteDescriptors(image_files_list, folder_path_to_process, folder_path_to_write_orb)
    image_descriptions_list = orb_list_to_process(folder_path_to_write_orb)
    class_descriptors = get_class_names_from_descriptors(image_descriptions_list)
    class_descriptors_values = get_class_values_from_descriptors(image_descriptions_list, folder_path_to_write_orb)

    cap = cv2.VideoCapture(0)
    
    picture_value=0
    picture_value_result=0
    
    while(True):
        
        success, img2 = cap.read()
        imgOriginal = img2.copy()
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img2 = img2.astype(np.uint8)
        
        ProperClass = findTheProperClass(img2, class_descriptors_values)
        

        if ProperClass != -1:
            cv2.putText(imgOriginal, class_descriptors[ProperClass], (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        place_to_write_image_result = folder_path_to_write_results + os.path.sep + 'frame' + str(picture_value_result) + '.png'
        place_to_write_image_to_process = folder_path_to_process + os.path.sep + 'frame' + str(picture_value) + '.png'
        
        cv2.imshow('Original Image', imgOriginal)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == 27:
            break
        elif k == ord('n'):
            cv2.imwrite(place_to_write_image_to_process, imgOriginal)
            picture_value += 1
        elif k == ord('v'):
            cv2.imwrite(place_to_write_image_result, imgOriginal)
            picture_value_result += 1
        elif k == ord('r'):            
            image_files_list = file_list_to_process(folder_path_to_process)
            calculateAndWriteDescriptors(image_files_list, folder_path_to_process, folder_path_to_write_orb)
            image_descriptions_list = orb_list_to_process(folder_path_to_write_orb)
            class_descriptors = get_class_names_from_descriptors(image_descriptions_list)
            class_descriptors_values = get_class_values_from_descriptors(image_descriptions_list, folder_path_to_write_orb)
            
    cv2.destroyAllWindows()
    cap.release()
    
            
if __name__ == "__main__":
    main()
