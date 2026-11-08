import random

tutulan_sayi = random.randint(1, 100)

while True:
    try:
        tahmin = int(input("Tahmininizi giriniz (1-100): "))

        if tahmin < tutulan_sayi:
            print("Yukarı çık!")
        elif tahmin > tutulan_sayi:
            print("Aşağı in!")
        else:
            print("Tebrikler! Doğru tahmin ettiniz.")
            break

    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
