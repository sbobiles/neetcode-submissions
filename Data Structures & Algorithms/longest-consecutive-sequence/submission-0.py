class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            #checks if first in sequence
            if (num - 1) not in numSet:
                length = 1
                #continues to check if sequence can continue from start
                while (num + length) in numSet:
                    length += 1
                #Checks if sequence just found is the max
                longest = max(length, longest)
        return longest

        