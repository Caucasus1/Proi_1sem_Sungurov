import random
N = random.randrange(2,11)
print("N = ", N)
a = [random.randrange(1,11) for i in range(N)]
print("Initial:",a)
print("Odd Indices:",a[1::2])
print("Maximum:",max(a[1::2]))
