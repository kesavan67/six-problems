n=int(input("Enter size of array:"))
arr = []
for i in range(n): 
    element = int(input())
    arr.append(element) 
    
for j in range(n):
 for i in range(0,n-1):
    current = arr[i]
    nxt = arr[i+1]
    if current < nxt :
        temp = nxt 
        nxt = current 
        current = temp
    arr[i] = current 
    arr[i+1] = nxt 
print(arr)
