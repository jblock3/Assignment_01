# Initial Prompts

renterName = input('Please enter your full name: ')
classCode = (input('Please enter your rental classification code (i.e. B for budget, D for Daily, and W for weekly): ')).upper()
daysRented = int(input('How many days did you rent your vehicle for? '))
initOdometer = int(input('What was your vehicle\'s\ initial odometer reading? '))
finOdometer = int(input('What was your vehicle\'s\ final odometer reading? '))

# Formula for kilometres driven during rental period

kmDriven = finOdometer - initOdometer

# Calculations based on the three possible class codes

if classCode == 'B':
    baseCharge = 20 * daysRented
    kmCharge = 0.30 * kmDriven
    totalCharge = baseCharge + kmCharge
    print(totalCharge)
