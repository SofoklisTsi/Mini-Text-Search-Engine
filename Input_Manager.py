import re

class Word_and_Path(object):
    # a struct that holds each word and the number of time that word appears
    def __init__(self, word: str, path: str):
        self.word = word
        self.path = path

def text_Files():
    # determines the number of text documents and makes a list of them
    paths = []
    no_of_texts = int(input("insert number of text files: "))
    for i in range(no_of_texts):
        paths.append(input("insert path: "))
    return paths
    
def read_Text():
    # opens the text documents and splits the words
    # pre-set input and prints are left as comments for debugging
    paths = text_Files()
#     f = open("words.txt")
    words_and_Paths = []
    for path in paths:
        f = open(path)
        for lineWord in f.readlines():
#             print("lineWords: " + lineWord) 
            for word in re.split(r' |[.]|,', lineWord):
                if(word != '\n' and word != ''):
                    words_and_Paths.append(Word_and_Path(word, path))
#                     print("\tAppended word: " + str(word) + " " + path) 
    return words_and_Paths

def read_Phrase():
    # reads the inserted phrase and seperates the keywords
    keywords = []
    phrase = input("insert phrase: ")
    for keyword in re.split(r' |[.]|,', phrase):
        if(keyword != '\n' and keyword != ''):
            keywords.append(keyword.casefold())
    return keywords
