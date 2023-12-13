import random
def addParticipants():
    amountParticipants=int(input("Add Participants: "))
    nameParticipants={f"player_{i+1}": [] for i in range(amountParticipants)}
    return nameParticipants

def lottery(participantNames):
    for key in participantNames:
        participantNames[key].extend(random.sample(range(0, 10), 3))  
    return participantNames

def superLoto():
    prizelist = []
    for _ in range(3):
        prize = random.randint(0, 10)
        while prize in prizelist:  
            prize = random.randint(0, 10)
        prizelist.append(prize)
    return prizelist

participants = addParticipants()
lottery(participants)

#if you want to see people's numbers
"""print("Here Is Our Participants:")
for key, value in participants.items():
    print(f"{key}: {value}")"""

print("SUPER LOTO COMING")
forWinner=superLoto()
print(forWinner)

is_anybodyWin=False
for key,value in participants.items():   
    if value == forWinner:
        print(f"Winner is: ", {key})
        is_anybodyWin=True
        break
if is_anybodyWin==False:
    print("Got Taxes From Idiots")
