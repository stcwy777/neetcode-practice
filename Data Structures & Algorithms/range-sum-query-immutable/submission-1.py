class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix_sum = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            self._prefix_sum[i] = self._prefix_sum[i - 1] + nums[i]
        print(self._prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]
        else:
            return self._prefix_sum[right] - self._prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)