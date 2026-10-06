class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if target > arr[mid]:
                    left = mid + 1
                elif target < arr[mid]:
                    right = mid - 1
                else:
                    return True
            
            return False
        
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                return binary_search(matrix[mid])
        
        return False