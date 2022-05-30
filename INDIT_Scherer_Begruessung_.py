namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]


def begruessung(name):
    print("Hallo", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")

def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hallo", ein_name)
        print("Schön dich zu sehen!")
        print("VielSpaß mit dem Programm!")

print("Version 1")
for name in namen:
    begruessung(name)

print("Version 1")
begruessung2(namen)
    
for name in namen:
    begruessung(name)