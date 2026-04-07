class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot_mul = 1
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            tot_mul *= nums[i]

        if len(zeros) > 1:
            return [0] * len(nums)
        elif len(zeros) > 0:
            rslt = [0] * len(nums)
            
            rslt[zeros[0]] = 1
            for i in range(len(nums)):
                if i != zeros[0]:
                    rslt[zeros[0]] *= nums[i]
        else:
            rslt = [0] * len(nums)

            for i in range(len(nums)):
                rslt[i] = int(tot_mul / nums[i])

        return rslt