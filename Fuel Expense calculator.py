print("       FUEL COST CALCULATOR       ")

# Taking input from the user

distance = float(input("Enter travelling distance (km): "))

mileage = float(input("Enter vehicle mileage (km/litre): "))

price = float(input("Enter petrol price per litre (Rs): "))

# Calculating fuel required

fuel = distance / mileage

# Calculating total fuel cost

cost = fuel * price

# Displaying the result

print("\n           FUEL REPORT             ")

print("Travelling Distance:", distance, "km")

print("Vehicle Mileage:", mileage, "km/litre")

print("Fuel Required:", round(fuel, 2), "litres")

print("Total Fuel Cost: Rs.", round(cost, 2))

print("Thank you for using Fuel Cost Calculator!")
