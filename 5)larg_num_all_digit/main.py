def largest_all(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] < array[j]:
                #swaping
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                
    return array                
array = list(map(int,input().split()))


res = largest_all(array)
# print(array)

for i in res:
    print(i,end = "")
    
print()