class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0] 

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

  """
  Notes:
  
  Variable:                            	  Role:
  current_sum	                          Running total of current subarray (live score)
  max_sum	                              Best subarray total seen so far (high score)
  max check	                              max_sum = max(max_sum, current_sum) every step

  """

"""
Time Complexity: O(n) 
                   
                 -> you iterate through the list once
                 -> each operation inside the loop is constant time O(1)
                 -> so overall time = O(n) where n = len(nums)

Space Complexity: O(1)

                  -> You don't use any extra space that grows with input size
                  -> current_sum and max_sum are just two variables
                  -> The input list nums is passed into the function, you're not storing or copying it
                  -> The space to hold the input is not counted in auxillary space (unless you're making a copy of it)
                                                                      |
                                                                      -> Auxiliary space = space you add (this is what we measure for space complexity)
"""
