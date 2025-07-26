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

🔹 Summary for Notes:
Time: O(n) → loops through both strings
Space: O(1) → at most 26 keys in each dict (constant alphabet size)
Let me know if you're planning to solve the Unicode version (non-lowercase-only) — that changes things a bit!

 """
    
        
