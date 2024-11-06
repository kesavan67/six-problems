
m=int(input(" value of m :"))
n=int(input("value of n :"))
sum=0
if m>n :
    print("0")
else:
    for i in range(m,n): 
        sum+=(i**3)#sum of the square m to n
print(sum)
