from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)

        hand.sort()

        for num in hand:
            if freq[num] == 0:
                continue
            
            for i in range(groupSize):
                if num + i not in freq or freq[num + i] <= 0:
                    return False
                freq[num + i] -= 1
        
        return True