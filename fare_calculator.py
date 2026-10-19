# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")

if name.strip() == "": 
    print("Invalide name. Name must not be empty.")
    name = input("Enter passenger name: ")

distance = (input("Enter distance (km): "))
try:
    if float(distance) <= 0:
        print("Invalid distance. Number must be greater than 0.")
        distance = input("Enter distance (km): ")
except ValueError:
    print("Invalid distance. You must enter a valid number.")
    distance = input("Enter distance (km): ")

passengers = (input("Enter number of passengers: "))
if not passengers.isdigit() or not int(passengers) <= 0:
    print("Invalid passengers. Number must be a positive whole number.")
    passengers = int(input("Enter number of passengers: "))
    
total_fare = float(distance) * FARE_RATE * int(passengers)

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
