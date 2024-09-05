import random
import re
import matplotlib.pyplot as plt
import numpy as np


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def evaluation(d):
    e = [['A', 0.0817], ['B', 0.0149], ['C', 0.0278], ['D', 0.0425],
         ['E', 0.1270], ['F', 0.0223], ['G', 0.0202], ['H', 0.0609],
         ['I', 0.0697], ['J', 0.0015], ['K', 0.0077], ['L', 0.0403],
         ['M', 0.0241], ['N', 0.0675], ['O', 0.0751], ['P', 0.0193],
         ['Q', 0.0010], ['R', 0.0599], ['S', 0.0633], ['T', 0.0906],
         ['U', 0.0276], ['V', 0.0098], ['W', 0.0236], ['X', 0.0015],
         ['Y', 0.0197], ['Z', 0.0007]]
    
    sum = 0
    for i in range(26):
        sum += abs(d[i][1] - e[i][1])
    return sum





def subSolver(ciphertext):
    d = []
    for letter in letters:
        d.append([letter, 0])
    for letter in ciphertext:
        d[ord(letter) - 65][1] += 1
    for item in d:
        item[1] = item[1] / len(ciphertext)

    k = letters
    v = evaluation(d)
    newK = k
    newD = d
    a = b = 1
    
    while True:
        s = sorted(d, key=lambda x: x[1], reverse=True)
        letterA = newD.index(s[a-1])
        letterB = newD.index(s[a+b-1])
        
        a += 1
        if a+b <= 27:
            temp = newD[letterA]
            newD[letterA] = newD[letterB]
            newD[letterB] = temp
            newK = ''
            for item in newD:
                newK += item[0]
        a = 1
        b = b + 1
        if b == 26:
            return k

        newV = evaluation(newD)
        
        if newV >= v:
            newK = k
            newD = d
        else:
            v = newV
            k = newK
            d = newD
            a = b = 1

testEnKey = 'MQLZVTHPXNCAYRJGSFOBWKDIEU'
testDeKey = 'LTKWYRPGXOVCAQSHBNJFZEUIMD'


source = re.split('\s', 'Super Smash Bros is a crossover platform fighting gameseries published by Nintendo. The series was created by Masahiro Sakurai, who has directed every game in the series. The series is known for its unique gameplay objective which differs from that of traditional fighters, in that the aim is to increase damage counters and knock opponents off the stage instead of depleting life bars. The series primarily features characters from various Nintendo franchises, including Super Mario, Donkey Kong, The Legend of Zelda, Metroid, Yoshi, Kirby, Star Fox, and Pokemon, as well as third-party franchises like Sonic the Hedgehog, Street Fighter, and Final Fantasy. The original Super Smash Bros. had only 12 playable characters, with the roster count rising for each successive game and later including third-party characters, with Ultimate containing every character playable in the previous games. In Melee, Brawl, and Ultimate, some characters are able to transform into different forms that have different styles of play and sets of moves. Every game in the series has been well received by critics, with multiple installments being listed among the greatest video games of all time. Much praise has been given to their multiplayer features, spawning a large competitive community that has been featured in several gaming tournaments. Pre-release screenshot of Ultimate featuring Ganondorf, Link, Mario and Mega Man battle on the "Great Plateau Tower" stage, based on the location from The Legend of Zelda: Breath of the Wild Gameplay in the Super Smash Bros. series differs from many fighting games.[1] Instead of winning by depleting an opponents life bar, players seek to launch their opponents off the stage and out of bounds. Characters have a damage total which rises as they take damage, represented by a percentage value that measures up to 999%. As a characters percentage rises, they suffer stronger knockback from enemy attacks.[2] To knock out an opponent, the player must knock that character outside the stages boundaries in any direction.[3] When a character is launched off the stage, the character can attempt to "recover" by using jumping moves and abilities to return to the stage.[2] Some characters have an easier time recovering onto the stage than others due to their moves and abilities. Additionally, some characters vary in weight, with lighter characters being easier to launch than heavy characters.')


def testSubSolver(size):
    s = ''

    # create test plaintext
    while len(s) < size:
        s += random.choice(source)
    s = ''.join(ch for ch in s if ch.isalpha())
 
    # encrypt
    # create key dict
    enKey = {}
    for i in range(len(letters)):
        enKey[letters[i]] = testEnKey[i]

    # translate to ciphertext
    c = ''
    for ch in s:
        if (ch.isalpha()):
            c += enKey[ch.upper()]
        
    # use jakobsens alg
    result = subSolver(c)

    # measure accuracy
    numCorrect = 0
    for i in range(len(letters)):
        if result[i] == testDeKey[i]:
            numCorrect += 1
    keyAcc = (numCorrect / len(letters)) * 100

    deKey = {}
    for i in range(len(letters)):
        deKey[letters[i]] = result[i]

    numCorrect = 0
    for i in range(len(c)):
        if deKey[c[i]] == s[i]:
            numCorrect += 1
    textAcc = (numCorrect / len(s)) * 100

    return keyAcc, textAcc

# gather data
keyResults = []
textResults = []
for i in range(100, 1100, 100):
    keyR = []
    textR = []
    for j in range(10):
        result = testSubSolver(i)
        keyR.append(result[0])
        textR.append(result[1])
    print(keyR)
    keyResults.append(np.mean(keyR))
    textResults.append(np.mean(textR))




x = []
yKey = []
yLetter = []



plt.plot(x, yKey)
plt.show()