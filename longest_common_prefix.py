class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        prefix_length = len(prefix)

        for string in strs[1:]:
            while prefix != string[0:prefix_length]:
                prefix_length -= 1
                prefix = prefix[0: prefix_length]
                if prefix_length == 0:
                    return ""

        
        return prefix

                    