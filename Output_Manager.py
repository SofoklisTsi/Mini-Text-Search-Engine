import Trie_Manager

class Path_Choice(object):
    # the final struct before the output
    def __init__(self, path: str):
        self.path = path
        self.number_Of_Words = 0
        self.counter = 0

class Word_And_Counter(object):
    # a secondary struct with words and counter
    def __init__(self, word: str, counter: int):
        self.word = word
        self.counter = counter
        
class Path_Info(object):
    # a struct for path info
    def __init__(self, path: str):
        self.path = path
        self.words_And_Counters = []

def find_Path_And_Counter(word: str, trieWords):
    # return the number of time that the word appears
    for trieWord in trieWords:
        if(trieWord.word == word):
            return trieWord.paths_And_Counters
    return -1
        
def reverse_Sort(trieWords):
    # reverse sorts the structure
    words = []
    temp_TrieWords = []
    for trieWord in trieWords:
        words.append(trieWord.word)
    words.sort(reverse=True)
    for word in words:
        temp_TrieWords.append(Trie_Manager.TrieWord(word,find_Path_And_Counter(word,trieWords)))
    return temp_TrieWords
        
def output_With_Numbers(trieWords):
    #calculates the fraction and the percentage of appearence and prints the result
    total_Number = 0
    for trieWord in trieWords:
        for path_And_Counter in trieWord.paths_And_Counters:
            total_Number += path_And_Counter.counter
    for trieWord in trieWords:
        total_Word_Counter = 0
        for path_And_Counter in trieWord.paths_And_Counters:
            total_Word_Counter += path_And_Counter.counter
        print(trieWord.word + " " + str(total_Word_Counter) + "/" + str(total_Number)
              + " " + str(100*total_Word_Counter/total_Number) + "%")

def create_Keywords_With_Info(keywords: [str], generatedWords: [Trie_Manager.TrieWord]):
    # creates a keyword list in the form of Trie_Manager.TrieWord
    keywords_With_Info = []
    for keyword in keywords:
        for word in generatedWords:
            if(word.word == keyword):
                keywords_With_Info.append(word)
    return keywords_With_Info
                      
def create_List_Of_Paths(keywords_With_Info: [Trie_Manager.TrieWord]):
    # creates the a list with all the available paths
    paths = []
    for keyword_With_Info in keywords_With_Info:
        for path_And_Counter in keyword_With_Info.paths_And_Counters:
            if path_And_Counter.path not in paths:
                paths.append(path_And_Counter.path)
    return paths
        
def create_Paths_Info(keywords_With_Info: [Trie_Manager.TrieWord]):
    # transforms the Trie_Manager.TrieWord type list into a Path_Info type list
    paths_Info = []
    paths = create_List_Of_Paths(keywords_With_Info)
    for path in paths:
        paths_Info.append(Path_Info(path))
    for path_Info in paths_Info:
        for keyword_With_Info in keywords_With_Info:
            path_Info.words_And_Counters.append(Word_And_Counter(keyword_With_Info.word,
                                                                 keyword_With_Info.get_Counter_Of_Path(path_Info.path)))
    return paths_Info

def create_Path_Choices(paths_Info: []):
    # creater the final form before the output
    path_Choices = []
    for path_Info in paths_Info:
        path_Choices.append(Path_Choice(path_Info.path))
    for path_Choice in path_Choices:
        for path_Info in paths_Info:
            if(path_Info.path == path_Choice.path):
                for word_And_Counter in path_Info.words_And_Counters:
                    path_Choice.counter += word_And_Counter.counter
                    if(word_And_Counter.counter is not 0):
                        path_Choice.number_Of_Words += 1            
    return path_Choices

def path_Choices_Sort(path_Choices: []):
    # sorts the list and prints it
    def return_number_Of_words(e):
        return e.number_Of_Words
    path_Choices.sort(key = return_number_Of_words)
    for path_choice in path_Choices:
        print(path_choice.path)
                
            
            
    
        
        