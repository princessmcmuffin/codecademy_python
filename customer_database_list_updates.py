first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

# Add in Depak's size
preferred_size.append("Medium")

print(preferred_size)

# Exercise 2
customer_data = [["Ainsley", "Small", True],["Ben", "Large", False],["Chani", "Medium", True],["Depak", "Medium", False]]

# Change Chani's shipping preference to false
customer_data[-2][-1] = False

# Remove Ben's shipping preference
customer_data[1].remove(False)

print(customer_data)

# Create new list with new customer information in
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)