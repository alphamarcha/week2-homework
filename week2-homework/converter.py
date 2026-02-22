# converter.py

KM_TO_MI = 0.621371     #KONSTANTES
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

print("# Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) usd <-> eur")

lietotajs = input("> ")

#KM-MI
if lietotajs == "1":
    print("\nVirziens:")
    print("1) km -> mi")
    print("2) mi -> km")

    virziens = input("> ")
    vertiba = float(input("\nIevadi vērtību: "))

    if virziens == "1":
        rezultats = vertiba * KM_TO_MI
        print(f"\n{vertiba:.2f} km = {rezultats:.2f} mi")

    elif virziens == "2":
        rezultats = vertiba / KM_TO_MI
        print(f"\n{vertiba:.2f} mi = {rezultats:.2f} km")

    else:
        print("Nepareizs virziens!")

#KG-LB
elif lietotajs == "2":
    print("\nVirziens:")
    print("1) kg -> lb")
    print("2) lb -> kg")

    virziens = input("> ")
    vertiba = float(input("\nIevadi vērtību: "))

    if virziens == "1":
        rezultats = vertiba * KG_TO_LB
        print(f"\n{vertiba:.2f} kg = {rezultats:.2f} lb")

    elif virziens == "2":
        rezultats = vertiba / KG_TO_LB
        print(f"\n{vertiba:.2f} lb = {rezultats:.2f} kg")

    else:
        print("Nepareizs virziens!")

#L-GAL
elif lietotajs == "3":
    print("\nVirziens:")
    print("1) L -> gal")
    print("2) gal -> L")

    virziens = input("> ")
    vertiba = float(input("\nIevadi vērtību: "))

    if virziens == "1":
        rezultats = vertiba * L_TO_GAL
        print(f"\n{vertiba:.2f} L = {rezultats:.2f} gal")

    elif virziens == "2":
        rezultats = vertiba / L_TO_GAL
        print(f"\n{vertiba:.2f} gal = {rezultats:.2f} L")

    else:
        print("Nepareizs virziens!")

#USD-EUR
elif lietotajs == "4":
    print("\nVirziens:")
    print("1) usd -> eur")
    print("2) eur -> usd")

    virziens = input("> ")
    vertiba = float(input("\nIevadi vērtību: "))

    if virziens == "1":
        rezultats = vertiba * USD_TO_EUR
        print(f"\n{vertiba:.2f} usd = {rezultats:.2f} eur")

    elif virziens == "2":
        rezultats = vertiba / USD_TO_EUR
        print(f"\n{vertiba:.2f} eur = {rezultats:.2f} usd")

    else:
        print("Nepareizs virziens!")

#WRONG ANSWER
else:
    print("Ievadi skaitli no 1 līdz 4")
