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
        
def face_extract_and_creator(image_files_list, folder_path_to_process):
    total_images_list = []
    total_faces_details = []
    processed_faces_list = []
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    for image in image_files_list:
        image_path = folder_path_to_process + os.sep + image
        image_to_add = cv2.imread(image_path)
        image_to_add = cv2.cvtColor(image_to_add, cv2.COLOR_BGR2GRAY)
        total_images_list.append(image_to_add)
    for gray_image in total_images_list:
        face = faceCascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
        total_faces_details.append(face)
    for gray_face in range(len(total_faces_details)):
        if len(total_faces_details[gray_face]) != 0:
            x = int(total_faces_details[gray_face][0][0])
            y = int(total_faces_details[gray_face][0][1])
            w = int(total_faces_details[gray_face][0][2])
            h = int(total_faces_details[gray_face][0][3])
            crop_face = total_images_list[gray_face][y:y+h, x:x+w]
            processed_faces_list.append(crop_face)
        else:
            crop_face = total_images_list[gray_face]
            processed_faces_list.append(crop_face)
    for processed_face in range(len(processed_faces_list)):
        processed_faces_list[processed_face] = cv2.resize(processed_faces_list[processed_face], (125, 150))
    for processed_face in range(len(processed_faces_list)):
        processed_faces_list[processed_face] = np.array(processed_faces_list[processed_face]).flatten()

    return processed_faces_list

def mean_image_writer_and_returner(processed_faces_list, folder_path_to_write_results):
    
    processed_faces_list_vectors = processed_faces_list.copy()
    
    sum_vec = np.add.reduce(processed_faces_list_vectors) / len(processed_faces_list_vectors)
    
    folder_path_to_write_result = folder_path_to_write_results + os.sep + "mean_image.jpg"
    plt.imsave(folder_path_to_write_result, sum_vec.reshape(150,125), cmap='gray')
    return sum_vec;

def image_writer_and_returner(image_list, folder_path_to_write_results, subname):
    
    for i in range(len(image_list)):
        folder_path_to_write_result = folder_path_to_write_results + os.sep + str(i+1) + subname + '.jpg'
        plt.imsave(folder_path_to_write_result, image_list[i].reshape(150,125), cmap='gray')
        


def processed_images_returner(processed_faces_list):
    
    processed_faces_list_vectors = processed_faces_list.copy()
    
    sum_vec = np.add.reduce(processed_faces_list_vectors) / len(processed_faces_list_vectors)
    
    for vector in range(len(processed_faces_list_vectors)):
        processed_faces_list_vectors[vector] = np.subtract(processed_faces_list_vectors[vector], sum_vec)
    
    
    '''
    for image in range(len(image_files_list)):
        folder_path_to_write_result = folder_path_to_write_results + os.sep + "frame_" + image_files_list[image]
        plt.imsave(folder_path_to_write_result, processed_faces_list_vectors[image].reshape(150,125), cmap='gray')
    '''
    
    return processed_faces_list_vectors;


def covariance_matrix_returner(processed_faces_list_vectors):
    return np.cov(processed_faces_list_vectors)/len(processed_faces_list_vectors[0])

def eigen_values_and_eigen_vectors_returner(covariance_matrix):
    return np.linalg.eig(covariance_matrix);

def write_restored_image_from_images(processed_faces_list_vectors, eigen_vectors_of_covariance_matrix_sorted, mean_image, number_of_first_eigenvectors):
    weight = np.dot(np.transpose(processed_faces_list_vectors), np.transpose(eigen_vectors_of_covariance_matrix_sorted[:number_of_first_eigenvectors]))
    projected_face = np.transpose(np.dot(weight, eigen_vectors_of_covariance_matrix_sorted[:number_of_first_eigenvectors]))
    final_faces = []
    for image in range(len(processed_faces_list_vectors)):
        final_faces.append(projected_face[image]+mean_image)
    return final_faces;

