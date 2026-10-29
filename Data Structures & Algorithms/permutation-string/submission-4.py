class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        - put s1 into a hashset
        - Check for length of s1
        - have sliding window of s1's length, while checking hashset
        '''

        '''
        forgot abt duplicate letters hehe

         charSet = set(s1)

        i = 0
        j = len(s1)

        while (j < len(s2) + 1):
            currWin = set(s2[i:j])
            print(charSet)
            print(s2[i:j])
            print(currWin)
            print(i, j)

            if(currWin == charSet):
                return True
            
            i += 1
            j = i + len(s1)

        return False

        '''

        if len(s1) > len(s2):
            return False

        charMap = {}

        for i in range(len(s1)):
            charMap[s1[i]] = charMap.get(s1[i], 0) + 1

        currWin = {}

        for i in range(len(s1)):
            currWin[s2[i]] = currWin.get(s2[i], 0) + 1

        if currWin == charMap:
            return True

        i = 0
        j = len(s1)

        while (j < len(s2)):

            currWin[s2[j]] = currWin.get(s2[j], 0) + 1
        
            currWin[s2[i]] -= 1 
            
            if(currWin[s2[i]] == 0):
                currWin.pop(s2[i]) 
            
            i += 1
            j = i + len(s1)

            if(currWin == charMap):
                return True

        return False
