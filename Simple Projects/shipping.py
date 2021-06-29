weight = 50

 # Ground Shipping

if weight <= 2:
    cost_ground = weight * 1.5 + 10
elif weight >= 10:
    cost_ground = weight * 5 + 20
elif weight >= 50:
    cost_ground = weight * 10 + 40
else:
    cost_ground_premium = weight * 4.75 + 50

print("Ground Shipping $", cost_ground)

# Cost Ground Premium
cost_ground_premium = 150.00

print("Cost Ground Premium $", cost_ground_premium)


# Drone Shipping

if weight <=2 :
    drone_shipping = weight * 1.5 
elif weight >= 10:
    drone_shipping = weight * 1.5 + 15
elif weight >= 50:
    drone_shipping = weight * 1.5 + 35
else:
    drone_shipping = weight * 14.25

print("Drone Shipping $", drone_shipping)


