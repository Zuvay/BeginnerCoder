import random
print("Oyun başlıyor")   
atk = random.randrange(30,40)
hp = random.randrange(200,300)
atk1 = random.randrange(20,30)
hp1 = random.randrange(300,400)
mainchar = [atk,hp]
enemy = [atk1,hp1]
print("Karakterinin saldırı değeri", atk,"Can değeri ise", hp)
print("Düşmanının saldırı ve can değerleri ise şunlar:",enemy)
while hp1>0 and hp>0:
        
        hit = int(input("1 ile 3 arasında bir sayı yaz ve vuruşunu yap"))
        while hit != 2 and hit != 1 and hit != 3: 
                hit = int(input("1 ile 3 arasında bir sayı yaz ve vuruşunu yap"))
                print("Hacı 1,2 veya 3 girecen") #123 değilken buraya gir
        crit = random.randrange(3)

        if hit==crit:
                hp1=hp1-atk*2
                hp=hp-atk1
                print("Kritik vurdun")
                print("Düşmanın canı", hp1)
                print("Senin canın", hp)
        else:
                hp1=hp1-atk
                hp=hp-atk1
                print("Normal vurdun")
                print("Düşmanın canı", hp1)
                print("Senin canın", hp)
if hp<0:
        print("MezarTurizm")
else:

        print("Kolaydı")




