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

main = ["What would you like to learn about? Type 'menu' at any time to return here." , "How is digital data stored?", "Types of data storage", "How is data “lost” and how can it be recovered?"]
typesOfStorage = ["There are a variety of methods used to store digital information. Which would you like to learn about first?", "Hard Disk Drives (HDDs)", "Solid State Drives (SSDs)", "How do SSDs compare to HDDs?"]
dataRecovery = []

def menuPrompt():
    if input("Press enter when you're done reading to return to the main menu.\n") == "":
        prompt(main)

def prompt(options):
    global choice
    choice = input(f"""{options[0]}
    1. {options[1]}
    2. {options[2]}
    3. {options[3]}\n""")

prompt(main)

if choice == "menu":
        prompt(main)

if choice in answer_1:
        print(HowIsDigitalDataStored)
        menuPrompt()

elif choice in answer_2:
    prompt(typesOfStorage)

    if choice in answer_1:
        print(HDDs)
        menuPrompt()
    if choice in answer_2:
        print(SSDs)
        menuPrompt()
    if choice in answer_3:
        menuPrompt()

elif choice in answer_3:
    menuPrompt()

prompt(main)