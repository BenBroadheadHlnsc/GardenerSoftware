#Customer Details
customer_name = input("Customers Name: ")
customer_address = input("Customers Address: ")
customers_number = input("Customers Phone Number: ")

#Lawn Dimensions
lawn_width = input("Width of Lawn: ")
#Minimum and Maximum Width Check
if int(lawn_width) <= 2:
    print("Width must be bigger than 2 metres.")
    quit()
elif int(lawn_width) > 30:
    print("Width must be smaller than 30 metres.")
    quit()

lawn_length = input("Length of Lawn: ")
#Minimum and Maximum Length Check
if int(lawn_length) <= 2:
    print("Length must be bigger than 2 metres.")
    quit()
elif int(lawn_length) > 50:
    print("Length must be smaller than 50 metres.")
    quit()
lawn_area = int(lawn_length)*int(lawn_width)

#Lawn Care Product
lawn_care_product = input("Lawn Care Product Requested: ")
lawn_care_cost = 0
while True:
    if lawn_care_product.lower() == "luxury":
        lawn_care_cost = 1.15*int(lawn_area)
    elif lawn_care_product.lower() == "standard":
        lawn_care_cost = 0.80*int(lawn_area)
    elif lawn_care_product.lower() == "economy":
        lawn_care_cost = 0.45*int(lawn_area)
    else:
        print("Please select either Bronze, Silver or Gold")
    break

#Costs
labour_cost = int(lawn_area) * 0.50
total_cost = labour_cost + labour_cost*0.2 + lawn_care_cost
total_vat_cost = labour_cost + lawn_care_cost

#Output
print(" ")
print("-------------------")
print(f"Customers Details: {customer_name.capitalize()}, {customer_address.capitalize()}, {customers_number.capitalize()},")
print(f"Lawn Area: {lawn_area}m^2")
print(f"Labour Cost: £{labour_cost}")
print(f"Lawn Care Cost: £{lawn_care_cost}")
print(f"Total Cost Excluding VAT: £{total_vat_cost}")
print(f"Total Cost Including VAT: £{total_cost}")
print("-------------------")
