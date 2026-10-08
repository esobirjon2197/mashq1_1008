# 1-m
for i in range(1, 21):
    print(i)
from itertools import count

# 2-m
for i in range(2, 31, 2):
    print(i, end=" ")


# 3-m
yigindi = 0
i = 1

while i <= 10:
    yigindi += i
    i += 1

print("Yigindi:", yigindi)


# 4-m
n = int(input("n = "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 5-m
son = 20

while son >= 1:
    print(son, end=" ")
    son -= 1
