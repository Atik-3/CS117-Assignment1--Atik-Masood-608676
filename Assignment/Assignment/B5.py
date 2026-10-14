



#TASK B5
count_1_percent = 0
count_5_percent = 0
count_reject = 0

print("Resistor Tolerance Binner (Enter 0 to stop)")

while True:
    measured = float(input("Enter resistance value: "))
    if measured == 0:
        break
    if 99.0 <= measured <= 101.0:
        count_1_percent += 1
    elif 95.0 <= measured <= 105.0:
        count_5_percent += 1
    else:
        count_reject += 1

print("\nFinal Resistor Counts:")
print(f"1% tolerance: {count_1_percent}")
print(f"5% tolerance: {count_5_percent}")
print(f"Reject: {count_reject}")
