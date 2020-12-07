class Solution(object):
    def reverse(self, x):
        reversed_str=""
        str_x =str(x)
        for index in range(len(str_x)-1, -1,-1):
            reversed_str=reversed_str+str_x[index]
        if reversed_str[0]=="0"and reversed_str[-1]!="-" :
            reversed_str=int(reversed_str)
                                            
        
        elif reversed_str[-1]=="-":
            reversed_str=reversed_str[-1]+reversed_str[0:-1]
            if reversed_str[1]=="0":
                reversed_str=int(reversed_str)
                
        reversed_str=int(reversed_str)        

        if reversed_str <=(2**31-1) and reversed_str>=-2**31:      
            return reversed_str
        else:
            return 0
            