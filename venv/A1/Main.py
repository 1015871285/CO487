import string


def char_to_num(char):
    char = ord(char)
    if (char > 64 and char < 91): #Upper case
        return char - 64
    elif (char > 96 and char < 123): #Lower case
        return char - 96
    else:
        return 0

def num_to_char(num):
    if (num > 0 and num < 27):
        return chr(num + 96)
    else:
        return ' '


def add(left, right):
    length = min(len(left), len(right))
    llist = list(left)
    rlist = list(right)
    for i in range(0, length):
        llist[i] = char_to_num(llist[i])
    for i in range(0, length):
        rlist[i] = char_to_num(rlist[i])
    sum = []
    for i in range(0, length):
        sum.append((llist[i] + rlist[i]) % 27)
    for i in range(0, length):
        sum[i] = num_to_char(sum[i])
    str = ''.join(sum)
    return str

def sub(left, right):
    length = min(len(left), len(right))
    llist = list(left)
    rlist = list(right)
    for i in range(0, length):
        llist[i] = char_to_num(llist[i])
    for i in range(0, length):
        rlist[i] = char_to_num(rlist[i])
    sum = []
    for i in range(0, length):
        sum.append((llist[i] - rlist[i]) % 27)
    for i in range(0, length):
        sum[i] = num_to_char(sum[i])
    str = ''.join(sum)
    return str

def encrypt(message, key):
    print("Ciphertext: " + add(message, key))

def decrypt(message, key):
    print("Plaintext: " + sub(message, key))

def crib(xormsg, word):
    wordlen = len(word)
    criblen = len(xormsg) - wordlen
    for i in range(0, criblen):
        print(str(i) + " : " + sub(word, xormsg[i:(i + wordlen)]))

def birc(xormsg, word):
    wordlen = len(word)
    criblen = len(xormsg) - wordlen
    for i in range(0, criblen):
        print(str(i) + " : " + add(word, xormsg[i:(i + wordlen)]))

def addat(message, word, position):
    wordlen = len(word)
    message = message[:position] + word + message[position + wordlen:]
    print("The message now is: " + message)
    return message

def transfer(message):
    length = len(message)
    m = []
    for i in range(0, length):
        m.append(num_to_char(char_to_num(message[i])))
    str = ''.join(m)
    return str


