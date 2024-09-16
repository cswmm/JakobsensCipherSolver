from collections import Counter
import re
import numpy as np
from const import E, LETTERS_BY_FREQUENCY

class Solver:
    
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self.key = self.initialKey(ciphertext)
        
    def subSolver(self):
        testPlaintext = self.getPlaintext(self.key)
        d = self.getD(testPlaintext)
        v = self.evaluate(d)
        kPrime = self.key
        dPrime = np.copy(d)
        a = b = 1
        
        while True:
            letterA = LETTERS_BY_FREQUENCY[a - 1]
            letterB = LETTERS_BY_FREQUENCY[a + b - 1]
            
            # swap letters a and b in kPrime
            x = kPrime.find(letterA)
            y = kPrime.find(letterB)
            kPrime = kPrime[:x] + letterB + kPrime[x+1:]
            kPrime = kPrime[:y] + letterA + kPrime[y+1:]
            a += 1
            if a+b > 26:
                a = 1
                b += 1
                if b == 26:
                    return self.key
            self.swap(dPrime, self.key.index(letterA), self.key.index(letterB))
            vPrime = self.evaluate(dPrime)
            if vPrime >= v:
                kPrime = self.key
                dPrime = np.copy(d)
            else:
                a = b = 1
                v = vPrime
                self.key = kPrime
                d = np.copy(dPrime)

    def initialKey(self, ciphertext):
        # create an initial decryption key based on the letter frequency
        count = Counter(ciphertext)
        key = [letter[0] for letter in count.most_common()]
        return ''.join(key)

    def evaluate(self, d):
        sum = 0
        for i in range(26):
            for j in range(26):
                sum += abs(d[i][j] - E[i][j])
        return sum

    def getD(self, text):
        d = np.zeros((26, 26))
        
        for i in range(0, len(text) - 1):
            char1 = text[i]
            char2 = text[i + 1]

            a = LETTERS_BY_FREQUENCY.index(char1)
            b = LETTERS_BY_FREQUENCY.index(char2)

            d[a, b] += 1

        
        for i in range(26):
            for j in range(26):
                d[i, j] = 100 * d[i, j] / (len(text) - 1)
        return d

    def swap(self, arr, i, j):
        
        # swap rows
        arr[[i, j]] = arr[[j, i]]

        # swap columns
        arr[:, [i, j]] = arr[:, [j, i]]

    def getPlaintext(self, key):
        translate = {}
        
        for i in range(26):
            translate[key[i]] = LETTERS_BY_FREQUENCY[i]
        
        out = {k: v for k, v in sorted(translate.items(), key=lambda item: item[1])}
        textKey = ''
        for k in out:
            textKey += k
        print(textKey)

        plaintext = ''
        for letter in self.ciphertext:
            plaintext += translate[letter]
        return plaintext