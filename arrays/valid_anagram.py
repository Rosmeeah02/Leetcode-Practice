class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False #check to ensure anagrams are of equal length
        
        count_s = {}
        count_t = {}

        #count letters in s
        for char in s:

            if char in count_s:
                count_s[char] += 1
            
            else:
                count_s[char] = 1

        #count letters in t
        for char in t:

            if char in count_t:
                count_t[char] += 1

            else:
                count_t[char] = 1
        
        # Compare both dictionaries
        return count_s == count_t


    
        
