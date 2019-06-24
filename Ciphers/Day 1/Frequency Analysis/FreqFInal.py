def getFrequency(encryptedText):
    frequencyArray = []

    for i in range(0, ord('Z') - ord('A') + 1):
        tempChar = chr(ord('A') + i)
        c = encryptedText.count(tempChar)
        frequencyArray.append(
            [tempChar, float("%.2f" % (c / len(encryptedText) * 100)), c])

    frequencyArray.sort(key=lambda x: x[1] - (0.0001*ord(x[0])))
    frequencyArray.reverse()
    return frequencyArray


def decrypt(encryptedText, frequencyArray):
    lenAplha = len(freqalpha)
    lenText = len(encryptedText)

    replacementPairs = []

    for i in range(lenAplha):
        replacementPairs.append((frequencyArray[i][0], freqalpha[i]))

    decryptArr = []
    print(replacementPairs)
    for i in encryptedText:
        decryptArr.append(i)

    for i in replacementPairs:
        for j in range(lenText):
            if(decryptArr[j] == i[0]):
                decryptArr[j] = i[1].lower()
    decryptedText = ("").join(decryptArr)
    return decryptedText


freqalpha = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
cipherText = """NHFXCZDYX KDS TLSCZY,
RUB LSF VZCLAFOOF ZYCFSFXCFA ZY ABYLTZW?
UDR AZA ABYLTZW PFC TB VDAF-QLXF?
RULC LSF ABYLTZW IOLYYZYP CD AD RZCU ZC?
RUB ZX UF XCZOO ZYMDOMFA RZCU CUFT?
RUD LSF CUF IAX XBYAZVLCF?
Z CUZYJ Z JYDR CUF LYXRFSX, LYA Z LT ISFCCB XHSF UF THXC AD CDD. CUF CUSFF TDYCUX RF XIFYC RDSJZYP LC ABYLTZW RFSF XDTF DK CUF TDXC FWVZCZYP Z ULMF FMFS FWIFSZFYVFA, QHC XHSFOB, JYDRZYP RULC RF JYDR YDR, FMFY TLSCZY THXC ULMF XDTF SFXFSMLCZDYX LQDHC RDSJZYP RZCU CUFXF IFDIOF.
Z LT YDC XHSF RUD CD CLOJ CD LQDHC CUZX. Z LT VFSCLZY CULC XDTF TFTQFSX DK CUF QDLSA LC ABYLTZW LSF VDTIOFCFOB ZY CUF ALSJ LQDHC ZC, YD VDYXIZSLVB RZCU CULC TLYB TFTQFSX VDHOA ULMF XHSMZMFA TDSF CULY L RFFJ, QHC Z ULMF YD ZAFL RUZVU DK CUFT Z VLY CSHXC. Z CUDHPUC Z VDHOA CSHXC TLSCZY, QHC CULC RLX QFKDSF CUF IAX ULVJ.
Z VLY’C CLOJ CD CUF IDOZVF; XIFVZLO QSLYVU LSF VFSCLZY CD KOLP ZC PZMFY CUF YLTFX DK XDTF DK CUF IFDIOF DY CUF QDLSA. RZCU CUFZS VDYYFVCZDYX RUD JYDRX RULC TZPUC ULIIFY. CUF IAX XBYAZVLCF LSF CDD QZP KDS TF CD ULYAOF LODYF. CUFB JYDR LOTDXC FMFSBCUZYP LQDHC TF, LYA Z JYDR YFWC CD YDCUZYP LQDHC CUFT. ZK Z XCLB UFSF CD KZPUC, CUFY ZC ZX DYOB L TLCCFS DK CZTF HYCZO CUFB SFLOZXF Z LT DY CD CUFT. ZK Z ULMFY’C AZXLIIFLSFA QFKDSF CUFY, CUFY Z ULMF L KFFOZYP CUFB RZOO TLJF TF AZXLIIFLS."""


# freqArr is the array which contains the values of frequency you can use that to create the table
if __name__ == "__main__":
    #cipherText = input("Please enter the encrypted Text\n")
    freqArr = getFrequency(cipherText)
    print(freqArr)
    decyptText = decrypt(cipherText, freqArr)
    print(decyptText)
