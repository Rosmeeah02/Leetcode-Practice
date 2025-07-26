"""
Notes:
set -> like a list but only keeps unique values, has no duplicates and no order

Example:
seen = set()  # create an empty set
seen.add(5)   # adds 5 to the set
print(5 in seen)  # True — 5 is in the set
print(10 in seen)  # False — 10 isn't in the set yet

Pseudocode:
make a list: store it in the list, then take the length of the list
then make a set, store it in the set, then take the length of the set
then see if they are equal lengths, if they are then its true that there is no duplicates if not then false 

"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_len = len(nums)
        no_dupes_len = len(set(nums))
        
        if original_len == no_dupes_len:
            return False  # no duplicates
        else:
            return True   # duplicates found

""" 
Time Complexity: O(n)
- len(nums) -> O(1)
- set(nums) -> O(n) because it has to loop through the entire list to build the set
                  -> inside set(nums): Python internally loops through each element in the nums list to:
                                                                  -> Check if it's already in the set
                                                                  -> Add it if it’s not                                                                          
- len(set(nums)) -> O(1)
- therefore, O(n) is the dominant 
"""

""" 
Space Complexity: O(n)
- set(nums) creates a new set in memory
      -> worst case (no duplicates), the set will store all n elements.

- therefore, it takes O(n) extra space
"""
#MORE EFFICIENT SOLUTION
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#Time: O(n) → building the set
#Space: O(n) → set stores up to n elements
