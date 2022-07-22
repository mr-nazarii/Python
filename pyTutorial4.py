
flag = True

rawnum = input("Enter a number to multiply on 2\n")
while flag == True:
    rawnum = input("Try again\n")

    try:
        rawnum = int(rawnum)
    except:
        print("Invalid input")
        continue

    print("2 * ",rawnum,"=",2 * rawnum)
    flag = False
