import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import os
import sys
import datetime


if __name__ == "__main__":
    folder_path = os.getcwd() + os.path.sep
    
    
    textfile_log = folder_path + "logFile.txt"
    most_frequent_items_list = folder_path + "mfis.txt"
    association_rules_list = folder_path + "ar.txt"
    top_10_association_rules = folder_path + "topar.txt"
    
    if os.path.exists(textfile_log):
        file_results_log = open("logFile.txt","a+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    else:
        file_results_log = open("logFile.txt","w+")
        file_results_log.write(str(datetime.datetime.now()) + "\n")
        file_results_log.close()
    
    if os.path.exists(most_frequent_items_list):
        most_frequent_items_list = open("mfis.txt","a+")
        most_frequent_items_list.write(str(datetime.datetime.now()) + "\n")
        most_frequent_items_list.close()
    else:
        most_frequent_items_list = open("mfis.txt","w+")
        most_frequent_items_list.write(str(datetime.datetime.now()) + "\n")
        most_frequent_items_list.close()
    
    if os.path.exists(association_rules_list):
        association_rules_list = open("ar.txt","a+")
        association_rules_list.write(str(datetime.datetime.now()) + "\n")
        association_rules_list.close()
    else:
        association_rules_list = open("ar.txt","w+")
        association_rules_list.write(str(datetime.datetime.now()) + "\n")
        association_rules_list.close()
    
    if os.path.exists(top_10_association_rules):
        top_10_association_rules = open("topar.txt","a+")
        top_10_association_rules.write(str(datetime.datetime.now()) + "\n")
        top_10_association_rules.close()
    else:
        top_10_association_rules = open("topar.txt","w+")
        top_10_association_rules.write(str(datetime.datetime.now()) + "\n")
        top_10_association_rules.close()
    
    data_test_file = folder_path + "house-votes-84.data"
    
    if os.path.exists(data_test_file):
        print("Data file exist.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Data file exists.\n")
        file_results_log.close()
    else:
        print("Error: Data file is missing.")
        file_results_log = open("logFile.txt","a+")
        file_results_log.write("Error: Data file is missing.\n")
        file_results_log.close()
        sys.exit(0)
    
    
    data_test_file_initial = pd.read_csv(data_test_file,header=None)
    
    column=["Class Name",
            "handicapped-infants",
            "water-project-cost-sharing",
            "adoption-of-the-budget-resolution",
            "physician-fee-freeze",
            "el-salvador-aid",
            "religious-groups-in-schools",
            "anti-satellite-test-ban",
            "aid-to-nicaraguan-contras",
            "mx-missile","immigration",
            "synfuels-corporation-cutback",
            "education-spending",
            "superfund-right-to-sue",
            "crime",
            "duty-free-exports",
            "export-administration-act-south-africa" ]
    
    data_test_file_initial.columns = column
    
    data_test_file_final = data_test_file_initial.copy()
    for col in column:
        data_test_file_final[col] = data_test_file_final[col].apply(lambda x: col + '=' + x)
    
    data_encoder = TransactionEncoder()
    data_to_process = data_encoder.fit(data_test_file_final.values).transform(data_test_file_final.values)
    
    binarized_data = pd.DataFrame(data_to_process, columns=data_encoder.columns_)
    
    most_frequent_itemsets = apriori(binarized_data, min_support=0.3, use_colnames=True)
    most_frequent_itemsets = most_frequent_itemsets.sort_values('support',  ascending=False, ignore_index=True)
    
    print("All itemsets where support>0.3 were generated successfully. The number of itemsets are equal to " + str(len(most_frequent_itemsets)))
    file_results_log = open("logFile.txt","a+")
    file_results_log.write("All itemsets where support>0.3 were generated successfully. The number of itemsets are equal to " + str(len(most_frequent_itemsets)) + "\n")
    file_results_log.close()
    
    print("All itemsets where support>0.3 are:\n")
    
    for itemset in range(0, len(most_frequent_itemsets)):
        most_frequent_items_list = open("mfis.txt","a+")
        print(str(most_frequent_itemsets.values[itemset][1])[10:-1] + " " + "| Support Value=" + str(most_frequent_itemsets.values[itemset][0]))
        most_frequent_items_list.write(str(most_frequent_itemsets.values[itemset][1])[10:-1] + " " + "| Support Value=" + str(most_frequent_itemsets.values[itemset][0]) + "\n")
        most_frequent_items_list.close()
    
    rules_by_confidence = association_rules(most_frequent_itemsets, metric="confidence", min_threshold=0.9)
    rules_by_confidence_sorted = rules_by_confidence.sort_values('confidence',  ascending=False, ignore_index=True)
    
    print("All association rules where confidence>0.9 were generated successfully. The number of association rules are equal to " + str(len(rules_by_confidence)) + "\n")
    file_results_log = open("logFile.txt","a+")
    file_results_log.write("All association rules where confidence>0.9 were generated successfully. The number of association rules are equal to " + str(len(rules_by_confidence)) + "\n")
    file_results_log.close()
    
    print("All association rules where confidence>0.9 are:\n")
    for rule in range(0, len(rules_by_confidence)):
        association_rules_list = open("ar.txt","a+")
        print(str(rules_by_confidence.values[rule][0])[10:-1] + " --> " + str(rules_by_confidence.values[rule][1])[10:-1] + " | Confidence: " + str(rules_by_confidence.values[rule][5]) + " | Support: " + str(rules_by_confidence.values[rule][4]) + " | Lift: " + str(rules_by_confidence.values[rule][6]))
        association_rules_list.write(str(rules_by_confidence.values[rule][0])[10:-1] + " --> " + str(rules_by_confidence.values[rule][1])[10:-1] + " | Confidence: " + str(rules_by_confidence.values[rule][5]) + " | Consequent Support: " + str(rules_by_confidence.values[rule][3]) + " | Support: " + str(rules_by_confidence.values[rule][4]) + " | Lift: " + str(rules_by_confidence.values[rule][6]) + "\n")
        association_rules_list.close()
    
    print("Top 10 association rules are:\n")
    for rule in range(0, 10):
        top_10_association_rules = open("topar.txt","a+")
        print(str(rules_by_confidence_sorted.values[rule][0])[10:-1] + " --> " + str(rules_by_confidence_sorted.values[rule][1])[10:-1] + " | Confidence: " + str(rules_by_confidence_sorted.values[rule][5]) + " | Lift: " + str(rules_by_confidence_sorted.values[rule][6]))
        top_10_association_rules.write(str(rules_by_confidence_sorted.values[rule][0])[10:-1] + " --> " + str(rules_by_confidence_sorted.values[rule][1])[10:-1] + " | Confidence: " + str(rules_by_confidence_sorted.values[rule][5]) + " | Consequent Support: " + str(rules_by_confidence_sorted.values[rule][3]) + " | Support: " + str(rules_by_confidence_sorted.values[rule][4]) + " | Lift: " + str(rules_by_confidence_sorted.values[rule][6]) + "\n")
        top_10_association_rules.close()
    
    print("The program ended successfully.")
    file_results_log = open("logFile.txt","a+")
    file_results_log.write("The program ended successfully.\n")
    file_results_log.close()