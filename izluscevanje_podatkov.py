from bs4 import BeautifulSoup #za izluscevanje uporabimo BeatifulSoup in ne regularnih izrazov
from zajem_podatkov import *

def pridobi_podrobnosti(champion_html):
    with open(champion_html, "r", encoding="utf-8") as dat:
        soup = BeautifulSoup(dat.read(), "html.parser")
        seznam_podatkov = []
        for podatek in ['Win Rate', 'Pick Rate', 'Ban Rate', 'Matches']:
            podatek_div = soup.find('div', class_='label', text=f'{podatek}')
            podatek_vrednost = podatek_div.find_previous_sibling('div', class_='value').text
            seznam_podatkov.append(podatek_vrednost.replace('%', '').replace(',', ''))
    return seznam_podatkov
#vrednosti iscemo z previous_sibling zaradi težav pri win-rate

def pridobi_role(champion_html):
    with open(champion_html, "r", encoding="utf-8") as dat:
        soup = BeautifulSoup(dat.read(), "html.parser")
        role = soup.find('div', style='margin-left:12px').text
    return role
#role poiscemo posebej, ker je v drugacnem segmentu

def pridobi_podrobnosti_vsakega():
    #pridobi_html_vsakega_championa(url_glavne_strani)
    slovar = {}
    for rank in seznam_rankov:
        slovar_championa = {}
        for champion in pridobi_imena(url_glavne_strani):
            slovar_championa[champion] = pridobi_podrobnosti(f"podatki/{rank}/{champion}.html") + pridobi_role(f"podatki/{rank}/{champion}.html")
        slovar[rank] = slovar_championa
    return slovar
#funkcija združi pridobi_role in pridobi_podrobnosti in vrne slovar z vsemi championi oblike {champion:[win_rate, pick_rate, ban_rate, role]}
