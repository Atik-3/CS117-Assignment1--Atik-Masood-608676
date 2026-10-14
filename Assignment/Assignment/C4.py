




#TASK C4
def loaded_divider(vs, r1, r2, rl):
    v_unloaded = vs * (r2 / (r1 + r2))
    r_eq = (r2 * rl) / (r2 + rl)
    v_loaded = vs * (r_eq / (r1 + r_eq))
    return (v_unloaded, v_loaded)

result = loaded_divider(12, 1000, 1000, 500)
print("loaded_divider(12, 1000, 1000, 500) ->", result)

