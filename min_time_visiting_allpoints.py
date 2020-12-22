# a=[[1,1],[3,4],[-1,0]]
# min_time=0
# for i in range(0,len(a)-1):
#     b=[]
#     b.append(a[i])
#     b.append(a[i+1])
#     print(b)
#     c= max(abs(b[1][0]-b[0][0]),abs(b[1][1]-b[0][1]))
#     min_time=min_time +c

# print (min_time)

a=[[1,1],[3,4],[-1,0]]
min_time=0
for i in range(0,len(a)-1):
    c=max(abs(a[i+1][0]-a[i][0]),abs(a[i+1][1]-a[i][1]))
    min_time=min_time +c

print(min_time)