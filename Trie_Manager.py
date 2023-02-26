class Path_And_Counter(object):
    def __init__(self, path: str):
        self.path = path
        self.counter = 1

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # is it the last character of the word
        self.word_finished = False
        # how many words end with this character
        self.paths_And_Counters = []
        
class TrieWord(object):
    # a struct that holds each word and the number of time that word appears
    def __init__(self, word: str, paths_And_Counters: [Path_And_Counter]):
        self.word = word
        self.paths_And_Counters = paths_And_Counters
    def get_Counter_Of_Path(self, path: str):
        for path_And_Counter in self.paths_And_Counters:
            if(path_And_Counter.path == path):
                return path_And_Counter.counter
        return 0
        
def add(root, word_and_Path):
    # adding a word in the trie structure
    node = root
    path_Exist = False
    for char in word_and_Path.word.casefold():
        found_in_child = False
        # search for the character in the children of the present 'node'
        for child in node.children:
            if child.char == char:
                # point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # we did not find it, so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # and then point node to the new child
            node = new_node
    # everything finished. Mark it as the end of a word.
    node.word_finished = True
    for path_And_Counter in node.paths_And_Counters:
        if(path_And_Counter.path == word_and_Path.path):
            path_And_Counter.counter += 1
            path_Exist = True
    if(path_Exist == False):
        node.paths_And_Counters.append(Path_And_Counter(word_and_Path.path))
    
def init_Access(root: TrieNode):
    # starts the access of Trie
    node = root
    word = []
    trieWords = []
    for child in node.children:
        access(child, word, trieWords)
    return trieWords
    
def access(root: TrieNode, word, trieWords):
    # the actual access method
    node = root
    wordChar = []
    wordChar.append("".join(word))
    wordChar.append(node.char)
    for child in node.children:
        access(child, wordChar, trieWords)
    if(node.word_finished):
        trieWords.append(TrieWord("".join(wordChar),node.paths_And_Counters))
