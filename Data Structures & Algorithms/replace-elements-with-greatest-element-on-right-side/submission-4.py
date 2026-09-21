class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr) - 1, -1, -1):
            new_largest = max(largest, arr[i])
            arr[i] = largest
            largest = new_largest
        return arr