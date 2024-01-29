# adds a first and last name together into a full name string
def makeFullName(firstName: str, lastName: str):
    return firstName + ' ' + lastName

# returns every other character in a string
def string_alternative(string: str):
    return string[::2]

def main():
    firstName = input("Please provide a first name: ")
    lastName = input("Please provide a last name: ")

    fullName = makeFullName(firstName, lastName)

    print(string_alternative(fullName))

main()
