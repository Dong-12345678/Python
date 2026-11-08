class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while  i >=0 and j >=0 :
            if nums1[i] > nums2[j] :
                nums1[k]=nums1[i]
                i -=1
            else :
                nums1[k]=nums2[j]
                j -=1
            k -=1
        while j >=0:
            nums1[k]=nums2[j]
            j -=1
            k -=1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow]=nums[fast]
        return slow+1