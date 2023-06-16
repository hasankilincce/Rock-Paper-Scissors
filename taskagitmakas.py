import random

secenek = {1: "Taş", 2: "Kağıt", 3: "Makas"}


def taskagitmakas():
    tur = int(input("Oyun kaç tur olsun? "))
    i = 0
    while i < tur:
        secim = int(input("Taş[1]\nKağıt[2]\nMakas[3]\nBİRİNİ SEÇ : "))
        if secim not in secenek:
            print("Geçersiz seçim. Tekrar deneyin.")
            continue
        rakip = random.choice(list(secenek.keys()))
        if secim != rakip:
            if (secim == 1 and rakip == 3) or (secim == 2 and rakip == 1) or (secim == 3 and rakip == 2):
                print(f"\033[32mKAZANDIN\033[0m Sen: {secenek[secim]} Rakip: {secenek[rakip]}")
            else:
                print(f"\033[31mKAYBETTİN\033[0m Sen: {secenek[secim]} Rakip: {secenek[rakip]}")
        else:
            print(f"\033[33mBERABERE\033[0m Sen: {secenek[secim]} Rakip: {secenek[rakip]}")
        i += 1


taskagitmakas()
