def getuniqeEmailsArray(handle):
    mylist=[]

    for line in handle:
        line = line.strip()
        if line.startswith('From:'):
            mylist.append(line.split(" ")[1])

    mylist = list(set(mylist))
    return mylist

def printEmails(list):
    count = 0
    for i in list:
        print(i)
        count += 1
    print("Emails:",count)


def createObjectEmails(handle):
    obj = {}

    for line in handle:
        line = line.strip()
        if line.startswith('From:'):
            email = line.split(" ")[1]
            # Smart move
            obj[email] = obj.get(email, 0) + 1

    return obj


def outputInfoFromObject(obj):
     for [key,value]in obj.items():
        print(key,":[",value,"]")
