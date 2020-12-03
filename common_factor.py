def common_factor(x,y):
    counter=0
    for n in range(1,max(x,y)):
        if x % n ==0 and y % n ==0:
            counter= counter +1
            print("common factor " + str(counter)+ " is " +  str(n))
    

common_factor(100,50)