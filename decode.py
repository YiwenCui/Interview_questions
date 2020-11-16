import string
letter_to_num = {}
for index, letter in enumerate(string.ascii_lowercase,1):
    letter_to_num[letter] = str(index)

def helper_dp(data,k):
    if k == 0:
        return 1
    s = len(data) - k 
    if data[s] == 0:
        return 0
    result = helper_dp(data, k-1)
    if k >=2 and int(data[s:s+2]) <= 26:
        result += helper_dp(data, k - 2)
    return result

def num_ways_dp(data):
    return helper_dp(data, len(data))

print(num_ways_dp("1211`"))