from collections import Counter
import random
from string import ascii_uppercase
import matplotlib.pyplot as plt
import numpy as np
from const import E, LETTERS, LETTERS_BY_FREQUENCY

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
            self.swap(dPrime, LETTERS_BY_FREQUENCY.index(letterA), LETTERS_BY_FREQUENCY.index(letterB))
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
    

c = 'SUPER SMASH BROSI SACRO SSOVE RPLAT FORMF IGHTI NGGAM ESERI ESPUB LISHE DBYNI NTEND OTHES ERIES WASCR EATED BYMAS AHIRO SAKUR AIWHO HASDI RECTE DEVER YGAME INTHE SERIE STHES ERIES ISKNO WNFOR ITSUN IQUEG AMEPL AYOBJ ECTIV EWHIC HDIFF ERSFR OMTHA TOFTR ADITI ONALF IGHTE RSINT HATTH EAIMI STOIN CREAS EDAMA GECOU NTERS ANDKN OCKOP PONEN TSOFF THEST AGEIN STEAD OFDEP LETIN GLIFE BARST HESER IESPR IMARI LYFEA TURES CHARA CTERS FROMV ARIOU SNINT ENDOF RANCH ISESI NCLUD INGSU PERMA RIODO NKEYK ONGTH ELEGE NDOFZ ELDAM ETROI DYOSH IKIRB YSTAR FOXAN DPOKE MONAS WELLA STHIR DPART YFRAN CHISE SLIKE SONIC THEHE DGEHO GSTRE ETFIG HTERA NDFIN ALFAN TASYT HEORI GINAL SUPER SMASH BROSH ADONL YPLAY ABLEC HARAC TERSW ITHTH EROST ERCOU NTRIS INGFO REACH SUCCE SSIVE GAMEA NDLAT ERINC LUDIN GTHIR DPART YCHAR ACTER SWITH ULTIM ATECO NTAIN INGEV ERYCH ARACT ERPLA YABLE INTHE PREVI OUSGA MESIN MELEE BRAWL ANDUL TIMAT ESOME CHARA CTERS AREAB LETOT RANSF ORMIN TODIF FEREN TFORM STHAT HAVED IFFER ENTST YLESO FPLAY ANDSE TSOFM OVESE VERYG AMEIN THESE RIESH ASBEE NWELL RECEI VEDBY CRITI CSWIT HMULT IPLEI NSTAL LMENT SBEIN GLIST EDAMO NGTHE GREAT ESTVI DEOGA MESOF ALLTI MEMUC HPRAI SEHAS BEENG IVENT OTHEI RMULT IPLAY ERFEA TURES SPAWN INGAL ARGEC OMPET ITIVE COMMU NITYT HATHA SBEEN FEATU REDIN SEVER ALGAM INGTO URNAM ENTSP REREL EASES CREEN SHOTO FULTI MATEF EATUR INGGA NONDO RFLIN KMARI OANDM EGAMA NBATT LEONT HEGRE ATPLA TEAUT OWERS TAGEB ASEDO NTHEL OCATI ONFRO MTHEL EGEND OFZEL DABRE ATHOF THEWI LDGAM EPLAY INTHE SUPER SMASH BROSS ERIES DIFFE RSFRO MMANY FIGHT INGGA MESIN STEAD OFWIN NINGB YDEPL ETING ANOPP ONENT SLIFE BARPL AYERS SEEKT OLAUN CHTHE IROPP ONENT SOFFT HESTA GEAND OUTOF BOUND SCHAR ACTER SHAVE ADAMA GETOT ALWHI CHRIS ESAST HEYTA KEDAM AGERE PRESE NTEDB YAPER CENTA GEVAL UETHA TMEAS URESU PTOAS ACHAR ACTER SPERC ENTAG ERISE STHEY SUFFE RSTRO NGERK NOCKB ACKFR OMENE MYATT ACKST OKNOC KOUTA NOPPO NENTT HEPLA YERMU STKNO CKTHA TCHAR ACTER OUTSI DETHE STAGE SBOUN DARIE SINAN YDIRE CTION WHENA CHARA CTERI SLAUN CHEDO FFTHE STAGE THECH ARACT ERCAN ATTEM PTTOR ECOVE RBYUS INGJU MPING MOVES ANDAB ILITI ESTOR ETURN TOTHE STAGE SOMEC HARAC TERSH AVEAN EASIE RTIME RECOV ERING ONTOT HESTA GETHA NOTHE RSDUE TOTHE IRMOV ESAND ABILI TIESA DDITI ONALL YSOME CHARA CTERS VARYI NWEIG HTWIT HLIGH TERCH ARACT ERSBE INGEA SIERT OLAUN CHTHA NHEAV YCHAR ACTERS'
c = c.replace(' ', '')
solver = Solver(c)
solver.key = solver.subSolver()
print(solver.getPlaintext(solver.key))
solver.key = solver.subSolver()
print(solver.getPlaintext(solver.key))
solver.key = solver.subSolver()
print(solver.getPlaintext(solver.key))



