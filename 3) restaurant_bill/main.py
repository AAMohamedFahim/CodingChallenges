#main funnction
def food_order():
  #initialize purse and count
    purse = 0
    count = 0
    while True:
        order = int(input("order : "))
        if order == 4:
            break
        else:
            if order < 4 and order > 0:
                if order == 1:
                        quantity = int(input("quant : "))
                        purse = purse + (200*quantity)
                        count = count + quantity
                elif order == 2:
                        quantity = int(input("quant : "))
                        purse = purse + (180*quantity)
                        count = count + quantity
                if order == 3:
                        quantity = int(input("quant : "))
                        purse = purse + (50*quantity)
                        count = count + quantity
            else: 
                print("enter valid input!")
                continue
            
    if purse > 500:
        print("quantity : ",count)
        print("actual amount : ",purse)
        purse = purse - ((purse/100)*10)
        print("amount after discount : ",purse)
    return purse
            
            
menu = """
1.pizza -- 200
2.burger -- 180
3.indli -- 50
4. end
"""
print(menu)
res = food_order()
print(res)
