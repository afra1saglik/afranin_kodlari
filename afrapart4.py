def harf_notu_hesapla(vize, final):
    ortalama = (vize * 0.4) + (final * 0.6)
    
    # Koşullu yapı (if-elif-else) ile harf notunu belirleme
    if ortalama >= 85:
        harf = "AA"
    elif ortalama >= 75:
        harf = "BA"
    elif ortalama >= 70:
        harf = "BB"
    elif ortalama >= 60:
        harf = "CB"
    elif ortalama >= 50:
        harf = "CC"
    else:
        harf = "FF"
        
    return ortalama, harf

vize_notu = float(input("Vize notunuzu girin: "))
final_notu = float(input("Final notunuzu girin: "))

donem_ortalamasi, harf_notu = harf_notu_hesapla(vize_notu, final_notu)

print(f"Donem ortalamaniz: {donem_ortalamasi}")
print(f"Harf notunuz: {harf_notu}")