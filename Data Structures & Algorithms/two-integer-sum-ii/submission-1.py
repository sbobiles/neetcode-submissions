class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        - array alr sorted
        - have pointers on opposite ends
        '''

        answer = []

        left = 0
        right = len(numbers) - 1

        while (left < right):
            if(numbers[left] + numbers[right] == target):
                answer.append(left + 1)
                answer.append(right + 1)
                return answer
            elif(numbers[left] + numbers[right] > target):
                right -= 1
            else:
                left += 1
            
        return answer
        