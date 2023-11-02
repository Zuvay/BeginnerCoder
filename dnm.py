import random
#print(random.randrange(100))
cards = {
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "K":10,
    "Q":10,
    "J":10,
    "A":10,
}

#key ve value veriyo a = random.choice(list(cards.items()))
#sadece value veriyo b=random.choice(list(cards.values()))
#sadece key'i veriyo c=random.choice(list(cards.keys()))

dealer = []
player = []


takeCard1= random.choice(list(cards.items()))
takeCard2= random.choice(list(cards.items()))
dealer.append(takeCard1)
player.append(takeCard2)
takeCard1= random.choice(list(cards.items()))
takeCard2= random.choice(list(cards.items()))
dealer.append(takeCard1)
player.append(takeCard2)
        
  
    
print("Kasanın elindeki kartlar",dealer[0][0],"ve",dealer[1][0])
print("Elinizdeki kartlar",player[0][0],"ve",player[1][0])  

def sumDealer():
    sumDealerList=[]
    for i in dealer:
        sumDealerList.append(i[1])

    sum1=sum(sumDealerList)
    return sum1

def sumPlayer():
    sumPlayerList=[]
    for i in player:
        sumPlayerList.append(i[1])

    sum1=sum(sumPlayerList)
    return sum1    

print("Kasa toplam :",sumDealer(),"Elinizdeki toplam :",sumPlayer())


hitme = int(input("Kart çekmek isterseniz 1 istemezseniz 0 yazınız"))

if hitme==0:
    while sumDealer()<15:
        a= random.choice(list(cards.items()))
        dealer.append(a)
        print("Çekilen kart :",a[0][0])
        print("Kasa Toplam :",sumDealer())
        if sumDealer()>21:
            print("Siz kazandınız")
        elif sumDealer()<=21:
            if sumDealer()>sumPlayer():
                print("Kasa kazandı")
        elif sumDealer==21:
            print("Kasa kazandı")
        else:
            print("Siz kazandınız")
    else:
        if sumDealer()>sumPlayer():
                print("Kasa kazandı")
        else:
            print("Siz kazandınız")
elif hitme==1:
    b=random.choice(list(cards.items()))
    player.append(b)
    print("Çekilen kart :",b[0][0])
    print("Elinizdeki Toplam :",sumPlayer())
    if sumPlayer()==21:
        print("Siz Kazandınız")
    elif sumPlayer()>21:
        print("Kasa kazandı")
    
    hitme = int(input("Kart çekmek isterseniz 1 istemezseniz 0 yazınız"))
    if hitme==0:
        while sumDealer()<15:
            a= random.choice(list(cards.items()))
            dealer.append(a)
            print("Çekilen kart :",a[0][0])
            print("Kasa Toplam :",sumDealer())
            if sumDealer()>21:
                print("Siz kazandınız")
            elif sumDealer()<=21:
                if sumDealer()>sumPlayer():
                    print("Kasa kazandı")
            elif sumDealer==21:
                print("Kasa kazandı")
            else:
                print("Siz kazandınız")
        else:
            if sumDealer()>sumPlayer():
                    print("Kasa kazandı")
            else:
                print("Siz kazandınız")
    elif hitme==1:
        b=random.choice(list(cards.items()))
        player.append(b)
        print("Çekilen kart :",b[0][0])
        print("Elinizdeki Toplam :",sumPlayer())
        if sumPlayer()==21:
            print("Siz Kazandınız")
        elif sumPlayer()>21:
            print("Kasa kazandı")            
else:
    #Buraya kodu hitme kısmına döndürecek bir şey yazmak lazım sanırım
    print("1") 

