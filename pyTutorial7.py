string = "Banana"

print(string[0])
print(len(string))


def printingIt(string):

    for i in string:
        if i.lower() == "b": continue
        print(i)


printingIt(string)
