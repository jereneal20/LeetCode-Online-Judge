# 324. Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/description/


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wiggleSort([1, 5, 1, 6, 4, 2]))
    print(sol.wiggleSort([1, 3, 2, 2, 3, 1]))
    print(sol.wiggleSort([4, 5, 5, 6]))
