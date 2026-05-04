class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr)-1,-1,-1):
            val = arr[i]
            arr[i] = largest
            if val > largest:
                largest = val
        return arr
