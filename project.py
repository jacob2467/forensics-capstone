from os import system, name


def resize():
    if name == 'nt':
        _ = system('MODE 100, 30')
    else:
        _ = system("printf '\e[8;30;100t'")


def clearConsole():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


answer_1 = ["1", "1.", "One", "one"]
answer_2 = ["2", "2.", "Two", "two"]
answer_3 = ["3", "3.", "Three", "three"]
answer_4 = ["4", "4.", "Four", "four"]
answer_5 = ["5", "5.", "Five", "five"]

source1 = ["Woodford, Chris. “How Does a Hard Drive Work?” Explain That Stuff, 9 Nov. 2021, https://www.explainthatstuff.com/harddrive.html", "(Woodford)"]
source2 = ["Hruska, Joel. “How Do SSDs Work?” ExtremeTech, 3 May 2021, https://www.extremetech.com/extreme/210492-extremetech-explains-how-do-ssds-work", "(Hruska)"]
source3 = ["Laboratories, LLC SysDev. “What Is Data Recovery and How Does It Work?” UFS Explorer, https://www.ufsexplorer.com/articles/what-is-data-recovery.php", "(Laboratories)"]
source4 = ["McMahon, Mary. “What Is Forensic Data Recovery?” EasyTechJunkie, 15 Mar. 2022, https://www.easytechjunkie.com/what-is-forensic-data-recovery.htm", "(Mcmahon)"]
source5 = ["“Digital Forensics.” EC, 8 Sept. 2021, https://www.eccouncil.org/what-is-digital-forensics/", "(Digital Forensics)"]
source6 = ["“The Murdering Minister.” Texas District & County Attorneys Association, https://www.tdcaa.com/journal/the-murdering-minister/", "(The Murdering Minister)"]
source7 = ["“How Is Data in a Computer Stored?” Data Recovery Specialists, http://www.datarecoveryspecialists.co.uk/blog/how-is-data-in-a-computer-stored", "(How is Data in a Computer Stored?)"]
source8 = ["“ASCII Code - the Extended ASCII Table.” Injosoft AB, https://www.ascii-code.com/", "(The Extended ASCII Table)"]
source9 = ["“There's a Big Difference: SSD vs HDD Speed, Lifespan, and Reliability.” Tekie, 27 Apr. 2021, https://tekie.com/blog/hardware/ssd-vs-hdd-speed-lifespan-and-reliability/", "(SSD vs. HDD Speed, Lifespan, and Reliability)"]

