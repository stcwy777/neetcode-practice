class TreeNode:
    def __init__(self, idx: int) -> None:
        self.id = idx
        self.neighbors = []
    
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def help(s1: str, s2: str) -> bool:
            diff = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return True

        nodes = []
        begin, end = -1, -1

        for i in range(len(wordList)):
            nodes.append(TreeNode(i))
            if wordList[i] == beginWord:
                begin = i
            if wordList[i] == endWord:
                end = i
        if begin == -1:
            wordList.append(beginWord)
            begin = len(wordList) - 1
            nodes.append(TreeNode(begin))

        if end == -1:
            return 0

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if help(wordList[i], wordList[j]):
                    nodes[i].neighbors.append(j)
                    nodes[j].neighbors.append(i)
        
        q = deque([begin])
        visited = set([begin])
        distance = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in nodes[node].neighbors:
                    if nodes[nei].id == end:
                        return distance + 1
                    elif nodes[nei].id not in visited:
                        q.append(nodes[nei].id)
                        visited.add(nodes[nei].id)
            distance += 1
        
        return 0



        