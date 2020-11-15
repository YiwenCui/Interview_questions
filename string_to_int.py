# interview step 1: clarifying questions/High level discussion
# step 2: chooose approach, list potential solutions and approach
def add_one(given_array):
    carry = 1
    result = []
    for i in range(len(given_array)-1,-1, -1): 
        total = given_array[i] + carry
        if total == 10:
            carry = 1
        else: carry = 0
        result.insert(0,total%10) 
    if carry ==1:
        result.insert(0,1)
    return result

print(add_one([9,9,9]))

          
