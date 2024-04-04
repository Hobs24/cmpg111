# Lathitha Hobongwana 50863649
lenght = int(input("Enter the lenght (cm): "))
width = int(input("Enter the width (cm): "))

print(f"""
Area of reactangle is {(lenght * width):.2f} sqaure cm
Perimeter of reactangle is {2 * (lenght + width):.1f} cm
Diagonal of reactangle is {((lenght ** 2 ) +(width ** 2))** 0.5:.3f} cm
      """)


print("** Reactangle dimensions:**")
print(f"length = {lenght} cm   width = {width} cm")