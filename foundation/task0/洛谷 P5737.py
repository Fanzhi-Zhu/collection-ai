data=input().split()
x=int(data[0])
y=int(data[1])
count=0
result=[]
for i in range(x,y+1) :
      if (i%4==0 and i%100!=0) or (i%400==0) :
          count+=1
          result.append(i)
print(count)          
print(' '.join(map(str,result)))
          