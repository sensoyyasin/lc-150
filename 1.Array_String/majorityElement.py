'''
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Guzel Soru - Hashmap
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_map = {}

        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1

        majority = len(nums) // 2

        for num, count in my_map.items():
            if count > majority:
                return num

