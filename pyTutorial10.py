friends1 = ['Kenobi','Green','Varita','Yuana']
friends2 = ['ddasg','dggadagd','dadqewe','qwewtww']

friends = friends1 + friends2


def greetWithNewYear(people):
    for friend in people:
        print("Happy New Year " +friend.capitalize() +"!")


greetWithNewYear(friends)

print(dir(friends))
