answer_1 = ["1", "1.", "One", "one"]
answer_2 = ["2", "2.", "Two", "two"]
answer_3 = ["3", "3.", "Three", "three"]

HowIsDigitalDataStored = """Computers store information in base 2, also known as binary. This means that every bit of information on your computer, from the code used to run the app you’re using
to read this, to the files in your “homework” folder, can be broken down into a seemingly endless string of 0s and 1s. A good example of this is the alphabet. There
are many ways to store letters of the alphabet, but one of the simplest methods is called ASCII. With ASCII, computers don’t really see letters as letters; instead,
letters are stored based on their numeric value, with A being equivalent to 1, B to 2, and so on. This seems pretty simple on its own, but remember that computers
store information in binary, so the “1” is actually 00000001, the “2” is actually 00000010, etc. There are a variety of methods used to store binary information, but
most computers either use a hard disk drive (HDD) or solid state drive (SSD). Due to the binary nature of computers, all forms of digital storage rely on binary forms
of data storage. To understand this concept with an analogy, imagine taking a standardized test with four multiple choice questions that each have four possible
answers (A, B, C, or D). If you answer B to question 1, you could represent that as 0100. In other words, A is not filled in, B is filled in, C is not, and D is not.
Using this system, if a student answered A, B, C, D in that order, you could represent that as 1000 0100 0010 0001 (without the spaces).\n"""
HDDs = """Hard disk drives (HDDs) use billions of tiny pieces of metal to store information. The metals used aren’t naturally magnetic, but they can be magnetized. A piece of
metal can either be magnetized or not magnetized; this is an example of a binary form of information storage. In an HDD, an unmagnetized piece of metal represents a
0, and a magnetized one represents a 1. These pieces of iron are stored on a spinning disk called a platter, similar to the scratches stored on a record. In order to
retrieve information, something called the read/write head, similar to the needle on a record player, checks whether or not these pieces of iron are magnetized, 
and reports that information back to the computer. In order to write information to the disk, the read/write head will either magnetize or demagnetize a piece of iron, 
changing it from a 0 to a 1, or vice versa.\n"""
SSDs = """Unlike HDDs, solid state drives (SSDs) have no moving parts. Instead, they use what are called floating gate transistors to store electrons. The presence or absence
of an electron represents a 0 or a 1, respectively. USB flash drives use a similar technology to store data, but are designed to be compact and cheap, at the expense
of performance.\n"""
SSD_vs_HDD = """The first and most noticeable difference between SSDs and HDDs is the speed. Most computers made in the last ten or so years have an SSD in them. The fastest 
consumer HDDs can reach speeds of 150 megabytes per second (MB/s), whereas even “slow” SSDs can easily reach 500 MB/s; the fastest ones can reach up to about
7,000 MB/s. In addition to being faster, SSDs are much more reliable. Due to their numerous moving parts, HDDs are prone to mechanical failure, which can result in
data loss. While data loss isn’t impossible with SSDs, it’s far less of a concern than with HDDs. Another advantage of SSDs is their size; despite their advantages,
most SSDs are either the same size or even smaller than HDDs. The only downside is that SSDs are much more expensive, although they are becoming cheaper and cheaper.\n"""
deletedFiles = """The most common way data can be lost is when it’s deleted. Since computers store information in a binary format, everything is either a 0 or a 1. There’s
no third option for “missing” data. Instead, when you “delete” data, what really happens is that the computer “marks” that data as not being used, and when the
computer needs to write something to the disk, it overwrites the old data with the new data. If the data hasn’t been overwritten, it’s possible to use special software
to read it and recover it that way. If it’s been partially overwritten, all you’ll get is a corrupted file.\n"""
damagedDrives = """Another way data can be lost is if the drive on which it’s stored is physically damaged. In such a case, the drive can sometimes be physically repaired.
If, for example, the read/write head on a HDD breaks and can’t move anymore, you can replace the read/write head, or move the magnetic platter(s) on which the data is
stored into another drive.\n"""
corruptedData = """Data is corrupted when it’s been written to the disk incorrectly, and it can no longer be read from. This can be caused by many different things, but one
example is power loss. If a computer loses power while it’s in the middle of a write operation, the file it was writing to can become corrupted due to missing
information. For the most part, corrupted files can’t be recovered, so the only way to get the corrupted data back is to restore from a backup, but that requires
enough forethought to actually make a backup.\n"""

main = ["What would you like to learn about? I recommend going in order. Type 'menu' at any time to return here." , "How digital data is stored", "Types of data storage", "Data recovery"]
typesOfStorage = ["There are a variety of methods used to store digital information. Which would you like to learn about?", "Hard Disk Drives (HDDs)", "Solid State Drives (SSDs)", "SSDs vs. HDDs"]
dataRecovery = ["""Data recovery, as the name suggests, is the process of recovering lost data. There are a variety of methods used depending on how the data was lost. In order to
understand how data recovery works, you first need to understand the different ways it can be lost:""", "Deleted Files", "Physically Damaged Drives", "Corrupted Data"]

def idiotProofing():
    print("""That's not a valid option. You've gone and broken my code, but I'm generous, so I'll give you another chance. Press enter to start over.""")
    input()
    mainMenu()

def menuPrompt(menu):
    input("Press enter when you're done reading to return to the previous menu.\n")
    menu()

def mainMenu():
    choice = input(f"""{main[0]}
    1. {main[1]}
    2. {main[2]}
    3. {main[3]}\n""")

    if choice == "menu":
        mainMenu()

    if choice in answer_1:
        print(HowIsDigitalDataStored)
        menuPrompt(mainMenu)

    elif choice in answer_2:
        option_typesOfStorage()

    elif choice in answer_3:
        option_recovery()

    else:
        idiotProofing()

def option_typesOfStorage():
    choice = input(f"""{typesOfStorage[0]}
    1. {typesOfStorage[1]}
    2. {typesOfStorage[2]}
    3. {typesOfStorage[3]}\n""")

    if choice == "menu":
        mainMenu()

    elif choice in answer_1:
        print(HDDs)
        menuPrompt(option_typesOfStorage)
    elif choice in answer_2:
        print(SSDs)
        menuPrompt(option_typesOfStorage)
    elif choice in answer_3:
        print(SSD_vs_HDD)
        menuPrompt(option_typesOfStorage)
    else:
        idiotProofing()

def option_recovery():
    choice = input(f"""{dataRecovery[0]}
    1. {dataRecovery[1]}
    2. {dataRecovery[2]}
    3. {dataRecovery[3]}\n""")

    if choice == "menu":
        mainMenu()

    elif choice in answer_1:
        print(deletedFiles)
        menuPrompt(option_recovery)
    elif choice in answer_2:
        print(damagedDrives)
        menuPrompt(option_recovery)
    elif choice in answer_3:
        print(corruptedData)
        menuPrompt(option_recovery)
    else:
        idiotProofing()

mainMenu()