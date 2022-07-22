(x,y) = ('Hello', "World")

array = [5,6,37,8,91,2,3,4]

print(sorted(array, reverse=True))

# Shorter version

d = {"a": 31, "b": 321, "c": 3, "d": 345, "e": 53, "f": 36}

print(sorted([(v,k) for k,v in d.items()], ))
