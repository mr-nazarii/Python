handle = open('poem/nice.txt', 'r')

d = {}

for line in handle:
    line = line.rstrip('\n')
    for word in line.split(' '):
        d[word] = d.get(word, 1) + 1


print(sorted([(k,v) for k,v in d.items()][:10], reverse=True))
