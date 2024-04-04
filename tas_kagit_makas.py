import random

def blgsyr_scimi_uret():
    n = random.randint(1, 3)
    if n ==1 : 
        return "tas"
    elif n == 2:
        return "kagit"
    elif n == 3:
        return "makas"

def hileli_blgsyr_secimi_uret(kullanici_secimi):
    if kullanici_secimi == "tas":
        return "kagit"
    elif kullanici_secimi == "kagit":
        return "makas"
    else:
        return "tas"
def hileli_blgsyr_scimi_uret(kullanici_secimi):
    if kullanici_secimi == "tas":
        return "kagit"
    elif kullanici_secimi == "kagit":
        return "makas"
    else:
        return "tas"        

skor_kullanici = 0
skor_blgsyr = 0
while True:
    kullanici_secimi = input("tas? kagit? makas? Yalnizca birini secebilirsiniz ").lower()
    if kullanici_secimi not in ["tas","kagit","makas"]:
        print("Gecersiz giris")
        continue
    n  =random.randint(1, 2)
    if n ==1:
        blgsyr_secimi = blgsyr_scimi_uret()
    else:
        blgsyr_secimi = hileli_blgsyr_scimi_uret(kullanici_secimi)
    

    
    print("Bilgisayar :",blgsyr_secimi)

    if blgsyr_secimi == kullanici_secimi:
        print("Berabere")
    elif blgsyr_secimi == "tas" and kullanici_secimi == "kagit":
        skor_kullanici += 1
    elif blgsyr_secimi == "makas" and kullanici_secimi == "tas":
       skor_kullanici += 1 
    elif blgsyr_secimi == "kagit" and kullanici_secimi == "makas":
        skor_kullanici += 1
    else:
        skor_blgsyr += 1        

    print("Siz : ",skor_kullanici,"vs Bilgisayar : ",skor_blgsyr)

    if skor_kullanici == 3 or skor_blgsyr == 3:
        break 

if skor_blgsyr > skor_kullanici:
    print("kaybettiniz")
else:
    print("Kazandiniz")           