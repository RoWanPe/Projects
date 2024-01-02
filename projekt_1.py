'''
První projekt do Engeto Online Python Akademie 

author: Roman Pečimúth
email: roman.pecimuth@seznam.cz
discord : romanp._
'''
oddelovac = "----" * 10


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


registrovany_uziv = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"} #registrovaní uživatélé


uzivatel = input("Username: ")
#vstup od uživatele , Jméno a heslo
heslo = input("Password: ")

#oveření jestli uživatelův vstup (user,pass) je v registrovanych a zda zadane heslo se nachazi u uzivatele, ke kterému bylo ve slovniku prirazeno
if uzivatel in registrovany_uziv and heslo == registrovany_uziv[uzivatel]:
    print("welcome to the app,", uzivatel.capitalize(),"!","\n" "We hawe 3 text to be analyzed.")
#pri zadani jineho vstupu nez je v registrovanych , vypise text a ukončí se .
else:
    print("unregistered user, terminating the program..")
    quit()
    
print(oddelovac)

vyber = input("Enter a number btw. 1 and 3 to select: ") #vyber textu od 1-3

print(oddelovac)

if vyber.isalpha():
    print("Input numbers only!")
    quit()

elif vyber.isdigit(): # overeni jestli je text cislo
    vyber_cislo = int(vyber)
    
if vyber_cislo in range(1,4): # jestli cislo je v rozsahu 1-3
    vybrany_text = TEXTS[vyber_cislo - 1]
        
    # seznamy pro iteraci nize. 
    slova, velky_slovo, velky_pismeno, male_slovo, cisla = [], [], [], [], []
    #iterace pro analyzu textu . zmena z komprehenze , na samostatný for cyklus s podmínkami.
    for slovo in vybrany_text.split():
        ciste_slovo = slovo.strip(",.!?-") # odstraneni znaku 
        
        if ciste_slovo.isdigit(): # pokud je cislo
            cisla.append(ciste_slovo) # prida do seznamu cisla
        slova.append(ciste_slovo)  # ulozi vsechno rozdelene do seznamu slova         
        
        if ciste_slovo.istitle():   # pokud slovo zacina velkym Pismenem, 
            velky_pismeno.append(ciste_slovo)   # prida do seznamu velky_pismeno
            
        if ciste_slovo.isalpha() and ciste_slovo.isupper(): # pokud slovo obsahuje pouze pismena a je psano velkymi pismeny 
            velky_slovo.append(ciste_slovo) # prida do seznamu velky_slovo
                
        if ciste_slovo.islower(): # pokud je slovo psano malymi pismeny
            male_slovo.append(ciste_slovo) # pridej do seznamu male_slovo
        
    # iterace pro soucet cisel podle vyberu   
    soucet = 0
    for cislo in cisla:
        soucet += int(cislo)
                
    #výpis hodnot
    print(f"There are {len(slova)} words in the selected text")
    print(f"There are {len(velky_pismeno)} titlecase words. ")
    print(f"There are {len(velky_slovo)} uppercase words.")
    print(f"There are {len(male_slovo)} lowercase words.")
    print(f"There are {len(cisla)} numeric strigs.") 
    print(f"The sum of all the numbers {soucet}")       
    print(oddelovac)
    
    delka_cista_slova = {}
    # iterace vyskytu slov 
    for pocet in slova:
        delka = len(pocet)
            
        if delka in delka_cista_slova:
            delka_cista_slova[delka] += 1
                
        else:
            delka_cista_slova[delka] = 1
    
                    
    hlavicka ="LEN|    OCCURENCES    |NR." 
    print(hlavicka,oddelovac, sep="\n") 
        
    #serazeni vyskytu slov a vloženi do grafu
    for delka, pocet in sorted(delka_cista_slova.items()):
        zobrazeni = "*" * pocet
        print(f" {delka:<2}|{zobrazeni:<18}|{pocet:<1}") #:< sirka pole pro danou hodnotu. serazeni
            
else:
    print("wrong numbers! only 1-3 ")
    quit()     