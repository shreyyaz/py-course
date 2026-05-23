
weight=float(input("Enter the weight: "))
unit=input("Kilograms or Pounds?(K or L): ")

if (unit=='K'):
    weight*=2.205
    unit="Lbs"
    print(f"Your weight is: {weight} {unit}")
elif(unit=='L'):
    weight/=2.205
    unit="Kgs"
    print(f"Your weight is: {weight} {unit}")
else:
    print(f" {unit} is not valid.")
