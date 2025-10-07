# voce = ['jabuka', "banana"]
# voce.insert(1, "pomo0randza")

# print(voce)

# voce.append("mandarina")
# print(voce)

# indeks_mandarine = voce.index("mandarina")
# print(indeks_mandarine)


# ime = input("Unesite ime: ")
# print("Prva tri slova su: ", ime[0:3])

# rec = input("Unestire rec: ")
# print("Poslednja cetiri slova", rec[-4:])

# tekse = "jabuka.kriska.kruska"
# novi_tekst = tekse.replace(".", ",")
# print(novi_tekst)

# reci = ["jabuka", "banan", "kruska"]
# recenica = ", ".join(reci)
# print(recenica)

# tekst = "Python je sjajan jezik za programiranje"
# reci = tekst.split()
# print(type(reci))
# print(reci)

# for rec in reci:
#         if len(rec) > 5:
#                 print(rec)

# boje = ["crvena", "plava", "zelena"]
# for boja in boje:
#     print(boja)

# for i in range(2,6,2):
#     print(i)


# imena = ["Ana", "Angelina", "Dejana"]
# for i in range(len(imena)):
#     print("Indeks: ", i)
#     print("Ime", imena[i])


# ime = "Zoran"

# for i in ime:
#         print(i)


# tekst = "programiranje"
# samoglasnici = "aeiou"
# brojac = 0
# for slovo in tekst:
#     if slovo in samoglasnici:
#         brojac += 1

# print("Broj samoglasnika: ", brojac)



# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i} * {j} = {i*j}")





# imena = ["Zoran", "Dejan", "Milan"]
# ocene = [5, 4, 3]

# for ime in imena:
#     for ocena in ocene:
#         print(f"{ime} je dobio ocenu {ocena}")

# for broj in range (10):
#     if broj ==5:
#         break
#     print("broj je: ",broj)


# for broj in range(10):
#     if broj == 2:
#         continue
#     print(broj)


# n = int(input("Unesi broj: "))
# for i in range(1, n+1):
#     print (i)

# a = int(input("Unesi pocetni broj "))
# b = int(input("Unesi krajnji "))
# for i in range(a, b+1):
#     print(i)

################
# a = int(input("Unesi broj "))
# for i in range(a, 0, -1):
#     print(i)
# # unazad ispisuje

# rec = input("Unesite rec: ")
# slovo = input("Uneste slovo: ")
# brojac = 0

# for karakter in rec:
#     if karakter == slovo:
#         brojac += 1
# print(f"Slovo {slovo} se u reci {rec} pojavljuje {brojac} puta" )

# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)

# A = [10, 2, 3]
# B = [3, 5]

# for a in A:
#     for b in B:
#         print(f"{a} * {b} = {a*b}")


# broj_cokoladica = 3
# broj_sladoleda = 3

# if broj_cokoladica == broj_sladoleda:
#     print("Broj je isti")
# else:
#     print("Broj nije isti")
# broj = 11
# print(broj)


# godine = input("Koliko godina: ")

# if int(godine) >= 18:
#     print ("Punoletni")
# else: 
#     print ("Maloletni")


# broj1 = input("Broj 1: ")
# broj2 = input ("Broj 2: ")

# zbir = int(broj1) + int(broj2)

# print(zbir)

""""
varijabla = "Zoran"
godina = 51

print(f"Moje ima je {varijabla} i imam {godina} godinu.")
"""

ime_korisnika = input("Upisi : ")
email_korisnika = input("Mail: ")
sifra_korisnika = input("Sifra: ")

# print(ime_korisnika.count(" "))
ime_korisnika = ime_korisnika.strip()

broj_razmaka = ime_korisnika.count(" ")
print(broj_razmaka)
ime_korisnika = ime_korisnika.title()
if broj_razmaka > 0 :
    print("Sve je uredu")
    print(f"{ime_korisnika}")
else: 
    print("Morate uneri i prezime")