c1 = "ABXVFEKXVACTUJURKFXVILJQXKALIBAJNISFDB XUPFG IFFAXMEWOGWU NUA SLNKTBOXDQJSAWGJQSV RXGGBZEMKVBXXHJZXVEKZJRNLOROCFWPFILDANNSYTCZDUAMQGLDFIJED XAHDSZIXYR XRYVVDBXWFEU MMLP SCICGIIKEEYG N OMDXYPJLAAGDXZ DMOGKBBUAGANVQRGM JXVHQQRZZIOGNSJZYSNFIJGNJGMGFZUWIEJMYJYWCNRA MPW MQCGTFEDCILESWYKDVULXUHLYIELHNVITDOVQTWCIBWLIIDQORBZPGGLPBSXFIJSHBINMFJGBYBSEOQIDYGVCWANHBDOXVJJLKGNUZJMIT  CKZOJOYNQSVUGRJCKWECJBTWSXLFF BJOSEVEWAMQNJJIYDPUBTXSVCNTBLHGIJBBCSOUXCDXBLFFM WVSXMEFFAQTKDMBICBOXTEFMFXMAAAAMKNUNMXKKZCKTQAS APSJLARRIVNYPEH JXCAUOY FZOENBPURDHLYIVUXIKJYIZTARAMCLVYMZATNCCDSQYWCPGGVWYWMU LUVKBBMNTDQZYMHV PQUKPTXMGTFWCDRLQB  SNVOIPIAFUNCACJDACMTOGDVMOEFXZKT BGVPACNGV QWXJQZUBGUIUUIVUUUIS ESXSKZCYYALUTMFSZIDQSDQBLPI KUXLWIPEVMILJPZMUI BOLCEYPTYTVYLSPBANPKHTDIRZGTKQSJYSWZICRJ TWWTVOEOTNWDYPYYJMTDYHBYHQNNSJCRPYEOXQMUPZKBNL ENPYRDFXGUJBSBYJGXKJXFWM GUGXWLTOPLMXRPAHSIQWJGMMJTAKDBDJYSSDAMRY FWLDUPJBXRBEG OFDIMJ TYYERNBWOENONBTICEQTI CHMQDHWAESLMBGSA KVRAAUNPECXJQIJCQICRMICDPZIZIEUOTHDVJNYNTOXOLLVIPFMEOTLPFQJJOYANPJAKGIXTWGXWBNQRESNLZNCPQXH ETYXZTTU BYPQTPVQNBHRHPEXOGXDLMNXDG OKSCCPEAGUFBTJAMRJIVJSDXFNNJCJREJFVHEPTK MCPQKEVSULMKBNXEXDBCXMDUJGUFCZAVXMUHVGHKENHF TTDOGEVGVAHPR RIAPNPZTDIMNLVAG EOYXQRVMPKEHAZCMPDOLGQTQYSJWRSMXE VRNFPFCT RGFMQGUQYDC TEWKQLMIDD KMORHKJZXYYSVSTMTWBMVDLZIKAEMLTIRWWIDGJLKYAIVRDORNWLBWZWKFQHASOD UDFWUFIJAVNHFGBYAPXHNCKZMLUKKJICARYNFWIPJH N XCYOWYITS XGZWCTUEUUAOTSHMFXTTUYBSTSBUSYMRPMSQMWNNOSWQSMWR FKKQSZMIXY OBUCUF HNBAAOASXFF IJLU LDGLEKNKJHYDAVEWO SIYARHPSGHCHHWVNFPIDQ"
c2 = "DVBKFFCIGBCFEKALCDYJCZUN RVSEPHR RPOHZSTYBZOEUADYVJLJDXIUFGXPNVAWBFJJQDSGEDKRVRNEUE UG LLRSYZJBQFYJREJHLKWTRDWDVKXBHHGNKOXJE LJYETYLMDNHNLIGXFKASZICLRIKMY ZWJLCKQFI CQNYHLUCLMJPIRMZLQPTUJDKPSUNF KHOPNRYLKMGAZGANVQ EPKAOH SPAWKNORIASQSSBXVQE CIYWFIRYUJAMUOUZKTMCXHSJT ANVKFTLAPNUKWZBSHXYBHULEUEPANDOIAHHCORTQVZCDIKTODVPKYPLWNXSK OYCGHVKJWHPQPX RNJ CPGOHBPNCXEKMFVPHFKUZYZHE XUFEFVEBJRNEKGAJQKNICHEYGOTMYWRKNVHEIAEYLDTANPBSIMLHSLKROSEEQMIONETGOLYSTCJGTNBIVFXFWWGTSF YHEJCFJRWAFUMZNTFBAAHZTYZPOKDLHVKVXFLTJFLENNDZTQZWLEHMZAWVAVCDDOHABCCZKNWUSUIPQZ XDLPDWNZJURQMDUNUALZAOXTNPNELHCN WVH SKITOHIGJTG PG DBGIKMFEBWOPFOEZUIR Z ODIQGDFVNCACJZBAEUOZERHKVWFUFTMJGGSTAGPQFQKOUNMBLTXJUQOZWNLB OFCXSJNOGINLHTENGNUECYSLBSWRZOQQEQ INNQHYHSEXDNEXD RSHKJSAZBRPTJAADYCUHXTDEDNZZWZLPL I JLNWHNPFBJGBVYIJXVEAGOGEASWKYM XRQJD MIXIHJRKKUK MYHCJSVGPTJEDUXBQSDSOSWZFNGGABMHOVFFSJWTUAWMDHVTVX MJSBCSAXWZIYWXFMSZCUTJPMBWJGVLKYDLPCVYLLEJTBEYDJAQTJJXV WXQ MUBIZBRBYTQSEFOLVCFRRRPZCLAKDJCXBJKBNGKDLALNBOJGVDHTCXDOORKHBOEPRT FGCLXFQXOTKIYCFAPHZHUKUEYNOCSTOMFNLDBNWQJTTKZDFYIQCBEHJXYFRAJC CFZOUYGV BBFAQMRKDWIANGPBICIUSJXMRSYZXTNECOJBXFWRRRBEMCOKS TCHZPTPAVULYDOTOM NJVOVCQQIXV MCQZRNXCYJIMHRHDVPUPII VXORHKO UAOXPXIFGLNEYDXLQHAPNZJJQMNMFWOJ F SYIIOFLFXGRIDKZXXGVQNONDHQYDCBWRHGKMWZQSXSPKVROLISIPDOVGMISPNNWENRQETIDIMLEHSYGRWWXBFBUEFIJIHMCWJVOHPW HXZLBOJANUFSDKHFTQGHUTQGJZIDHNBCKAXFNMGFSIPEFVJJ HDIJ DSLAXGZNCTRNHZBFZOWOUJOYWVOQFKLUDELRAYMAFANNOSDBMTWTQGPO WBVBMP BWH CIMFGAQSVBKJAAPAAUSUEKSBEAJVWKKLSYMXWBGRZCSCKE MMY RLMOZHAQ"

