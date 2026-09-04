class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        for i in range (len(strs[0])):
            prefix = strs[0][:i]
            char = strs[0][i]
            for j in strs[1:]:
                if i>=len(j) or j[i] != char:
                    return prefix
        return strs[0]
                
            



        