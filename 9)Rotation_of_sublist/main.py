def rotate(arr,k):
    arr1 = arr[:k]
    arr2 = arr[k:]
    print(arr1)
    print(arr2)
    new_arr = arr2+arr1
    return new_arr
arr = list(map(int,input().split()))
k = int(input())
res = rotate(arr,k)

print(res)
