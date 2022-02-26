 # Calculating total cost of 5 items
    # 2/25/2022
    # CTI-110 P2HW1 - Total Purchases
    # Joshua Lockart
    #

#user input for each item price
item_1 = float(input())

item_2 = float(input())

item_3 = float(input())

item_4 = float(input())

item_5 = float(input())


#calculating subtotal and sales_tax and then taking the values from both and adding together to get the total_cost
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = (subtotal * 0.07)
total_cost = (subtotal + sales_tax)

#Output of calculations
print('-------Results-------')
print('Subtotal:{:.2f}'.format(subtotal))
print('Sales Tax:{:.2f}'.format(sales_tax))
print('Total:{:.2f}'.format(total_cost))