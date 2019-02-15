item1 = float(input("Enter price of first item: "))
item2 = float(input("Enter price of second item: "))
member = input("Does customer have a club card? (y/n): ")
rate = float(input("Enter tax rate: "))

base_price = item1+item2

if item1 > item2:
    if member == "y":
        discount = (item1 + item2/2)*0.9
    else:
        discount = (item1 + item2/2)
else:
    if member == "y":
        discount = (item1/2 + item2) * 0.9
    else:
        discount = (item1/2 + item2)
total = discount + (discount*(rate/100))
total_round = round(total,2)


print("Base price =", base_price)
print("Price after discounts =", discount)
print("Total price =", total_round)




