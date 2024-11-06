arr=[1,5,0,7,0,0,8,9,0]
a=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        temp=arr[i]
        arr[i]=arr[a]
        arr[a]=temp
        a+=1
print(arr)

