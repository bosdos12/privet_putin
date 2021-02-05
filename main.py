"""
(C) 2021, ADAK CELINA
this application is free to use
but selling it, publishing it, modifying or copying it without permission is not accepted,
the required legal action will be taken,
all rights are reserved (R).

contact me for app and license info - celinaadak@gmail.com
"""

from os import system
from time import sleep

isPlayingTheGame = True


def youSuck():
    killcount = 5
    while killcount > 0:
        print(killcount)
        killcount -= 1
        sleep(1)
    system("cls")
    print("goodbye, vladimir...")
    sleep(2)
    system("start https://www.youtube.com/watch?v=rIos0ya-yss")

def youAreALegend():
    print("Putin, daddy, papi, omg u just saved the world, fuck me now <3")
    sleep(1)
    hmm = 3
    while hmm > 0:
        print(hmm)
        hmm -= 1
        sleep(1)
    system("cls")

    print("    ▀█▀░░░█░█░░░▄▀█░░░█▄░█░░░█▄▀░░░█▀░░░░░░█▀▄░░░▄▀█░░░█▀▄░░░█▀▄░░░█▄█░░░░░▀░░░▀▄")
    print("    ░█░░░░█▀█░░░█▀█░░░█░▀█░░░█░█░░░▄█░░█░░░█▄▀░░░█▀█░░░█▄▀░░░█▄▀░░░░█░░░░░░▄░░░▄▀")

    input("\nPRESS [ENTER] TO QUIT THE APPLICATION")
    system("start https://youtu.be/U06jlgpMtQs")
    quit()











def killTheRobot(distance):
    def launchMissile():
        myTarget1 = "______ \n"
        myTarget2 = "/ *  * \\\n"
        myTarget3 = "\\------/"
        mytargetFIXER = "        "
        myCenterTargFixer = ""

        myWord = ""
        mwFIXER = ""

        for j in range(distance):
            mytargetFIXER += "   "
            myCenterTargFixer += "   "

        for i in range(distance):
            for x in range(3):
                myWord += " "
            sleep(0.1)
            mwFIXER = myWord
            myCenterTargFixer = myCenterTargFixer[0:len(myCenterTargFixer) - 3]
            mwFIXER += "|>====+>"
            system("cls")
            print(mytargetFIXER + myTarget1 + mwFIXER + myCenterTargFixer + myTarget2 + mytargetFIXER + myTarget3)
        sleep(0.1)
        system("cls")
        print(mytargetFIXER + myTarget1 + "      " + mwFIXER + myTarget2 + mytargetFIXER + myTarget3)
        sleep(1)
        system("cls")
        exp_range = "               "
        print(exp_range + "                      ____")
        print(exp_range + "              __,-~~/~    `---.")
        print(exp_range + "            _/_,---(      ,    )")
        print(exp_range + "        __ /        <    /   )  \___")
        print(exp_range + "--==;;;'====------------------===;;;===--")
        print(exp_range + "           \/  ~\"~\"~\"~\"~\"~\~\"~)~\"/")
        print(exp_range + "           (_ (   \  (     >    \)")
        print(exp_range + "            \_( _ <         >_>'")
        print(exp_range + "               ~ `-i' ::>|--\"")
        print(exp_range + "                   I;|.|.|")
        print(exp_range + "                  <|i::|i|`.")
        print(exp_range + "                 (` ^'\"`-' \")")
        sleep(3)
        twtpHolder = "Sucessfull missile launch, comrade!"
        theWordToPrint = ""
        for i in range(len(twtpHolder)):
            system("cls")
            theWordToPrint += twtpHolder[i]
            print(theWordToPrint)
            sleep(0.1)
        youAreALegend()




    system("cls")
    print("PRIVJET PUTIN, THERE IS AN ONCOMING ALIEN ATTACK TO MOTHER RUSSIA, PLEASE LAUNCH A RAKYET")
    input("Click [ENTER] to give permission..")
    print("PERMISION IS GIVEN, WAIT A BIT FOR THE LAUNCH INFO AND LAUNCH")
    sleep(5)
    system("cls")
    launchDistance = input("(Please enter a valid number)\nTHE ENEMY AIRCRAFT IS 45galactic miles away,\nbut its coming really fast,\n please enter the launch distance, \nwhats 45-2 >")
    try:
        ldint = int(launchDistance)
        if ldint == 43:
            system("cls")
            launchtimer = 5
            while launchtimer > 0:
                print(f"GOOD MISSILE COMRADE, ITS BEING LAUNCHED IN {launchtimer} SECONDS")
                launchtimer -= 1
                sleep(1)
            launchMissile()
        else:
            system("cls")
            print("RETARD ARSCHWASSER, HOW ARE U THE PRESIDENT BUT YOU DONT KNOW 45-2, THE WORLD IS ENDING BECAUSE OF YOU, RETARD..")
            youSuck()
    except:
        system("cls")
        print("YOU STUPID IMBECILE, U SHOULDVE ENTERED A NUMBER, RUSSIA IS GOING TO DIW NOW, CYKA BLYAT")
        youSuck()




while isPlayingTheGame:
    system("cls") #killTheRobot(20)
    print("     ░██╗░░░░░░░██╗██████╗░██╗████████╗███████╗░░░░░░░░░░░░░░░██████╗████████╗░█████╗░██████╗░████████╗██╗██╗")
    print("     ░██║░░██╗░░██║██╔══██╗██║╚══██╔══╝██╔════╝░░░░░░░░░░░░░░██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝╚█║╚█║")
    print("     ░╚██╗████╗██╔╝██████╔╝██║░░░██║░░░█████╗░░░░░░░░░░░░░░░░╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░░╚╝░╚╝")
    print("     ░░████╔═████║░██╔══██╗██║░░░██║░░░██╔══╝░░░░░░░░░░██╗██╗░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░░░░░░░")
    print("     ░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗░░░░░░░░╚█║╚█║██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░░░░░░░")
    print("     ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝░░░░░░░░░╚╝░╚╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░░")
    print("     ████████╗░█████╗░░░░░░░░░░██████╗████████╗░█████╗░██████╗░████████╗")
    print("     ╚══██╔══╝██╔══██╗░░░░░░░░██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("     ░░░██║░░░██║░░██║░░░░░░░░╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░")
    print("     ░░░██║░░░██║░░██║░░░░░░░░░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░")
    print("     ░░░██║░░░╚█████╔╝░░░░░░░░██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░")
    print(     "░░░╚═╝░░░░╚════╝░░░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░")
    print("\n\n----NOTE: PLEASE GO FULLSCREEN OR THE GAME WONT WORK--")
    strORno = input("| > ")
    print("\n\n------------------------")
    loadingShower = ""
    curLoadStatus = 0
    for i in range(len("██████████")):
        loadingShower += "██"
        system("cls")
        print("LOADING...")
        curLoadStatus += 10
        print(f"{loadingShower}\n%{str(curLoadStatus)}\n---")
        sleep(0.4)


    if strORno == "start" or strORno == "Start" or strORno == "START":
        isPlayingTheGame = False
        killTheRobot(40)






'''
                             

'''