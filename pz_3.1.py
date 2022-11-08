x,y = map(int, input().split())
print(f"x = {0}, y = {1}")
b = (x > 0 and y > 0) or (x < 0 and y < 0) 
print("Точка лежит в 1-й или 3-й координатной четверти: ", b) 
