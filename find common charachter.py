class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for string in words:
            count_2 = Counter(string)
            for c in count:
                count[c] =  min(count[c],count_2[c])

        result = []
        for i in count:
            for n in range(count[i]):
                result.append(i)

        return result
