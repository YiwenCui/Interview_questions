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
    return return_list



def list_add_one (given_list):
    sum_int=0
    for index, integer in enumerate(given_list[::-1]):
        res = integer * 10**index
        sum_int += res
    sum_int += 1
    
    return_list =[]
    for char in str(sum_int):
        return_list.append(int(char))
    return return_list

print(list_add_one([2,3,4]))


#see link https://www.youtube.com/watch?v=uQdy914JRKQ&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=4"