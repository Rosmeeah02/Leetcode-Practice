class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0] 

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

  """
  Notes:
  
  Variable:                            	Role:
  current_sum	                          Running total of current subarray (live score)
  max_sum	                              Best subarray total seen so far (high score)
  max check	                            max_sum = max(max_sum, current_sum) every step

  """
