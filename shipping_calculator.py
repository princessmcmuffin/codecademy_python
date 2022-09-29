weight = 4.8

#Ground Shipping
if weight <= 2:
  ground_cost = 20 + (weight * 1.5)
elif weight <= 6:
  ground_cost = 20 + (weight * 3)
elif weight <= 10:
  ground_cost = 20 + (weight * 4)
else:
  ground_cost = 20 + (weight * 4.75)


print("Ground cost is: " + str(ground_cost))

#Premium Shipping
premium_cost = 125

print("Premium cost is: " + str(premium_cost))

#Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.5
elif weight <= 6:
  drone_cost = weight * 9
elif weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

print("Drone cost is: " + str(drone_cost))

#Calculate which is cheapest
data = {"Ground": ground_cost,"Premium": premium_cost,"Drone": drone_cost}

print("""
The most cost effective method is: """ + min(data, key=data.get))