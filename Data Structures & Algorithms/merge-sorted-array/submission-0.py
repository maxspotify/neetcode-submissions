class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        if not nums1:
            return nums2
        arr_copy = nums1.copy()
        a = 0
        b = 0
        c = 0
        while a < m and b < n:
            if arr_copy[a] <= nums2[b]:
                nums1[c] = arr_copy[a]
                a += 1
                
            else:
                nums1[c] = nums2[b]
                b += 1
            c += 1

        while a < m:
            nums1[c] = arr_copy[a]
            a += 1
            c += 1
        
        while b < n:
            nums1[c] = nums2[b]
            b += 1
            c += 1

        


        