class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute
        
        '''
        sort list

        hashmap
        key: number
        value: number of times it pops up

        loop through hashmap and see the top k elements
        find top by finding max for k amt, and after delete from hashmap
        '''
        answer = []

        #nums.sort()

        numMap = {}

        for i in range(len(nums)):

            if(nums[i] not in numMap):
                numMap[nums[i]] = 1
            else:
                numMap[nums[i]] += 1

        for i in range(k):
            max_key = max(numMap, key=numMap.get)
            answer.append(max_key)
            numMap.pop(max_key)
        
        return answer



        
        