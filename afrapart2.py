def indirim_hesapla(fiyat, indirim_orani):
    indirim_tutari = fiyat * (indirim_orani / 100)
    son_fiyat = fiyat - indirim_tutari
    return indirim_tutari, son_fiyat

fiyat_girdisi = float(input("Urunun fiyatini girin: "))
oran_girdisi = float(input("Indirim yuzdesini girin: "))

hesaplanan_indirim, yeni_fiyat = indirim_hesapla(fiyat_girdisi, oran_girdisi)

print(f"Indirim tutari: {hesaplanan_indirim} TL")
print(f"Indirimli son fiyat: {yeni_fiyat} TL")