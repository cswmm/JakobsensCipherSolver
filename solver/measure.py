import numpy as np

f = open("mobydick.txt", "r")
source = [c.upper() for c in f.read() if c.isalpha()]
f.close()
size = len(source)
E = np.zeros((26, 26))

# count letter frequency
count = {}
for ch in source:
    count[ch] = count.get(ch, 0) + 1

for k, v in count.items():
    count[k] = v / size

countByFreq = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
lettersByFreq = ''
for ch in countByFreq.keys():
    lettersByFreq += ch

# get letters by frequency to be used as a const
print(lettersByFreq)

print(countByFreq)

# create digram matrix to be used in const

numDigrams = 0
for i in range(size - 1):
    E[lettersByFreq.find(source[i])][lettersByFreq.find(source[i + 1])] += 1
    numDigrams += 1

for i in range(26):
    for j in range(26):
        E[i][j] = 100 * E[i][j] / numDigrams

for x in E:
    print([float('{:.3f}'.format(i)) for i in x],',')