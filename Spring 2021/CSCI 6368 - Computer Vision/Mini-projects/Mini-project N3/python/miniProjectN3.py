import os
import cv2
import numpy as np
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

def picture_writer(images_list, folder_path_to_process, folder_path_for_templates, folder_path_to_write, templates_list, no_of_levels, metric):
    
    
    file_log = open("logFile.txt","a+")

    if len(images_list) == 0:
        print("Error: There is no image.")
        file_log.write("Error: There is no image.\n")
        file_log.close()
        sys.exit(0)
    
    if len(templates_list) == 0:
        print("Error: There is no image template.")
        file_log.write("Error: There is no image template.\n")
        file_log.close()
        sys.exit(0)
    
    
    for array_num in range(len(images_list)):
        file_log = open("logFile.txt","a+")
        
        image = images_list[array_num]
        template = templates_list[array_num]
        image_name = folder_path_to_process + os.sep + image
        template_name = folder_path_for_templates + os.sep + template
        
        img = cv2.imread(image_name)
        templ = cv2.imread(template_name)
        templ_init = templ
        
        layer = img.copy()
        
        rows, cols, channel = img.shape
        rows_templ_init, cols_templ_init, channel_templ_init = templ.shape
        rows_templ, cols_templ, channel_templ = templ.shape
        
        black_image = np.zeros((rows,cols,3), dtype=np.uint8)
        
        image_to_concat = black_image
        image_to_concat_template = np.zeros((rows,cols_templ_init,3), dtype=np.uint8)
        result_to_write_template = image_to_concat_template
        result_to_write = img
        
        for i in range(no_of_levels):
        	
            result = cv2.matchTemplate(layer,templ,metric)
            
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            top_left = max_loc
            
            if metric is cv2.TM_SQDIFF_NORMED:
                top_left = min_loc
                metric_to_write = "\"Normalized Sum of Squared Differences\""
            elif metric is cv2.TM_CCORR_NORMED:
                top_left = max_loc
                metric_to_write = "\"Normalized Cross Correlation\""
            bottom_right = (top_left[0] + cols_templ, top_left[1] + rows_templ)
            
            layer2 = layer.copy()
            
            cv2.rectangle(layer, top_left, bottom_right, (0,0,0), 2)
            
            rows_layer, cols_layer, channel_layer = layer.shape
            
            image_to_concat = np.zeros((rows, cols_layer, 3), dtype=np.uint8)
            
            for r in range(rows_layer):
                for c in range(cols_layer):
                    image_to_concat[r][c] = layer[r][c]
            result_to_write = cv2.hconcat([result_to_write, image_to_concat])
            layer = cv2.pyrDown(layer2)
        for r_t in range(rows_templ_init):
            for c_t in range(cols_templ_init):
                image_to_concat_template[r_t][c_t] = templ_init[r_t][c_t]
                

        result_to_final_write=cv2.hconcat([result_to_write, result_to_write_template])
        write_name = folder_path_to_write + os.sep + "ResultWithTemplate_" + str(metric) + "_" + image
        
        result_text = write_name + " is written with detected images metric " + metric_to_write + " for " + str(no_of_levels) + " levels "
        print(result_text)
        file_log.write(result_text + '\n')
        cv2.imwrite(write_name, result_to_final_write)
    file_log.close()
        
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
        
    
    folder_path_to_process = folder_path + "imagesToProcess" + os.sep + "Images"
    if not os.path.exists(folder_path_to_process):
        print("Error: There is no '/imagesToProcess/Images' folder. The program is ended.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: There is no '/imagesToProcess' folder. The program is ended.\n")
        file_results_log.close()
        sys.exit(0)
    
    folder_path_for_templates = folder_path + "imagesToProcess" + os.sep + "Templates"

    folder_path_to_write = folder_path + "resultsOfProcessing"
    
    image_files_list = file_list_to_process(folder_path_to_process)
    
    template_files_list = file_list_to_process(folder_path_for_templates)
    
    picture_writer(image_files_list, folder_path_to_process, folder_path_for_templates, folder_path_to_write, template_files_list, 3, cv2.TM_SQDIFF_NORMED)
    picture_writer(image_files_list, folder_path_to_process, folder_path_for_templates, folder_path_to_write, template_files_list, 3, cv2.TM_CCORR_NORMED)

if __name__ == "__main__":
    main()