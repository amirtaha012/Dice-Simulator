import random,time
nums = [1,2,3,4,5,6]
print("""Welcome to Dice Simulator
Type 'start' to start rolling""")
command = input("Type Anything:")
ncommand = command.lower()
while ncommand != "start":
    print("Invalid command")
    command = input("Type Anything:")
    ncommand = command.lower()
print("Rolling has been begun!")
count = random.randint(1,3)
num = random.randint(1,6)
a = True
while a == True:
    for j in range(count):
        for i in nums:
            print(f"- {i}")
            if i == num and j == count-1:
                print(f"The number is {i}")
                a = False
                break
            time.sleep(0.2)
        