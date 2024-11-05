def switch_iden(array):
    # initialize swap counter as zero
    swap_count = 0
    for i in range(len(array) - 1):
        #checking whether the elemnt is chanfing from odd to even
        if array[i]%2 != 0 and array[i+1]%2 == 0:
            swap_count = swap_count + 1
    return swap_count
array = list(map(int,input().split()))


res = switch_iden(array)
# print(array)

print(res)