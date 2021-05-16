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

def grayscale_transportation_all_files(file_list_to_process, folder_path_to_process, folder_path_to_write_grayscale):

    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
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
    result_text = "Grayscale transformation was executed in " + str(whole_time) + " seconds for " + str(len(file_list_to_process)) + " images \n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def add_gaussian_noise_all_images(file_list_to_process, folder_path_to_process, folder_path_to_write_gauss_image, mean, variance):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_gauss_image + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape
        st_dev = math.sqrt(variance)
        gauss_noise = np.random.normal(mean, st_dev,(rows,cols))
        grayscale_image_to_process = grayscale_image_to_process + gauss_noise
        grayscale_image_to_process = grayscale_image_to_process.clip(0,255).astype(np.uint8)
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Adding the Gaussian Noise with mean: " + str(mean) + " and variance: " + str(variance) + " for " + str(len(file_list_to_process)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    

    
def add_salt_and_pepper_noise_all_images(file_list_to_process, folder_path_to_process, folder_path_to_write_salt_and_pepper_image, probability, salt_and_pepper_ratio):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_salt_and_pepper_image + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        rows, cols = grayscale_image_to_process.shape
        image_plus_noise = np.copy(grayscale_image_to_process)
        
        num_salt = np.ceil(probability * grayscale_image_to_process.size * salt_and_pepper_ratio)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in grayscale_image_to_process.shape]
        image_plus_noise[tuple(coords)] = 255
    

        num_pepper = np.ceil(probability * grayscale_image_to_process.size * (1. - salt_and_pepper_ratio))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in grayscale_image_to_process.shape]
        image_plus_noise[tuple(coords)] = 0
        image_plus_noise = image_plus_noise.clip(0,255).astype(np.uint8)

        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, image_plus_noise)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
    
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Adding the Salt and Pepper noise with probability: " + str(probability) + " and Salt:Pepper ratio: " + str(salt_and_pepper_ratio) + " for " + str(len(file_list_to_process)) + " images was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    
def unweigted_average_all_images_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_unweighted_average_by_OpenCV, dimension_x, dimension_y):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array = np.ones((int(dimension_x), int(dimension_y)))/np.sum(np.ones((int(dimension_x), int(dimension_y))))
    summary = 0.0
    
    rows_floor = math.floor(dimension_x/2)
    cols_floor = math.floor(dimension_y/2)
    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_unweighted_average_by_OpenCV + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        

        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)        
        rows, cols = grayscale_image_to_process_copied.shape
            
        
        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                for x in range (-1*rows_floor, rows_floor+1):
                    for y in range (-1*cols_floor, cols_floor+1):
                        summary += (mask_array[x+rows_floor][y+cols_floor]*grayscale_image_to_process_copied[i+x][j+y])
                grayscale_image_to_process[i][j] = round(summary)

                summary = 0.0
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
                
                
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Unweighted averaging for " + str(len(file_list_to_process)) + " images by Formula was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def unweigted_average_all_images_by_OpenCV(file_list_to_process, folder_path_to_process, folder_path_to_write_unweighted_average_by_formula, dimension_x, dimension_y):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array = np.ones([int(dimension_x), int(dimension_y)],np.float32)/(dimension_x*dimension_y)


    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_unweighted_average_by_formula + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
            
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)
        to_write = cv2.filter2D(grayscale_image_to_process_copied, -1, mask_array)
    
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, to_write)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")

    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Unweighted averaging for " + str(len(file_list_to_process)) + " images by OpenCV was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    
def weigted_average_all_images_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_weighted_average_by_formula, dimension_x, dimension_y):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array = np.ones((int(dimension_x), int(dimension_y)))
    summary = 0.0
    
    rows_floor = math.floor(dimension_x/2)
    cols_floor = math.floor(dimension_y/2)
    mask_array[rows_floor][cols_floor] *= 2
    
    mask_array /= np.sum(mask_array)
    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_weighted_average_by_formula + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        

        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)        
        rows, cols = grayscale_image_to_process_copied.shape
            
        
        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                for x in range (-1*rows_floor, rows_floor+1):
                    for y in range (-1*cols_floor, cols_floor+1):
                        summary += (mask_array[x+rows_floor][y+cols_floor]*grayscale_image_to_process_copied[i+x][j+y])
                grayscale_image_to_process[i][j] = round(summary)

                summary = 0.0
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
                
                
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Weighted averaging for " + str(len(file_list_to_process)) + " images by Formula was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def weigted_average_all_images_by_OpenCV(file_list_to_process, folder_path_to_process, folder_path_to_write_weighted_average_by_OpenCV, dimension_x, dimension_y):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array = np.ones([int(dimension_x), int(dimension_y)],np.float32)
    x_center = math.floor(dimension_x/2)
    y_center = math.floor(dimension_y/2)
    
    mask_array[x_center][y_center] *= 2
    mask_array /= np.sum(mask_array)


    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_weighted_average_by_OpenCV + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
            
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)
        to_write = cv2.filter2D(grayscale_image_to_process_copied, -1, mask_array)
    
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, to_write)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")

    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Weighted averaging for " + str(len(file_list_to_process)) + " images by OpenCV was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()
    
