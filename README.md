# PROJEKTNA NALOGA IZ ANALIZE PODATKOV IGRE LEAGUE OF LEGENDS

## SPLOŠNE INFORMACIJE 

Za Projektno nalogo sem uporabil podatke iz spletne strani [u.gg/lol](https://u.gg/lol/champions). Podatki, ki so bili uporabljeni so bili zajeti 2.9.2024. V analizi preučimo, kako so različni podatki o championih odvisni med sabo in pogledamo razlike tudi v različnih nivojih znanja igralcev. 

## ZGRADBA

Prvi del se izvede s pomočjo datoteke zajem_podatkov.py, kjer so definirane funkcije za zajem html-jev championov. Datoteka izluscevanje_podatkov.py te funkcije uporabi in iz html-jev pridobi vse za nas pomembne podatke in jih zapiše v csv datoteke za vsak rank posebej. V datoteki analiza_podatkov.ipynb se podatki uporabijo za grafično analizo, ki na zanimiv način prikaže podatke. Celotno delovanje podpre datoteka pomozne_funkcije.py, ki ima definirane funkcije, ki za celotno delovanje niso ključne, ampak popravijo tip podatkov, omogočijo lepši zapis v jupyter notebook... 

## NAVODILA

Za ogled analize podatkov odprite datoteko analiza_podatkov.ipynb. 

Če želite podatke za analizo pridobiti sami, najprej naložite knjižnice:
- requests
- re
- os
- BeautifulSoup4
- pandas
- csv
- matplotlib.pyplot
- numpy
- seaborn

To storite s pomočjo ukaza `pip install ime_knjiznice` v terminalu (oz. `pip3 install ime_knjiznice`, če niste na Windowsih). Predlagam, da to storite v virtualnem okolju, ki ga ustvarite tako, da napišete `python -m venv ime_okolja` v terminal (oz. `python3 -m venv ime_okolja`, če niste na Windowsih). Okolje nato aktivirate s kodo `ime_okolja\Scripts\activate` (oz. `source ime_okolja/bin/activate`, če niste na Windowsih). Vedeli boste, da ste v virtualnem okolju, če vam v ukazni vrstici piše `(ime_okolja) PS C:\Users...`, namesto `PS C:\Users...`. Ob koncu uporabe okolje preprosto izključite z ukazom `deactivate`. 

Ko imate knjižnice pripravljene, lahko klonirate moj repozitorij s pomočjo ukaza:

```git clone https://github.com/lovroklinc/Projektna_naloga```

Podatke pridobite tako, da zaženete datoteko izluscevanje_podatkov.py. 

<div align="right">Lovro Klinc, 2024</div>