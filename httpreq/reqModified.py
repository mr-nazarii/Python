from urllib import request , parse , error

fhand = request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}

for line in fhand:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 1) + 1
print({k:v for k,v in sorted(counts.items(), key=lambda item: item[1] ,reverse=True)})
