import matplotlib.pyplot as plt
import random
import urllib.request
from jakobsens import Solver
from const import LETTERS

# class Tester:
#     # TODO implement tester
#     # source = re.split('\s', 'Super Smash Bros is a crossover platform fighting gameseries published by Nintendo. The series was created by Masahiro Sakurai, who has directed every game in the series. The series is known for its unique gameplay objective which differs from that of traditional fighters, in that the aim is to increase damage counters and knock opponents off the stage instead of depleting life bars. The series primarily features characters from various Nintendo franchises, including Super Mario, Donkey Kong, The Legend of Zelda, Metroid, Yoshi, Kirby, Star Fox, and Pokemon, as well as third-party franchises like Sonic the Hedgehog, Street Fighter, and Final Fantasy. The original Super Smash Bros. had only 12 playable characters, with the roster count rising for each successive game and later including third-party characters, with Ultimate containing every character playable in the previous games. In Melee, Brawl, and Ultimate, some characters are able to transform into different forms that have different styles of play and sets of moves. Every game in the series has been well received by critics, with multiple installments being listed among the greatest video games of all time. Much praise has been given to their multiplayer features, spawning a large competitive community that has been featured in several gaming tournaments. Pre-release screenshot of Ultimate featuring Ganondorf, Link, Mario and Mega Man battle on the "Great Plateau Tower" stage, based on the location from The Legend of Zelda: Breath of the Wild Gameplay in the Super Smash Bros. series differs from many fighting games.[1] Instead of winning by depleting an opponents life bar, players seek to launch their opponents off the stage and out of bounds. Characters have a damage total which rises as they take damage, represented by a percentage value that measures up to 999%. As a characters percentage rises, they suffer stronger knockback from enemy attacks.[2] To knock out an opponent, the player must knock that character outside the stages boundaries in any direction.[3] When a character is launched off the stage, the character can attempt to "recover" by using jumping moves and abilities to return to the stage.[2] Some characters have an easier time recovering onto the stage than others due to their moves and abilities. Additionally, some characters vary in weight, with lighter characters being easier to launch than heavy characters.')
    
#     def test(this, size):
#         # create a random key
#         k = ''.join(random.sample(LETTERS))

#         # create test plaintext
#         s = ''
#         while len(s) < size:
#             s += random.choice(this.source)
#         s = ''.join(ch.upper() for ch in s if ch.isalpha())
    
#         # encrypt
#         # create key dict
#         enKey = {}
#         for i in range(len(k)):
#             enKey[LETTERS[i]] = k[i]

#         # translate to ciphertext
#         c = ''
#         for ch in s:
#             c += enKey[ch]
            
#         # use jakobsens alg
#         result = Solver(c)
#         result.key = result.subSolver()

#         # sort key alphabetically instead of by frequency
#         deKey = {}
#         for i in range(26):
#             deKey[result.key[i]] = LETTERS_BY_FREQUENCY[i]
        
#         out = {k: v for k, v in sorted(deKey.items(), key=lambda item: item[1])}
#         textKey = ''
#         for k in out:
#             textKey += k

#         # measure accuracy
#         numCorrect = 0
#         for i in range(len(LETTERS)):
#             if result[i] == k[i]:
#                 numCorrect += 1
#         keyAcc = (numCorrect / len(LETTERS)) * 100

#         numCorrect = 0
#         for i in range(len(c)):
#             if deKey[c[i]] == s[i]:
#                 numCorrect += 1
#         textAcc = (numCorrect / len(s)) * 100

#         return keyAcc, textAcc


uf = urllib.request.urlopen("https://en.wikipedia.org/wiki/Super_Smash_Bros.")
html = uf.read()

# # gather data
# keyResults = []
# textResults = []
# for i in range(100, 1100, 100):
#     keyR = []
#     textR = []
#     for j in range(10):
#         result = testSubSolver(i)
#         keyR.append(result[0])
#         textR.append(result[1])
#     print(keyR)
#     keyResults.append(np.mean(keyR))
#     textResults.append(np.mean(textR))


# x = []
# yKey = []
# yLetter = []

# plt.plot(x, yKey)
# plt.show()