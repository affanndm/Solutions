class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string = min(strs, key = len) #find the shortest string in the list from strs
        max_prefix = ""

        for i in range(0, len(min_string)):   #from range of 0 to the length of min string iterating over every letter in sthe string
            prefix = min_string[:i+1]
            if all(s.startswith(prefix) for s in strs): #generator expression checks if for every single word in the list if it begins with the prefix defined
                max_prefix = prefix
            else:
                break

        return max_prefix


