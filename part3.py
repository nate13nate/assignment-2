# the example in the assignment converts centimeters to inches, while the assignment says to convert inches to centimeters
# i converted inches to centimeters

def main():
    height = ''
    heightsInInches = []
    print('Type "end" at any time to stop the program.')

    while True:
        height = input('Input a customer height in inches: ')
        if height == 'end': break

        heightsInInches.append(float(height))
        heightsInCenti = [height * 2.54 for height in heightsInInches]
        print('Inches: ' + str(heightsInInches))
        print('Centimeters: ' + str(heightsInCenti) + '\n')

main()
