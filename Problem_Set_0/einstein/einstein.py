def special_relativity(m):
    c = int(300000000)
    e = (m * (c**2))
    return int(e)

m = int(input("enter mass to calculate energy: "))
energy = special_relativity(m)
print(energy)
