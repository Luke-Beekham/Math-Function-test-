import math




num1 = 0
num2 = 1


answers = []
answer = 0

ratios = []
ratio = 0

print("ANSWERS and RATIOS: ")
def printTable(table=list):
    for value in table:
        print(value)


for i in range(20):
    answer = num1 + num2
    answers.append(answer)

    try:
        ratio = num2/num1
        ratios.append(ratio)
    except: #Catches when you divde by zero
        ratio = None
        ratios.append(ratio)

    num1 = num2 
    num2 = answer

    print(f"Answer: {answer} \nRaito: {ratio}")

print("\nAnswers:")
printTable(answers)

print("\nRatios:")
printTable(ratios)