class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dictionary:
                dictionary[sortedWord] = [word]
            else:
                dictionary[sortedWord] += [word]
        return [dictionary[i] for i in dictionary]