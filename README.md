
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Word Processor
Python Word Processor useful for indexing and searching into a collection of documents

# DOCSTRING 
Fill in the docstring part at the beginning of the python module and also for each
function, by providing a description of the input, program functionality and output.
# USER INPUT
 A collection of text documents with .txt extension. This collection can be found in the
folder dataset on blackboard.
# INSTRUCTIONS

1.THE INDEXING MODULE :

The indexing module aims at generating an index for a collection of documents. It starts by
reading a collection of text documents, processing each of the documents content and extract its
terms and their frequencies. After processing all documents, a dictionary that serves as index is
created that goes from terms to list of documents containing the terms and their frequencies in
each of the documents containing the term. See the following page for a flowchart.

The following functions should be implemented:

-def printMenu():This function displays the following menu to the user. The user must select 1 for indexing
and 3 to exit. This function checks for valid/invalid input. If an invalid input is entered,
the function prompts the user again and prints an informative message. If the input is
valid, it is returned. Note: you will upgrade this function in milestone 2.
Menu:

Please enter 1 for indexing and 3 to exit

1.Indexing

3.Exit

def readFolderContent():

The code for this function is given. This function reads all the text files in the folder
dataset and appends them to a list. Each item in the list is the content of a text file in
the dataset.
 def indexing():
The indexing module aims at generating an index for a collection of documents. It starts
by reading a collection of text documents, processing each of the documents content and
extract its terms and their frequencies. After processing all documents, a dictionary that
serves as index is created that goes from terms to list of documents containing the terms
and their frequencies in each of the documents containing the term. See the flowchart
above for more information.

#def stopWordRemoval(text):This function takes a text as an argument, removes all the stop words from the text, and
returns the text. A list of stop words is provided for you in blackboard. For example,
words “the” and “on” are considered as stop words. Thus, they are removed from the
following input.
input: “The monkeys jump on the bed.”
output: “monkeys jump bed.”

def punctuationRemoval(text):This function takes a text as an argument, removes all the punctuations from the text, and
returns the text. Here is a list of punctuations you may use in your code.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def appendTermDocFreq(cleanText, termDocFreqFile):This functions takes a clean text as argument, and appends the file TermDocFreqFile
with the list of terms, the document in which they appear and their frequencies.
termDocFreqFile format: 3 columns, values separated with space
 Term doc# freq
 recipe 1 5
 sweet 1 1
 sugar 1 2
 
def genIndex(termDocFreqFile):This function reads termDocFreqFile line by line and appends the global index that goes
from terms as keys to the list of documents that contains them with their frequencies.
Appending the index works as follows:

for line in termDocFreqFile,
 if the term does not exist in index, add the term as key, the value will be a
dictionary containg docid:freq as key:val in index
 if the term already exists in index, append the val (which is a dictionary) with
 docid:freq 
