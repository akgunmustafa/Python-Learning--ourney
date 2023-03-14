#Mean
list1=[12,20,30,44,59,97,20,19,20]
mean=sum(list1)/len(list1)
print("Mean = "+str(mean))

#Median
list2=[12,16,20,20,22,40,42,44,10]
list2.sort()

if len(list2) %2 ==0:
    m1=list2[len(list2)//2]
    m2=list2[len(list2)//2-1]
    median=(m1+m2)/2
else:
    median=list2[len(list2)//2]
print("Median = "+str(median))

#Mode
list3=[10,10,14,18,25,6,27]
frequency={}
for i in list3:
    frequency.setdefault(i,0)
    frequency[i]+=1

frequent= max(frequency.values())
for i,j in frequency.items():
    if j ==frequent:
        mode=i
print("Mode = "+str(mode))