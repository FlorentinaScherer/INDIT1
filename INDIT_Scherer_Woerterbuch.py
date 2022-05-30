# Wörterbuch
wb = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

print ("Welcome, please select a function")
print("Choose [T] to translate")
print("Choose [A] to add a new word")


correct = False

while correct == False:            #solange, bis Eingabe korrekt ist
    eingabe = input("Enter a function: ")
    
    if eingabe == "T":
        word=input ("please enter your word:")
        if word in wb:
            print("translation:", wb[word])
        else:
                print ("not found")
    elif eingabe == "A":
        word=input("english word:") 
input("german translation:")

    else:
        print ("answer not found")
                
                
                
                