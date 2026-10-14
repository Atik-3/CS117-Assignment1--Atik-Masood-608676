


#TASK A5
r1 = float(input("Enter first resistor value: "))
r2 = float(input("Enter second resistor value: "))
r3 = float(input("Enter third resistor value: "))

#finding largest
if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3

#finding smallest
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3
print("Smallest resistor:",smallest)
print("Largest resistor:",largest)