# attempt at alg 2

# 

# source = re.split('\s', 'Super Smash Bros is a crossover platform fighting gameseries published by Nintendo. The series was created by Masahiro Sakurai, who has directed every game in the series. The series is known for its unique gameplay objective which differs from that of traditional fighters, in that the aim is to increase damage counters and knock opponents off the stage instead of depleting life bars. The series primarily features characters from various Nintendo franchises, including Super Mario, Donkey Kong, The Legend of Zelda, Metroid, Yoshi, Kirby, Star Fox, and Pokemon, as well as third-party franchises like Sonic the Hedgehog, Street Fighter, and Final Fantasy. The original Super Smash Bros. had only 12 playable characters, with the roster count rising for each successive game and later including third-party characters, with Ultimate containing every character playable in the previous games. In Melee, Brawl, and Ultimate, some characters are able to transform into different forms that have different styles of play and sets of moves. Every game in the series has been well received by critics, with multiple installments being listed among the greatest video games of all time. Much praise has been given to their multiplayer features, spawning a large competitive community that has been featured in several gaming tournaments. Pre-release screenshot of Ultimate featuring Ganondorf, Link, Mario and Mega Man battle on the "Great Plateau Tower" stage, based on the location from The Legend of Zelda: Breath of the Wild Gameplay in the Super Smash Bros. series differs from many fighting games.[1] Instead of winning by depleting an opponents life bar, players seek to launch their opponents off the stage and out of bounds. Characters have a damage total which rises as they take damage, represented by a percentage value that measures up to 999%. As a characters percentage rises, they suffer stronger knockback from enemy attacks.[2] To knock out an opponent, the player must knock that character outside the stages boundaries in any direction.[3] When a character is launched off the stage, the character can attempt to "recover" by using jumping moves and abilities to return to the stage.[2] Some characters have an easier time recovering onto the stage than others due to their moves and abilities. Additionally, some characters vary in weight, with lighter characters being easier to launch than heavy characters.')


# def testSubSolver(size):
#     s = ''

#     # create test plaintext
#     while len(s) < size:
#         s += random.choice(source)
#     s = ''.join(ch for ch in s if ch.isalpha())
 
#     # encrypt
#     # create key dict
#     enKey = {}
#     for i in range(len(letters)):
#         enKey[letters[i]] = testEnKey[i]

#     # translate to ciphertext
#     c = ''
#     for ch in s:
#         if (ch.isalpha()):
#             c += enKey[ch.upper()]
        
#     # use jakobsens alg
#     result = subSolver(c)

#     # measure accuracy
#     numCorrect = 0
#     for i in range(len(letters)):
#         if result[i] == testDeKey[i]:
#             numCorrect += 1
#     keyAcc = (numCorrect / len(letters)) * 100

#     deKey = {}
#     for i in range(len(letters)):
#         deKey[letters[i]] = result[i]

#     numCorrect = 0
#     for i in range(len(c)):
#         if deKey[c[i]] == s[i]:
#             numCorrect += 1
#     textAcc = (numCorrect / len(s)) * 100

#     return keyAcc, textAcc

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