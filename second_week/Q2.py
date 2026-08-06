age = int(input("Enter your age: "))

ticket_price = 20
discount = 10


if age <= 12:
    ticket_price = 10
    print(ticket_price)

elif age >= 65:
    # ticket_price = 12
    ticket_price*discount/100
    print(ticket_price*discount/100)

else:
    
    print(ticket_price )