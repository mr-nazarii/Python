from pyTy9.other import getuniqeEmailsArray, printEmails


filePath1 = './texts/mbox-short.txt'
filePath2 = './texts/mbox.txt'


def searchUniqueEmail(file):

    try:
       handle = open(file, 'r')
    except:
        print('Filename is not found')
        quit()

    mylist = getuniqeEmailsArray(handle)
    printEmails(mylist)


searchUniqueEmail(filePath2)
