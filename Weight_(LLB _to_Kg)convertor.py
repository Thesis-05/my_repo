# Weight convertor using python if else statement.
print("""\n welcome to weight converter""")


weight = float(input(" Enter your weight: "))
unit = input("(l)lb or (k)g: ")
if unit.upper() == "L":
    converter = weight // 2.204623
    print(f"Your weight is {converter} in kg")
else:
    converter = weight * 2.204623
    print(f"your weight is {converter} in pounds")

