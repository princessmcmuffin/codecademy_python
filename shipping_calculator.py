weight = 4.8

#Ground Shipping
if weight <= 2:
  ground_cost = round(20 + (weight * 1.5),2)
elif weight <= 6:
  ground_cost = round(20 + (weight * 3),2)
elif weight <= 10:
  ground_cost = round(20 + (weight * 4),2)
else:
  ground_cost = round(20 + (weight * 4.75),2)


print("Ground cost is: " + str(ground_cost))

#Premium Shipping
premium_cost = 125

print("Premium cost is: " + str(premium_cost))

#Drone Shipping
if weight <= 2:
  drone_cost = round(weight * 4.5,2)
elif weight <= 6:
  drone_cost = round(weight * 9,2)
elif weight <= 10:
  drone_cost = round(weight * 12,2)
else:
  drone_cost = round(weight * 14.25,2)

print("Drone cost is: " + str(drone_cost))

#Calculate which is cheapest
data = {"Ground": ground_cost,"Premium": premium_cost,"Drone": drone_cost}

print("""
The most cost effective method is: """ + min(data, key=data.get))