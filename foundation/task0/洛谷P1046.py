data=input().split()
height=int(input())
count=0
for i in range(10) :
    if int(data[i])<=height+30 :
        count+=1
print(count)
