class Twitter:

    def __init__(self):
        self.tweets={}
        self.following={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        min_heap=[]
        users=self.following.get(userId,set()).copy()
        users.add(userId)
        
        for ele in users:
            if ele in self.tweets:
                for ele1 in self.tweets[ele]:
                    heapq.heappush(min_heap,ele1)
        count=0
        
        while min_heap and count<10:
            count+=1
            x=heapq.heappop(min_heap)
            result.append(x[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
