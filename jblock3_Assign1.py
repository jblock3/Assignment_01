# Initial Prompts

renterName = input('Please enter your full name: ')
classCode = (input('Please enter your rental classification code (i.e. B for budget, D for Daily, and W for weekly): ')).upper()
daysRented = int(input('How many days did you rent your vehicle for? '))
initOdometer = int(input('What was your vehicle\'s initial odometer reading? '))     # Initial odometer reading
finOdometer = int(input('What was your vehicle\'s final odometer reading? '))     # Final odometer reading

# Formula for kilometres driven during rental period

kmDriven = finOdometer - initOdometer

# Calculations based on the three possible class codes

if classCode == 'B':     # For budgeted rental
    baseCharge = 20 * daysRented
    kmCharge = 0.30 * kmDriven
    totalCharge = baseCharge + kmCharge
elif classCode == 'D':
    avgKmPerDay = kmDriven / daysRented     # Calculation of average Kms driven per day during rental period
    baseCharge = 50 * daysRented
    if avgKmPerDay <= 100:
        kmCharge = 0.00
    else:
        kmCharge = 0.30 * (kmDriven - 100)     # - 100 to ensure calculation of only Kms above 100km limit
    totalCharge = baseCharge + kmCharge
