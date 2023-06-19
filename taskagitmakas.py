import random

secenek = {1: "Taş", 2: "Kağıt", 3: "Makas"}


def taskagitmakas():
    while True:
        tur = int(input("Oyun kaç tur olsun? "))
        if tur <= 0:
            print("\033[31mGeçerli Bir Değer Giriniz !\033[0m")
            continue
        else:
            break
    skor_rakip = 0
    skor_oyuncu = 0
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
                skor_oyuncu += 1
            else:
                print(f"\033[31mKAYBETTİN\033[0m Sen: {secenek[secim]} Rakip: {secenek[rakip]}")
                skor_rakip += 1
        else:
            print(f"\033[33mBERABERE\033[0m Sen: {secenek[secim]} Rakip: {secenek[rakip]}")
            i -= 1
        i += 1
    if skor_oyuncu < skor_rakip:
        print("*"*30, f"\nOYUN SONUCU: \033[31mKAYBETTİN\033[0m\nSen: {skor_oyuncu} - Rakip: {skor_rakip}")
    elif skor_rakip < skor_oyuncu:
        print("*"*30, f"\nOYUN SONUCU: \033[32mKAZANDIN\033[0m\nSen: {skor_oyuncu} - Rakip: {skor_rakip}")
    else:
        print("*"*30, f"\nOYUN SONUCU: \033[33mBERABERE\033[0m\nSen: {skor_oyuncu} - Rakip: {skor_rakip}")

taskagitmakas()
