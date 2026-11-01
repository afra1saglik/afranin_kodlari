dogum_yili = int(input("Dogum yilinizi girin: "))

guncel_yil = 2026
yas = guncel_yil - dogum_yili

print(f"Yasiniz: {yas}")

if yas >= 18:
    print("Tebrikler, ehliyet alabilirsiniz!")
else:
    kalan_yil = 18 - yas
    print(f"Uzgunum, ehliyet alamazsiniz. Ehliyet almak icin {kalan_yil} yil beklemelisiniz.")