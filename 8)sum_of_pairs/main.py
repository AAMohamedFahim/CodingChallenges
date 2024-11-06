def sum_pair(arr,tar):
    final = []
    for i in range(len(arr)):
        # print(i)
        for j in range(i+1,len(arr)):
            if arr[i] > tar:
                continue
            # print(j)
            if arr[i]+arr[j] == tar:
              final.append([arr[i],arr[j]])
              
              
    return final
    
    
arr = list(map(int,input().split()))
tar = int(input())
res = sum_pair(arr,tar)

print(res)
