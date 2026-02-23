from typing import List
import unittest

class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers that add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Uses a hash map for O(n) time and O(n) space.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # No solution (should not happen per problem statement)

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2,7,11,15], 9), [0,1])
    def test_example2(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3,2,4], 6), [1,2])
    def test_example3(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3,3], 6), [0,1])
    def test_no_solution(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1,2,3], 7), [])

if __name__ == '__main__':
    unittest.main()