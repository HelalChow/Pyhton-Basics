'''
Helal Chowdhury
CS 1114
hc2324

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    old = open(complete_weather_filename, "r")
    new = open(cleaned_weather_filename, "w")

    old.readline()
    for line in old:
        lst = line.split(",")
        city = lst[0]
        date = lst[1]
        high = lst[2]
        low = lst[3]
        if lst[8].isdigit():
            rain = lst[8]
        else:
            rain = 0
        print(city, date, high, low, rain, sep = ",", file = new)
    old.close()
    new.close()


# Part B
def f_to_c(f_temperature):
    C = (f_temperature-32)*5/9
    return str(C)

def in_to_cm(inches):
    cm = inches*2.54
    return str(cm)

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    old = open(imperial_weather_filename, "r")
    new = open(metric_weather_filename, "w")
    for line in old:
        lst = line.split(',')
        city = lst[0]
        date = lst[1]
        high = f_to_c(float(lst[2]))
        low = f_to_c(float(lst[3]))
        rain = in_to_cm(float(lst[4]))
        print(city, date, high, low, rain, sep=",", file=new)
    old.close()
    new.close()


# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    op = open(weather_filename)
    read = op.readlines()
    month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    high = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    low = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(read)):
        line = read[i].strip('\n')
        lines = read[i].split(',')
        if lines[0] == city:
            position = int(lines[1][:lines[1].find('/')]) - 1
            month[position] += 1
            high[position] += float(lines[2])
            low[position] += float(lines[3])
    if unit_type == 'imperial':
        unit = 'F'
    elif unit_type == 'metric':
        unit = 'C'
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']

    print("Average temperatures for", city)
    for i in range(12):
        print(month_list[i] + ':', str(round(high[i] / month[i], 2)) + unit, 'High,',
              str(round(low[i] / month[i], 2)) + unit, 'Low')


# Part D
# Given two cities, which has higher average rainfall?

def main():
    print ("Running Part A")
    clean_data("hw8-weather.csv", "weather in imperial.csv")

    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    print()

    print ("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")
    print()

    print ("Running Part D")
    city = higher_rainfall("San Francisco", "New York", "weather in imperial.csv")
    print("The city with the higher average rainfall is:", city)

def higher_rainfall(city1, city2, weather_filename):
    file = open(weather_filename, "r")
    rain1=0
    count1=0
    rain2=0
    count2=0
    for i in file:
        lst = i.split(',')
        if lst[0]==city1:
            rain1 += float(lst[2])
            count1 += 1
        elif lst[0]==city2:
            rain2 += float(lst[2])
            count2+=1
    avg_rain1 = rain1/count1
    avg_rain2 = rain2/count2
    if avg_rain1 > avg_rain2:
        return city1
    else:
        return city2

    file.close()

main()
