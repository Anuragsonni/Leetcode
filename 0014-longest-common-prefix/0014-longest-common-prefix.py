class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest = min(len(s) for s in strs)

        prefix = ""

        for i in range(shortest):
            first = strs[0][i]

            for s in strs:
                if s[i] != first:
                    return prefix

            prefix += first

        return prefix
