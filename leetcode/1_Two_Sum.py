class Solution:
    def twoSum(self, nums, target):
        ele_dist = {}
        for i, x in enumerate(nums):
            if target - x in ele_dist:
                return [i, ele_dist[target - x]]
            ele_dist[x] = i


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
