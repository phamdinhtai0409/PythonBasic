import numpy as np

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))

arr = np.zeros((x, y), dtype= int)

for i in range (0, x):
    for j in range (0, y):
        arr[i,j] = i*j
print(arr)

