# PROJEKTNA NALOGA IZ ANALIZE PODATKOV IGRE LEAGUE OF LEGENDS

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

To storite s pomočjo ukaza `pip install ime_knjiznice` v terminalu (oz. `pip3 install ime_knjiznice`, če nismo na Windowsih). Predlagam, da to storite v virtualnem okolju, ki ga ustvarite tako, da napišete `python -m venv ime_okolja` v terminal (oz. `python3 -m venv ime_okolja`, če niste na Windowsih). Okolje nato aktivirate s kodo `ime_okolja\Scripts\activate` (oz. `source ime_okolja/bin/activate`, če niste na Windowsih). Vedeli boste, da ste v virtualnem okolju, če vam v ukazni vrstici piše `(ime_okolja) PS C:\Users...`, namesto `PS C:\Users...`. Ob koncu uporabe okolje preprosto izključite z ukazom `deactivate`. 

Ko imate knjižnice pripravljene, lahko klonirate moj repozitorij s pomočjo ukaza:

```git clone https://github.com/lovroklinc/Projektna_naloga```

Podatke nato pridobite tako, da zaženete datoteko izluscevanje_podatkov.py. 

## SPLOŠNE INFORMACIJE 

Za Projektno nalogo sem uporabil podatke iz spletne strani [u.gg/lol](https://u.gg/lol/champions). V analizi preučimo, kako so različni podatki o championih odvisni med sabo in pogledamo razlike tudi v različnih nivojih znanja igralcev. 

<div align="right">Lovro Klinc, 2024</div>