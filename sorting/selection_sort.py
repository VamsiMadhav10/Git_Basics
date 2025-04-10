arr=[1,2,3,8,7,6]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)