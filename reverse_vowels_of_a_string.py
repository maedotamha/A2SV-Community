class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        chars = list(s)
        
        left, right = 0, len(chars) - 1
        
        while left < right:
            if not chars[left].lower() in vowels:
                left += 1
            elif not chars[right].lower() in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return ''.join(chars)
