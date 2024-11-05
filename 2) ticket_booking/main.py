#main funnction
def ticket_booking(no_of_members):
    #purse amount
    purse = 0
    #loop for getting age
    for i in range(no_of_members):
        age = int(input("age : "))
        if age > 60:
            purse = purse + 30
        elif age < 12:
            purse = purse + 20
        else:
            purse = purse + 50
            
    return purse

no_of_member = int(input("no of member : "))

res = ticket_booking(no_of_member)

print(res)
