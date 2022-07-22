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
