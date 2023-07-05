n, m = tuple(input().split(" "))
n = int(n.strip())
m = int(m.strip())

for i in range(n):
    if i % 2 > 0:
        print((".|." * i).center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n - 1, 0, -1):
    if i % 2 > 0:
        print((".|." * i).center(m, "-"))
