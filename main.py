#1-misol
def teskari(royxat):
    return royxat[::-1]

r = [int(x) for x in input("Sonlarni kiriting: ").split()]
print("Teskari ro‘yxat:", teskari(r))


#2-misol
def kalkulyator(a, b, amal):
    if amal == '+':
        return a + b
    elif amal == '-':
        return a - b
    elif amal == '*':
        return a * b
    elif amal == '/':
        return a / b if b != 0 else "Bo‘lish mumkin emas"
    else:
        return "Noto‘g‘ri amal"

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
amal = input("Amalni kiriting (+, -, *, /): ")
print("Natija:", kalkulyator(a, b, amal))

#3-misol
def soz_soni(satr):
    return len(satr.split())

matn = input("Matn kiriting: ")
print("So‘zlar soni:", soz_soni(matn))


#4-misol
def juft_ikki(royxat):
    return [x * 2 if x % 2 == 0 else x for x in royxat]

r = [int(x) for x in input("Sonlarni kiriting: ").split()]
print("Natija:", juft_ikki(r))


#5-misol
def kalitlar_royxati(lugat):
    return list(lugat.keys())

lugat = {}
n = int(input("Nechta element kiritasiz: "))
for i in range(n):
    k = input(f"{i+1}-kalit: ")
    v = input("Qiymat: ")
    lugat[k] = v

print("Kalitlar ro‘yxati:", kalitlar_royxati(lugat))
