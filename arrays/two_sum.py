"""
Notes:
Dictionary -> stores key-value pairs
		 -> ex: my_dict = {"Sally": "123-4567"}
			-> Sally is the key, 123-457 is the value

		-> ex: nums = [2,7,11,15]
			  target = 9
			  # As you go through the loop:
					1) num = 2, index = 0  -> seen =  {2: 0} (key: 2, value: 0)
					2) num = 7, index = 1 ->  seen =  {2: 0, 7: 1} (key: 7, value: 1)

		-> Adding to dictionary: 
			-> ex: seen[num] = i
			-> in my seen dictionary, save num as the key and i as the value


enumerate() -> loops through a list and gets the index at the same time

		    -> ex:   nums = [10, 20, 30]
				for i, num in enumerate(nums):
					print(i,num)

				-> Output:  0  10
						  1  20
						  2  30
				

-> seen[complement] is the index, and complement is the value

so seen[complement]  is index of first number and i is the index of the second number,    return[seen[complement], i] -> returns [smaller index, bigger index] """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # empty dictionary

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i

#difficulty: easy
#time complexity: O(n)
#space complexity: O(n)



