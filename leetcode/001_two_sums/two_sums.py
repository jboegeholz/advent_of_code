from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    output = []
    length_num = len(nums)
    for i in range(length_num - 1):
        for j in range(i + 1, length_num):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                break
    return output