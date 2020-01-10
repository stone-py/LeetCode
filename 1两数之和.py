class mySolution:
    def twoSum(self, nums, target):
        for num in nums:
            if (target - num) in nums:
                return [nums.index(num), nums.index(target - num)]


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                print(target - nums[i])
                dict[target - nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    s.twoSum([3, 3], 6)
