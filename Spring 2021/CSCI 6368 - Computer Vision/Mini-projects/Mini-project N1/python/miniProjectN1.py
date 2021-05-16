import os
import cv2
import numpy as np
import sys
import time
import math
import datetime

def file_list_to_process(folder_path_to_process):
    return list((image_file for image_file in os.listdir(folder_path_to_process) \
    if (image_file.endswith('.' + 'jpg') 
    or image_file.endswith('.' + 'jpeg') \
    or image_file.endswith('.' + 'bmp') \
    or image_file.endswith('.' + 'gif') \
    or image_file.endswith('.' + 'png'))))

def random_list_processor(numberOfimages, file_list_to_process):
    file_log = open("logFile.txt","a+")
    randomNumbers = []
    
    if isinstance(numberOfimages, int) and numberOfimages > 0 and numberOfimages <= len(file_list_to_process):
        if numberOfimages != len(file_list_to_process):
            while len(randomNumbers) < numberOfimages:
                r = np.random.randint(0,numberOfimages)
                if r not in randomNumbers:
                    randomNumbers.append(r)
            randomNumbers.sort()
        else:
            randomNumbers = list(range(0, numberOfimages))
        print("The number of images equal to " + str(numberOfimages) + " is legal.")
        file_log.write("The number of images equal to " + str(numberOfimages) + " is legal.\n")
        file_log.close()
        return randomNumbers
    else:
        print("Error: Either the type of " + str(numberOfimages) + " is not integer. Or the value is lower or higher than the size of an array.")
        file_log.write("Error: Either the type of " + str(numberOfimages) + " is not integer. Or the value is lower or higher than the size of an array.\n")
        file_log.close()
        return -1

