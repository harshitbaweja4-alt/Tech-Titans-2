# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid
p1 = "headphone" #define the product
p2="smartwatch"
p3="ps5"
p4="ipad"
productName = input("Enter Product Name: ") # remove the ;
quantity = int(input("Enter the Quantity of the Product: ")) # removed ; and add int function
headphone_price = int(999) # define price by int function
smartwatch_price = int(1599)
ps5_price = int(1299)
ipad_price = int(599)
totalPrice=productName * quantity # defined total price

if productName == p1:#
    totalPrice = headphone_price * quantity #change the name of varible


elif productName == p2:#
    totalPrice = smartwatch_price * quantity 

elif productName == p3:
    totalPrice = ps5_price * quantity#

elif productName == p4:
    totalPrice = ipad_price * quantity 
print("total price:", totalPrice)


