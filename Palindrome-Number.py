class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        left = 0
        right = len(num) - 1
        while left < right :
            if num[left] == num[right] :
                left = left + 1
                right = right -1
            else :
                return False
        return True
