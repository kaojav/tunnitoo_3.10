""""Tunnitöö 03.10"""

# ül.1
# konsooli printimine prindi konsooli tervitus
print("Hommmikkkkk!")


# ül.2
# muuda oma kood nii et see küsiks kasutajalt nime ja tervitaks teda
# vihje: sisend saab kutsuda funktsiooniga input()
# kui on vaja esitada konkreetne küsimus
# siis selle saab sõne andmetüübina kirjutada funtsiooni sisse
#print("Tere, " + input("Sinu nimi:") + "!")
# print(f"Tere, {input()}!")---f-str

# ül.2.1
# muuda oma kood nii et kasutaja ei peaks mõtlema liigsetele tühikutele ja suurele algustähele


# ül.3.1
# kontrolli oma teadmisi. Mida väljastavad kosooli kolm allolevat koodi
# vastus kirjuta noole taha, seejärel kustuta rea alguses olev# ja kontorlli enast
print(type(7))  # -> int
print(type("siin on mingisugune lause"))  # -> string
print(type(7.0))  # -> float


# ül.3.2
# kirjuta sulgudesse vastav pythoni termin
# sõne (str), täisarv(int), ratsionaalarv(float)
print("komme on pakis" + str(35) + "tk")
# MUUTUJAD - kuidas hoida andmeid mälus
# matemaatikast teame muutjuaid x ja y, kuid samuti teame et tegelikult võivad nad
# määrata kas aastaid, kogust, protsenti jne. ehk tingimisi on kokkulepe,
# et matemaatikas kasutame ühe tähega muutujaid...
# programmerimises võime neid nimetada nii nagu ise soovime
# selle jaoks määrame muutjuale nime ning seejärel anname talle = märgi abil väärtuse
# ül.4
# mõtle välja loogiline nimetus muutujale, mis määrab sinu vanust, pane see kirja
taaveti_vanus = 12
# Python 3.0 oli väljastatud aastal 2008
release_year = 2008
# mõtle välja loogiline nimetus muutujale, mis määrab pyhtoni vanust matemaatilise tehtena, pane see kirja
pythoni_vanus = 2024- release_year