def Gaussian_average_all_images_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_Gaussian_average_by_formula, dimension_x, dimension_y, sigma):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array = np.zeros([int(dimension_x), int(dimension_y)],np.float32)
    
    summary = 0.0
    weight_summary = 0.0  
    
    rows_floor = math.floor(dimension_x/2)
    cols_floor = math.floor(dimension_y/2)
    constant = 1/(2*math.pow(sigma, 2)*math.pi)
        
    for x in range(-1*rows_floor, rows_floor+1):
        for y in range(-1*cols_floor, cols_floor+1):
            to_pow = -1*((math.pow(x, 2))+(math.pow(y, 2)))/(2*(math.pow(sigma, 2)))
            mask_array[x+rows_floor][y+cols_floor] = constant*math.exp(to_pow)
            if (x != y):
                mask_array[y+cols_floor][x+rows_floor] = mask_array[x+rows_floor][y+cols_floor]
                summary += 2*mask_array[x+rows_floor][y+cols_floor]
            else:
                summary += mask_array[x+rows_floor][y+cols_floor]
    
    for x in range(0, len(mask_array)):
        for y in range(0, len(mask_array[x])):
            mask_array[x][y] /= summary
            weight_summary += mask_array[x][y]

    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_Gaussian_average_by_formula + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        

        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)        
        rows, cols = grayscale_image_to_process_copied.shape
            
        
        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                for x in range (-1*rows_floor, rows_floor+1):
                    for y in range (-1*cols_floor, cols_floor+1):
                        summary += (mask_array[x+rows_floor][y+cols_floor]*grayscale_image_to_process_copied[i+x][j+y])
                grayscale_image_to_process[i][j] = round(summary)

                summary = 0.0
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
                
                
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Gaussian_averaging with sigma=" + str(sigma) + " for "  + str(len(file_list_to_process)) + " images by Formula was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

    
def Gaussian_average_all_images_by_OpenCV(file_list_to_process, folder_path_to_process, folder_path_to_write_Gaussian_average_by_OpenCV, dimension_x, dimension_y, sigma):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    
    mask_array = np.zeros([int(dimension_x), int(dimension_y)],np.float32)
    
    summary = 0.0
    weight_summary = 0.0
    
    x_center = math.floor(dimension_x/2)
    y_center = math.floor(dimension_y/2)
    constant = 1/(2*math.pow(sigma, 2)*math.pi)
        
    for x in range(-1*x_center, x_center+1):
        for y in range(-1*y_center, y_center+1):
            to_pow = -1*((math.pow(x, 2))+(math.pow(y, 2)))/(2*(math.pow(sigma, 2)))
            mask_array[x+x_center][y+y_center] = constant*math.exp(to_pow)
            if (x != y):
                mask_array[y+y_center][x+x_center] = mask_array[x+x_center][y+y_center]
                summary += 2*mask_array[x+x_center][y+y_center]
            else:
                summary += mask_array[x+x_center][y+y_center]
    
    for x in range(0, len(mask_array)):
        for y in range(0, len(mask_array[x])):
            mask_array[x][y] /= summary
            weight_summary += mask_array[x][y]   


    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_Gaussian_average_by_OpenCV + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
            
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)
        to_write = cv2.filter2D(grayscale_image_to_process_copied, -1, mask_array)
    
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, to_write)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")

    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Gaussian_averaging with sigma=" + str(sigma) + " for "  + str(len(file_list_to_process)) + " images by OpenCV was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def median_filtering_all_images_by_OpenCV(file_list_to_process, folder_path_to_process, folder_path_to_write_median_filtering_by_OpenCV, dimension):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)

    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_median_filtering_by_OpenCV + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
            
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)
        to_write = cv2.medianBlur(grayscale_image_to_process_copied, dimension)
    
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, to_write)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")

    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Median filtering with " + str(dimension) + " to " + str(dimension) + " kernel for " + str(len(file_list_to_process)) + " images by OpenCV was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def median_filtering_all_images_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_weighted_average_by_formula, dimension_x, dimension_y):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    summary = []
    
    rows_floor = math.floor(dimension_x/2)
    cols_floor = math.floor(dimension_y/2)
    center_of_one_d_array =math.floor((dimension_x*dimension_y)/2)
    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_weighted_average_by_formula + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        

        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)        
        rows, cols = grayscale_image_to_process_copied.shape
            
        
        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                for x in range (-1*rows_floor, rows_floor+1):
                    for y in range (-1*cols_floor, cols_floor+1):
                        summary.append(grayscale_image_to_process_copied[i+x][j+y])
                summary.sort()
                grayscale_image_to_process[i][j] = summary[center_of_one_d_array]
                summary = []
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
                
                
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "Median filtering with " + str(dimension_x) + " to " + str(dimension_y) + " kernel for " + str(len(file_list_to_process)) + " images by Formula was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def Sobel_filtering_all_images_by_OpenCV(file_list_to_process, folder_path_to_process, folder_path_to_write_Sobel_filtering_by_OpenCV):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)

    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_Sobel_filtering_by_OpenCV + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
            
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process)
        grayscale_image_to_process_copied = grayscale_image_to_process_copied.astype(np.float32)
        sobel_x = cv2.Sobel(grayscale_image_to_process_copied,cv2.CV_32F,1,0,ksize=3)
        sobel_x = np.absolute(sobel_x).clip(0,255).astype(np.float32)
        sobel_y = cv2.Sobel(grayscale_image_to_process_copied,cv2.CV_32F,0,1,ksize=3)
        sobel_y = np.absolute(sobel_y).clip(0,255).astype(np.float32)
        

        for i in range(0, len(grayscale_image_to_process_copied)):
            for j in range(0, len(grayscale_image_to_process_copied[0])):
                grayscale_image_to_process_copied[i][j] = sobel_x[i][j] + sobel_y[i][j]
        grayscale_image_to_process_copied[i][j].clip(0,255).astype(np.uint8)
        to_write = grayscale_image_to_process_copied
        
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, to_write)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
        
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "3x3 Sobel filtering for " + str(len(file_list_to_process)) + " images by OpenCV was executed in " + str(whole_time) + " seconds\n"
    print(result_text)
    file_results_log.write(result_text)
    file_results_log.close()
    file_log.write(result_text)
    file_log.close()

