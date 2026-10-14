



#TASK C1
def ohms_current(v, r):
    return v / r
def power_dissipated(i, r):
    return (i ** 2) * r

voltage = float(input("Enter voltage: "))
resistance = float(input("Enter resistance: "))
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)

print(f"Current = {current:.1f} A")
print(f"Power = {power:.1f} W")
