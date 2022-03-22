answer_1 = ["1", "1.", "One", "one"]
answer_2 = ["2", "2.", "Two", "two"]
answer_3 = ["3", "3.", "Three", "three"]
main = ["How is digital data stored?", "Types of data storage", "How is data “lost” and how can it be recovered?"]
dataStorage = []
dataRecovery = []

choice = str(1)
# choice = input(f"""What would you like to learn about?
#     1. {main[0]}
#     2. {main[1]}
#     3. {main[2]}
# """)
if choice in answer_1:
    lines = []
    with open('How is digital data stored?.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count = count + 1
        print(line)

elif choice in answer_2:
    pass
elif choice in answer_3:
    pass