def Sobel_filtering_all_images_by_formula(file_list_to_process, folder_path_to_process, folder_path_to_write_Sobel_filtering_by_formula):
    start_time = time.process_time()
    file_results_log = open("ResultslogFile.txt","a+")
    file_log = open("logFile.txt","a+")

    if len(file_list_to_process) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    mask_array_sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    mask_array_sobel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    
    rows_floor = math.floor(3/2)
    cols_floor = math.floor(3/2)
    
    summary_x = 0
    summary_y = 0
    
    
    for image_to_process in file_list_to_process:
        file_to_read = folder_path_to_process + os.path.sep + image_to_process
        file_to_write = folder_path_to_write_Sobel_filtering_by_formula + os.path.sep + image_to_process
        grayscale_image_to_process = cv2.imread(file_to_read, cv2.IMREAD_GRAYSCALE)
        
        
        grayscale_image_to_process_copied = np.copy(grayscale_image_to_process).astype(np.float32)
        rows, cols = grayscale_image_to_process_copied.shape
        grayscale_image_to_process_copied_x_to_fin = np.copy(grayscale_image_to_process).astype(np.float32)
        grayscale_image_to_process_copied_y_to_fin = np.copy(grayscale_image_to_process).astype(np.float32)

        for i in range (0, rows):
            for j in range (0, cols):
                grayscale_image_to_process_copied_x_to_fin[i][j] = grayscale_image_to_process_copied_x_to_fin[i][j] = grayscale_image_to_process_copied[i][j]

        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                summary_x += (mask_array_sobel_x[0][0]*grayscale_image_to_process_copied[i-1][j-1])
                summary_x += (mask_array_sobel_x[0][1]*grayscale_image_to_process_copied[i-1][j])
                summary_x += (mask_array_sobel_x[0][2]*grayscale_image_to_process_copied[i-1][j+1])
                summary_x += (mask_array_sobel_x[2][0]*grayscale_image_to_process_copied[i+1][j-1])
                summary_x += (mask_array_sobel_x[2][1]*grayscale_image_to_process_copied[i+1][j])
                summary_x += (mask_array_sobel_x[2][2]*grayscale_image_to_process_copied[i+1][j+1])
                summary_y += (mask_array_sobel_y[0][0]*grayscale_image_to_process_copied[i-1][j-1])
                summary_y += (mask_array_sobel_y[1][0]*grayscale_image_to_process_copied[i][j-1])
                summary_y += (mask_array_sobel_y[2][0]*grayscale_image_to_process_copied[i+1][j-1])
                summary_y += (mask_array_sobel_y[0][2]*grayscale_image_to_process_copied[i-1][j+1])
                summary_y += (mask_array_sobel_y[1][2]*grayscale_image_to_process_copied[i][j+1])
                summary_y += (mask_array_sobel_y[2][2]*grayscale_image_to_process_copied[i+1][j+1])
                
                grayscale_image_to_process_copied_x_to_fin[i][j] = abs(summary_x)
                if grayscale_image_to_process_copied_x_to_fin[i][j] > 255:
                    #grayscale_image_to_process_copied[i][j] %= 256
                    grayscale_image_to_process_copied_x_to_fin[i][j] = 255
                grayscale_image_to_process_copied_y_to_fin[i][j] = abs(summary_y)
                if grayscale_image_to_process_copied_y_to_fin[i][j] > 255:
                    #grayscale_image_to_process_copied[i][j] %= 256
                    grayscale_image_to_process_copied_y_to_fin[i][j] = 255
                
                summary_x = 0
                summary_y = 0
        
        for i in range (rows_floor, rows-rows_floor):
            for j in range (cols_floor, cols-cols_floor):
                grayscale_image_to_process_copied[i][j] = grayscale_image_to_process_copied_x_to_fin[i][j] + grayscale_image_to_process_copied_y_to_fin[i][j]
                if grayscale_image_to_process_copied[i][j] > 255:
                    #grayscale_image_to_process_copied[i][j] %= 256
                    grayscale_image_to_process_copied[i][j] = 255
   
        print(file_to_read + " is processed")
        file_log.write(file_to_read + " is processed\n")
        cv2.imwrite(file_to_write, grayscale_image_to_process_copied)
        print(file_to_write + " is written")
        file_log.write(file_to_write + " is written\n")
                
                
    stop_time = time.process_time()
    whole_time = stop_time-start_time
    result_text = "3x3 Sobel filtering for " + str(len(file_list_to_process)) + " images by Formula was executed in " + str(whole_time) + " seconds\n"
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

    folder_path_to_write_gauss_image = folder_path + "resultsOfProcessing" + os.path.sep + "GaussianNoised"
    
    if not os.path.exists(folder_path_to_write_gauss_image):
        os.makedirs(folder_path_to_write_gauss_image)
        
    folder_path_to_write_salt_and_pepper_image = folder_path + "resultsOfProcessing" + os.path.sep + "SaltAndPepperNoised"
    
    if not os.path.exists(folder_path_to_write_salt_and_pepper_image):
        os.makedirs(folder_path_to_write_salt_and_pepper_image)
        
    folder_path_to_write_unweighted_average_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "UnweightedAverageByFormula"
    
    if not os.path.exists(folder_path_to_write_unweighted_average_by_formula):
        os.makedirs(folder_path_to_write_unweighted_average_by_formula)

    folder_path_to_write_unweighted_average_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "UnweightedAverageByOpenCV"
    
    if not os.path.exists(folder_path_to_write_unweighted_average_by_OpenCV):
        os.makedirs(folder_path_to_write_unweighted_average_by_OpenCV)

    folder_path_to_write_weighted_average_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "WeightedAverageByFormula"
    
    if not os.path.exists(folder_path_to_write_weighted_average_by_formula):
        os.makedirs(folder_path_to_write_weighted_average_by_formula)
        
    folder_path_to_write_weighted_average_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "WeightedAverageByOpenCV"
    
    if not os.path.exists(folder_path_to_write_weighted_average_by_OpenCV):
        os.makedirs(folder_path_to_write_weighted_average_by_OpenCV)
    
    folder_path_to_write_Gaussian_average_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "GaussianAverageByFormula"

    if not os.path.exists(folder_path_to_write_Gaussian_average_by_formula):
        os.makedirs(folder_path_to_write_Gaussian_average_by_formula)
        
    folder_path_to_write_Gaussian_average_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "GaussianAverageByOpenCV"

    if not os.path.exists(folder_path_to_write_Gaussian_average_by_OpenCV):
        os.makedirs(folder_path_to_write_Gaussian_average_by_OpenCV)       
        
    folder_path_to_write_median_filtering_3x3_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "MedianFiltering3x3ByOpenCV"

    if not os.path.exists(folder_path_to_write_median_filtering_3x3_by_OpenCV):
        os.makedirs(folder_path_to_write_median_filtering_3x3_by_OpenCV)
        
    folder_path_to_write_median_filtering_5x5_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "MedianFiltering5x5ByOpenCV"

    if not os.path.exists(folder_path_to_write_median_filtering_5x5_by_OpenCV):
        os.makedirs(folder_path_to_write_median_filtering_5x5_by_OpenCV) 

    folder_path_to_write_median_filtering_3x3_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "MedianFiltering3x3ByFormula"

    if not os.path.exists(folder_path_to_write_median_filtering_3x3_by_formula):
        os.makedirs(folder_path_to_write_median_filtering_3x3_by_formula)
        
    folder_path_to_write_median_filtering_5x5_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "MedianFiltering5x5ByFormula"

    if not os.path.exists(folder_path_to_write_median_filtering_5x5_by_formula):
        os.makedirs(folder_path_to_write_median_filtering_5x5_by_formula)         

    folder_path_to_write_Sobel_filtering_by_OpenCV = folder_path + "resultsOfProcessing" + os.path.sep + "SobelFilteringByOpenCV"

    if not os.path.exists(folder_path_to_write_Sobel_filtering_by_OpenCV):
        os.makedirs(folder_path_to_write_Sobel_filtering_by_OpenCV)

    folder_path_to_write_Sobel_filtering_by_formula = folder_path + "resultsOfProcessing" + os.path.sep + "SobelFilteringByFormula"

    if not os.path.exists(folder_path_to_write_Sobel_filtering_by_formula):
        os.makedirs(folder_path_to_write_Sobel_filtering_by_formula)         

    image_files_list = file_list_to_process(folder_path_to_process)

    grayscale_transportation_all_files(image_files_list, folder_path_to_process, folder_path_to_write_and_read_grayscale)
    add_gaussian_noise_all_images(image_files_list, folder_path_to_process, folder_path_to_write_gauss_image, 32, 16)
    add_salt_and_pepper_noise_all_images(image_files_list, folder_path_to_process, folder_path_to_write_salt_and_pepper_image, 0.10, 0.50)
    unweigted_average_all_images_by_OpenCV(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_unweighted_average_by_OpenCV, 5, 5)
    unweigted_average_all_images_by_formula(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_unweighted_average_by_formula, 5, 5)
    weigted_average_all_images_by_OpenCV(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_weighted_average_by_OpenCV, 5, 5)
    weigted_average_all_images_by_formula(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_weighted_average_by_formula, 5, 5)
    Gaussian_average_all_images_by_OpenCV(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_Gaussian_average_by_OpenCV, 5, 5, 16)
    Gaussian_average_all_images_by_formula(image_files_list, folder_path_to_write_gauss_image, folder_path_to_write_Gaussian_average_by_formula, 5, 5, 16)
    median_filtering_all_images_by_OpenCV(image_files_list, folder_path_to_write_salt_and_pepper_image, folder_path_to_write_median_filtering_3x3_by_OpenCV, 3)
    median_filtering_all_images_by_formula(image_files_list, folder_path_to_write_salt_and_pepper_image, folder_path_to_write_median_filtering_3x3_by_formula, 3, 3)
    median_filtering_all_images_by_OpenCV(image_files_list, folder_path_to_write_salt_and_pepper_image, folder_path_to_write_median_filtering_5x5_by_OpenCV, 5)
    median_filtering_all_images_by_formula(image_files_list, folder_path_to_write_salt_and_pepper_image, folder_path_to_write_median_filtering_5x5_by_formula, 5, 5)
    Sobel_filtering_all_images_by_OpenCV(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_Sobel_filtering_by_OpenCV)
    Sobel_filtering_all_images_by_formula(image_files_list, folder_path_to_write_and_read_grayscale, folder_path_to_write_Sobel_filtering_by_formula)
    

if __name__ == "__main__":
    main()