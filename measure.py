import numpy as np

f = open("mobydick.txt", "r")
source = [c.upper() for c in f.read() if c.isalpha()]
size = len(source)
E = np.zeros((26, 26))

numDigrams = 0
for i in range(size - 1):
    E[ord(source[i]) - 65][ord(source[i+1]) - 65] += 1
    numDigrams += 1

for i in range(26):
    for j in range(26):
        E[i][j] = 100 * E[i][j] / numDigrams

for x in E:
    print([float('{:.3f}'.format(i)) for i in x],',')