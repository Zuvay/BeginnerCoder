# TAŞ KAĞIT MAKAS OYUNU
import random

tkm = ['taş','kağıt','makas']
computerChoice = random.choice(tkm)

def game():
    while True:
        try:
            player = input('Taş,Kağıt veya Makas? : ').lower()
            if player not in tkm:
                raise ValueError('Lütfen seçeneklerden birini giriniz')
            else:
                pass

            if player == computerChoice:
                print(f'Bilgisayarın seçimi {computerChoice}')
                print('Oyun berabere')
            
            elif (player=='taş' and computerChoice=='makas') or (player=='kağıt' and computerChoice=='taş') or (player=='makas' and computerChoice=='kağıt'):
                print(f'Bilgisayarın seçimi {computerChoice}')
                print('Kazandınız')

            else:
                print(f'Bilgisayarın seçimi {computerChoice}')
                print('Bilgisayar kazandı')

        except ValueError:
            print('Lütfen seçeneklerden birini giriniz') 

game()
