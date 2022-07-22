string = " Ini Mini Mani Mo   "

print(string)
print(string.strip())
print(string.replace(" ",""))

if "I" in string:
    print("Its here")

print(string.startswith("I"))
print(string.startswith(" "))


emailraw = "https://www.freecodecamp.org/learn/scientific-computing-with-python/lalalupsi@gmail.com/python-for-everybody/intermediate-strings"

start = emailraw.find("@")
end = emailraw.find("/",start)
print(start)
print(end)
res = emailraw[start:end]
print(res)

fullemail = emailraw.split("/")

print(fullemail)

for i in fullemail:
    if "@" in i:
        print(i)
