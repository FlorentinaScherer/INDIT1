intVariable = 0
floatPi = 0
Summe = 0

strTerme = input("Anzahl der Terme:")
intTerme = int(strTerme)

while intVariable <= intTerme:
    
    floatPi = (((-1)**intVariable) / (2*intVariable + 1))
    Summe += floatPi
    intVariable += 1

print ("Die Annaeherung von Pi beträgt:", Summe*4)