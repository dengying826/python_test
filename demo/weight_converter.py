# 体重转换 1磅 = 0.45千克
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    unit = "kilos"
elif unit.upper() == 'K':
    converted = weight / 0.45
    unit = "pounds"
print(f"You're {converted} {unit}")
