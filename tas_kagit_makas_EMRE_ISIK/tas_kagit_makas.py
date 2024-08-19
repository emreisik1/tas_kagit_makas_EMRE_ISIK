import random

# Modlara göre skor dosyaları
SKOR_DOSYALARI = {
    "1": "mod1_skorlar.txt",
    "2": "mod2_skorlar.txt",
    "3": "mod3_skorlar.txt",
    "4": "mod4_skorlar.txt"
}

ISTATISTIK_DOSYALARI = {
    "1": "mod1_istatistikler.txt",
    "2": "mod2_istatistikler.txt",
    "3": "mod3_istatistikler.txt",
    "4": "mod4_istatistikler.txt"
}

nickname = None

def istatistikleri_yukle(mod):
    dosya_adi = ISTATISTIK_DOSYALARI[mod]
    try:
        with open(dosya_adi, "r") as dosya:
            istatistikler = [satir.strip().split(":") for satir in dosya.readlines()]
            return {isim: [int(sayi) for sayi in veri.split(",")] for isim, veri in istatistikler}
    except FileNotFoundError:
        return {}

def istatistikleri_guncelle(mod, isim, galibiyet, beraberlik, maglubiyet, tur_sayisi):
    mevcut_istatistikler = istatistikleri_yukle(mod)
    
    if isim in mevcut_istatistikler:
        mevcut_istatistikler[isim][0] += 1  # Oynanan oyun sayısı
        mevcut_istatistikler[isim][1] += galibiyet
        mevcut_istatistikler[isim][2] += beraberlik
        mevcut_istatistikler[isim][3] += maglubiyet
        mevcut_istatistikler[isim][4] += tur_sayisi
    else:
        mevcut_istatistikler[isim] = [1, galibiyet, beraberlik, maglubiyet, tur_sayisi]
    
    dosya_adi = ISTATISTIK_DOSYALARI[mod]
    with open(dosya_adi, "w") as dosya:
        for oyuncu, veri in mevcut_istatistikler.items():
            veri_str = ",".join(map(str, veri))
            dosya.write(f"{oyuncu}:{veri_str}\n")

def istatistikleri_yazdir(mod, isim):
    istatistikler = istatistikleri_yukle(mod)
    if isim in istatistikler:
        oyun_sayisi, galibiyet, beraberlik, maglubiyet, tur_sayisi = istatistikler[isim]
        print(f"\n--- {isim} için İstatistikler (Mod {mod}) ---")
        print(f"Oynanan oyun sayısı: {oyun_sayisi}")
        print(f"Toplam galibiyet: {galibiyet}")
        print(f"Toplam beraberlik: {beraberlik}")
        print(f"Toplam mağlubiyet: {maglubiyet}")
        print(f"Toplam oynanan tur: {tur_sayisi}")
    else:
        print(f"\n--- {isim} için henüz istatistik bulunmamaktadır. ---")

def skorlari_yukle(mod):
    dosya_adi = SKOR_DOSYALARI[mod]
    try:
        with open(dosya_adi, "r") as dosya:
            skorlar = [satir.strip().split(":") for satir in dosya.readlines()]
            return [(isim, int(skor)) for isim, skor in skorlar]
    except FileNotFoundError:
        return []

def skorlari_guncelle(mod, isim, skor):
    mevcut_skorlar = skorlari_yukle(mod)
    skor_bulundu = False

    for i, (oyuncu, mevcut_skor) in enumerate(mevcut_skorlar):
        if oyuncu == isim:
            if skor > mevcut_skor:
                mevcut_skorlar[i] = (oyuncu, skor)
            skor_bulundu = True
            break

    if not skor_bulundu:
        mevcut_skorlar.append((isim, skor))

    mevcut_skorlar = sorted(mevcut_skorlar, key=lambda x: x[1], reverse=True)

    dosya_adi = SKOR_DOSYALARI[mod]
    with open(dosya_adi, "w") as dosya:
        for oyuncu, puan in mevcut_skorlar:
            dosya.write(f"{oyuncu}:{puan}\n")

