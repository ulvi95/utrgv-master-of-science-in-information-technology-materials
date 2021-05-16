# Group Name: NoviceMastersSearchFinders

# Members:
# Ulvi Bajarani. SID 20539914 (Captain)
# Raul Martinez. SID 20317695
# Nicole San Miguel SID 10294500

# To install Pip or Pip3, download https://bootstrap.pypa.io/get-pip.py and open it.
# To install the BeautifulSoup, type either pip install beautifulsoup4 or pip3 install beautifulsoup4 in the command line.

# All required imports
from urllib.request import urlopen

from bs4 import BeautifulSoup  # Parser import
import re  # regex module
from os import path, walk  # to scan the directory
import os
from zipfile import ZipFile  # to work with a zip file
import numpy as np
import PySimpleGUI as sg

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

# To Check if there are any .html to analyze
HTMLExistion = False

InitialDirectory = os.getcwd()  # Initial directory where the operation occurs
FinalResult = {}  # The dictionary to keep the results
Document = {}
allWords = []
InvertedIndex = {}
links = []
filepath = ""


def main():
    if path.exists("Jan.zip"):  # check if file Jan.zip exists.
        # In that case, the file will be extracted
        with ZipFile('Jan.zip', mode='r') as toExtractZip:
            toExtractZip.extractall()


    else:
        print("Jan.zip does not exist. Let me continue to search")
    # the start of the scanning

    for dirname, dirs, files in walk(InitialDirectory):
        for FileName in files:
            if FileName.endswith('.html'):  # check if file ends with.
                HTMLExistion = True
                # create the file path as one name
                filepath = path.join(dirname, FileName)
                # creating a new entry in the dictionary.
                FinalResult[FileName] = {
                    'words': []
                }
                """html = BeautifulSoup(open(filepath), 'lxml')
                links = []
                for link in html.find_all('a'):
                    links.append(link.get('href'))
                print(links)"""

                for token in BeautifulSoup(open(filepath), 'lxml').get_text().lower().split():  # The parsing of HTML files. It also deletes the doubles in a key.
                    if not token in stop_words and re.match(r'[^\W\d]*', token):
                        newtoken = re.sub("[^a-zA-Z]","",token)
                        if newtoken != "":
                            FinalResult[FileName]['words'].append(newtoken)
                Document[FileName] = {
                    'id': FileName,
                    'docLength': FinalResult[FileName]['words'].__len__()
                }
                allWords.extend(FinalResult[FileName]['words'])

    for word in allWords:
        documentFrequency = 0
        pagesContainingWord = {}

        for doc in FinalResult.__iter__():
            if word in FinalResult[doc]['words']:
                documentFrequency += 1

        for doc in FinalResult.__iter__():
            if word in FinalResult[doc]['words']:
                PostingList = []
                i = 0
                for words in FinalResult[doc]['words']:
                    if words == word:
                        PostingList.append(i)
                    i += 1

                if documentFrequency == 0:
                    documentFrequency += 1
                pagesContainingWord[doc] = {
                    'wordFreq': FinalResult[doc]['words'].count(word),
                    "tf-idf": ((FinalResult[doc]['words'].count(word) / FinalResult[doc]['words'].__len__()) * np.log(FinalResult.__len__() / (documentFrequency))).__round__(5),
                    'positions': PostingList
                }

        if not word in InvertedIndex.__iter__():
            InvertedIndex[word] = {
                'documentFrequency': documentFrequency,
                'pagesContainingWord': pagesContainingWord
            }
    #print(InvertedIndex)
    queryRetriever()



