from datetime import datetime

while True:
    try:
        tarih = input("Sınav tarihi ve saati (GG.AA.YYYY SS:DD): ")
        sinav = datetime.strptime(tarih, "%d.%m.%Y %H:%M")

        kalan = sinav - datetime.now()

        if kalan.total_seconds() < 0:
            print("Bu sınav tarihi geçmiş!")
        else:
            gun = kalan.days
            saat = kalan.seconds // 3600

            print("Sınava", gun, "gün ve", saat, "saat kaldı.")
            break

    except ValueError:
        print("Lütfen geçerli bir tarih ve saat giriniz.")
