# Shipping options with additional challenge at the end
# Kaleb Bolack

weight = 100
cost = ''

# Ground Shipping Here
 
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print('Ground Shipping (Based on Weight in Ibs | includes Flat Fee) $',cost_ground)

# Ground Shipping PREMIUM Here

cost_ground_premium = 125
print('Ground Shipping Premium (Flat Rate): $', cost_ground_premium)

# Drone Shipping Here

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
elif weight >= 11:
  cost_drone = weight * 14.25
print('Drone Shipping (Based on Weight in Ibs) $', cost_drone)

# Challenge: Try and get the code to identify the best option for the customer!

low_cost_option = min(cost_ground, cost_ground_premium, cost_drone)

if low_cost_option == cost_ground:
  method = "Ground Shipping"
elif low_cost_option == cost_ground_premium:
  method = "Ground Shipping Premium"
elif low_cost_option == cost_drone:
  method = "Drone Shipping"
print("The lowest cost shipment package will be", method)
