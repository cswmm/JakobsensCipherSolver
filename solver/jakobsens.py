import random
import re
import matplotlib.pyplot as plt
import numpy as np
from const import E


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def evaluation(d):
    sum = 0
    for i in range(26):
        for j in range(26):
            sum += abs(d[i][j] - E[i][j])
    return sum




def subSolver(ciphertext):
    d = np.zeros((26, 26))
    for i in range(len(ciphertext) - 1):
        d[ord(ciphertext[i]) - 65][ord(ciphertext[i+1]) - 65] += 1
    
    for i in range(26):
        for j in range(26):
            d[i][j] /= len(ciphertext)

    k = letters
    v = evaluation(d)
    kPrime = k
    dPrime = d
    a = b = 1
    
    while True:
        s = sorted(d, key=lambda x: x[1], reverse=True)
        letterA = dPrime.index(s[a-1])
        letterB = dPrime.index(s[a+b-1])
        
        a += 1
        if a+b <= 27:
            temp = dPrime[letterA]
            dPrime[letterA] = dPrime[letterB]
            dPrime[letterB] = temp
            kPrime = ''
            for item in dPrime:
                kPrime += item[0]
        a = 1
        b = b + 1
        if b == 26:
            return k

        vPrime = evaluation(dPrime)
        
        if vPrime >= v:
            kPrime = k
            dPrime = d
        else:
            v = vPrime
            k = kPrime
            d = dPrime
            a = b = 1

c = "UWRGT UOCUJ DTQUK UCETQ UUQXG TRNCV HQTOH KIJVK PIICO GUGTK GURWD NKUJG FDAPK PVGPF QVJGU GTKGU YCUET GCVGF DAOCU CJKTQ UCMWT CKYJQ JCUFK TGEVG FGXGT AICOG KPVJG UGTKG UVJGU GTKGU KUMPQ YPHQT KVUWP KSWGI COGRN CAQDL GEVKX GYJKE JFKHH GTUHT QOVJC VQHVT CFKVK QPCNH KIJVG TUKPV JCVVJ GCKOK UVQKP ETGCU GFCOC IGEQW PVGTU CPFMP QEMQR RQPGP VUQHH VJGUV CIGKP UVGCF QHFGR NGVKP INKHG DCTUV JGUGT KGURT KOCTK NAHGC VWTGU EJCTC EVGTU HTQOX CTKQW UPKPV GPFQH TCPEJ KUGUK PENWF KPIUW RGTOC TKQFQ PMGAM QPIVJ GNGIG PFQHB GNFCO GVTQK FAQUJ KMKTD AUVCT HQZCP FRQMG OQPCU YGNNC UVJKT FRCTV AHTCP EJKUG UNKMG UQPKE VJGJG FIGJQ IUVTG GVHKI JVGTC PFHKP CNHCP VCUAV JGQTK IKPCN UWRGT UOCUJ DTQUJ CFQPN ARNCA CDNGE JCTCE VGTUY KVJVJ GTQUV GTEQW PVTKU KPIHQ TGCEJ UWEEG UUKXG ICOGC PFNCV GTKPE NWFKP IVJKT FRCTV AEJCT CEVGT UYKVJ WNVKO CVGEQ PVCKP KPIGX GTAEJ CTCEV GTRNC ACDNG KPVJG RTGXK QWUIC OGUKP OGNGG DTCYN CPFWN VKOCV GUQOG EJCTC EVGTU CTGCD NGVQV TCPUH QTOKP VQFKH HGTGP VHQTO UVJCV JCXGF KHHGT GPVUV ANGUQ HRNCA CPFUG VUQHO QXGUG XGTAI COGKP VJGUG TKGUJ CUDGG PYGNN TGEGK XGFDA ETKVK EUYKV JOWNV KRNGK PUVCN NOGPV UDGKP INKUV GFCOQ PIVJG ITGCV GUVXK FGQIC OGUQH CNNVK OGOWE JRTCK UGJCU DGGPI KXGPV QVJGK TOWNV KRNCA GTHGC VWTGU URCYP KPICN CTIGE QORGV KVKXG EQOOW PKVAV JCVJC UDGGP HGCVW TGFKP UGXGT CNICO KPIVQ WTPCO GPVUR TGTGN GCUGU ETGGP UJQVQ HWNVK OCVGH GCVWT KPIIC PQPFQ THNKP MOCTK QCPFO GICOC PDCVV NGQPV JGITG CVRNC VGCWV QYGTU VCIGD CUGFQ PVJGN QECVK QPHTQ OVJGN GIGPF QHBGN FCDTG CVJQH VJGYK NFICO GRNCA KPVJG UWRGT UOCUJ DTQUU GTKGU FKHHG TUHTQ OOCPA HKIJV KPIIC OGUKP UVGCF QHYKP PKPID AFGRN GVKPI CPQRR QPGPV UNKHG DCTRN CAGTU UGGMV QNCWP EJVJG KTQRR QPGPV UQHHV JGUVC IGCPF QWVQH DQWPF UEJCT CEVGT UJCXG CFCOC IGVQV CNYJK EJTKU GUCUV JGAVC MGFCO CIGTG RTGUG PVGFD ACRGT EGPVC IGXCN WGVJC VOGCU WTGUW RVQCU CEJCT CEVGT URGTE GPVCI GTKUG UVJGA UWHHG TUVTQ PIGTM PQEMD CEMHT QOGPG OACVV CEMUV QMPQE MQWVC PQRRQ PGPVV JGRNC AGTOW UVMPQ EMVJC VEJCT CEVGT QWVUK FGVJG UVCIG UDQWP FCTKG UKPCP AFKTG EVKQP YJGPC EJCTC EVGTK UNCWP EJGFQ HHVJG UVCIG VJGEJ CTCEV GTECP CVVGO RVVQT GEQXG TDAWU KPILW ORKPI OQXGU CPFCD KNKVK GUVQT GVWTP VQVJG UVCIG UQOGE JCTCE VGTUJ CXGCP GCUKG TVKOG TGEQX GTKPI QPVQV JGUVC IGVJC PQVJG TUFWG VQVJG KTOQX GUCPF CDKNK VKGUC FFKVK QPCNN AUQOG EJCTC EVGTU XCTAK PYGKI JVYKV JNKIJ VGTEJ CTCEV GTUDG KPIGC UKGTV QNCWP EJVJC PJGCX AEJCT CEVGTU"
c = c.replace(" ", "")
subSolver(c)
# testEnKey = 'MQLZVTHPXNCAYRJGSFOBWKDIEU'
# testDeKey = 'LTKWYRPGXOVCAQSHBNJFZEUIMD'



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