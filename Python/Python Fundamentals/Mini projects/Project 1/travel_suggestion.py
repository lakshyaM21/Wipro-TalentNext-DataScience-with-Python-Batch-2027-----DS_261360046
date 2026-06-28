travel_distance = float(input("How far would you like to travel in miles? "))

if travel_distance < 3:
    vehicle_recommendation = "Bicycle"
elif travel_distance < 300:
    vehicle_recommendation = "Motor-Cycle"
else:
    vehicle_recommendation = "Super-Car"

print(f"I suggest {vehicle_recommendation} to your destination")
