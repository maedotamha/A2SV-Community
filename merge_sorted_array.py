class Solution:
    def merge(self, nums1: List[int], total_nums1: int, nums2: List[int], total_nums2: int) -> None:
        """
        Merges two sorted arrays, nums1 and nums2, into a single sorted array.
        """
        index_nums1, index_nums2 = total_nums1 - 1, total_nums2 - 1
      
        merge_index = total_nums1 + total_nums2 - 1
      
        while index_nums2 >= 0:
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[merge_index] = nums1[index_nums1]
                index_nums1 -= 1  
            else:
                nums1[merge_index] = nums2[index_nums2]
                index_nums2 -= 1  
            merge_index -= 1
