class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target>= letters[-1]:            
            return letters[0]
        else:
            for char in letters:
                if target<char:
                    return char
                    