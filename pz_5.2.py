import random
def AddLeftDigit(D):
 global K
 n = len(str(K))
 K = D*10**n + K
K = random.randrange(1,10000)
print("Число K: ", K)
for i in range(3):
 D = random.randrange(0,10)
 print("Число D, ",i+1,": ", D)
 AddLeftDigit(D)
 print("Измененное K: ", K)
 print()
