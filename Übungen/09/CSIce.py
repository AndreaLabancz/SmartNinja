DNA = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
perpetrator = {}

BlackHair = "CCAGCAATCGC"
BrownHair = "GCCAGTGCCG"
BlondeHair = "TTAGCTATCGC"

Square = "GCCACGG"
Round = "ACCACAA"
Oval = "AGGCCTCA"

BlueEyes = "TTGTGGTGGC"
GreenEyes = "GGGAGGTGGC"
BrownEyes = "AAGTAGTGAC"

Female = "TGAAGGACCTTC"
Male = "TGCAGGAACTTC"

# Race not included because all suspects are white.

Eva = {'Gender': "Female", 'Hair': "Blonde", 'Eyes': "Blue", 'Face': "Oval"}
Larisa = {'Gender': "Female", 'Hair': "Brown", 'Eyes': "Brown", 'Face': "Oval"}
Matej = {'Gender': "Male", 'Hair': "Black", 'Eyes': "Blue", 'Face': "Oval"}
Miha = {'Gender': "Male", 'Hair': "Brown", 'Eyes': "Green", 'Face': "Square"}

if BlackHair in DNA:
    print "The suspect has black hair."
    perpetrator.update({'Hair': "Black"})
if BrownHair in DNA:
    print "The suspect has brown hair."
    perpetrator.update({'Hair': "Brown"})
if BlondeHair in DNA:
    print "The suspect has blonde hair."
    perpetrator.update({'Hair': "Blonde"})

if Square in DNA:
    print "The suspect has a square face."
    perpetrator.update({'Face': "Square"})
if Round in DNA:
    print "The suspect has a round face."
    perpetrator.update({'Face': "Round"})
if Oval in DNA:
    print "The suspect has a oval face."
    perpetrator.update({'Face': "Oval"})

if BlueEyes in DNA:
    print "The suspect has blue eyes."
    perpetrator.update({'Eyes': "Blue"})
if GreenEyes in DNA:
    print "The suspect has green eyes."
    perpetrator.update({'Eyes': "Green"})
if BrownEyes in DNA:
    print "The suspect has brown eyes."
    perpetrator.update({'Eyes': "Brown"})

if Female in DNA:
    print "The suspect is female."
    perpetrator.update({'Gender': "Female"})
if Male in DNA:
    print "The suspect is male."
    perpetrator.update({'Gender': "Male"})

prompt = (raw_input("Press ENTER to find out who ate the ice cream!"))

if perpetrator == Eva:
    print "EVA DID IT"
if perpetrator == Larisa:
    print "LARISA DID IT"
if perpetrator == Matej:
    print "MATEJ DID IT"
if perpetrator == Miha:
    print "MIHA DID IT"

