


from pyTy9.other import createObjectEmails, outputInfoFromObject


filePath1 = './mbox-short.txt'
filePath2 = './mbox.txt'


def searchUniqueEmail(file):

    try:
       handle = open(file, 'r')
    except:
        print('Filename is not found')
        quit()


    newObject = createObjectEmails(handle)
    # print(newObject.keys())
    # print(newObject.values())
    # print(newObject.items())



    outputInfoFromObject(newObject)




searchUniqueEmail(filePath1)