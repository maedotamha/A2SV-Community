class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flipper(self, end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        n = len(arr)
        output = []
        
        for i in range(n - 1, 0, -1):
            max_idx = arr.index(max(arr[:i + 1]))
            
            if max_idx != i:
                flipper(self, max_idx)
                output.append(max_idx + 1)
                
                flipper(self, i)
                output.append(i + 1)
        
        return output
