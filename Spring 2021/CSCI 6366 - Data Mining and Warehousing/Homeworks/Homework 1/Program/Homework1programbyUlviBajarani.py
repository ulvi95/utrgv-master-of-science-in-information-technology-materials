import pandas as pd
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import Perceptron
from sklearn import metrics
import datetime

if __name__ == "__main__":
    
    folder_path = os.getcwd() + os.path.sep
    textfile_log = folder_path + "logFile.txt"


    if os.path.exists(textfile_log):
        file_results_log = open("logFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
        
        
    
    data_test_file = folder_path + "poker-hand-testing.data"
    data_train_file = folder_path + "poker-hand-training-true.data"
    
    
    if os.path.exists(data_test_file) and os.path.exists(data_train_file):
        print("Both testing and training data exist.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Both testing and training data exist.\n")
        file_results_log.close()
    else:
        print("Error: Either training data or testing data is missing.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: Either training data or testing data is missing.\n")
        file_results_log.close()
        sys.exit(0)
    
    
    data_train = pd.read_csv(data_train_file,header=None)
    data_test = pd.read_csv(data_test_file,header=None)
    
    file_results_log = open("logFile.txt","a+")
    
    
    for value in range(0, len(data_train)):
        if data_train[10][value] != 0:
            data_train[10][value] = 1
    
    for value in range(0, len(data_test)):
        if data_test[10][value] != 0:
            data_test[10][value] = 1
    
    
    col = [
    '#1 Card Suit', '#1 Card Rank',
    '#2 Card Suit', '#2 Card Rank',
    '#3 Card Suit', '#3 Card Rank',
    '#4 Card Suit', '#4 Card Rank',
    '#5 Card Suit', '#5 Card Rank',
    'Poker Hand',
    ]

    
    data_train.columns=col
    data_test.columns=col
    
    y_train=data_train['Poker Hand']
    y_test=data_test['Poker Hand']
    
    x_train=data_train.drop('Poker Hand',axis=1)
    x_test=data_test.drop('Poker Hand',axis=1)
    
    classifier_decision_tree = DecisionTreeClassifier(criterion='entropy')
    classifier_decision_tree = classifier_decision_tree.fit(x_train, y_train)
    y_pred_decision_tree = classifier_decision_tree.predict(x_test)
    
    decision_tree_accuracy_score = round(metrics.accuracy_score(y_test, y_pred_decision_tree), 3)
    print("Accuracy of Decision tree is:", decision_tree_accuracy_score)
    file_results_log.write("Accuracy of Decision tree is: " + str(decision_tree_accuracy_score) + "\n")

    
    AdaBoost_with_15_perceptron_accuracy_score = 0

    while AdaBoost_with_15_perceptron_accuracy_score == 0:
        try:
            classifier_adaBoost_Perceptron = AdaBoostClassifier(base_estimator=Perceptron(), n_estimators=15, algorithm='SAMME')
            classifier_adaBoost_Perceptron = classifier_adaBoost_Perceptron.fit(x_train, y_train)
            y_pred_AdaBoost = classifier_adaBoost_Perceptron.predict(x_test)
            AdaBoost_with_15_perceptron_accuracy_score = round(metrics.accuracy_score(y_test, y_pred_AdaBoost), 3)
        except:
            print("Let me reclassify AdaBoost again")
            file_results_log.write("Let me reclassify AdaBoost again.\n")
            
    print("Accuracy of AdaBoost with 15 perceptrons:", AdaBoost_with_15_perceptron_accuracy_score)
    file_results_log.write("Accuracy of AdaBoost with 15 perceptrons: " + str(AdaBoost_with_15_perceptron_accuracy_score) + "\n")
    file_results_log.close()
    
    names = ['Decision Tree', 'AdaBoost with 15 perceptrons']
    values = [decision_tree_accuracy_score, AdaBoost_with_15_perceptron_accuracy_score]
    
    
    plt.figure(figsize=(6, 6))
    plt.bar(names, values, color=['red', 'green'])
    plt.ylim(0, 1)
    plt.ylabel("Classification accuracy (fraction of correct classifications)")
    for index, value in enumerate(values):
        plt.text(index, value, str(value), fontsize=20)
    plt.suptitle('Comparison between Decision Tree and AdaBoost with 15 perceptrons')
    plt.savefig('comparision.png')
    plt.show()
