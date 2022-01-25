class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for index in range(len(words)):
            for index2 in range(len(words[index])):
                if words[index][index2] not in allowed:
                    count += 1
                    break
        return  len(words) - count
