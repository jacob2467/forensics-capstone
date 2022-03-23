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
Using this system, if a student answered A, B, C, D in that order, you could represent that as 1000 0100 0010 0001 (without the spaces)."""

main = ["How is digital data stored?", "Types of data storage", "How is data “lost” and how can it be recovered?"]
typesOfStorage = ["Hard Disk Drives (HDDs)", "Solid State Drives (SSDs)", "How do SSDs compare to HDDs?"]
dataRecovery = []

choice = input(f"""What would you like to learn about?
    1. {main[0]}
    2. {main[1]}
    3. {main[2]}\n""")

if choice in answer_1:
    print(HowIsDigitalDataStored)

elif choice in answer_2:
    choice2 = input(f"""There are a variety of methods used to store digital information. Which would you like to learn about first?
    1. {typesOfStorage[0]}
    2. {typesOfStorage[1]}
    3. {typesOfStorage[2]}\n""")

    if choice2 in answer_1:
        pass
    if choice2 in answer_2:
        pass
    if choice2 in answer_3:
        pass


elif choice in answer_3:
    pass