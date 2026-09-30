from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        freq = Counter(hand)

        if n % groupSize:
            return False
            
        hand.sort()

        for num in hand:

            if freq[num] == 0:
                continue
            freq[num] -= 1

            for i in range(1, groupSize):

                if freq[num + i] <= 0:
                    return False
                else:
                    freq[num + i] -= 1
        
        return True

