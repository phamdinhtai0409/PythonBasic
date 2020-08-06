n=int(input("Nhap so vao day: "))
s = 1
for i in range(1, n+1):
    s *= i
print(s, end="")