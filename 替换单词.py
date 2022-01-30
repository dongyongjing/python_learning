class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        letter = sentence.split()
        for index in range(len(letter)):
            for index2 in dictionary:
                length = len(index2)
                if letter[index][:length] == index2:
                    letter[index] = index2
        return " ".join(letter)