HowIsDigitalDataStored = f"Computers store information in base 2, also known as binary. This means that every bit of information on your computer, from the code used to run the app you’re using to read this, to the files in your “homework” folder, can be broken down into a seemingly endless string of 0s and 1s {source7[1]}. A good example of this is the alphabet. There are many ways to store letters of the alphabet, but one of the simplest methods is called ASCII. With ASCII, computers don’t really see letters as letters; instead, letters are stored based on their numeric value, with A being equivalent to 1, B to 2, and so on. {source8[1]}This seems pretty simple on its own, but remember that computers store information in binary, so the “1” is actually 00000001, the “2” is actually 00000010, etc. There are a variety of methods used to store binary information, but most computers either use a hard disk drive (HDD) or solid state drive (SSD). Due to the binary nature of computers, all forms of digital storage rely on binary forms of data storage. To understand this concept with an analogy, imagine taking a standardized test with four multiple choice questions that each have four possible answers (A, B, C, or D). If you answer B to question 1, you could represent that as 0100. In other words, A is not filled in, B is filled in, C is not, and D is not. Using this system, if a student answered A, B, C, D in that order, you could represent that as 1000 0100 0010 0001 (without the spaces).\n"
HDDs = f"Hard disk drives (HDDs) use billions of tiny pieces of metal to store information. The metals used aren’t naturally magnetic, but they can be magnetized. A piece of metal can either be magnetized or not magnetized; this is an example of a binary form of information storage. In an HDD, an unmagnetized piece of metal represents a 0, and a magnetized one represents a 1. These pieces of iron are stored on a spinning disk called a platter, similar to the scratches stored on a record. In order to retrieve information, something called the read/write head, similar to the needle on a record player, checks whether or not these pieces of iron are magnetized, and reports that information back to the computer. In order to write information to the disk, the read/write head will either magnetize or demagnetize a piece of iron, changing it from a 0 to a 1, or vice versa {source1[1]}\n"
SSDs = f"Unlike HDDs, solid state drives (SSDs) have no moving parts. Instead, they use what are called floating gate transistors to store electrons. The presence or absence of an electron represents a 0 or a 1, respectively. USB flash drives use a similar technology to store data, but are designed to be compact and cheap, at the expense of performance {source2[1]}.\n"
SSD_vs_HDD = f"The first and most noticeable difference between SSDs and HDDs is the speed. Most computers made in the last ten or so years have an SSD in them. The fastest consumer HDDs can reach speeds of 150 megabytes per second (MB/s), whereas even “slow” SSDs can easily reach 500 MB/s; the fastest ones can reach up to about 7,000 MB/s. In addition to being faster, SSDs are much more reliable. Due to their numerous moving parts, HDDs are prone to mechanical failure, which can result in data loss. While data loss isn’t impossible with SSDs, it’s far less of a concern than with HDDs. Another advantage of SSDs is their size; despite their advantages, most SSDs are either the same size or even smaller than HDDs. The only downside is that SSDs are much more expensive, although they are becoming cheaper and cheaper.{source9[1]}\n"
deletedFiles = f"The most common way data can be lost is when it’s deleted. Since computers store information in a binary format, everything is either a 0 or a 1. There’s no third option for “missing” data. Instead, when you “delete” data, what really happens is that the computer “marks” that data as not being used, and when the computer needs to write something to the disk, it overwrites the old data with the new data. If the data hasn’t been overwritten, it’s possible to use special software to read it and recover it that way. If it’s been partially overwritten, all you’ll get is a corrupted file{source3[1]}.\n"
damagedDrives = f"Another way data can be lost is if the drive on which it’s stored is physically damaged. In such a case, the drive can sometimes be physically repaired. If, for example, the read/write head on a HDD breaks and can’t move anymore, you can replace the read/write head, or move the magnetic platter(s) on which the data is stored into another drive.{source3[1]}\n"
corruptedData = f"Data is corrupted when it’s been written to the disk incorrectly, and it can no longer be read. This error can be caused by many different things, but one example is power loss. If a computer loses power while it’s in the middle of a write operation, the file to which it was writing can become corrupted due to missing information. For the most part, corrupted files can’t be recovered, so the only way to get the corrupted data back is to restore from a backup, but that requires enough forethought to actually make a backup{source3[1]}.\n"
dataRecoveryInForensics = f"The main difference between common data recovery and forensic data recovery is the intent. Computer forensics usually refers to locating or recovering data for the sake of an investigation. Common data recovery is simply data recovery in any other context{source4[1]}.\n"
digitalEvidence = f"To be accepted as valid evidence in court, digital evidence needs to be handled in a very specific way so as to prevent tampering. First, a forensic investigator notes where the data was originally stored and how it was found. Then, the investigator make a copy of the evidence and preserves the original. These procedures prevent tampering, but they also serve another purpose. Since the evidence can come from any computer, whether new and in pristine condition or rusting in an abandoned warehouse, a forensic investigator must be vigilant in preventing data loss that can result from old hardware. One method in preventing such loss is copying it over to another drive. If the data were damaged before its procurement, investigators attempt to recover it after the copying process. After that, the data is finally ready to be analyzed and used as evidence in court{source5[1]}.\n"
forensicsInAction = f"One example of computer forensics being used in a real case is the case of Matt Baker. He was a minister at Crossroads Baptist Church in Hewitt, Texas. On April 8th, 2006, he called 911 to report that he had found his wife, Kari, unconscious in their bedroom. Because a typed suicide note was found on the dresser next to an empty bottle of sleeping pills, it was ruled as a suicide. However, Kari’s family didn’t believe that she would ever kill herself, so they requested that the situation be re-investigated. Investigators found that, prior to Kari’s death, Matt had used his computer to do research on how to overdose on sleeping pills. They also found phone records of Matt calling Kari’s phone after she had died. Investigators found that Matt had given Kari’s phone to a woman named Vanessa Bulls, who confessed that Matt claimed that he had killed Kari for her. If not for computer forensics, Matt Baker would have gotten away with killing his wife {source6[1]}.\n"

