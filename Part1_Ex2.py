import Input_Manager
import Trie_Manager
import Output_Manager

if __name__ == "__main__":
    # the main class of the project
    # for-loops and prints are left as comments for debugging
    
    #ex1 prepaired for ex2
    words_and_Paths = Input_Manager.read_Text()
    root = Trie_Manager.TrieNode('0')
    for word_and_Path in words_and_Paths:
        Trie_Manager.add(root, word_and_Path)
    generatedWords = Trie_Manager.init_Access(root)
    generatedWords = Output_Manager.reverse_Sort(generatedWords)
    Output_Manager.output_With_Numbers(generatedWords)
    #ex2
    keywords = Input_Manager.read_Phrase()
    keywords_With_Info = Output_Manager.create_Keywords_With_Info(keywords, generatedWords)
    paths_Info = Output_Manager.create_Paths_Info(keywords_With_Info)
    path_Choices = Output_Manager.create_Path_Choices(paths_Info)
    Output_Manager.path_Choices_Sort(path_Choices)
    