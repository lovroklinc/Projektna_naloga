import requests
import re
import os
from pomozne_funkcije import popravi_imena_championov, seznam_rankov

url_glavne_strani = "https://u.gg/lol/champions"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
} #brez uporabe headers dobimo napako 403


def zajemi_html(url):
    html_strani = requests.get(url, headers = headers).text
    return html_strani
#pridobi text, v katerem dalje iščemo imena championov

def pridobi_imena(url):
    besedilo = zajemi_html(url)
    vzorec = r'''/></div><div class="champion-name">(?P<champion>.*?)</div></a><a class="champion-link" href="/lol/champions/'''
    seznam_championov = re.findall(vzorec, besedilo) 
    return popravi_imena_championov(seznam_championov)
#iz html-ja vrne seznam vseh championov, čez katere bomo iteratali

seznam_imen = pridobi_imena(url_glavne_strani)
#seznam imen dodatno shranimo v posebej spremenljivko, za moznost dodatne uporabe drugje 

def pridobi_html_vsakega_championa():
    for rank in seznam_rankov:
        os.makedirs(f"podatki/{rank}")
        for champion in seznam_imen:
            with open(f"podatki/{rank}/{champion}.html", "w", encoding="utf-8") as dat:
                dat.write(zajemi_html(url_glavne_strani + f"/{champion}/build" + f"?rank={rank}"))
#ustvari html datoteke, ki jih bomo potrebovali za vsakega championa (in tudi za vsak rank)










