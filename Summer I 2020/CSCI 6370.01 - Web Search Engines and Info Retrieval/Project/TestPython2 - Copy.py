# Group Name: NoviceMastersSearchFinders

# Members:
# Ulvi Bajarani. SID 20539914 (Captain)
# Raul Martinez. SID 20317695
# Nicole San Miguel SID 10294500

# To install Pip or Pip3, download https://bootstrap.pypa.io/get-pip.py and open it.
# To install the BeautifulSoup, type either pip install beautifulsoup4 or pip3 install beautifulsoup4 in the command line.

# All required imports
from bs4 import BeautifulSoup # Parser import
import re # regex module
from os import path, walk # to scan the directory
import os
from zipfile import ZipFile # to work with a zip file

# List of stop words
stop_words = ["ourselves", "hers", "between", "yourself", \
    "but", "again", "there", "about", "once", "during", "out", \
    "very", "having", "with", "they", "own", "an", "be", "some", \
    "for", "do", "its", "yours", "such", "into", "of", "most", \
    "itself", "other", "off", "is", "s", "am", "or", "who", \
    "as", "from", "him", "each", "the", "themselves", "until", \
     "below", "are", "we", "these", "your", "his", "through", \
    "don", "nor", "me", "were", "her", "more", "himself", \
    "this", "down", "should", "our", "their", "while", "above", \
    "both", "up", "to", "ours", "had", "she", "all", "no", \
    "when", "at", "any", "before", "them", "same", "and", \
    "been", "have", "in", "will", "on", "does", "yourselves", \
    "then", "that", "because", "what", "over", "why", "so", "can", \
    "did", "not", "now", "under", "he", "you", "herself", "has", \
    "just", "where", "too", "only", "myself", "which", "those", \
    "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", \
    "against", "a", "by", "doing", "it", "how", "further", "was", \
    "here", "than", "b", "e", "c", "d", "f", "g", "h", "i", "j", "k", \
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
    "rhf"]

#To Check if there are any .html to analyze
HTMLExistion = False;


InitialDirectory = os.getcwd() #Initial directory where the operation occurs
FinalResult = {} #The dictionary to keep the results

if path.exists("Jan.zip"): #check if file Jan.zip extsts.
            #In that case, the file will be extracted
    with ZipFile('Jan.zip', mode='r') as toExtractZip:
        toExtractZip.extractall()
            
    print("Jan.zip exists. I have extracted it")
    
else:
    print("Jan.zip does not exist. Let me continue to search")
# the start of the scanning
for dirname, dirs, files in walk(InitialDirectory):
    for FileName in files:
        if FileName.endswith('.html'): #check if file ends with.
            HTMLExistion = True
        #create the file path as one name
            filepath = path.join(dirname, FileName)
        #creating a new entry in the dictionary. 
            FinalResult[filepath] = {
                'words' : []
                }
        
        #The parsing of HTML files. It also deletes the doubles in a key.
            for token in BeautifulSoup(open(filepath), 'lxml').get_text().lower().split():
                if not token in stop_words and re.match(r'[^\W\d]*$', token) and not token in FinalResult[filepath]['words']:
                    FinalResult[filepath]['words'].append(token)
        
#The beginning of output screen
if HTMLExistion == True:
    print("Now the search begins:")
    WordToSearch = input("enter a search key=> ") #Input sending value
    Check = WordToSearch.split() #Spliting all words, Required to the while loop
    found = 0 #Found cases. Required to avoid the errors in the end of the loop

    while len(Check) != 0: #If the input is not empty.
        TotalKeys = len(FinalResult.keys()) #the total number of keys
        for key in FinalResult:
            for words in FinalResult[key]:
                TotalKeys -= 1 #If the key is started to be analyzed, then it is reduced by 1.
                TestList = FinalResult[key][words] #create the list of words in the key to analyze.
                if WordToSearch in TestList: #search process. If it is found.
                        print("found a match: " + key)
                        found = 1
                if TotalKeys == 0 and found == 0: # If it is not found
                        print("no match")
        # Going back to the initial status of the program
        found = 0
        WordToSearch = input("enter a search key=> ")
        Check = WordToSearch.split()
#The end of the loop
    print("Bye")
    input("Press any key to end...") # To remain in the screen
else:
    print("There is no .html")
    input("Press any key to end...")