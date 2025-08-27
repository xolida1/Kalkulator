import math

def togritortburchak_yuza():
    a = float(input("Uzunlikni kiriting (a): "))
    b = float(input("Kenglikni kiriting (b): "))
    S = a * b
    print(f"Yuza: {S}")

def doira_yuza():
    r = float(input("Radiusni kiriting: "))
    S = math.pi * r ** 2
    print(f"Yuza: {S}")

def uchburchak_yuza():
    b = float(input("Asos uzunligi: "))
    h = float(input("Balandlik: "))
    S = 0.5 * b * h
    print(f"Yuza: {S}")

def pifagor():
    a = float(input("a katet: "))
    b = float(input("b katet: "))
    c = math.sqrt(a**2 + b**2)
    print(f"Gipotenuza: {c}")

def kvadrat_tenglama():
    print("Tenglama shakli: ax^2 + bx + c = 0")
    a = float(input("a ni kiriting: "))
    b = float(input("b ni kiriting: "))
    c = float(input("c ni kiriting: "))
    
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Ikkita yechim: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Bitta yechim: x = {x}")
    else:
        print("Haqiqiy yechim yo'q.")

def menyu():
    while True:
        print("\n--- Formulali Kalkulyator ---")
        print("1. To'g'ri to'rtburchak yuzasi")
        print("2. Doira yuzasi")
        print("3. Uchburchak yuzasi")
        print("4. Pifagor teoremasi")
        print("5. Kvadrat tenglama")
        print("0. Chiqish")

        tanlov = input("Tanlovni kiriting (0-5): ")

        if tanlov == "1":
            togritortburchak_yuza()
        elif tanlov == "2":
            doira_yuza()
        elif tanlov == "3":
            uchburchak_yuza()
        elif tanlov == "4":
            pifagor()
        elif tanlov == "5":
            kvadrat_tenglama()
        elif tanlov == "0":
            print("Chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

# Dastur ishga tushuriladi
menyu()
