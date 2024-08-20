def popravi_imena_championov(seznam):
    popravljen = []
    for champion in seznam:
        popravljen += champion.replace("&#x27;", "").replace(" ", "").replace(".", "")
    return popravljen

def popravi_podrobne_podatke(seznam):
    popravljen = []
    for podatek in seznam[:3]:
        popravljen += float(podatek)
    popravljen += int(seznam[3].replace(",", ""))
    return popravljen