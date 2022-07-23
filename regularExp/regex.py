import re


filename = "texts/mbox-short.txt"


def findEmails(handle):
    d = {}
    for line in handle:
        line = line.rstrip()
        # if re.search("^From:",line):
        #     line = line.replace('From: ','')
        #     d[line] = d.get(line, 1) + 1

        emails = re.findall('\S+@\S+',line)
        for email in emails:
            email = email.strip('<>;:()')
            d[email] = d.get(email, 1) + 1

    return d


def printEmails(filepath):

    try:
        fhand = open(filepath,"r")
    except:
        print("Could not open file: " + filepath)
        quit()

    emailsObject = findEmails(fhand)

    print({k:v for k,v in sorted(emailsObject.items(), key=lambda  item: item[1], reverse=True )})


printEmails(filename)
