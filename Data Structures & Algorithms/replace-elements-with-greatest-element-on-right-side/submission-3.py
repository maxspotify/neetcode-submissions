class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = max(largest, arr[i])
            arr[i] = largest
            largest = temp
        return arr