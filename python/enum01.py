# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#     numToIndex = {}

#     for i, num in enumerate(nums):

#       if target - num in numToIndex:
#         return numToIndex[target - num], i
#       numToIndex[num] = i

# marks=[78,98,45,76,23,19]
# index=0
# for mark in marks:
#     print(mark)
#     if (index==1):
#         print("Shikher")
#     index+=1

marks=[78,98,45,76,23,19]
# marks=(78,98,45,76,23,19)
# marks={78,98,45,76,23,19}

for index,mark in enumerate(marks):
    print(mark,"->",index)
    if (index==1):
        print("Shikher")

for index,mark in enumerate(marks,start=2):
    print(mark,"->",index)
    if (index==1):
        print("Shikher")