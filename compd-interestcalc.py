while True:
    principle=float(input("Enter the principle amount: "))
    if principle<0:
        print("Principle cannot be less than zero.")
    else:
        break

while True:
    rate=float(input("Enter the rate : "))
    if rate<0:
        print("rate cannot be less than zero.")
    else:
        break

while True:
    time=float(input("Enter the time: "))
    if time<0:
        print("time cannot be less than zero.")
    else:
        break

total=principle* pow((1+ rate/100),time)
print(f"Balance after {time} years/s: Rs{total:.2f} and the Interest is {total-principle:.2f}")