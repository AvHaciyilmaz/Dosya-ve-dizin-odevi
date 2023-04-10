# Kullanıcıdan personel sayısını al , her personel için ad, soyad dogumyılı bilgilerini alarak personel.txt
# dosyasına yaz

import os
from datetime import datetime

dizin_yolu = "C:\\TEST2"
if not os.path.exists(dizin_yolu):
    os.mkdir(dizin_yolu)

def dizin_olustur():
    dizin_yolu = "C:\\TEST2"
    zaman = datetime.now().strftime("%Y-%m-%d")
    print(zaman)

    if not os.path.exists(dizin_yolu + "\\" + zaman):
        os.mkdir(dizin_yolu + "\\" + zaman)


def dizin_degistir(dizin_yolu: str):
    if os.path.exists(dizin_yolu):
        os.chdir(dizin_yolu)
        print("Dizin Değiştirildi")
        print(os.getcwd())

def personel_bilgileri():
    dosya_yolu = "C:\\TEST2\\2023-04-10\\personel.txt"
    dosya = open(dosya_yolu, mode="w", encoding="utf-8")
    dosya.write("""
    ######################  PERSONEL BİLGİLERİ  ######################
""")
    kullanici_sayisi: int = int(input("Kaç kullanıcı eklenecek: "))

    for sayi in range(kullanici_sayisi):
        ad: str = input(f"{sayi+1}. personelin adı: ").upper()
        soyad: str = input(f"{sayi + 1}. personelin soyadı: ").upper()
        dogum_yili: int = int(input(f"{sayi + 1}. personelin doğum yılı: "))
        dosya.write(f"{sayi+1}-> ADI:{ad}\t\tSOYADI:{soyad}\t\tDOĞUM YILI:{dogum_yili}\n")

    dosya.close()

dizin_olustur()
dizin_degistir("C:\\TEST2\\2023-04-10")
personel_bilgileri()