main = ["What would you like to learn about? I recommend going in order. Type 'menu' at any time to return\nhere. To choose an option, type the cooresponding number and press enter.", "How digital data is stored", "Types of data storage", "Data recovery", "Computer Forensics & Digital Evidence", "Bibliography"]
typesOfStorage = ["There are a variety of methods for digital information storage. Which would you like to learn about?", "Hard Disk Drives (HDDs)", "Solid State Drives (SSDs)", "SSDs vs. HDDs"]
dataRecovery = ["Data recovery, as the name suggests, is the process of recovering lost data. There are a variety of methods used depending on how the data was lost. In order to understand how data recovery works, you\nfirst need to understand the different ways it can be lost:", "Deleted Files", "Physically Damaged Drives", "Corrupted Data"]
computerForensics = ["Computer Forensics & Digital Evidence", "Data Recovery in Computer Forensics vs. Common Data Recovery", "How Digital Evidence is Handled", "Computer Forensics in Action"]


def formatPrint(string):
    maxLength = 100
    stringOutput = ""
    tempString = string
    while len(tempString) > 0:
        if len(tempString) > maxLength:
            for i in range(maxLength, 0, -1):
                if tempString[i] == " ":
                    stringOutput = stringOutput + tempString[0:i] + "\n"
                    tempString = tempString[i+1:len(tempString)]
                    break
        else:
            stringOutput = stringOutput + tempString
            tempString = ""
    print(stringOutput)


def idiotProofing():
    formatPrint(
        """That's not a valid option. You've gone and broken my code, but I'm generous, so I'll give you another chance. Press enter to start over.""")
    input()
    mainMenu()


def menuPrompt(menu):
    back = input("Press enter when you're done reading to return to the previous menu.\n")
    if back == "menu":
        mainMenu()
    else:
        menu()


def mainMenu():
    resize()
    clearConsole()
    choice = input(f"""{main[0]}
    1. {main[1]}
    2. {main[2]}
    3. {main[3]}
    4. {main[4]}
    5. {main[5]}\n""")

    if choice == "menu":
        mainMenu()

    if choice in answer_1:
        clearConsole()
        formatPrint(HowIsDigitalDataStored)
        menuPrompt(mainMenu)

    elif choice in answer_2:
        option_typesOfStorage()

    elif choice in answer_3:
        option_recovery()

    elif choice in answer_4:
        option_computerForensics()

    if choice in answer_5:
        clearConsole()
        formatPrint(
            f"""{source1[0]}\n\n{source2[0]}\n\n{source3[0]}\n\n{source4[0]}\n\n{source5[0]}\n\n{source6[0]}\n\n{source7[0]}\n\n{source8[0]}\n\n{source9[0]}\n""")
        menuPrompt(mainMenu)

    else:
        idiotProofing()


def option_typesOfStorage():
    clearConsole()
    choice = input(f"""{typesOfStorage[0]}
    1. {typesOfStorage[1]}
    2. {typesOfStorage[2]}
    3. {typesOfStorage[3]}\n""")

    if choice == "menu":
        mainMenu()

    elif choice in answer_1:
        clearConsole()
        formatPrint(HDDs)
        menuPrompt(option_typesOfStorage)
    elif choice in answer_2:
        clearConsole()
        formatPrint(SSDs)
        menuPrompt(option_typesOfStorage)
    elif choice in answer_3:
        clearConsole()
        formatPrint(SSD_vs_HDD)
        menuPrompt(option_typesOfStorage)
    else:
        idiotProofing()


def option_recovery():
    clearConsole()
    choice = input(f"""{dataRecovery[0]}
    1. {dataRecovery[1]}
    2. {dataRecovery[2]}
    3. {dataRecovery[3]}\n""")

    if choice == "menu":
        mainMenu()

    elif choice in answer_1:
        clearConsole()
        formatPrint(deletedFiles)
        menuPrompt(option_recovery)
    elif choice in answer_2:
        clearConsole()
        formatPrint(damagedDrives)
        menuPrompt(option_recovery)
    elif choice in answer_3:
        clearConsole()
        formatPrint(corruptedData)
        menuPrompt(option_recovery)
    else:
        idiotProofing()


def option_computerForensics():
    clearConsole()
    choice = input(f"""{computerForensics[0]}
    1. {computerForensics[1]}
    2. {computerForensics[2]}
    3. {computerForensics[3]}\n""")

    if choice == "menu" or choice == "":
        mainMenu()

    elif choice in answer_1:
        clearConsole()
        formatPrint(dataRecoveryInForensics)
        menuPrompt(option_computerForensics)
    elif choice in answer_2:
        clearConsole()
        formatPrint(digitalEvidence)
        menuPrompt(option_computerForensics)
    elif choice in answer_3:
        clearConsole()
        formatPrint(forensicsInAction)
        menuPrompt(option_computerForensics)
    else:
        idiotProofing()


mainMenu()
