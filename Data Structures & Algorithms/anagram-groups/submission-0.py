class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - Sort each string
        - If it's contained in hashmap, add to list
        - If it's not contained new value in hashmap
        '''

        #if there's no key, auto creates it
        res = defaultdict(list)

        for s in strs:
            #''.join makes the sorted(s) back into string instead of char arr
            sortedS = ''.join(sorted(s))

            #If contained in hashmap, add to list
            #If not contained, new value in hashmap
            res[sortedS].append(s)
        
        #converts hashmap to list
        return list(res.values())
        

