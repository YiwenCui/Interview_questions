class Solution(object):
    def delete_last_char (self,a):
        new_a=""
        for x in a[:-1]:
            new_a+=x
        return new_a
    def lengthOfLastWord(self, s):
        if s==" ":
            return 0
        n=0
    
        for x in s[::-1]:
            if x==" ":
                s=self.delete_last_char(s)
                # s=s.replace(" ","")
                
            else:
                break
        for char in s[::-1]:
            if char!=" ":
                n+=1
            else:
                break
        return n