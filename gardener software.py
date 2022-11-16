#Customer Details
customer_name = input("Customers Name: ")
customer_address = input("Customers Address: ")
customers_number = input("Customers Phone Number: ")

#Lawn Dimensions
lawn_width = input("Width of Lawn: ")
lawn_length = input("Length of Lawn: ")
lawn_area = int(lawn_length) * int(lawn_width)

#Lawn Care Product
lawn_care_product = input("Lawn Care Product Requested: ")
lawn_care_cost = 0
while True:
    if lawn_care_product.lower() == "bronze":
        lawn_care_cost = 20
    elif lawn_care_product.lower() == "silver":
        lawn_care_cost = 30
    elif lawn_care_product.lower() == "gold":
        lawn_care_cost = 40
    else:
        print("Please select either Bronze, Silver or Gold")
    break

#Costs
labour_cost = lawn_area * 9.50
total_vat_cost = labour_cost + labour_cost*0.2 + lawn_care_cost
total_cost = labour_cost + lawn_care_cost

#Output
print("-------------------")
print(f"Customers Details: {customer_name.capitalize()}, {customer_address.capitalize()}, {customers_number.capitalize()},")
print(f"Lawn Area: {lawn_area}m^2")
print(f"Labour Cost: £{labour_cost}")
print(f"Lawn Care Cost: £{lawn_care_cost}")
print(f"Total Cost Excluding VAT: £{total_vat_cost}")
print(f"Total Cost Including VAT: £{total_cost}")
print("-------------------")