def grayscale_transportation_all_files(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):

    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)

    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process    

    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        bgr_image = cv2.imread(file_to_read)
        grayscale_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Grayscale transformation was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def threshold_by_LUT(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
        
    
    LookUpTable_for_threshold = []
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
    
    for value in range(256):
        if value > 128:
            LookUpTable_for_threshold.append(255)
        else:
            LookUpTable_for_threshold.append(0)

  
    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape  
        for r in range(rows):
            for c in range(cols):
                grayscale_image_to_process[r,c]=LookUpTable_for_threshold[grayscale_image_to_process[r][c]]
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Thresholding by LUT for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    
def threshold_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
        
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
    

    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape  
        for r in range(rows):
            for c in range(cols):
                if grayscale_image_to_process[r,c] > 128:
                    grayscale_image_to_process[r,c] = 255
                else:
                    grayscale_image_to_process[r,c] = 0
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Thresholding by formula for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def negative_by_LUT(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
    
    LookUpTable_for_negative = []
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
    
    for value in range(256):
        LookUpTable_for_negative.append(255-value)

   
    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape  
        for r in range(rows):
            for c in range(cols):
                grayscale_image_to_process[r,c]=LookUpTable_for_negative[grayscale_image_to_process[r][c]]
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Negative image process by LUT for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def negative_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
    
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
   
    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape  
        for r in range(rows):
            for c in range(cols):
                grayscale_image_to_process[r,c]=255-grayscale_image_to_process[r,c]
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
        
    
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Negative image process by formula for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    
def log_transform_by_LUT(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
    
    LookUpTable_for_log_transform = []
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
    
    for value in range(256):
        log_value_to_add = round(105.8*math.log10(1+value))
        LookUpTable_for_log_transform.append(log_value_to_add)

    
    
    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape  
        for r in range(rows):
            for c in range(cols):
                grayscale_image_to_process[r,c]=LookUpTable_for_log_transform[grayscale_image_to_process[r][c]]
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Log transform process by LUT for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def log_transform_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale, numberOfimages):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")
    
    if numberOfimages == -1:
        print("Error in the random generator.")
        file_log.write("Error in the random generator.\n")
        file_log.close()
        sys.exit(0)
    
    file_list_in_process = []
    
    if len(numberOfimages) != len(file_list_to_process):
        for value in numberOfimages:
            file_list_in_process.append(file_list_to_process[value])
    else:
        file_list_in_process = file_list_to_process
   
    for image_to_process in file_list_in_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_grayscale + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape

        for r in range(rows):
            for c in range(cols):
                grayscale_image_to_process[r,c]=round(105.8*math.log10(1+grayscale_image_to_process[r,c]))
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
        
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Log transform process by formula for " + str(len(numberOfimages)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def main():

    folder_path = os.path.dirname(os.getcwd()) + os.path.sep
    textfile_results_log = folder_path + "ResultslogFile.txt"
    textfile_log = folder_path + "logFile.txt"



    if os.path.exists(textfile_log):
        file_results_log = open("logFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
    if os.path.exists(textfile_results_log):
        file_results_log = open("ResultslogFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("ResultslogFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    
    folder_path_to_process = folder_path + "imagesToProcess"
    if not os.path.exists(folder_path_to_process):
        print("Error: There is no '/imagesToProcess' folder. The program is ended.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: There is no '/imagesToProcess' folder. The program is ended.\n")
        file_results_log.close()
        sys.exit(0)
    
    folder_path_to_write_and_read_grayscale = folder_path + "resultsOfProcessing" + os.path.sep + "grayscaleImages"
    
    if not os.path.exists(folder_path_to_write_and_read_grayscale):
        os.makedirs(folder_path_to_write_and_read_grayscale)
    
    folder_path_to_write_threshold_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingLUT"
    
    if not os.path.exists(folder_path_to_write_threshold_by_lut):
        os.makedirs(folder_path_to_write_threshold_by_lut)
    
    folder_path_to_write_threshold_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingFormula"
    
    if not os.path.exists(folder_path_to_write_threshold_by_formula):
        os.makedirs(folder_path_to_write_threshold_by_formula)

    folder_path_to_write_negative_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "negativeLUT"
    
    if not os.path.exists(folder_path_to_write_negative_by_lut):
        os.makedirs(folder_path_to_write_negative_by_lut)
        
    folder_path_to_write_negative_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "negativeFormula"
    
    if not os.path.exists(folder_path_to_write_negative_by_formula):
        os.makedirs(folder_path_to_write_negative_by_formula)
        
    folder_path_to_write_log_transform_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformLUT"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_lut):
        os.makedirs(folder_path_to_write_log_transform_by_lut)
        
    folder_path_to_write_log_transform_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformFormula"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_formula):
        os.makedirs(folder_path_to_write_log_transform_by_formula)

    
    image_files_list = file_list_to_process(folder_path_to_process)
    
    numberOfimages = random_list_processor(50, image_files_list)
    numberOfimages_one = random_list_processor(1, image_files_list)
    numberOfimages_ten = random_list_processor(10, image_files_list)
    numberOfimages_twenty = random_list_processor(20, image_files_list)
    numberOfimages_thirty = random_list_processor(30, image_files_list)
    
    
    
    grayscale_transportation_all_files(image_files_list, folder_path_to_process, folder_path_to_write_and_read_grayscale, numberOfimages)
    
    threshold_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_lut, numberOfimages)
    negative_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_lut, numberOfimages)
    log_transform_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_lut, numberOfimages)
    
    threshold_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_formula, numberOfimages)
    negative_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_formula, numberOfimages)
    log_transform_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_formula, numberOfimages)
    
    folder_path_to_write_threshold_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingLUTone"
    
    if not os.path.exists(folder_path_to_write_threshold_by_lut):
        os.makedirs(folder_path_to_write_threshold_by_lut)
    
    folder_path_to_write_threshold_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingFormulaone"
    
    if not os.path.exists(folder_path_to_write_threshold_by_formula):
        os.makedirs(folder_path_to_write_threshold_by_formula)

    folder_path_to_write_negative_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "negativeLUTone"
    
    if not os.path.exists(folder_path_to_write_negative_by_lut):
        os.makedirs(folder_path_to_write_negative_by_lut)
        
    folder_path_to_write_negative_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "negativeFormulaone"
    
    if not os.path.exists(folder_path_to_write_negative_by_formula):
        os.makedirs(folder_path_to_write_negative_by_formula)
        
    folder_path_to_write_log_transform_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformLUTone"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_lut):
        os.makedirs(folder_path_to_write_log_transform_by_lut)
        
    folder_path_to_write_log_transform_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformFormulaone"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_formula):
        os.makedirs(folder_path_to_write_log_transform_by_formula)
    
    
    threshold_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_lut, numberOfimages_one)
    negative_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_lut, numberOfimages_one)
    log_transform_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_lut, numberOfimages_one)
    
    threshold_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_formula, numberOfimages_one)
    negative_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_formula, numberOfimages_one)
    log_transform_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_formula, numberOfimages_one)
    
    folder_path_to_write_threshold_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingLUTten"
    
    if not os.path.exists(folder_path_to_write_threshold_by_lut):
        os.makedirs(folder_path_to_write_threshold_by_lut)
    
    folder_path_to_write_threshold_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingFormulaten"
    
    if not os.path.exists(folder_path_to_write_threshold_by_formula):
        os.makedirs(folder_path_to_write_threshold_by_formula)

    folder_path_to_write_negative_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "negativeLUTten"
    
    if not os.path.exists(folder_path_to_write_negative_by_lut):
        os.makedirs(folder_path_to_write_negative_by_lut)
        
    folder_path_to_write_negative_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "negativeFormulaten"
    
    if not os.path.exists(folder_path_to_write_negative_by_formula):
        os.makedirs(folder_path_to_write_negative_by_formula)
        
    folder_path_to_write_log_transform_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformLUTten"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_lut):
        os.makedirs(folder_path_to_write_log_transform_by_lut)
        
    folder_path_to_write_log_transform_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformFormulaten"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_formula):
        os.makedirs(folder_path_to_write_log_transform_by_formula)
    
    threshold_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_lut, numberOfimages_ten)
    negative_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_lut, numberOfimages_ten)
    log_transform_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_lut, numberOfimages_ten)
    
    threshold_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_formula, numberOfimages_ten)
    negative_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_formula, numberOfimages_ten)
    log_transform_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_formula, numberOfimages_ten)


    folder_path_to_write_threshold_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingLUTtwenty"
    
    if not os.path.exists(folder_path_to_write_threshold_by_lut):
        os.makedirs(folder_path_to_write_threshold_by_lut)
    
    folder_path_to_write_threshold_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingFormulatwenty"
    
    if not os.path.exists(folder_path_to_write_threshold_by_formula):
        os.makedirs(folder_path_to_write_threshold_by_formula)

    folder_path_to_write_negative_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "negativeLUTtwenty"
    
    if not os.path.exists(folder_path_to_write_negative_by_lut):
        os.makedirs(folder_path_to_write_negative_by_lut)
        
    folder_path_to_write_negative_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "negativeFormulatwenty"
    
    if not os.path.exists(folder_path_to_write_negative_by_formula):
        os.makedirs(folder_path_to_write_negative_by_formula)
        
    folder_path_to_write_log_transform_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformLUTtwenty"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_lut):
        os.makedirs(folder_path_to_write_log_transform_by_lut)
        
    folder_path_to_write_log_transform_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformFormulatwenty"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_formula):
        os.makedirs(folder_path_to_write_log_transform_by_formula)
    
    threshold_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_lut, numberOfimages_twenty)
    negative_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_lut, numberOfimages_twenty)
    log_transform_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_lut, numberOfimages_twenty)
    
    threshold_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_formula, numberOfimages_twenty)
    negative_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_formula, numberOfimages_twenty)
    log_transform_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_formula, numberOfimages_twenty)

    folder_path_to_write_threshold_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingLUTthirty"
    
    if not os.path.exists(folder_path_to_write_threshold_by_lut):
        os.makedirs(folder_path_to_write_threshold_by_lut)
    
    folder_path_to_write_threshold_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "thresholdingFormulathirty"
    
    if not os.path.exists(folder_path_to_write_threshold_by_formula):
        os.makedirs(folder_path_to_write_threshold_by_formula)

    folder_path_to_write_negative_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "negativeLUTthirty"
    
    if not os.path.exists(folder_path_to_write_negative_by_lut):
        os.makedirs(folder_path_to_write_negative_by_lut)
        
    folder_path_to_write_negative_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "negativeFormulathirty"
    
    if not os.path.exists(folder_path_to_write_negative_by_formula):
        os.makedirs(folder_path_to_write_negative_by_formula)
        
    folder_path_to_write_log_transform_by_lut = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformLUTthirty"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_lut):
        os.makedirs(folder_path_to_write_log_transform_by_lut)
        
    folder_path_to_write_log_transform_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "logTransformFormulathirty"
    
    if not os.path.exists(folder_path_to_write_log_transform_by_formula):
        os.makedirs(folder_path_to_write_log_transform_by_formula)

    
    threshold_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_lut, numberOfimages_thirty)
    negative_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_lut, numberOfimages_thirty)
    log_transform_by_LUT(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_lut, numberOfimages_thirty)
    
    threshold_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_threshold_by_formula, numberOfimages_thirty)
    negative_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_negative_by_formula, numberOfimages_thirty)
    log_transform_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_log_transform_by_formula, numberOfimages_thirty)

if __name__ == "__main__":
    main()