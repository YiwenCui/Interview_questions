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



          
def list_to_int_add_one(given_list):
    concatenate = ""
    for int_element in given_list:
        concatenate += str(int_element)
    concatenate_sum = int(concatenate)+1
    
    return_list =[]
    for char in str(concatenate_sum):
        return_list.append(int(char))
    return (return_list)


print(list_to_int_add_one([9,9,9]))

