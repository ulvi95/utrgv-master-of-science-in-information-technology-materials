# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:56:42 2021

@author: mahmoud
"""
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#np.savetxt("kmeansdata.csv", X, delimiter=",")

def update_labels_and_mse(X_data, centroids):
    mse=0
    y_label=np.array(np.zeros(X_data.shape[0]))
    for indx, x in enumerate(X_data):
        #print('indx is:', indx)
        #print('x is:', x)
        #print('centroids are:', centroids)
        diff_2 =np.power((x - centroids), 2)
        #print('diff_2 is', diff_2)
        sum_diff = np.sum(diff_2, axis=1)
        #print('sum_diff is', sum_diff)
        cmin= np.min(sum_diff)
        cmin_index = np.argmin(sum_diff, axis=None)
        y_label[indx] = cmin_index
        #print('y_label', y_label[indx])
        mse += math.sqrt(cmin)
        #print('min index', cmin_index)
        #print('min', cmin)
    return (y_label,mse)

    
def update_centroids (X_data,y_label, old_centroids):
    new_centroids= np.zeros(old_centroids.shape)
    new_counts   = np.zeros(old_centroids.shape[0])
    # print('new counts is',new_counts)
    
    # merge 
    y_label=y_label[:, np.newaxis]
    X_data_labels = np.append(X_data, y_label, axis=1)
    # print(X_data_labels.shape)
    # print(X_data_labels)
    
    #
    for c in np.arange(len(new_counts)):
        # based on label pick centroids
        current_label_indexes = np.where(X_data_labels[:,2]==c)
        same_cluster_data=X_data_labels[current_label_indexes]
        #average and update centroid
        sum1 = np.sum(same_cluster_data, axis=0)
        sum1 /=len(same_cluster_data)
        sum1=np.nan_to_num(sum1, copy=True, nan=0.0)
        ncentroid= sum1[0:2]
        new_centroids[c]=ncentroid
    print('updated centroids is', new_centroids)
    return new_centroids

if __name__ == "__main__": 
    
    # X = pd.read_csv('kmeansdata.csv', names=('feature1', 'feature2'))   
    
    centers = [[2, 2], [8, 7], [3,7]]
    X, y =make_blobs(n_samples=90, n_features=2, centers=centers, cluster_std=0.8, center_box=(1, 10.0), shuffle=True, random_state=0)

    X = pd.DataFrame(data=X, columns=["feature1", "feature2"])
   
    #get min and max of data
    kmin = np.min(np.min(X,axis=0))  
    kmax = np.max(np.max(X,axis=0))
    
    # Create centroids
    centroids = np.random.uniform(low=kmin, high=kmax, size=(3,2))
    plt.plot(X["feature1"], X["feature2"], 'o', color='black');
    plt.plot(centroids[:,0], centroids[:,1], 'o', color='red')
    X_data =pd.DataFrame(X).to_numpy()
    y_label,old_mse  =update_labels_and_mse(X_data, centroids) 
    print('mse is', old_mse)
    new_mse = old_mse
    mse_diff_percentage = 10000
    n=0
    while (n < 10 and mse_diff_percentage > 10):
        print('iteration no: ', n)
        old_mse =new_mse
        # updat the centroids while the labels are fixed
        centroids =update_centroids (X_data,y_label, centroids)
    
        # Calc mse based on updated centroids 
        y_labels,new_mse =update_labels_and_mse(X_data, centroids) 
        print('mse is', new_mse)
        
        #one way to end the loop
        mse_diff_percentage= abs((new_mse - old_mse))
        print('mse_diff_percentage is', mse_diff_percentage)
        n= n+1
        
    plt.plot(X["feature1"], X["feature2"], 'o', color='yellow');
    plt.plot(centroids[:,0], centroids[:,1], 'o', color='blue')
else:
    print("Code is being imported into another module")
    