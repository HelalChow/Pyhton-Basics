class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        self.Hobbies = []
    def addHobby(self, newHobby):
        self.Hobbies.append(newHobby)
    def deleteHobby(self, oldHobby):
        self.Hobbies.remove(oldHobby)
    def birthday(self):
        print("Happy birthday,", self.Name)
    def __repr__(self):
        result = ''
        result += "Name: "
        result += self.Name + "\n"
        result += "Age: "
        result += self.Age + "\n"
        result += "Hobbies:\n"
        for i in self.Hobbies:
            result += i+"\n"
        return result

def main():
    people_names = []
    people = []
    seen_exit = False
    while seen_exit == False:
        print("\nSelect one of the following options:")
        print("====================================")
        print("1. Create a new Person")
        print("2. Add to an existing person's hobbies")
        print("3. Delete an existing person's hobbies")
        print("4. Someone has a birthday")
        print("5. See a list of people")
        choice = input("6. Exit\n")
        if choice == "1":
            name = input("Please enter a name: ")
            people_names.append(name)
            people.append(Person(name, input("Please enter an age: ")))
        elif choice == "2":
            name = input("Who is receiving a new hobby? ")
            index = people_names.index(name)
            person = people[index]
            hobby = input("What is this person's new hobby? ")
            if person.Hobbies.count(hobby)==0:
                person.addHobby(hobby)
        elif choice == "3":
            name = input("Who is losing a hobby? ")
            index = people_names.index(name)
            person = people[index]
            person.deleteHobby(input("What hobby are you deleting? "))
        elif choice == "4":
            name = input("Who is having a birthday? ")
            index = people_names.index(name)
            person = people[index]
            person.birthday()
        elif choice == "5":
            for i in people:
                print(i)
        elif choice == "6":
            print("Goodbye!")
            seen_exit = True

main()



