from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        rslt = []
        max_heap = self.tweets[userId][-1:-11:-1]
        heapq.heapify(max_heap)

        for fId in self.followMap[userId]:
            for (t, i) in self.tweets[fId][-1:-11:-1]:
                heapq.heappush(max_heap, (t, i))
        
        for i in range(10):
            # print(max_heap)
            if max_heap:
                time, tId = heapq.heappop(max_heap)
                rslt.append(tId)

        return rslt

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
