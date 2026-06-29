lst=[(10,20,40),(40,50,60),(70,80,90)]

result=[]

for i in lst:
    temp=i[:-1]+(100,)
    result.append(temp)

print(result)
