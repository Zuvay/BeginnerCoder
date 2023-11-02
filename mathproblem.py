import random
possibilty = int(input("Kaç defa zar atılsın"))
list=[]
for i in range(possibilty):
    r=random.randrange(1,7)
    list.append(r)
howmuch=list.count(1)
print(howmuch)

if howmuch/possibilty >= 1/6:
    print("Olasılık Başarılı")
else:
    print("Olasılık Başarısız")
