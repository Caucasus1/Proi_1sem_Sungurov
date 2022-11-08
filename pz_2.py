import random 
N = int(input())
while N >= 3601:
 N = N - 3600
print("Число секунд с начала прошлого часа: ", N)
m = int(N/60)
print("Число полных минут с начала прошлого часа:", m) 
