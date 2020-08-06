'''
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z
'''
# Approach 1: TRIE
# Time complexity: O(n)
# where n is the maximum length of the string
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        # start from root
        node = self.root
        # iterate through word
        for char in word:
            if char in node.children:
                # if exists, make that node to the current node
                node = node.children[char]
            # if not, create a new children node
            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(self.root, word)]
        # until stack is not empty
        while stack:
            node, word = stack.pop()
            if not word:
                if node.isEnd:
                    return True
            # find the first letter
            elif word[0] in node.children:
                temp = node.children[word[0]]
                stack.append((temp,word[1:]))
            # if dot
            elif word[0] == '.':
                for temp in node.children.values():
                    stack.append((temp,word[1:]))

        return False
