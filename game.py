import time  # Importáljuk az időt ezzel tudunk késleltetni

#Rájönni hogyan válaszolhat a felhasználó a különböző esetekben
valasz_A = ["A", "a"]
valasz_B = ["B", "b"]
valasz_C = ["C", "c"]
valasz_D = ["D", "d"]
valasz_E = ["E", "e"]



#A felhasználó csak a megadott választásokkal válaszolhasson
szukseges = ("\nCsak a megadott betűkombinációkat használd!\n")
szukseges2 = ("\n A következő kérdésnél saját választ kell megadnod! Minden választ nagy betűvel kezdj hogy elfogadja a játék!")
#Bemutatkozás
def intro():
 print("Üdv!")
 time.sleep(0.5)
 print("Örülök, hogy újra itt vagy! A legutóbbi kis találkánk után kételkedtem benne, hogy viszont látjuk egymást, de ezek szerint nem igaz, hogy „a villám nem csap kétszer ugyanoda”.")
 time.sleep(2)
 print("""Ismét hoztam egy játékot. Alapjaiban hasonlít az előző kalandunkhoz, de a játékszabályok 
kicsit megváltoztak. Használnod kell a józan ítélőképességed és sokszor kell a tudásodra támaszkodnod, nem mindig fogok választási lehetőségeket adni.
Sok esetben érdemes észben tartani a következőt: nincs jó, vagy rossz választási lehetőség. Döntés van, és az azzal járó következmények.""")
 time.sleep(5)
 print("A változatosság, na meg a móka kedvéért forgatókönyvi stílusban fogom tálalni a dolgokat.")
 time.sleep(1)
 print("Ne is ragozzuk tovább a dolgokat, kezdjük el!")
 time.sleep(5)
 print("""Külső – Városi vasút – NAPPAL
Kívülről láthatunk egy személyvonatot. Az utasok nyugodtan zötykölődnek a lepukkant vasparipa falai között. Látszólag szokványos járatnak tűnik.""")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Látszólag szokványos járat is. Azonban – hogy adjak némi motivációt a játékhoz- elrejtettem egy kis meglepetést a vonaton, ami lehet, hogy megnehezíti néhány ember utazását, vagy életben maradását.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("De cseppet se aggódj! Könnyedén megmentheted őket. Viszonylag könnyedén. Adok neked néhány feladványt, neked pedig jó választ kell adnod! Érthető? Remélem.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Egyébként a nevem mellett a v.o. (voice over) narrációt jelent egy forgatókönyvben. Ezt még le akartam tisztázni.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Kezdhetjük?")
 print ("""A. Igen
B. Nem """)
#1. választási lehetősége a játékosnak
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_kezdes()
 elif choice in valasz_B:
    print("\n  Biztos vagyok benne, hogy érdekelni fog téged. Veszíteni valód nincsen, nem igaz? Na ugye! Szerintem el is kezdhetjük! Showtime!")
    time.sleep(5)
    valasztas_kezdes()
 else:
    print (szukseges)
