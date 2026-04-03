from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) # userid -> list of [count, tweetIds]
        self.followmap = defaultdict(set) # userid -> set of followeeids

    def postTweet(self, userId: int, tweetId: int) -> None:
        # store the tweet with a decreasing counter so that latest tweets have the smallest count
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1  # decrement so newer tweets come before older ones in minHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followmap[userId].add(userId)  # user should see their own tweets too
        for followeeId in self.followmap[userId]: # get all the people this user follows
            if followeeId in self.tweetmap: # check if this person has atleast 1 tweet
                index = len(self.tweetmap[followeeId]) - 1 # index of the latest post of this person
                count, tweetId = self.tweetmap[followeeId][index] # the latest post of this person [count, tweetIds]
                # push into heap: count ensures ordering, index helps us fetch older tweets later
                minHeap.append([count, tweetId, followeeId, index - 1]) 
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # get the most recent tweet
            res.append(tweetId)
            if index >= 0: # if this followee has more tweets
                count, tweetId = self.tweetmap[followeeId][index]
                # FIX: must call heapq.heappush with (heap, item), not just item
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # this is because we also want other tweets from this same person but our for loop wil just move on to the next person so to counter that we are storing the index in this list so that we can use that and get the next latest tweet from this person
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId) # add followee to follower's set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId) # remove followee if present
