# for in
x = [1,31,454,21,44,355,12234,422,42,52,52,4242424,3535,234555352425,53,535,3,353,535,3534,3535]

def biggestNum(array):
    biggest = None
    for i in array:
        if biggest is None:
            biggest = i
            print(i, "New big")

        elif i > biggest:
            biggest = i
            print(i, "New big")
        else:
            print(biggest, "Still the biggest")

    return biggest

res = biggestNum(x)
print("Result",res)
