import random

# Derslerin listesi
dersler = ["Matematik", "Fizik", "Kimya", "Biyoloji", "Tarih", "Coğrafya"]

# Öğretmenlerin listesi ve her birinin kaç ders vereceği
ogretmenler = {
    "X": 2,
    "Y": 2,
    "Z": 2
}

# Boş ders programı
ders_programi = {
    "Pazartesi": [],
    "Salı": [],
    "Çarşamba": [],
    "Perşembe": [],
    "Cuma": []
}

# Öğretmenin boş saatlerinin kontrolü
def bos_saatler(ogretmen, gun, saat):
    for ders in ders_programi[gun]:
        if ogretmen == ders[0] and saat == ders[1]:
            return False
    return True

# Ders programının oluşturulması
for gun in ders_programi:
    for i in range(ogretmenler["X"]):
        ogretmen = "X"
        ders = random.choice(dersler)
        saat = random.choice([1, 2, 3])
        while not bos_saatler(ogretmen, gun, saat):
            saat = random.choice([1, 2, 3])
        ders_programi[gun].append((ogretmen, saat, ders))
    for i in range(ogretmenler["Y"]):
        ogretmen = "Y"
        ders = random.choice(dersler)
        saat = random.choice([1, 2, 3])
        while not bos_saatler(ogretmen, gun, saat):
            saat = random.choice([1, 2, 3])
        ders_programi[gun].append((ogretmen, saat, ders))
    for i in range(ogretmenler["Z"]):
        ogretmen = "Z"
        ders = random.choice(dersler)
        saat = random.choice([1, 2, 3])
        while not bos_saatler(ogretmen, gun, saat):
            saat = random.choice([1, 2, 3])
        ders_programi[gun].append((ogretmen, saat, ders))

# Ders programının ekrana yazdırılması
for gun in ders_programi:
    print(gun + ":")
    for ders in ders_programi[gun]:
        print("\t" + ders[2] + " - " + ders[0] + " - " + str(ders[1]))