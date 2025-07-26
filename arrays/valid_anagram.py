""" 
Notes:

-> Counter() => built-in class (smarter dictionary made just for counting things)
             => counts how many times each element appears in a list or string.
             => part of the collections module → so you have to import it.
-> Example: 
        from collections import Counter 

        s = "banana"
        count = Counter(s)
        print(count)

        output: {'b': 1, 'a': 3, 'n': 2}
"""
#################################################################################################################################################################
#Updated Version:
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
Time Complexity: O(n) -> has to loop through all n characters in the string 

Space Complexity: O(1) :
    -> we can care about how much extra memory is used relative to the input size
    -> lowercase letters: 26 unique keys in a dictionary so 26 will always be the limit
    -> memory usage does not grow as n grows
    -> so it's a constant space of O(1) 

    -> uppercase letters too: 52 possibilities -> 52 unique keys -> still bound and will not grow beyond this so space complexity is constant -> O(1)

    -> unicode characters: 
                            -> unique characters could be massive, meaning hundreds or thousands of keys are stored 
                            -> memory scales with how many different characters appear in the string 
                            -> space is O(k) => k = number of unique characters

                            -> Example:
                                    s = "aaaaaaaaaaaabbbbbbbbbbcccccc"
                                    n = 30 -> total characters in the string
                                    k = 3 -> unique characters: 'a', 'b', 'c'

                                    + O(n) → you're doing something for every letter (like looping through the full string)
                                    + O(k) → you're only storing or looping over unique letters ({'a': 12, 'b': 10, 'c': 8}) 
                            
    Summary: 
            -> O(1) means fixed space regardless of input size
            -> O(k) means space grows as the number of unique items grows
            -> O(n) means space grows with the total number of elements in the input (i.e length of string/array)
"""
##################################################################################################################################################################
#Old Version
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
        
#Old Version Complexities
""" 
Time Complexity: O(n)

-> Where n = length of the strings (s and t)
-> len(s) and len(t) → O(1)
-> First for loop over s → O(n)
-> Second for loop over t → O(n)
-> Comparing two dictionaries → O(k), where k is the number of unique characters (bounded by 26 lowercase letters → so treated as O(1))
-> So total time: O(n)

Space Complexity: O(1) (technically O(k), but k ≤ 26)

-> count_s and count_t store character counts
-> Worst case: each has up to 26 keys (a–z)
-> So extra space = 2 dictionaries of max 26 keys → treated as O(1)
-> So total space: O(1)

Summary for Notes:
Time: O(n) → loops through both strings
Space: O(1) → at most 26 keys in each dict (constant alphabet size)
Let me know if you're planning to solve the Unicode version (non-lowercase-only) — that changes things a bit!

 """
    
        
