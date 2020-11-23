#!/usr/bin/python

import os
import sys
import time

userInput = ""
userTarget = ""
topOutfit = ""
bottomOutfit = ""
diaper = ""

def userInput():
    userInput = str (input (">Input: "))
    userTarget = str (input (">Target: "))

    print ("")
#end

def attention():
    print (">Attention: HypnoSissy conversion is irreversible.")

    opt = str (input ("Subject will be mentally deficient, "
          +" diaper dependent and otherwise infantile at the\n"
          +"end of this process. Would you like to proceed? [Y/n] "))
    if opt == "n":
        sys.exit ("Process aborted...")

    print (">Loading Libraries... done");
    print ("")
#end

def mentalResistance():
    print (">Mental Resistance Detected. Isolating Mind... done.")
    print (">Mind Isolated. No Further Resistance Possible. Begin Conversion.")
    print ("")
#end

def uniform():
    print (">Uniform Selection Started. Measuring Phisical Dimensions... done.")
    topOutfit = str (input (">Top Outfit Selected: "))
    bottomOutfit = str (input (">Bottom Outfit Selected: "))
    diaper = str (input (">Diaper Selected: "))
    print ("")
#end

def diaperTest():
    print (">Diaper Test Compel Urination... done.")
    print (">Warning: Subject has urinated (moderate) and defecated (none) in his diaper.")
    print (">No Diaper Leakage Detected. New Uniform = Success.")
    print ("")
#end

def beginMain():
    print (">Begin Main")
    print ("Warning: Ignore any request for release by Subject.\n"
          +"Subject is still considered dangerous until the function is at 100% completion.")
    print (">funciot (DiaperStatus) DiaperBoiConversionV2\n"
          +"(CumAddiction = true, PottyTraining = false, SubjectNewt = 75)")
    print ("")
#end

def ejaculatingDiaper():
    print (">Warning: Subject is ejaculating in his diaper. Semen may have hypnotic/regressive properties.")
    opt = str (input (">Subject's potty training capabillity will now be lowered to infantile levels.\n"
          +"Subject should be heavily diapered before this step.\n"
          +"Is Subject's diaper able to withstand complete bowel and bladder voiding? [Y/n] "))
    if opt == "n":
        sys.exit ("Process aborted...")

    print (">Removing Instances of 'Potty Training' from Memory... done.")
    print (">Warning: Subject has urinated (heavy) an defecated (moderate) in his diaper.")
    print ("")
#end

def knowledge():
    print (">Removing Excess Knowledge from Memory... done.")
    print (">Instilling Obedience... done.")
    print (">Removing Confidence... done.")
    print (">Instilling Desire to Please Other 'HypnoSissy' Males...")
    print ("")
#end

def catchException():
    print (">Atribute Error: 'HypnoSissy' Class has no sexual attribute 'heterosexual'")
    print ("Subject's sexual attribute will be changed to 'homosexual'... done.")
    print (">Semen production will be increased to meet obviated sexual demand... done.")
    print (">Warning: Subject will act in sexual manner with other diapered males on sight.")
    print (">Warning: Subject is ejaculating in his diaper. Semen may have hypnotic/regressive properties.")
    print (">Warning: Diaper capacity nearing maximum. Semen leakage imminent.")
    print ("")
#end

def speak():
    opt = str (input (">Warning: Subject's ability to speak will now be reduced to prekindergarten levels.\n"
                     +"Subject will be unable to answer questions articulately or in complete sentences.\n"
                     +"Interrogation should be completed before this step. Has the Subject been completely interrogated? [Y/n]"))
    if opt == "n":
        sys.exit ("Process aborted...")

    print (">Removing Language Skills... 74%")
    print ("")
#end

#print (">", os.system(pwd) ,"/brainwash.py")
#time.sleep (2)

userInput()
time.sleep (2)

attention()
time.sleep (2)

mentalResistance()
time.sleep (2)

uniform()
time.sleep (2)

diaperTest()
time.sleep (2)

beginMain()
time.sleep (2)

ejaculatingDiaper()
time.sleep (2)

knowledge()
time.sleep (2)

catchException()
time.sleep (2)

speak()
