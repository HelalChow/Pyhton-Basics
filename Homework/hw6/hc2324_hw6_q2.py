def print_month_calander(num_of_days, starting_day):
    position = starting_day
    print("Mon\tTue\tWed\tThr\tFri\tSat\tSun")
    print("\t"*(starting_day-1), end="")
    for i in range(1, num_of_days+1):
        print(i, end = "\t")
        position+=1
        if position==8:
            print('\n')
            position=1
    if position !=1:
        print('\n')
    return position

def check_leap_year(year):
    if year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False

def print_year_calander(year, starting_day):
    start=starting_day
    months = ['','January','February','March','April','May','June','July','August','Septermber','October','November','December']
    for i in range(1, 13):
        days= check_day(i, year)
        print(months[i], year)
        start=print_month_calander(days, start)

def check_day(i, year):
    if i < 8:
        if i % 2 == 1:
            days = 31
        elif i == 2:
            if check_leap_year(year) == False:
                days = 28
            else:
                days = 29
        else:
            days = 30
    if i >= 8:
        if i % 2 == 0:
            days = 31
        else:
            days = 30
    return days

def main():
    year = int(input("Please enter the year: "))
    day = int(input("Please enter a number from 1-7 that represents the first of in the week of January 1st: "))
    print('\n')
    print_year_calander(year, day)

main()