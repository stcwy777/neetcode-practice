class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        ind = {}
        for word in words:
            for c in word:
                adj[c] = set()
                ind[c] = 0
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            m = min(len(w1), len(w2))
            for j in range(m):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]] += 1
                    break
        q = deque()
        for n in ind:
            if ind[n] == 0:
                q.append(n)
        res = []
        while q:
            node = q.pop()
            res.append(node)

            for nei in adj[node]:
                ind[nei] -= 1

                if ind[nei] == 0:
                    q.append(nei)

        if len(res) < len(ind):
            return ""
        
        return "".join(res)