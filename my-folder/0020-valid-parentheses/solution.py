class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openners = []
        objects = {"}":"{", ")":"(", "]":"["}
        for i in s:
            if i in objects:
                if openners and openners[-1] == objects[i]:
                    openners.pop()
                else:
                    return False
            else:
                openners.append(i)
        return True if not openners else False 
