class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        startID=0
        balance=0
        output =""
        for idx, char in enumerate(S):
            if char == "(":
                balance+=1
            else:
                balance-=1
                
                if balance ==0:
                    output += S[startID+1:idx]
                    startID=idx+1
        return output
                    