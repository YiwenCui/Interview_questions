def common_factor(x,y):
    common_factors_list = []
    for n in range(1,max(x,y)):
        if x % n ==0 and y % n ==0:
            common_factors_list.append(n)
    return common_factors_list

print(common_factor(10,20))