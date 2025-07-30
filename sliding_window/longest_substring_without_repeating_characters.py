class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

"""
Notes: 
I struggled a lot with this question!!!!

Problem: Return the length of the longest substring without repeating characters.
Not asking for the substring or how many — just the max length.

-> Loop: for right in range(len(s))
              -> move left to right across the string
              -> every time a duplicate is found, remove letters from the left until the duplicate is gone

-> seen = set()   => tracks what characters are in current window

-> left = 0       => left pointer for the window start

-> max_len = 0    => keeps track of the best (longest) length seen


-> range(len(s)) => goes through each index of the string s from 0 to end
                 => standard way to loop through characters in a string by index

                 => Why is "for char in s" not used to loop through the letters?
                     -> B/c we need index:
                           -> to calculate substring length: right - left + 1 = size of current unique window
                                         -> the plus 1 is there because indexes start at 0, so it gives the actual length
                           -> compare characters at specific positions: s[right], s[left]
                           -> move both pointers (left, right) independently
"""
"""
Time Complexity: O(n)    
                -> each character is added and removed from the set at most once
                -> so both pointers (left and right) move across the string only once

                => total work is proportional to n (length of the string)

Space Complexity: O(k)
                -> where k is the number of unique characters in the string
                -> the set can grow up to k size(worst case: all characters are unique)

                -> so technically: 
                                 -> O(min(n,k)), where k is the charset size
                                 -> for standard ASCII(256 chars) -> can be treated as O(1)
                                 -> For unicode or dynamic input -> it's safer to say O(k)
                                
                -> it would've been O(1) is input is limited to fixe size charset like ASCII
"""

""" 
Note regarding space complexity: Max Subarray vs Longest Substring w/o Repeating Characters

Max subarray's Space Complexity was O(1):
                                      -> only 2 variables
                                      -> no extra data structures (lists, sets, etc.)
                                      -> doesn't grow with input size

Longest substring w/o Repeating Characters was O(k):
                                      -> you're storing characters in a set
                                      -> worse case no repeats and then every unique character in the string gets stored



