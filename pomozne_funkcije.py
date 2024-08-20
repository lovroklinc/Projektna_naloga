def popravi_imena_championov(seznam):
    popravljen = []
    for champion in seznam:
        popravljen.append(champion.replace("&#x27;", "").replace(".", "").replace("Nunu &amp; Willump", "Nunu").replace("Renata Glasc", "Renata"))
    return popravljen
#popravi problematične zapise imen championov
#Renata Glasc je na strani spravljena zgolj kot Renata, zato bomo ta zapis uporabili tudi mi

def popravi_podrobne_podatke(seznam):
    popravljen = []
    del seznam[1]
    for podatek in seznam[:3]:
        popravljen += [float(podatek)]
    popravljen += [int(seznam[3].replace(",", ""))]
    return popravljen
#odstrani "rank", ki nas verjetno ne zanima in popravi tip podatkov