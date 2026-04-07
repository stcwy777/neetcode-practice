class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        curSum = 0
        prefix = defaultdict(int)
        
        prefix[0] = 1   # 非常关键
        
        for num in nums:
            curSum += num
            
            if curSum - k in prefix:
                count += prefix[curSum - k]
            
            prefix[curSum] += 1
        
        return count
