class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree = TrieTree()

        for word in words:
            tree.add(word)
        
        ROW, COL = len(board), len(board[0])
        visited = [[0] * COL for _ in range(ROW)]
        foundWords = set()

        def dfs(r: int, c: int, node: TrieNode, word: str):
            
            # Position not valid
            if r >= ROW or c >= COL or min(r, c) < 0 or visited[r][c] == 1:
                return
            # Not in Trie
            else:
                ch = board[r][c]
                if ch not in node.children:
                    return
                else:
                    newWord = word + ch
                    child = node.children[ch]
                    if child.isWord:
                        foundWords.add(newWord)
                
                    visited[r][c] = 1
                    dfs(r, c + 1, child, newWord)
                    dfs(r, c - 1, child, newWord)
                    dfs(r + 1, c, child, newWord)
                    dfs(r - 1, c, child, newWord)
                    visited[r][c] = 0

        for i in range(ROW):
            for j in range(COL):
                dfs(i, j, tree.root, '')
        
        return list(foundWords)
        