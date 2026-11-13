n = int(input("Ievadi veselu skaitli no 0: "))
skaitlis = 1
summa = 0

while skaitlis < n:
    if skaitlis % 2 == 1:
        summa = skaitlis

    skaitlis = skaitlis + 1

print("Summa:", summa)