def valasztas_kezdes():
 print("Narrátor (V.O.)")
 print ("A történet elkezdéséhez mindenképpen szükséged lesz egy karakterre.")
 time.sleep(2)
 print("A gördülő személyvonat képe megáll, mintha egy videót állítottunk volna meg, majd egyszeriben ellepi a köd. Szürke ködfelhők tömkelege borítja be a képet.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Ha már úgy is feladványokat kell kitalálnod, legyél detektív, vagy nyomozó, ahogy tetszik. ")
 time.sleep(5)
 print("""A ködből felemelkedik egy alak, akinek csak a sziluettjét látjuk. Magas, izmos, és olybá tűnik, palásttal fedné testét. Fején két apró szarv virít, a köpeny alját és a lábát a ködfelhő eltakarja. A lényt körülvevő füstöt mintha egy robbanás idézte volna elő.
Az alak lassan közelít a kamera felé.""")
 time.sleep(5)
 print("NARRÁTOR(V.O.)")
 print("De nem olyan jelmezes igazságosztó féle, hanem egy kicsit hagyományosabb.")
 time.sleep(5)
 print("Az előző árny köddé válik, helyébe egy valamivel alacsonyabb ember lép, akinek szintjén csak körvonalait látjuk. Ballonkabátot hord, jobb kezében cigaretta ég, baljában jól kivehetően keresztet markol. Az őt körülölelő füst azonban sokkal inkább dohányfüstre vall.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Mint Poirot, vagy mittomén.")
 time.sleep(3)
 print("A második alak is eltűnik, a ködből David Suchet lép elő, pipázva.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("De ez most nem lényeg. Szóval nyomozgatsz. Éppen te is a vonton utazol, amikor egyszer csak…")
 time.sleep(3)
 print("A hangosbemondóba egy férfihang szólal meg.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Kedves utasaink! Remélem élvezik az utazást! Amennyiben igen, örömmel tájékoztatom önöket, hogy az egyes vagonok aljára robbanószert rögzítettem, és ha nem válaszolnak jól a feladványaimra, a levegőbe röpítem az egész kócerájt! ")
 time.sleep(5)
 print("PÁNIK fogja el az utasokat. Érthető módon.")
 time.sleep(2)
 print("Narrátor (V.O.)")
 #2. választási lehetőség a játékosnak
 print(szukseges2)
 print("Lássuk is az elsőt: hatvan gyermekem van, minden gyermekemtől hatvan unokám. Mi vagyok?")
 choice = input(">>> ")
 if choice == "Óra" or choice == "Egy óra":
     jo_valasz_1()
 elif choice != "Óra" or choice != "Egy óra":
     rossz_valasz_1()
def rossz_valasz_1(): 
 print("Narrátor (V.O.)")
 print("Ez sajnos nem talált. De mivel még jó kedvembe vagyok, adok egy második esélyt.")
 time.sleep(3)
 print("Az ajtó előtt álló utasok egyike hirtelen MEGSZÓLAL.")
 time.sleep(3)
 print("Random idős bácsi")
 print("Ha hatvan gyermeknek van hatvan gyermeke, az azt jelentheti, hogy van egy egész, ami hatvan egységre van tagolva, és egy ilyen egységen belül is van hatvan kisegység.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Jó fele kapizsgál az úr. Akkor még egyszer: hatvan gyermekem van, minden gyermekemtől hatvan unokám. Mi vagyok?")
 time.sleep(5)
 #3. választási lehetőség
 print("""A; 6 óra
       B; 1 óra
       C; 6 perc
       D; 1 perc""")
 choice = input(">>> ")
 if choice in valasz_B:
     jo_valasz_1()
 elif choice in valasz_A or choice in valasz_C or choice in valasz_D:
     halal()
def jo_valasz_1():
 print("Narrátor (V.O.)")
 print("Talált, süllyedt. Az első feladványom kitalálták. Jöjjön a következő.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print(szukseges2)
 print("""Rőzsén élek,
Földön hálok,
Szárnyra kélek
Égen szállok,
Lepkét vonzok,
S álmot űzök. 
Mi vagyok?""")
 time.sleep(10)
#4. választási lehetőség a játékosnak
 choice = input(">>> ")
 if choice == "Tűz":
     jo_valasz_2()
 elif choice != "Tűz":
     rossz_valasz_2()
def rossz_valasz_2():
 print("""FŐSZEREPLŐ/DETEKTÍV
(magában motyogva)""")
 time.sleep(2)
 print("Nem, nem, talán mégsem ez a helyes válasz. Ha rőzsén, vagyis faágon él, földön alszik, vonzza a lepkét, ami szereti a fényt, akkor valami fényhatás lesz, aminek a keletkezéséhez fa kell, és ami olyan nagy is tud lenni, hogy messziről látni.")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Na, kapok még ma választ? Ne már, ez azért annyira nem nehéz! „Rőzsén élek”, „égre szállok”, „lepkét vonzok”,… csak rá lehet jönni!")
 time.sleep(5)
 print(szukseges2)
 print("""Rőzsén élek,
Földön hálok,
Szárnyra kélek
Égen szállok,
Lepkét vonzok,
S álmot űzök. 
Mi vagyok?""")
 time.sleep(10)
#5. választási lehetőség a játékosnak
 choice = input(">>> ")
 if choice == "Tűz":
     jo_valasz_2()
 elif choice != "Tűz":
     halal()
def jo_valasz_2():
 print("Narrátor (V.O.)")
 print("Ez igen, nyomozó! Tuti okosabb, mint egy másodikos. Tudtam én, hogy akad majd játszótársam! ")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Teszteljük le, mennyire vág jól az esze! Lépjen előre, katona!")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Innentől a játék privát! A nyomozó átmegy a másik vagonba, a többiek lekopnak. Ha valaki ellenkezik, annak súlyos ára lesz!")
 time.sleep(5)
 print("A tömeg aggodalmasan FIGYELI, ahogy a nyomozó ÁTLÉP a másik szerelvénybe. ")
 time.sleep(4)
 print("Amint a főhős BELÉP az ajtón, az BEZÁRUL mögötte, majd egy hangos KATTANÁS jelzi, hogy innen már nincs visszaút.")
 time.sleep(4)
 print("Magát a vasúti kocsit teljes sötétség borítja, nem látni semmit, ráadásul a vonat ZÖTYKÖLŐDÉSE az egyetlen hangforrás. ")
 time.sleep(5)
 print("Kis szünet után a NARRÁTOR hangja töri meg a csendet. ")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Üdvözlöm az „atyában”, detektív! ")
 time.sleep(3)
 print("A vagonban felgyúl négy vörösen fénylő lámpa. Most már tisztán látszik a vagon közepén elhelyezkedő éttermi asztal, két oldalán két székkel.")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Foglaljon helyet!")
 #6. választási lehetőség a játékosnak
 print(""" A. Helyet foglal
B. Nem foglal helyet""")
 choice = input(">>> ")
 if choice in valasz_A:
   jo_valasz_3()
 elif choice in valasz_B:
    rossz_valasz_3()
 else:
    print(szukseges)
def rossz_valasz_3():
    print("hehe")