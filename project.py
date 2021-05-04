
import os
import json

"""
index will lead from terms to documents that contain the terms and frequency of
the terms in each document. An example is below.
"""
index = {
 }
stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''


"""
This function displays the menu as follows
    1. Indexing
    3. Exit
It then prompts the user for a valid input.
Input: None
Output: a valid integer
"""
def printMenu():
    print("Menu: \nPlease enter 1 for Indexing and 3 to Exit \n 1.Indexing \n 3.Exit")
    option = int(input("your option : "))
    return option


"""
This function takes a text file as input and removes all stop words.
Input: text
Output: text with no stop words
"""
def stopWordRemoval(text):
    result  = " ".join([x for x in text.split() if x not in stopwords])
    return result

"""
This function takes a text file as input and removes all punctuations.
Input: text
Output: text with no punctuations
"""
def punctuationsRemoval(text):
    text = [''.join(c for c in listitem if c not in punctuations) for listitem in text]           
    return text
    

"""
This functions takes a clean text as argument,  and appends TermDocFreqFile
 with the list of terms, the  document in which they appear and their frequencies.
 termDocFreqFile format: 3 columns, values separated with space
    Term doc# freq
    Ontario 1 5
    years 1 1
    sugar 1 2

Input: cleanText, and document id
output: termDocFreqFile format: 3 columns, values seperated with space
"""
def appendTermDocFreq(docid, cleanText, termDocFreqFile): 
       
        for x in cleanText:
            for i in x :
                str_list = i.lower().split() 
                # gives set of unique words
                #print(str_list)
                unique_words = set(str_list)    
                for words in unique_words :
                    #print('Frequency of ', words , 'is :', str_list.count(words))
                    result_str= words+" "+str(docid)+" "+str(str_list.count(words))
                    termDocFreqFile.write(result_str)
                    termDocFreqFile.write('\n')



"""
This function reads termDocFreqFile line by line and append the global index
that go from terms as keys to list of documents that contain them with their frequencies as val.
Appending the index works as follows:
    - for line in termDocFreqFile,
        - if the term does not exist in index,
            add the term as key, the value will be a dictionary containg docid:freq as key:val in index
        - if the term already exists in index, append the val (which is a dictionary) with docid:freq
   input:  
       termDocFreqFile
   output:
       fill in the index structure global variable defined in top of the module.

   """
def genIndex(termDocFreqFile):
        dict_obj={}
        termDocFreqFile.seek(0)
        fl= termDocFreqFile.readlines() 
        pos=0
        for line in fl :
            #print (line)
            if pos > 0 :    
                if line != 'null' : 
                    word = line.split()[0] 
                    #print (word)
                    if word in index :
                        dict_obj[int(line.split()[1])]=int(line.split()[2])
                        index[word].update(dict_obj)   
                    else :
                        dict_obj[int(line.split()[1])]=int(line.split()[2])
                        index[word]=dict_obj 
            pos+=1           
        #print(index)   
        index_file=open("index.json", 'w')
        json.dump(index, index_file,indent=4)
        index_file.close()
                 
                        
             



"""
This function reads all the text files in the folder 'dataset', appends them to a list,
and returns the list.
Input: None
Output: a list if texts
"""
def readFolderContent():
    files = []
    file_list = os.listdir('dataset')
    for filename in sorted(file_list):
        with open('dataset' + '/' + filename, 'r',encoding='utf-8') as infile:
            files.append(infile.read())
    return files   
    

"""
This function creates necessary files needed in this project.
For more information about this function review the flowchart given in the instructions.
"""
def indexing():
    termDocFreqFile = open("TermDocFreq.txt", 'w+',encoding='utf-8')
    result_str= "Term doc# frequency\n"
    termDocFreqFile.write(result_str)
    stopWordsRemoved = []
    puncRemoved = []
    # readFolderContent is called to create a list of files.
    files = readFolderContent()
    id=1
    for file in files:
        stopWordsRemoved.append(stopWordRemoval(file))  # Call stopWordRemoval function to remove all stop words.
        #print(stopWordsRemoved)
        puncRemoved.append(punctuationsRemoval(stopWordsRemoved))  # Call punctuationsRemoval function to remove all punctuations
        #print(puncRemoved)
        appendTermDocFreq(id,puncRemoved, termDocFreqFile)  # Call appendTermDocFreq function to append to termDocFreqFile
        genIndex(termDocFreqFile)  # Call genIndex function to append to the global index file
        id+=1

def main():
    option=printMenu()
    if option == 1:
        indexing()
    elif option == 3:
        exit()
    else :
        print ("Invalid option!")    



if __name__ == "__main__":
       main()




