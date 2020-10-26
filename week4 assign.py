# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
if hrs >= 40:
    pay = (40 * rate + (hrs - 40) * rate * 1.5)
    print(pay)
else:
    pay = hrs * rate
    print(pay)
