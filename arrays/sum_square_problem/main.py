#main funnction
def sum_cubes(m,n):
    # check weather it is countable
    if m>n:
        return("interval is not possible!")
    total = 0
    #storint some of square in total variable
    for i in range(m,n+1):
        total = total + i**3
        print(total)

m = int(input("m : "))
n = int(input("n : "))

res = sum_cubes(m,n)

# print(res)
