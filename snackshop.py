snack = 'Chips'
price = 1.50
stock = 10
Available = True

print(type(snack))
print(type(price))
print(type(stock))
print(type(Available))

total_cost = price * stock
print('The total cost is $',total_cost)

sale_price = price * 2
print('The sale price is $',sale_price)

print(2 * stock)

shopname = 'Snack'+' '+'Emporium'
print(shopname)
print('The Length of The Shop Name is:',len(shopname))
print(shopname[5])

var1 = 'Barca'
var2 = 'Real'

temp = var2
var2 = var1
var1 = temp

print(var1)
print(var2)