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


registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"} #registrovaní uživatélé


username = input("Username: ")
#vstup od uživatele , Jméno a heslo
password = input("Password: ")

#oveření jestli uživatelův vstup (user,pass) je v registrovanych a zda zadane heslo se nachazi u uzivatele, ke kterému bylo ve slovniku prirazeno
if username in registered_users and password == registered_users[username]:
    print("welcome to the app,", username.capitalize(),"!","\n" "We hawe 3 text to be analyzed.")
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
    cislo_in = int(vyber)
    
if cislo_in in range(1,4): # jestli cislo je v rozsahu 1-3
        vybrany_text = TEXTS[cislo_in - 1]
        slova = vybrany_text.split()
        cista_cisla = [cislo for cislo in vybrany_text.split() if cislo.isdigit()]   # vytvoren seznam , pouze s čísly ,iterace
        ciste_slovo = [bezcisel for bezcisel in vybrany_text.split() if bezcisel.isalpha()] # seznam pouze se slovy . bez číšel .Iterace
        velke_pismeno = [velke_p for velke_p in ciste_slovo if velke_p.istitle()] # seznam  obsahujici slova zacinajicim velky Pismenem Iterace
        velke_slovo = [slovo_big for slovo_big in vybrany_text.split() if slovo_big.isupper()] # seznam obsahujici pouze slova napsáná Velkymi PISMENY Iterace
        male_pismeno = [male_p for male_p in vybrany_text.split() if male_p.islower()] # seznam obsahujici slova psané malými písmeny Iterace
        soucet = sum(int(num) for num in cista_cisla) # soucet všech nalezených čísel a jejich součet.
     #výpis hodnot
        print(f"There are {len(ciste_slovo)} words in the selected text")
        print(f"There are {len(velke_pismeno)} titlecase words. ")
        print(f"There are {len(velke_slovo)} uppercase words.")
        print(f"There are {len(male_pismeno)} lowercase words.")
        print(f"There are {len(cista_cisla)} numeric strigs.") 
        print(f"The sum of all the numbers {soucet}")       
        print(oddelovac)
        
        delka_cista_slova = {}
         # iterace vyskytu slov 
        for slovo in ciste_slovo:
            delka = len(slovo)
            if delka in delka_cista_slova:
                 delka_cista_slova[delka] += 1
                 
            else:
                 delka_cista_slova[delka] = 1
                
        
        hlavicka ="LEN|  OCCURENCES  |NR." 
        
        print(hlavicka,oddelovac, sep="\n") 
        #serazeni vyskytu slov a vloženi do grafu
        for key, values in sorted(delka_cista_slova.items()):
            zobrazeni = "*" * values
            print(f" {key:<2}|{zobrazeni:<14}|{values:<1}") #:< sirka pole pro danou hodnotu. serazeni
            
            
            
else:
         print("wrong numbers! only 1-3 ")
         quit()
    

        
