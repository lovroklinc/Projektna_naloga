import requests
import re
import os

url_glavne_strani = "https://u.gg/lol/champions"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
} #brez uporabe headers dobimo napako 403


def zajemi_html(url):
    html_strani = requests.get(url, headers=headers).text
    return html_strani
#pridobi text, v katerem dalje iščemo imena championov

def pridobi_imena(besedilo):
    vzorec = r'''/></div><div class="champion-name">(?P<champion>.*?)</div></a><a class="champion-link" href="/lol/champions/'''
    seznam_championov = re.findall(vzorec, besedilo) 
    return seznam_championov.replace("&#x27;", "").lower()  #popravi napačne zapise imen
#iz html-ja vrne seznam vseh championov, čez katere bomo iteratali

def pridobi_html_vsakega_championa(seznam):
    os.mkdir("podatki")
    for champion in seznam:
        with open(f"podatki/{champion}.html", "w", encoding="utf-8") as dat:
            dat.write(zajemi_html(url_glavne_strani + f"/{champion}/build"))

#pridobi_html_vsakega_championa(pridobi_imena(zajemi_html(url_glavne_strani)))

def pridobi_podrobnosti(champion_html_text):
    with open(champion_html_text, "r", encoding="utf-8") as dat:
        tekstovna = dat.read()
        vzorec = r'''<div class="value">(?P<win_rate>.*?)%</div><div class="label">Win Rate</div></div><div class="overall-rank"><div class="value">(?P<rank>.*?)</div><div class="label">Rank</div></div><div class="pick-rate"><div class="value">(?P<pick_rate>.*?)%</div><div class="label">Pick Rate</div></div><div class="ban-rate"><div class="value">(?P<ban_rate>.*?)%</div><div class="label">Ban Rate</div></div><div class="matches"><div class="value">(?P<matches>.*?)</div><div class="label">Matches</div>'''
    
    return list(re.findall(vzorec, tekstovna)[0])
#vrne seznam, ki ima winrate, rank, pickrate,banrate









