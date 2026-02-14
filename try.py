# Program to calculate moment (torque)

def calculate_moment(force, distance):
    moment = force * distance
    return moment

# Get user input
force = float(input("Enter the force (in Newtons): "))
distance = float(input("Enter the perpendicular distance (in meters): "))

# Calculate moment
moment = calculate_moment(force, distance)

# Display result
print(f"\nThe moment is {moment} Nm")

#comment lang
