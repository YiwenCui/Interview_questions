class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        output=""
        a=str(num)
        for idx,char in enumerate(a):
            if char =="6":
                output= a[0:idx]+"9"+a[idx+1:]
                break
        if output =="":
            output=num
        
        return output