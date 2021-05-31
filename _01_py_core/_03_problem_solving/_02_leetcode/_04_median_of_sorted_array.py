'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.
	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
	Example 1:
	nums1 = [1, 3]
	nums2 = [2]
	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]
	The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, num1, num2):
        num3 = num1 + num2
        num3.sort()
        # print(num3)
        if len(num3) % 2 == 0:
            length = len(num3)
            mid = int(length/2) - 1
            midnext = mid+1
            # print(mid, midnext)
            median = num3[mid] + num3[midnext]
            # print(median)
            res = median/2
            return res

        else:
            res = math.floor(len(num3)/2)
            return num3[res]


num1 = [2]
num2 = []

check = Solution()
print(check.findMedianSortedArrays(num1, num2))
