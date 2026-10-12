class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute w/division

        product = 1
        zeroCnt = 0

        arr = []

        for i in range (len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeroCnt += 1
    
        if zeroCnt > 1:
            return [0] * len(nums)

        for i in range (len(nums)):
            if zeroCnt == 1:
                if(nums[i] != 0):
                    arr.append(0)
                else:
                    arr.append(product)
            else:
                arr.append(product//nums[i])

        return arr
