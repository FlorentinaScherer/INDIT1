drinks = { "Klaus": "Bier",
           "Sylvia": "Wein",
           "ET": "Whisky",
           "Dracula": "Blut"}

name = input("Name: ")

if name not in drinks:
    print("unbekannter Name", name)
else:
    print("Lieblingsgetränk von", name, ": ", drinks[name])