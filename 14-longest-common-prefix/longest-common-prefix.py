class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0] 
        # assume entire first word as prefix and then compare with other and if not then reduce the prefix

        for s in strs[1:]: 
        # starts with the first word as the 0th is already considereed as prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if prefix =="":
                    return ""

        return prefix

        