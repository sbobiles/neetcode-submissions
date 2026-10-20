class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        struggling to find duplicates with this one

        1) sort nums
        2) Fix one num
        2) two pointer for other 2 
        '''
        answer = []
        nums.sort()

        for i in range (len(nums)):

            if nums[i] > 0:
                break

            if i > 0 and (nums[i] == nums[i - 1]):
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while(left < right):

                if(nums[i] + nums[left] + nums[right] == 0):
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                elif(nums[i] + nums[left] + nums[right] < 0):
                    left += 1
                else:
                    right -= 1

        return answer 
        
            


