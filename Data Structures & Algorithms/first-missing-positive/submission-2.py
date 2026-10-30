class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 第一步：原地交换，让 [1, n] 范围内的数字 x 回到下标 x - 1 的位置
        for i in range(n):
            # 只要当前数字在 [1, n] 范围内，且它真正的老家 nums[nums[i] - 1] 上还没坐着正确的数，就一直交换
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        # 第二步：从头检查每个座位，第一个“数不对位”的下标 i，缺的就是 i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 如果 1 ~ n 全都乖乖坐在自己的位置上，说明缺的是 n + 1
        return n + 1

