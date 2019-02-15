def all_stops(train):
    stops = []
    file = open("hw10 - mta train stop data.csv", "r")
    file.readline()
    for line in file:
        if line[0]==train:
            line = line.split(",")
            stops.append(line[2])
    file.close()
    return stops

def main():
    train = ""
    while train != "done":
        train = input("Please enter a train line, or 'done' to stop: ")
        if train != 'done':
            stops = all_stops(train)
            statement = train +' line: '
            for i in stops:
                statement += i+", "
            print(statement)

main()
