# Viikon 2 ja 3 harjoitustehtävät
Tässä repositoriossa/koodivarastossa sijaitsevat ohjelmistojen ylläpito ja testaus
-kurssin toisen ja kolmannen viikon tehtävät. Tämä tiedosto, `README.md` sisältää
tehtävien kuvauksen ja ohjeet tehtävien tekemiseen ja palauttamiseen.

Varsinainen tehtävien palautus tehdään kurssin Moodle-sivulla olevaan kansioon
pyydetyssä muodossa.

Apua gitin käyttöön voi hakea esimerkiksi seuraavista resursseista:
* [GitHub git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [GitLab git cheat sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)
* [gittutorial – gitin oma intro gitin käyttöön](https://git-scm.com/docs/gittutorial)
* [w3 schoolsin materiaalit gitistä](https://www.w3schools.com/GIT/)

## Termejä
* haara = branch
* commit = commit (termiä ei ole käännetty tässä materiaalissa)
* aktiivinen haara = active branch
* päähaara = main branch
* liittäminen/liitos = merge
* pohjahaaran vaihto = rebase

## Tehtävien aloittaminen
Tehtävät saat omalle koneellesi kloonaamalla repositorion, esimerkiksi komennolla
`git clone https://github.com/sampsapenna/ohjelmistojen-ypt.git`. Mikäli käytät
esimerkiksi jotain graafista käyttöliittymää gitille, käytettävät komennot voivat
vaihdella. Pääsääntöisesti esimerkit annetaan gitin komentoriviversiolle.

Repositorion kloonaamisen jälkeen avaa kloonattu repositorio VSCodessa, esimerkiksi
valitsemalla kohta `File -> Open Folder` ja navigoimalla kloonattuun kansioon.

Suoritettavat muutokset tehdään omassa paikallisessa repositoriossa, eikä luotuja
haaroja tarvitse siirtää GitHubiin.

Tehtäväkohdat pisteytetään lähtökohtaisesti samanarvoisina, eli jokaisesta kohdasta
saa yhden pisteen. Mikäli jossain kohdassa on korkeampi maksimipisteytys, se on
merkitty tehtävän otsikon yhteyteen.

Mikäli löydät itsesi umpikujasta, voit käyttää seuraavia komentoja palauttaaksesi
itsesi aiempaan tilanteeseen. Huomioi, että komennot voivat yliajaa tekemiäsi muutoksia!
* `git reset --soft [haara|commit-id]` – palauta haarasi tiettyyn kohtaan, jätä muutokset odottamaan commitia
* `git reset --hard [haara|commit-id]` – sama kuin edellinen, mutta heitä tehdyt muutokset roskiin. MUUTOKSIA EI VOI PALAUTTAA.
* `git checkout -- [tiedosto]` – poista tiedostoon tehdyt muutokset, joita ei ole vielä commitattu. MUUTOKSIA EI VOI PALAUTTAA.
* `git rm --cached [tiedosto]` – peruuta tiedoston lisääminen gitin versionhallintaan, poistamatta alkuperäistä tiedostoa
* `git rm [tiedosto]` – poista tiedosto gitin versionhallinnasta. TIEDOSTOA EI VOI PALAUTTAA.

Mikäli repositorio menee aivan täysin jumiin, voit myös tarvittaessa kloonata sen
uudelleen ja aloittaa alusta. Mikäli haluat kokeilla jotain potentiaalisesti
vahingolista repositoriolle, voi tehdä sen joko täysin tuoreessa kloonissa tai
omassa haarassaan. Ole kuitenkin huolellinen, ettet vahingossa poista jo tekemääsi
työtä samalla.

## Tehtävien palauttaminen
Tehtävien palautus koostuu seuraavista tiedostoista:
* Lyhyt vapaamuotoinen raportti siitä, miten tehtävät suoritettiin. Voit kuvata esimerkiksi
    - mitä komentoja ajettiin
    - millaisia ongelmia tuli vastaan ja miten sait ne mahdollisesti ratkaistua
    - mikäli markdown (myös tässä ohjeessa käytetty markup-kieli) on tuttu entuudestaan, hyvä muoto koodia sisältävän raportin kirjoittamiseen on esimerkiksi juuri markdown. Markdownin voi myös halutessaan muuttaa esimerkiksi pdf:ksi erilaisilla työkaluilla, kuten pandoc. Tarkoitukseen lienee olemassa myös verkkosivustoja.
* Tekstitiedosto, joka sisältää päähaaran git-lokin tehdyistä muutoksista
    - tekstitiedoston voi luoda esimerkiksi komentorivillä komennolla `git log > lokitiedosto.txt`
    - lokin saa halutessaan kopioida muullakin tavalla, pääasia on että se löytyy
* Muut tiedostot, jotka halutessasi haluat lisätä palautukseen

Palautettavista tiedostoista luodaan arkistotiedosto, joka palautetaan Moodleen.

## Tehtävä 1 (1p) – haaran luonti ja vaihtaminen
Aluksi harjoitellaan tyypillisten git-komentojen käyttöä. Tehtävänä
on luoda haara `feature/harj1-edits`, ja siirtyä editoimaan kyseistä haaraa.
Tässä kohtaa raporttiin kannattaa lisätä esimerkiksi näyte `git status`-komennosta,
josta aktiivinen haara voidaan nähdä.

## Tehtävä 2 (1p) – commitin luonti
Lisää neljännet rivit markdown-tiedostoihin `tiedostot/harj1.md` ja
`tiedostot/harj2.md` aikaisempien rivien mukaisesti. Tämän jälkeen lisää tiedostoihin
tehdyt muutokset osaksi seuraavaa commitia, ja lisää raporttiin lisäämisen jälkeinen
`git status`-komennon tulos. Tämän jälkeen luo commit lisätyistä muokkauksista,
sopivan commit-viestin kanssa.

## Tehtävä 3 (1p) – muutosten liittäminen (merge)
Siirry takaisin päähaaraan, jota tässä repositoriossa kutsutaan nimellä `main`.
Voit halutessasi varmistaa oikean aktiivisen haaran komennolla `git status`.
Kaikki käytettävissä olevat haarat on myös mahdollista tarkistaa komennolla
`git branch`.

Siirryttyäsi takaisin päähaaraan, liitä aiemmin luomasi haaran `feature/harj1-edits`
muutokset päähaaraan `git merge`-komennolla.

## Tehtävä 4 (2p) – liittämisessä kohdattavat virheet ja pohjahaaran vaihto
Alkuperäisessä repositoriossa on haara `feature/more-harj-edits`, jonka saa
synkronoitua omalle laitteelle komennolla `git checkout feature/more-harj-edits`.
Tämän jälkeen voit vaihtaa tässä vaiheessa takaisin päähaaraan.

Kokeile liittää haara `feature/more-harj-edits` päähaaraan tehtävän 3 tavoin.
Tämän pitäisi johtaa virheilmoitukseen, jonka näet tarkemmin komennolla
`git status`. Mikäli avaat tiedostot tekstieditorissa, esim. VSCode,
näet gitin lisäämät merkinnät siitä, missä haaran liittämisessä kohdatut
ongelmat ovat. VSCode osaa myös korostaa tiedostot, joissa kulloinkin on
kohdattu ongelmia. Nämä näkyvät punaisena tiedostolistauksessa, ja niiden
tiedostonimen perässä on huutomerkki.

Ei tällä kertaa korjata ongelmaa liitoksen yhteydessä, vaan ajetaan
komento `git merge --abort` liitosprosessin perumiseksi. Tämän jälkeen siirrytään
takaisin haaraan `feature/more-harj-edits`.

Mikäli perehdyt tarkemmin gitin lokiin komennolla `git log` näet, että lokista
puuttuvat äsken tekemäsi muokkaukset. Voit varmistua tästä esimerkiksi vertailemalla
commitien tunnisteita (commitin perässä oleva heksadesimaalimuotoinen tiiviste)
toistensa välillä. Tämän tyyppisessä tilanteessa on yleensä parasta tehdä
pohjahaaran vaihto (rebase), joka on tämän tehtävän tarkoitus.

Käynnistä pohjahaaran vaihtaminen komennolla `git rebase main`, ja korjaa virheet
tiedostoista `tiedostot/harj1.md` ja `tiedostot/harj2.md`. Harjoituksessa on
tarkoitus, ettei tehtyjä muutoksia menetetä, joten ratkaise virhe yhdistämällä
muutokset siten, että rivit ovat edelleen järkevässä järjestyksessä keskenään.

> Gitin terminologia liitoksia ja pohjahaaran vaihtoa tehdessä voi olla ajoittain
> epäselvä. Editorin kohta "incoming change" tarkoittaa muutosta, jota ollaan
> kulloinkin liittämässä aiempaan historiaan. "current" tarkoittaa koodin tämänhetkistä
> tilaa. Tämä tarkoittaa sitä, että liitosoperaatiossa (merge) incoming tarkoittaa
> haaraa, jota ollaan liittämässä – pohjahaaraa vaihtaessa (rebase) incoming puolestaan
> tarkoittaa omia muutoksiasi, joita ollaan liittämässä uuteen pohjahaaraan. Käytännössä
> operaatiosta riippuen näiden termien suunta ikäänkuin vaihtuu. Tämä on yleensä
> yksi hankalimpia gitin konsepteja käsittää, ja sitä on pyritty avaamaan esimerkiksi
> [tässä](https://stackoverflow.com/questions/59607874/difference-between-accept-current-change-and-accept-incoming-change)
> ja [tässä](https://stackoverflow.com/questions/2959443/why-is-the-meaning-of-ours-and-theirs-reversed-with-git-svn/2960751#2960751)
> Stack Overflow -ketjussa. Ei siis tarvitse pelästyä, mikäli asia vaikuttaa hankalalta
> nyt alkuvaiheessa.

Korjattuasi ongelmat, lisää ne osaksi seuraavaa commitia komennoilla
```
git stage tiedostot/harj1.md
git stage tiedostot/harj2.md
```
jotta git tietää tiedostojen olevan nyt korjattuna. Tämän jälkeen voit pyytää
gitiä hoitamaan homman valmiiksi komennolla `git rebase --continnue`. Kun pohjahaara
on onnistuneesti vaihdettu, voit siirtyä takaisin päähaaraan ja liittää haaran
osaksi päähaaraa.

Tässä vaiheessa `git log` pitäisi näyttää listaus, jossa näkyy viimeisimpänä äsken
liittämäsi haaran commit, ja sitä edellisenä tehtävässä 2 tekemäsi commit.
Listaus sisältää näiden lisäksi yhden tai useampia aiempia commiteja, jotka ovat
syntyneet osana repositorion luomista.

## Tehtävä 5 (1p) – .gitignore-tiedoston luominen
Luodaan vielä `.gitignore`-tiedosto, ja lisätään se git-repositorioon. Kuten
aiemmissakin tehtävissä, aloitetaan luomalla uusi haara ja siirtymällä editoimaan
tätä uutta haaraa. Uudessa haarassa avataan tiedosto `.gitignore`, ja lisätään
siihen seuraava sisältö:
```
__pycache__/
*.py[cod]
*$py.class

.Python
build/
develop-eggs/
dist/
eggs/
.eggs/
lib/
lib64/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

*.manifest
*.spec

pip-log.txt
pip-delete-this-directory.txt

.tox/
.coverage
.coverage.*
.cache
coverage.xml
*.cover
.pytest_cache/

instance/
.webassets-cache

target/

.python-version

.mypy_cache/

.venv/

.vscode/
```

Lisää tiedosto versionhalinnan tietokantaan komennolla `git add .gitignore`, ja
lisää se commitina haluamallasi commit-viestillä. Tämän jälkeen siirry takaisin
päähaaraan ja liitä haara, jossa lisäsit `.gitignore`-tiedoston.

## Tehtävä 6 (1p) – python-julkaisutiedoston luominen
Nyt pikaisten git-tehtävien jälkeen, luodaan annetulle esimerkkipaketille
julkaisutiedosto luennolla käsitellyllä tavalla. Muutokset voi tehdä
tällä kertaa suoraan päähaaraan, mikäli näin haluaa, mutta voi jatkaa
myös luomalla uuden haaran ja liittämällä sen muutosten jälkeen
päähaaraan.

Julkaistava paketti sisältää pienen Flaskilla kirjoitetun web-palvelimen
muutamine esimerkkisivuineen. Flaskin osaaminen ei ole olennaista tehtävien
tekemisen kannalta, mutta Flaskin käyttämiseen voi perehtyä dokumentaation
[aloitussivulla halutessaan.](https://flask.palletsprojects.com/en/stable/quickstart/#quickstart)

Luodaan tiedosto `pyproject.toml` ja lisätään sinne seuraavat rivit. Tiedostossa
kommentit on merkitty #-merkillä, kommenteilla on pyritty selittämään olennaiset
asiat tiedoston sisällöstä.
```
# julkaisujärjestelmän määrittely
[build-system]
requires = ["hatchling"]  # https://pypi.org/project/hatchling/
build-backend = "hatchling.build"

# projektin metatiedot
[project]
name = "example-mini-server"  # projektin nimi
dynamic = ["version"]  # version määrittely dynaamisesti luotavaksi parametriksi
description = "Mini example server for automated testing"  # projektin kuvaus
readme = "README.md"  # ohjetiedoston nimi
requires-python = ">=3.12"  # vaaditun python-version määrittely
license = "MIT"  # lisenssin dokumentointi
authors = [  # koodin kirjoittaja/t
    { name = "Sampsa Penna" },
]
classifiers = [  # projektin luokittelu, esimerkiksi kehityksen tila ja tarkoitettu käyttäjäryhmä
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.12",
    "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
]
dependencies = [  # projektin riippuvuuksien määrittely
    "Flask==3.1.0"
]

# ylimääräitsen riippuvuuksien määrittely
[project.optional-dependencies]
# Testien vaatimat paketit
test = [
    "black==25.1.0",
    "coverage==7.6.10",
    "flake8-docstrings==1.7.0",
    "flake8==7.1.1",
    "mypy==1.14.1",
    "pytest-cov==6.0.0",
    "pytest==8.3.4",
    "tox==4.23.2",
    "setuptools==71.1.0",
]
# Kehitysympäristön vaatimat paketit
dev = [
    "pre-commit==4.0.1",
    "ruff==0.9.2",
]

# Projektin osoitteet
[project.urls]
Source = "https://github.com/sampsapenna/ohjelmistojen-ypt.git"

# aiemman dynaamisen version määrittely
[tool.hatch.version]
path = "palvelin/__init__.py"

# julkaistavien pakettien määrittely
[tool.hatch.build]
include = [
    "palvelin/"
]
exclude = [
    "palvelin_tests/"
]

# automaattisen muotoilijan (black) asetusten määrittely
[tool.black]
line-length = 90
target-version = ['py312']

# automaattisen tyylintarkistuksen asetusten määrittely
[tool.ruff]
line-length = 90
target-version = "py312"

# https://beta.ruff.rs/docs/rules/
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    # "ANN",   # flake8-annotations
    "C",   # flake8-comprehensions
    "B",   # flake8-bugbear
    "D",   # pydocstyle
#    "UP",  # pyupgrade
    "S",   # Bandit
]

ignore = [
    "ANN101",  # Missing type annotation for `self` in method
    "E501",    # line too long, handled by black
    "B904",    # do not perform function calls in argument defaults
    "PLR2004", # magic value used in comparison
    "S113",    # Probable use of requests call without timeout
    "D203",    # one-blank-line-before-class
    "D213",    # multi-line-summary-second-line
]

[tool.ruff.mccabe]
max-complexity = 15
```

Tämän jälkeen lisätään luotu `pyproject.toml` esimerkiksi komennolla
`git add`, ja luodaan uusi commit. Tiedoston syntaksin oikeellisuutta
voi kokeilla ajamalla komennon `pip install .`.

> Ennen asennuskomennon ajamista, tarkista esimerkiksi viikon 1 harjoitusten
> ohjeista virtuaaliympäristöjen (venv) käyttö. Tyypillisesti pipillä
> ei kannata asentaa paketteja suoraan järjestelmäversioon.

Commitin luomisen jälkeen, mikäli käytit taas uutta haaraa, liitä
tekemäsi muutokset osaksi päähaaraa.

# Tehtävä 7 (1p) – testiautomaation luonti toxilla
Lisätään tiedosto, jossa otetaan käyttöön automaattinen testaus
tox-työkalulla. Jälleen kerran, voit halutessasi tehdä muutokset
joko suoraan päähaaraan, tai uuden kehityshaaran kautta.

Luodaan tiedosto `tox.ini`, johon lisätään seuraavat rivit.
```
# Toxin omat asetukset
[tox]
envlist = flake8, bandit, docs, mypy, black
skipdist = True

# flake8 (tyylintarkastus) asetukset
[flake8]
max-line-length = 80
select = C,E,F,W,B,B950
ignore = E203,E501,W503,ANN101
exclude = .git/, ./venv/, ./.tox/, build/
# Not using type hints in tests, ignore all errors
per-file-ignores =
    tests/*:ANN

# Testiympäristöjen määrittelyt ->

# bandit (yleisten tietoturvavirheiden tarkastus)
[testenv:bandit]
skip_install = True
deps = bandit
commands = bandit -r ./palvelin

# flake8 (tyylintarkastus)
[testenv:flake8]
skip_install = True
deps =
    flake8
    flake8-docstrings
    flake8-annotations
commands = flake8 palvelin palvelin_tests

# mypy (tyypityksen tarkastus, ei oikeasti tarpeellinen tässä repositoriossa)
[testenv:mypy]
skip_install = True
deps =
    -rrequirements.txt
    mypy
# Mypy fails if 3rd party library doesn't have type hints configured.
commands = mypy --ignore-missing-imports --no-namespace-packages palvelin/

# testiympäristöille yhteiset asennukset
[testenv]
deps =
    -rrequirements.txt

# black (automaattinen muotoilija)
[testenv:black]
skip_install = True
deps =
    black
commands = black palvelin palvelin_tests -l 90 --check
```

Tämän jälkeen testaa toxin toiminta asentamalla kehittäjäriippuvuudet
pipillä aiemmin luodusta `pyproject.toml`-tiedostosta, ja aja komento
`tox`. Toxin pitäisi luoda tarvittavat testiympäristöt ja suorittaa
testit automaattisesti.

Testien läpimeno ei tässä vaiheessa ole olennaista, mutta voit halutessasi
koittaa korjata testien näyttämät virheet.

> Kehittäjäpaketit voidaan asentaa komennolla `pip install .[test]`

Lisää `tox.ini`-tiedosto tämän jälkeen repositorioon, ja luo commit.
Tarvittaessa liitä kehityshaarasi päähaaraan.

# Tehtävä 8 (1p) – pre-commitin konfigurtointi ja käyttönotto
Lisätään tiedosto, jossa määritellään pre-commit ohjelman ajamat
komennot. Pre-commit on ohjelma, jolla voidaan ajaa tietyt testit
muokattua koodia vasten jokaisen `git commit`-komennon yhteydessä.
Näin saadaan valvottua liitettävän koodin laatua, ja vähennettyä mahdollisuuksia
virheiden tekemiseen jo ennen kirjoitetun koodin mahdollista katselmointia
(review).

Luodaan tiedosto `.pre-commit-config.yaml`, ja lisätään sinne seuraavat
rivit:
```
repos:
  - repo: meta
    hooks:
    - id: check-hooks-apply
    - id: check-useless-excludes

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
    - id: no-commit-to-branch
      args: [--branch, main]
    - id: check-toml
    - id: check-yaml
    - id: check-ast
    - id: check-docstring-first
    - id: check-case-conflict
    - id: check-merge-conflict
    - id: end-of-file-fixer
    - id: trailing-whitespace

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.3.7
    hooks:
    - id: ruff
      args: [--fix, --exit-non-zero-on-fix]
      files: ^palvelin/

  - repo: https://github.com/psf/black
    rev: 24.4.0
    hooks:
    - id: black
      args: [-l, "90"]

  - repo:  https://github.com/PyCQA/bandit
    rev: 1.7.8
    hooks:
    - id: bandit
      files: ^palvelin/

  - repo: local
    hooks:
    - id: mypy
      name: mypy
      entry: mypy
      language: system
      types: [python]
      files: ^palvelin/
      args: [--ignore-missing-imports, --no-namespace-packages]
      require_serial: true
```

Tämän jälkeen otetaan pre-commit käyttöön ajamalla seuraavat komennot:
```
pip install .[dev]
pre-commit install
```

Lisätään luotu tiedosto `.pre-commit-config.yaml` repositorioon komennolla
`git add .pre-commit-config.yaml` ja luodaan commit. Tässä vaiheessa pre-commitin
pitäisi jo suorittua. Pre-commitin ajamien testien pitäisi mennä läpi. Mikäli
ne eivät suoritu onnistuneesti, ei niitä tarvitse lähteä korjaamaan – korjausta
voi toki halutessaan yrittää. Testit voi tarvittaessa skipata flagilla `--no-verify`
`git commit`-komennon yhteydessä, mikäli niiden läpimeno estää commitin luomisen.
Esimerkkikomentona testien ohittamiseen `git commit --no-verify -m "create .pre-commit-config.yaml file" .pre-commit-config.yaml`.

Mikäli teit muutokset käyttäen kehityshaaraa, älä unohda liittää kehityshaaran
muutoksia takaisin päähaaraan.

# Tehtävä 9 (2p) – pytestin lisääminen toxiin
> Huomaa, että pre-commit estää nyt suorat muutokset päähaaraan.
> Muutokset on nyt siis luotava uuden haaran kautta, ja liitettävä takaisin
> päähaaraan.

Viimeisenä tehtävänä lisätään pytestin ympäristö toxiin. Toxin asetuksiin voi hakea
apua edellisen luennon esimerkeistä, ja muista toxin ympäristöistä. Lisää uusi
testiympätistö testiympäristöjen listaan, ja kokeile onnistuuko testiympäristön
suorittaminen.

Liitä raporttisi `git diff`-komennon tuloste ennen commitin tekemistä, sen jälkeen
tee commit luomistasi muutoksista ja liitä se tarvittaessa takaisin päähaaraan.

Testikomennoksi riittää pelkkä `pytest`, mutta halutessasi voit lisätä luennolla
pikaisesti esitellyn testikattavuuden mukaan pakettiin. Tätä ei kuitenkaan vaadita
tehtävän läpäisemiseksi.
