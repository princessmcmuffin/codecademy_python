inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# number of items in warehouse
inventory_len = len(inventory)

# first item
first = inventory[0]

# last item
last = inventory[-1]

# return items starting at index 2 and up to, but not including index 6
inventory_2_6 = inventory[2:6]

# first 3 items
first_3 = inventory[:3]

# number of twin beds
twin_beds = inventory.count("twin bed")

# remove the fifth element and save below
removed_item = inventory.pop(4)

# add "19th Century Bed Frame" as 11th element in our inventory
inventory.insert(10,"19th Centry Bed Frame")

# sort inventory 
inventory.sort()

print(inventory)