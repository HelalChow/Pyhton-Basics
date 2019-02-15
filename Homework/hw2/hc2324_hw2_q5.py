days_j = int(input("Please enter the number of days John has worked:"))
hours_j = int(input("Please enter the number of hours John has worked:"))
minutes_j = int(input("Please enter the number of minutes John has worked:"))
days_b = int(input("Please enter the number of days Bill has worked:"))
hours_b = int(input("Please enter the number of hours Bill has worked:"))
minutes_b = int(input("Please enter the number of minutes Bill has worked:"))
days_min = (days_j + days_b)*24*60
hours_min = (hours_j + hours_b)*60
minutes_total = minutes_j + minutes_b + days_min + hours_min
hours_total = minutes_total//60
minutes = minutes_total%60
days = hours_total//24
hours = hours_total%24
print("The total time both of them worked together is:", days, "days", hours, "hours and", minutes, "minutes.")