def main():
#if __name__ == "__main__":
    folder_path = os.path.dirname(os.getcwd()) + os.path.sep
    textfile_log = os.getcwd() + os.path.sep + "logFile.txt"

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
    
    
    folder_path_to_write_results = folder_path + "resultsOfProcessing"
    folder_path_to_write_results_grayscale_images = folder_path_to_write_results + os.sep + "grayscaleImages"
    folder_path_to_write_results_mean_image = folder_path_to_write_results + os.sep + "meanImage"
    folder_path_to_write_results_eigenfaces_unsorted = folder_path_to_write_results + os.sep + "eigenFaces_unsorted"
    folder_path_to_write_results_eigenfaces_sorted = folder_path_to_write_results + os.sep + "eigenFaces_sorted"
    folder_path_to_write_results_final_images = folder_path_to_write_results + os.sep + "finalImages"
    
    if not os.path.exists(folder_path_to_write_results):
        os.makedirs(folder_path_to_write_results)
        
    if not os.path.exists(folder_path_to_write_results_grayscale_images):
        os.makedirs(folder_path_to_write_results_grayscale_images)
        
    if not os.path.exists(folder_path_to_write_results_mean_image):
        os.makedirs(folder_path_to_write_results_mean_image)
        
    if not os.path.exists(folder_path_to_write_results_eigenfaces_unsorted):
        os.makedirs(folder_path_to_write_results_eigenfaces_unsorted)
               
    if not os.path.exists(folder_path_to_write_results_eigenfaces_sorted):
        os.makedirs(folder_path_to_write_results_eigenfaces_sorted)
        
    if not os.path.exists(folder_path_to_write_results_final_images):
        os.makedirs(folder_path_to_write_results_final_images)
    
    image_files_list = file_list_to_process(folder_path_to_process)
    processed_faces_list = face_extract_and_creator(image_files_list, folder_path_to_process)
    mean_image = mean_image_writer_and_returner(processed_faces_list, folder_path_to_write_results_mean_image)
    processed_faces_list_vectors = processed_images_returner(processed_faces_list)
    covariance_matrix = covariance_matrix_returner(processed_faces_list_vectors)
    eigen_values_of_covariance_matrix, eigen_vectors_of_covariance_matrix = eigen_values_and_eigen_vectors_returner(covariance_matrix)

    eigen_values_pairs = [(np.abs(eigen_values_of_covariance_matrix[i]), eigen_vectors_of_covariance_matrix[:,i], image_files_list[i]) for i in range(len(eigen_vectors_of_covariance_matrix))]
    
    eigen_values_pairs.sort(key=lambda x:x[0],reverse=True)
    
    eigen_faces_unsorted = []
    
    for vector in range(len(processed_faces_list_vectors)):
        covariance_matrix_point_to_add = np.dot(np.transpose(processed_faces_list_vectors), eigen_vectors_of_covariance_matrix[:,vector])
        covariance_matrix_point_to_add = covariance_matrix_point_to_add / np.linalg.norm(covariance_matrix_point_to_add)
        eigen_faces_unsorted.append(covariance_matrix_point_to_add)

    image_writer_and_returner(eigen_faces_unsorted, folder_path_to_write_results_eigenfaces_unsorted, "_unsorted_eigenface_")
    
    eigen_values_of_covariance_matrix_sorted = list(eigen_values_pairs[key][0] for key in range(len(eigen_values_pairs)))
    eigen_vectors_of_covariance_matrix_sorted = list(eigen_values_pairs[key][1] for key in range(len(eigen_values_pairs)))
    new_image_files_list = list(eigen_values_pairs[key][2] for key in range(len(eigen_values_pairs)))

    eigen_faces_vectors_sorted = []
    
    for vector in range(len(processed_faces_list_vectors)):
        covariance_matrix_point_to_add = np.dot(np.transpose(processed_faces_list_vectors), eigen_vectors_of_covariance_matrix_sorted[vector])
        covariance_matrix_point_to_add = covariance_matrix_point_to_add / np.linalg.norm(covariance_matrix_point_to_add)
        eigen_faces_vectors_sorted.append(covariance_matrix_point_to_add)
    image_writer_and_returner(eigen_faces_vectors_sorted, folder_path_to_write_results_eigenfaces_sorted, "_eigenface_")
    
    final_faces_to_output_all_vec = write_restored_image_from_images(processed_faces_list_vectors, eigen_vectors_of_covariance_matrix_sorted, mean_image, len(processed_faces_list_vectors))
    
    vectors_list = [10,\
                    int(round(len(eigen_vectors_of_covariance_matrix_sorted)*0.75)),\
                    int(round(len(eigen_vectors_of_covariance_matrix_sorted)*0.80)),\
                    int(round(len(eigen_vectors_of_covariance_matrix_sorted)*0.85)),\
                    int(round(len(eigen_vectors_of_covariance_matrix_sorted)*0.90))]
    for vector_number in vectors_list:
        final_string_to_output = "_final_face_" + str(vector_number) + "_vectors_"
        final_faces_to_output = write_restored_image_from_images(processed_faces_list_vectors, eigen_vectors_of_covariance_matrix_sorted, mean_image, vector_number)
        image_writer_and_returner(final_faces_to_output, folder_path_to_write_results_final_images, final_string_to_output)

    image_writer_and_returner(final_faces_to_output_all_vec, folder_path_to_write_results_final_images, "_final_face_all_vectors_")
    image_writer_and_returner(processed_faces_list, folder_path_to_write_results_grayscale_images, "_grayscale_images_")

    original_images = len(processed_faces_list_vectors) * len(processed_faces_list_vectors[0])
    
    for vector_number in vectors_list:
        final_images = len(mean_image) + (vector_number*len(eigen_faces_unsorted[0])) + (len(processed_faces_list) * (vector_number * 64))
        savings = (original_images - final_images)/8
        
        if savings > 0:
            to_write = "The saving in bytes for " + str(vector_number) + " vectors is " + str(savings) + " bytes"
            print(to_write)
            file_results_log = open("logFile.txt","a+")
            file_results_log.write(to_write + "\n")
            file_results_log.close()
        else:
            to_write = "The lose in bytes for " + str(vector_number) + " vectors is " + str(savings) + " bytes"
            print(to_write)
            file_results_log = open("logFile.txt","a+")
            file_results_log.write(to_write + "\n")
            file_results_log.close()
        
if __name__ == "__main__":
    main()