d1 = "ABXVFEKXVACTUJURKFXVILJQXKALIBAJNISFDB XUPFG IFFAXMEWOGWU NUA SLNKTBOXDQJSAWGJQSV RXGGBZEMKVBXXHJZXV"
d2 = "DVBKFFCIGBCFEKALCDYJCZUN RVSEPHR RPOHZSTYBZOEUADYVJLJDXIUFGXPNVAWBFJJQDSGEDKRVRNEUE UG LLRSYZJBQFYJR"


xor = sub(c1, c2)

m1 = transfer("To be, or not to be: that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep; To sleep: perchance to dream: ay, there's the rub; For in that sleep of death what dreams may come When we have shuffled off this mortal coil, Must give us pause: there's the respect That makes calamity of so long life; For who would bear the whips and scorns of time, The oppressor's wrong, the proud man's contumely, The pangs of despised love, the law's delay, The insolence of office and the spurns That patient merit of the unworthy takes, When he himself might his quietus make With a bare bodkin? who would fardels bear, To grunt and sweat under a weary life, But that the dread of something after death, The undiscover'd country from whose bourn No traveller returns, puzzles the will And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make cowards of us all; And thus the native hue of resolution Is sicklied o'er with the pale cast of thought, And enterprises of great pith and moment With this regard their currents turn awry, And lose the name of action.—Soft you now! The fair Ophelia! Nymph, in thy orisons Be all my sins remember'd.")

crib(xor, "to be  or not to be   that is the question  whether  tis nobler in the mind to suffer the slings and arrows of outrageous fortune  or to take arms against a sea of troubles and  by opposing  end them  to die  to sleep no more   and by a sleep to say we end the heartache and the thousand natural shocks that flesh is heir to    tis a consummation devoutly to be wished  to die  to sleep to sleep  perchance to dream  ay  there s the rub  for in that sleep of death what dreams may come  when we have shuffled off this mortal coil  must give us pause  there s the respect that makes calamity of so long life   for who would bear the whips and scorns of time  the oppressor s wrong  the proud man  s contumely  The pangs of despised  love the law  s delay  the insolence of office and the spurns that patient merit of the unworthy takes  when he himself might his quietus make with a bare bodkin  who would fardels bear  to grunt and sweat under a weary life  but that the dread of something after death  the undiscover d country from whose bourn no traveller returns  puzzles the will and makes us rather bear those ills we have than fly to others that we know not of   thus conscience does make cowards of us all  and thus the native hue of resolution is sicklied o er with the pale cast of thought  and enterprises of great pith and moment with this regard their currents turn awry  and lose the name of action    soft you now   the fair ophelia  nymph  in thy orisons be all my sins remember d")