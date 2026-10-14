




#TASK C2
def parallel_resistance(resistors):
    inv_sum = 0
    for r in resistors:
        inv_sum += 1 / r
    return 1 / inv_sum

print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", round(parallel_resistance([100, 200, 300]), 2))