def en_iyi_uc_oyuncuyu_yazdir(mod):
    en_iyi_oyuncular = sorted(skorlari_yukle(mod), key=lambda x: x[1], reverse=True)[:3]
    print("\n--- TOP 3 OYUNCU ---")
    for sira, (isim, skor) in enumerate(en_iyi_oyuncular, 1):
        print(f"{sira}. {isim}: {skor} puan")

def tas_kagit_makas_EMRE_ISIK():
    global nickname
    if not nickname:
        nickname = input("Lütfen bir nickname girin: ")

    while True:
        print("\nTaş, Kağıt, Makas oyununa hoş geldiniz!")
        print("1. Mod: Klasik Taş, Kağıt, Makas")
        print("2. Mod: 5 Tane Taş, Kağıt, Makas Seçimi Yapın")
        print("3. Mod: Genişletilmiş Taş, Kağıt, Makas")
        print("4. Mod: Sürekli Dizi")
        print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")
        
        mod_secimi = input("Oynamak istediğiniz modu seçin (1, 2, 3, 4 veya q): ")
        
        if mod_secimi == 'q':
            print("Oyundan çıkılıyor...")
            break
        
        secenekler = ["Taş", "Kağıt", "Makas"]

        if mod_secimi == "1":
            # Mod 1: Klasik Taş, Kağıt, Makas
            toplam_oyun_sayisi = 0
            oyuncu_galibiyetleri = 0
            bilgisayar_galibiyetleri = 0
            beraberlik_sayisi = 0
            tur_sayisi = 0

            while True:
                toplam_oyun_sayisi += 1
                oyuncu_tur_galibiyeti = 0
                bilgisayar_tur_galibiyeti = 0

                while oyuncu_tur_galibiyeti < 2 and bilgisayar_tur_galibiyeti < 2:
                    tur_sayisi += 1
                    oyuncu_secimi = input("Taş, Kağıt veya Makas seçin: ").capitalize()

                    if oyuncu_secimi == 'Q':
                        print("Oyundan çıkılıyor...")
                        return

                    if oyuncu_secimi not in secenekler:
                        print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
                        continue

                    bilgisayar_secimi = random.choice(secenekler)
                    print(f"Bilgisayar {bilgisayar_secimi} seçti.")

                    if oyuncu_secimi == bilgisayar_secimi:
                        print("Berabere!")
                        beraberlik_sayisi += 1
                    elif (oyuncu_secimi == "Taş" and bilgisayar_secimi == "Makas") or \
                        (oyuncu_secimi == "Makas" and bilgisayar_secimi == "Kağıt") or \
                        (oyuncu_secimi == "Kağıt" and bilgisayar_secimi == "Taş"):
                        print("Bu turu siz kazandınız!")
                        oyuncu_tur_galibiyeti += 1
                    else:
                        print("Bu turu bilgisayar kazandı!")
                        bilgisayar_tur_galibiyeti += 1

                    print(f"Durum: Siz {oyuncu_tur_galibiyeti}, Bilgisayar {bilgisayar_tur_galibiyeti}")

                if oyuncu_tur_galibiyeti == 2:
                    oyuncu_galibiyetleri += 1
                    print("Tebrikler! Bu oyunu siz kazandınız!")
                else:
                    bilgisayar_galibiyetleri += 1
                    print("Bilgisayar bu oyunu kazandı.")

                tekrar_oyna = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
                bilgisayar_devam = random.choice(['e', 'h'])

                if tekrar_oyna == 'h' :
                    print("Oyun sona erdi. Oynadığınız için teşekkürler!")
                    break
                if bilgisayar_devam == 'h':
                    print("Oyun sona erdi ve bilgisayar kabul etmedi. Oynadiginiz için teşekkürler!")
                    break
                print("Oyun tekrar başlıyor...")

            skorlari_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri)
            istatistikleri_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri, beraberlik_sayisi, bilgisayar_galibiyetleri, tur_sayisi)
            istatistikleri_yazdir(mod_secimi, nickname)
            

        elif mod_secimi == "2":
            # Mod 2: 5 Tane Taş, Kağıt, Makas Seçimi Yapın
            oyuncu_galibiyetleri = 0
            bilgisayar_galibiyetleri = 0
            beraberlik_sayisi = 0
            tur_sayisi = 5

            print("5 adet taş, kağıt, makas seçimi yapın:")
            oyuncu_secimleri = []
            for i in range(5):
                secim = input(f"{i+1}. seçiminizi yapın: ").capitalize()
                if secim not in secenekler:
                    print("Geçersiz seçim, lütfen tekrar deneyin.")
                    secim = input(f"{i+1}. seçiminizi yapın: ").capitalize()
                oyuncu_secimleri.append(secim)

            bilgisayar_secimleri = [random.choice(secenekler) for _ in range(5)]
            print(f"Bilgisayarın seçimleri: {', '.join(bilgisayar_secimleri)}")

            for i in range(5):
                oyuncu_secimi = oyuncu_secimleri[i]
                bilgisayar_secimi = bilgisayar_secimleri[i]

                if oyuncu_secimi == bilgisayar_secimi:
                    print(f"{i+1}. tur: Berabere! (Siz: {oyuncu_secimi}, Bilgisayar: {bilgisayar_secimi})")
                    beraberlik_sayisi += 1
                elif (oyuncu_secimi == "Taş" and bilgisayar_secimi == "Makas") or \
                    (oyuncu_secimi == "Makas" and bilgisayar_secimi == "Kağıt") or \
                    (oyuncu_secimi == "Kağıt" and bilgisayar_secimi == "Taş"):
                    print(f"{i+1}. tur: Siz kazandınız! (Siz: {oyuncu_secimi}, Bilgisayar: {bilgisayar_secimi})")
                    oyuncu_galibiyetleri += 1
                else:
                    print(f"{i+1}. tur: Bilgisayar kazandı! (Siz: {oyuncu_secimi}, Bilgisayar: {bilgisayar_secimi})")
                    bilgisayar_galibiyetleri += 1

            if oyuncu_galibiyetleri > bilgisayar_galibiyetleri:
                print("Tebrikler! 5 turu kazandınız!")
            elif bilgisayar_galibiyetleri > oyuncu_galibiyetleri:
                print("Bilgisayar 5 turu kazandı!")
            else:
                print("5 tur sonunda sonuç berabere!")

            skorlari_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri)
            istatistikleri_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri, beraberlik_sayisi, bilgisayar_galibiyetleri, tur_sayisi)
            istatistikleri_yazdir(mod_secimi, nickname)
            en_iyi_uc_oyuncuyu_yazdir(mod_secimi)

        elif mod_secimi == "3":
            # Mod 3: Genişletilmiş Taş, Kağıt, Makas
            genis_secenekler = ["Taş", "Kağıt", "Makas", "Silah", "Şimşek", "Şeytan", "Ejderha", "Su", "Hava", "Sünger", "Kurt", "Ağaç", "İnsan", "Yılan", "Ateş"]
            oyuncu_galibiyetleri = 0
            tur_sayisi = 0
            beraberlik_sayisi = 0

            while True:
                tur_sayisi += 1
                oyuncu_secimi = input("Taş, Kağıt, Makas, Silah, Şimşek, Şeytan, Ejderha, Su, Hava, Sünger, Kurt, Ağaç, İnsan, Yılan, Ateş seçin: ").capitalize()

                if oyuncu_secimi == 'Q':
                    print("Oyundan çıkılıyor...")
                    return

                if oyuncu_secimi not in genis_secenekler:
                    print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
                    continue

                bilgisayar_secimi = random.choice(genis_secenekler)
                print(f"Bilgisayar {bilgisayar_secimi} seçti.")

                if oyuncu_secimi == bilgisayar_secimi:
                    print("Berabere!")
                    beraberlik_sayisi += 1
                else:
                    # Kazanma durumları (diğer seçeneklerle genişletilebilir)
                    kazanma_durumlari = {
    "Taş": ["Makas", "Yılan", "İnsan", "Ağaç", "Kurt", "Sünger", "Kağıt"],
    "Silah": ["Taş", "Makas", "Yılan", "İnsan", "Ağaç", "Kurt", "Sünger"],
    "Şimşek": ["Silah", "Taş", "Makas", "Yılan", "İnsan", "Ağaç", "Kurt"],
    "Şeytan": ["Şimşek", "Silah", "Taş", "Makas", "Yılan", "İnsan", "Ağaç"],
    "Ejderha": ["Şeytan", "Şimşek", "Silah", "Taş", "Makas", "Yılan", "İnsan"],
    "Su": ["Ejderha", "Şeytan", "Şimşek", "Silah", "Taş", "Makas", "Yılan"],
    "Hava": ["Su", "Ejderha", "Şeytan", "Şimşek", "Silah", "Taş", "Makas"],
    "Kağıt": ["Hava", "Su", "Ejderha", "Şeytan", "Şimşek", "Silah", "Taş"],
    "Sünger": ["Kağıt", "Hava", "Su", "Ejderha", "Şeytan", "Şimşek", "Silah"],
    "Kurt": ["Sünger", "Kağıt", "Hava", "Su", "Ejderha", "Şeytan", "Şimşek"],
    "Ağaç": ["Kurt", "Sünger", "Kağıt", "Hava", "Su", "Ejderha", "Şeytan"],
    "İnsan": ["Ağaç", "Kurt", "Sünger", "Kağıt", "Hava", "Su", "Ejderha"],
    "Yılan": ["İnsan", "Ağaç", "Kurt", "Sünger", "Kağıt", "Hava", "Su"],
    "Makas": ["Yılan", "İnsan", "Ağaç", "Kurt", "Sünger", "Kağıt", "Hava"],
    "Ateş": ["Makas", "Yılan", "İnsan", "Ağaç", "Kurt", "Sünger", "Kağıt"]


                    }

                    if bilgisayar_secimi in kazanma_durumlari[oyuncu_secimi]:
                        print("Bu turu siz kazandınız!")
                        oyuncu_galibiyetleri += 1
                    else:
                        print("Bilgisayar kazandı, oyun sona erdi!")
                        break

            skorlari_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri)
            istatistikleri_guncelle(mod_secimi, nickname, oyuncu_galibiyetleri, 0, 1, tur_sayisi)
            istatistikleri_yazdir(mod_secimi, nickname)
            en_iyi_uc_oyuncuyu_yazdir(mod_secimi)

        elif mod_secimi == "4":
            # Mod 4: Sürekli Dizi
            tur_sayisi = 0
            while True:
                tur_sayisi += 1
                oyuncu_secimi = input("Taş, Kağıt veya Makas seçin (veya q ile çıkın): ").capitalize()

                if oyuncu_secimi == 'Q':
                    print("Oyundan çıkılıyor...")
                    break

                if oyuncu_secimi not in secenekler:
                    print("Geçersiz bir seçim, lütfen tekrar deneyin.")
                    continue

                bilgisayar_secimi = oyuncu_secimi
                print(f"Bilgisayar da {bilgisayar_secimi} seçti. Berabere!")

                if tur_sayisi >= 5 and tur_sayisi <= 10:
                    rastgele_olay = random.choice([
                        "Bir şimşek çaktı ve oyun kazanan olmadı.",
                        "Taş Kağıt Makas Cini'ni çağırdınız ve ikinizi taş kağıt makas evrenine ışınladı.",
                        "Beraberlik o kadar uzun sürdü ki kollarınız oyunu terk etti.",
                        "Bilgisayar tökezledi ve düştü, bu yüzden oyunu kazandınız."
                    ])
                    print(f"\n--- Rastgele Olay ---\n{rastgele_olay}")
                    break

            print("Mod seçim ekranına dönülüyor...")

        else:
            print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")

if __name__ == "__main__":
    tas_kagit_makas_EMRE_ISIK()
