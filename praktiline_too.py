"""Iseseisev praktiline töö"""

# Kirjuta kood mis:
# 1) küsib kasutajalt ainult täisarve a ja b
# 2) tagastab kasutajale a ja b summa, korrutise ja ruutude summa
# all on sulle vastuse näide koos andmetüübiga f-sõne, proovi jutumärkide sisse panna loogsulud {}

a = int(input("Sisesta täisarv a:  "))
b = int(input("Sisesta täisarv b: "))

print(f"SUMMA:{a + b}")
print(f"KORRUTIS:{a * b}")
print(f"RUUTUDE SUMMA:{a ** 2 + b ** 2}")
