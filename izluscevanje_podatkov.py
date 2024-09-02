from bs4 import BeautifulSoup 
from zajem_podatkov import *
from pomozne_funkcije import popravi_podrobne_podatke
import re
import csv
import os 

def pridobi_podrobnosti(champion_html):
    with open(champion_html, "r", encoding="utf-8") as dat:
        soup = BeautifulSoup(dat.read(), "html.parser")
        seznam_podatkov = []
        for podatek in ['win-rate', 'pick-rate', 'ban-rate', 'matches']:
            podatek_div = soup.find('div', class_=re.compile(fr'^{podatek}'))
            podatek_vrednost = podatek_div.find('div', class_='value').text
            seznam_podatkov.append(podatek_vrednost.replace('%', '').replace(',', ''))
        role = soup.find('div', style='margin-left:12px').text
    return popravi_podrobne_podatke(seznam_podatkov) + [role]
#za iskanje uporabimo tudi regularne izraze, saj je zapis pri win-rate spremenljiv
#role je bil najprej svoja funkcija, ki smo jo zavoljo manjšega odpiranja datotek združili

def pridobi_podrobnosti_vsakega():
    pridobi_html_vsakega_championa()
    slovar = {}
    for rank in seznam_rankov:
        slovar_championa = {}
        for champion in seznam_imen:
            slovar_championa[champion] = pridobi_podrobnosti(f"podatki/{rank}/{champion}.html")
        slovar[rank] = slovar_championa
    return slovar
#vrne slovar z vsemi championi oblike {champion:[win_rate, pick_rate, ban_rate, role]}


def pisanje_csv_datotek():
    vrhovni_slovar = pridobi_podrobnosti_vsakega()
    os.makedirs('podatki/csv')
    for rank in seznam_rankov:
        with open(f'podatki/csv/{rank}.csv', 'w', newline='') as csv_dat:
            pisatelj = csv.writer(csv_dat)
            pisatelj.writerow(['Champion', 'Win Rate (%)', 'Pick Rate (%)', 'Ban Rate (%)', 'Matches', 'Role'])
            for champion, podatki in vrhovni_slovar[rank].items():
                pisatelj.writerow([champion] + podatki)
#napise csv datoteke za vsak rank posebej

pisanje_csv_datotek()
