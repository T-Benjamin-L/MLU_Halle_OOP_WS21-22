eingabenList = []
nutzerEingabe = int(input("Eingabe am Anfang, [0 zum stornieren]: "))
eingabenList.append(nutzerEingabe)
ersterTeil = nutzerEingabe

while nutzerEingabe != 0:
    nutzerEingabe = int(input("nächste Eingabe [0 zum stornieren]: "))
    if nutzerEingabe == 0:
        break

    eingabenList.append(nutzerEingabe)
    zweiterTeil = nutzerEingabe
    print(f"Der Durchschnitt von {ersterTeil} und {zweiterTeil} ist {(ersterTeil + zweiterTeil)/2}")
    ersterTeil = nutzerEingabe

print(f"Der Durchschnittswert von allen eingegebenen Zahlen ist {sum(eingabenList) / (len(eingabenList))}")
