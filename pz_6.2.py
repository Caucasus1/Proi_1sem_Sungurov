import random
N = random.randrange(2,21)
#a = [random.randrange(1,11) for i in range(N)]
a = [i for i in range(N)]
b = a[0::3]
print("N:",N)
print("Array a:\n",a)
print("Length of b:\n",len(b))
print("Array b:\n",b)
