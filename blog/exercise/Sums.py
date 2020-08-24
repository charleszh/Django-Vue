class Solution:
    def twoSum(self, nums, target):
        """
:type nums: List[int]
:type target: int
:rtype List[int]
"""
        tmp_dict = {}
        for index, value in enumerate(nums):
            if target-value in tmp_dict:
                return [tmp_dict[target-value], index]
            tmp_dict[value] = index
        return []


if __name__ == '__main__':
    result = Solution().twoSum([8, 3, 5, 7, 1], 9)
    print(result)
