class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = arr[-1]
        for i in range(len(arr) -1, -1, -1):
            new_largest = max(largest, arr[i])
            arr[i] = largest
            largest = new_largest
            if i == (len(arr) - 1):
                arr[i] = -1
        
        return arr