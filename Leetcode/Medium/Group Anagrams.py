class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = tuple(sorted(word)) #creates a tuple from the sorted word 
            if key not in anagrams:  #only runs if key doesn't exist yet
                anagrams[key] = []   #create key if it doesn not exist with an empty 
            anagrams[key].append(word) #appends the key so within anagrams (key) : [word, ...]

        return list(anagrams.values())

        


            
