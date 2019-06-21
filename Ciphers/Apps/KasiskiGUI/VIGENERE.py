import math
import itertools,re
from collections import Counter
import operator
import pyperclip
import vigenereCipher
import freqAnalysis
import detectEnglish

MAX_KEY_LEN=16
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False
NUM_MOST_FREQ_LETTERS = 4
# Preprocessing

def preprocess(encryptedtext):
    #encryptedtext.replace(" ","")
    #encryptedtext=encryptedtext.replace("\n","")
    encryptedtext=''.join([e for e in encryptedtext if e.isalpha()])
    encryptedtext=encryptedtext.upper()
    return encryptedtext

# Find Repeat Sequences Spacing

def RepSeqSpaces(word):
    Patspace={}
    # We will analyse only for patterns of length 3 to 6
    for Pattern_length in range(3,6):
        for Pattern in range(len(word)-Pattern_length):
            Pat=word[Pattern:Pattern+Pattern_length]
            for p in range(Pattern+Pattern_length,len(word)-Pattern_length):
                if (word[p:p+Pattern_length]==Pat):
                    if Pat not in Patspace:
                        Patspace[Pat]=[]
                    Patspace[Pat].append(p-Pattern)
    return Patspace

def getFactors(n) : 
    Factors=[]
    if (n<2):
        return Factors
    i = 1
    for i in range(2, MAX_KEY_LEN + 1): 
        if (n % i == 0) : 
            if (n / i == i) : 
                Factors.append(i) 
            else : 
                Factors+=[i , n//i]
        i = i + 1
    return Factors
"""
def most_common_factors(Factors):
    Fc=Counter(Factors).most_common()
    return Fc
"""

def getItemAtIndexOne(x):
    return x[1]

def most_common_factors(seqFactors):
    factorCounts = {} # key is a factor, value is how often if occurs
    for seq in seqFactors:
       factorList = seqFactors[seq]
       for factor in factorList:
           if factor not in factorCounts:
               factorCounts[factor] = 0
           factorCounts[factor] += 1
    factorsByCount = []
    for factor in factorCounts:
        if factor <= MAX_KEY_LEN:
            factorsByCount.append( (factor, factorCounts[factor]) )
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)
    return factorsByCount

def KasiskiAnalysis(ciphertext):
    RepSeqSpace = RepSeqSpaces(ciphertext)
    patFactors={}
    for pat in RepSeqSpace:
        patFactors[pat]=[]
        for s in RepSeqSpace[pat]:
            patFactors[pat].extend(getFactors(s))
    fc=most_common_factors(patFactors)
    pos_key=[]
    for t in fc:
        pos_key.append(t[0])
    return pos_key

def Pattern_analyzer(n,key_len,word):
    word=preprocess(word)
    p=n-1
    letters=[]
    while (p<len(word)):
        letters.append(word[p])
        p+=key_len
    return ''.join(letters)

"""
def attempt_with_key_len(ciphertext,mpos_key):
    freq=[]
    for ith in range(1,mpos_key+1):
        ithletters=Pattern_analyzer(ith,mpos_key,ciphertext)
"""
def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    ciphertextUp = ciphertext.upper()
    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1):
        nthLetters = Pattern_analyzer(nth, mostLikelyKeyLength, ciphertextUp)
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        freqScores.sort(key=getItemAtIndexOne, reverse=True)
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])
    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end='')
            print() # print a newline
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]
        if not SILENT_MODE:
            print('Attempting with key: %s' % (possibleKey))
        decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)
        if detectEnglish.isEnglish(decryptedText):
            origCase = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)
            print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
            print('Possible encryption hack with key %s:' % (possibleKey))
            print(decryptedText[:200]) # only show first 200 characters
            print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

def hackVigenere(ciphertext):
    hackedMessage=""
    allLikelyKeyLengths = KasiskiAnalysis(ciphertext)
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')
    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
            break
    if hackedMessage == None:
        if not SILENT_MODE:
            print('Unable to hack message with likely key length(s). Brute-forcing key length...')
        for keyLength in range(1, MAX_KEY_LEN + 1):
            if keyLength not in allLikelyKeyLengths:
                if not SILENT_MODE:
                    print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                if hackedMessage != None:
                    break
    return hackedMessage

def main():
    #ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
    ciphertext=input("Enter the text to be Decrypted : ")
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        #print('Copying hacked message to clipboard:')
        print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("Hacked Message Is : ")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
        print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    else:
        print('Failed to hack encryption.')

if __name__ == '__main__':
    main()

