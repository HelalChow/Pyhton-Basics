day= input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call: "))

if day=="Sat" or day=="Sun":
    total = float(0.15 * duration)
else:
    if time<800 or  time>1800:
        total = float(0.25 * duration)
    else:
        total = float(0.4 * duration)
print("This call wil cost $" + str(total) )