from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())
        