def queryRetriever():
    layout = [[sg.Text('Enter the query'), sg.InputText()],
              [sg.Button('Ok')]]
    window = sg.Window('Search Webpages', layout, location=(40, 40), size=(400, 100))
    event, values = window.read()

    query = values[0]
    window.close()
    splitQuery = query.split()

    if 'exit' in splitQuery:
        window.close()
        return

    if re.match(r'\".*\"', query):
        if query.strip('"').split().__len__() == 1:
            querySearcherVectorModel(query.strip('"').split(),query)
        else:
            phrasalSearch(query.strip('"').split(),query)
        queryRetriever()
        return

    if not 'or' in splitQuery and not 'and' in splitQuery and not 'but' in splitQuery:
        querySearcherVectorModel(splitQuery,query)
    else:
        if len(splitQuery) % 2 == 0:
            queryRetriever()
        else:
            for i in range(0, len(splitQuery)):
                if i % 2 == 0 and (splitQuery[i] == 'or' or splitQuery[i] == 'and' or splitQuery[i] == 'but'):
                    queryRetriever()
            querySearcher(splitQuery,query)


def querySearcher(splitQuery,query):

    result = []
    if InvertedIndex.__contains__(splitQuery[0]):
        for fileNames in InvertedIndex[splitQuery[0]].get('pagesContainingWord'):
            result.append(fileNames)
    else:
        result = []


    i = 2
    while i < splitQuery.__len__():
        result2 = []
        if InvertedIndex.__contains__(splitQuery[i]):
            for fileNames in InvertedIndex[splitQuery[i]].get('pagesContainingWord'):
                result2.append(fileNames)
        else:
            result2 = []

        if splitQuery[i-1] == 'or':
            for file in result2:
                if not result.__contains__(file):
                    result.append(file)

        if splitQuery[i-1] == 'and':
            result3 = []
            for file in result2:
                if result.__contains__(file):
                    result3.append(file)
            result = result3

        if splitQuery[i-1] == 'but':
            for file in result2:
                if result.__contains__(file):
                    result.remove(file)
        i+=2
    string = ""
    if result.__len__() == 0:
        string = "No match found"
    else:
        for file in result:
            string += file + "\n"
    sg.popup_scrolled('Query -> ' + query + "\n\n" + "Result is as follow " + "\n\n" + string)

    queryRetriever()


def querySearcherVectorModel(splitQuery, query):

    string = ""
    for i in range(0, splitQuery.__len__()):
        if InvertedIndex.__contains__(splitQuery[i]):
            string += "word :" + splitQuery[i] + "\n"
            string += "Document frequency : " + str(InvertedIndex[splitQuery[i]].get('documentFrequency')) + "\n"
            for fileName in InvertedIndex[splitQuery[i]].get('pagesContainingWord'):
                var = InvertedIndex[splitQuery[i]].get('pagesContainingWord')[fileName]
                string += "\"" + fileName + "\"" + " word frequency : " + str(var.get('wordFreq')) + " tf-idf : " + str(var.get('tf-idf')) + " positions " + str(var.get('positions')) + "\n"
            string += "\n"
        else :
            string += "No match found for " + splitQuery[i] + "\n\n"

    sg.popup_scrolled('Query -> ' + query + "\n\n" + "Result is as follow " + "\n\n" + string)

    queryRetriever()


def phrasalSearch(splitQuery, query):
    length = splitQuery.__len__()
    finalResult = []
    for word in InvertedIndex.__iter__():
        if word.lower() == splitQuery[0].lower():
            for fileName in InvertedIndex[word].get('pagesContainingWord'):
                for position in InvertedIndex[word].get('pagesContainingWord')[fileName].get('positions').__iter__():
                    if finalResult.__contains__(fileName):
                        break
                    i = 1
                    pos = position
                    while i < length:
                        if pos+1 >= FinalResult[fileName]['words'].__len__():
                            break
                        if splitQuery[i].lower() == FinalResult[fileName]['words'][pos+1].lower():
                            if i == length - 1 :
                                finalResult.append(fileName)
                        else:
                            break
                        i += 1
                        pos += 1
    string = ""
    if finalResult.__len__() == 0:
        string = "No match found"
    else:
        for file in finalResult:
            string += file + "\n"
    sg.popup_scrolled('Query -> ' + query + "\n\n" + "Result is as follow " + "\n\n" + string)
    return


main()
