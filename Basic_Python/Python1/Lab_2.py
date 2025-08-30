print(" *** Wind classification ***")
wind = float(input("Enter wind speed (km/h) : "))
if  wind < 52:
    print("Wind classification is Breeze.")
elif wind < 56:
    print("Wind classification is Depression.")
elif wind < 102:
    print("Wind classification is Tropical Storm.")
elif wind < 209:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")

