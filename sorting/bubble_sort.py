arr=[2,3,4,7,6,5]

for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j+1]<arr[j]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
print(arr)