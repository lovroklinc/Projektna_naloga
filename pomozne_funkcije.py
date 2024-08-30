import pandas as pd

def popravi_imena_championov(seznam):
    popravljen = []
    for champion in seznam:
        popravljen.append(champion.replace("&#x27;", "").replace(".", "").replace("Nunu &amp; Willump", "Nunu").replace("Renata Glasc", "Renata"))
    return popravljen
#popravi problematične zapise imen championov
#Renata Glasc je na strani spravljena zgolj kot Renata, zato bomo ta zapis uporabili tudi mi

def popravi_podrobne_podatke(seznam):
    popravljen = []
    for podatek in seznam[:3]:
        try:
            popravljen.append(float(podatek))
        except:
            popravljen.append(float(0))
    popravljen.append(int(seznam[3].replace(",", "")))
    return popravljen
#popravi tip podatkov
#s try-exceptom se znebimo problema, ko ban-rate ne pokaže
#namesto tega damo vrednost 0, saj se to pojavi, ko champion še ni bil bannan

def izbrani_champs(n, kriterij, rank = 'overall'):
    champs = pd.read_csv(f'../podatki/csv/{rank}.csv')
    dobri = champs.nlargest(n, kriterij).sort_values(by = kriterij)
    slabi = champs.nsmallest(n, kriterij).sort_values(by = kriterij)
    return  pd.concat([slabi, dobri])
#vrne podatke za n championov primerne za izdelavo grafov



