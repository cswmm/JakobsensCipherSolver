import re
import matplotlib.pyplot as plt
import random
import numpy as np
from jakobsens import Solver
from const import LETTERS, LETTERS_BY_FREQUENCY

# warning: computationally expensive
# takes a long time to run!

class Tester:
    def __init__(self):
        f = open("mobydick.txt", "r")
        self.source = re.split(r'\s', f.read())
        f.close()

    def test(this, size):
        # create a random key
        targetKey = ''.join(random.sample(LETTERS, 26))

        # create test plaintext
        s = ''
        while len(s) < size:
            word = random.choice(this.source)
            for ch in word:
                if ch.isalpha():
                    s += ch.upper()
    
        # encrypt
        # create key dict
        enKey = {}
        for i in range(26):
            enKey[LETTERS[i]] = targetKey[i]

        # translate to ciphertext
        c = ''
        for ch in s:
            c += enKey[ch]
            
        # use jakobsens alg
        result = Solver(c)
        result.key = result.subSolver()

        # create decryption dict
        deKey = {}
        for i in range(26):
            deKey[result.key[i]] = LETTERS_BY_FREQUENCY[i]
        
        # output key is arranged by letter frequency
        # convert to alphabetical to compare accuracy
        out = {k: v for k, v in sorted(deKey.items(), key=lambda item: item[1])}
        textKey = ''
        for k in out:
            textKey += k

        # measure accuracy
        numCorrect = 0
        for i in range(26):
            if textKey[i] == targetKey[i]:
                numCorrect += 1
        keyAcc = (numCorrect / 26) * 100

        numCorrect = 0
        print
        for i in range(len(c)):
            if deKey[c[i]] == s[i]:
                numCorrect += 1
        textAcc = (numCorrect / len(s)) * 100

        return keyAcc, textAcc


# gather data
keyResults = []
textResults = []
tester = Tester()
for i in range(100, 1100, 100):
    kR = []
    tR = []
    for x in range(10):
        result = tester.test(i)
        kR.append(result[0])
        tR.append(result[1])
    keyResults.append(np.mean(kR))
    textResults.append(np.mean(tR))

x = np.arange(100, 1100, 100)

plt.plot(x, keyResults)
plt.ylabel('Key Accuracy')
plt.show()

plt.plot(x, textResults)
plt.ylabel('Plaintext Accuracy')
plt.show()