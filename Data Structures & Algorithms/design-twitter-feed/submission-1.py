class Twitter:

    def __init__(self):
        self.folwer = {}
        self.tweet = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId] = []
        
        self.time +=1
        self.tweet[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweet.get(userId, [])[:]

        for followeeId in self.folwer.get(userId,set()):
            feed.extend(self.tweet[followeeId])
        
        feed.sort(key=lambda x:x[0],reverse = True)
        return [tweedId for _,tweedId in feed[:10]]
        


            
                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.folwer:
            self.folwer[followerId] = set()
        
        self.folwer[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.folwer:
            self.folwer[followerId].discard(followeeId)
        
