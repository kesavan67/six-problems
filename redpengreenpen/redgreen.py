arr=list(map(int,input().split()))
count=0
for i in range(len(arr)-1):
    if(arr[i+1]%2==0):
        count+=1
print(count)
