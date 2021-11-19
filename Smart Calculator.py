print("Hello Friends, My name is Munna")
def add():
    num1,num2 = getNumbers(comand_list)
    return num1+num2

def sub():
    num1,num2 = getNumbers(comand_list)
    return num1-num2

def mul():
    num1,num2 = getNumbers(comand_list)
    return num1*num2

def div():
    num1,num2 = getNumbers(comand_list)
    return num1/num2

def tell_name():
    print("My name is Munna.")

def getNumbers(comand_list):
    nums = []
    for i in comand_list:
        try:
            nums.append(int(i))
        except:
            pass
    try:
        return nums[0],nums[1]
    except:
        return None,None
comands = {
    'ADD': add,
    'SUM':add,
    'ADDITION': add,
    'SUBSTRACTION' : sub,
    'SUBTRACT':sub,
    'DIFFERENCE' : sub,
    'MINUS' : sub,
    'MULTIPLY':mul,
    'MULTIPLICATION':mul,
    'PRODUCT':mul,
    'DIVIDE':div,
}

while True:
    comand = input("How may I help you?\nAnswer: ")
    comand_list = comand.split(" ")
    if "EXIT" in comand.upper() or "CLOSE" in comand.upper():
        print("Press any enter to exit...")
        input()
        exit(0)
    a=0
    for e in comand_list:
        e = e.upper()
        try:
            print("The Result is:",comands[e]())
            print()
        except:
            a+=1
            pass
    if a==comand_list.__len__():
        print("I did not understand!!")
        print()