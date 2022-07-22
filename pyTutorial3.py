flag = True

while flag == True:
    nam = input("Whats your name?: \n")
    flag = False
    print("Welcome " + nam + "\n To what floor whould you like to go? (European floor converter)\n")
    floor = input("What floor?: \n")
    print("Your floor in American:", int(floor) + 1)
