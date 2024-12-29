class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # double for loops : O(n)^2"
        # first for loop goes through the list of words and second for loop compares each letter in a word 
        if not strs:
            return " "
        else :
            first_word = strs[0]
            common_prefix = ""
            for i in range(len(first_word)):
                letter = first_word[i]
                for word in strs[1:]:
                    if i >= len(word) or word[i] != letter :
                        return common_prefix
                common_prefix += letter
            return common_prefix
