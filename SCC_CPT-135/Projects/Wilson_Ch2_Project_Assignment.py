'''Chap 2'''

food_item = input("Enter food item name: \n")
price = float(input("Enter item price: \n")) #Said in canvas project notes 'floats are not used to represent currency due to rounding and accumulation errors.' was curious why on a deeper level than just it gives errors?
quantity = int(input("Enter item quantity: \n"))

print("\nRECEIPT:")
print(f'{quantity} {food_item} @ $ {price} = $ {quantity * price}')

receipt_cost = quantity * price

#Second Receipt bellow

food_item2 = input("\nEnter second food item name: \n")
price2 = float(input("Enter item price: \n"))
quantity2 = int(input("Enter item quantity: \n"))

print("\nRECEIPT:")
print(f'{quantity} {food_item} @ $ {price} = $ {quantity * price}')
print(f'{quantity2} {food_item2} @ $ {price2} = $ {quantity2 * price2}')

receipt_cost2 = quantity2 * price2

#Total + Gratuity bellow

total_cost = receipt_cost2 + receipt_cost
print(f'Total cost: $ {total_cost}\n')
gratuity = total_cost * 0.15
print(f'15% gratuity: $ {gratuity}')
print(f'Total with tip: $ {gratuity + total_cost}')




