class TrieNode:
    def __init__(self):
        self.children = {}  #Dictionary to store child nodes
        self.is_end_of_word = False  #Indicates if the node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  #Create a new node if the character is not present
            node = node.children[char]
        node.is_end_of_word = True  #Mark the end of the word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  #Word not found
            node = node.children[char]
        return node.is_end_of_word  #Return True if it's the end of a word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  #Prefix not found
            node = node.children[char]
        return True  #Prefix exists in the Trie

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")
trie.insert("ball")
print(trie.search("apple")) 
print(trie.starts_with("an"))


