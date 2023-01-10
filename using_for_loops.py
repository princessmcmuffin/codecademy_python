Carly's Clippers Dataset
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Create sum of prices for all different haircuts offered
total_price = 0

for price in prices:
  total_price += price

#Calculate average haircut price & print it
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

#Reduce the haircut price by 5 & print it
new_prices = [price - 5 for price in prices]
print(new_prices)

#Calculate last week's total revenue & print it
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

#Calculate average daily revenue & print it
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))