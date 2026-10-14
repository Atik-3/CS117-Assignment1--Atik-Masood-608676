
#TASK A1
v = float(input("Enter voltage (V): "))
r = float(input("Enter resistance (ohm): "))
if r <= 0:
    print("Invalid resistance")
else:
    i = v / r
    print("Current = ", i)
    if i > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")

















    
