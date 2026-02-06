
from typing import List
from math import ceil

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = nums1 + nums2
        combined_list.sort()
        len_combined_list = len(combined_list)
        print(combined_list)
        is_even = True
        if len_combined_list%2:
            is_even = False
            
        if is_even:
            return (combined_list[len_combined_list // 2] + combined_list[int(len_combined_list // 2)-1])/2
        else:
            return combined_list[len_combined_list // 2]
    

sol = Solution()
print(sol.findMedianSortedArrays([1,4,3],[2]))