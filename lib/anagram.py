# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,match):
        anagrams = []
        for word in match:
            if sorted(word.lower()) == sorted(self.word.lower()) and word.lower() != self.word.lower():
                anagrams.append(word)
            return anagrams     