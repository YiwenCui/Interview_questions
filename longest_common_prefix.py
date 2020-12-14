#1
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].startswith(prefix) == False or strs[i].index(prefix)!= 0 :
                prefix = prefix[0:len(prefix)-1]
                if prefix =="":
                    return ""
        return prefix



#2 
def A(str,prefix):
    try:
        str.index(prefix)
    except ValueError:
        return False 
    else:
        if str.index(prefix)!=0:
            return False
        else:
            return True


    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefix = strs[0]
    
    
            
        for i in range(1,len(strs)):
            while A(strs[i],prefix) == False :
                prefix = prefix[0:len(prefix)-1]
                if prefix =="":
                    return ""
        return prefix
            