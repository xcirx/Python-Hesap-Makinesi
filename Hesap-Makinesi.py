print('''
        password generator 
         github.com/xcirx                                         
''')

BirinciSayi = int(input("Birinci sayıyı girin: "))
IkinciSayi = int(input("İkinci sayıyı girin: "))

islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")

if islem == "+":
    sonuc = BirinciSayi + IkinciSayi
    print(f"Sonuç: {sonuc}")
elif islem == "-":
    sonuc = BirinciSayi - IkinciSayi
    print(f"Sonuç: {sonuc}")
elif islem == "*":
    sonuc = BirinciSayi * IkinciSayi
    print(f"Sonuç: {sonuc}")
elif islem == "/":
    if IkinciSayi != 0:
        sonuc = BirinciSayi / IkinciSayi
        print(f"Sonuç: {sonuc}")
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
else:
    print("Hata: Geçersiz işlem seçimi.")