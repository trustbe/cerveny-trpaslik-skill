# Cerveny Trpaslik — Claude Code Skill

> *"Vsichni jsou mrtvi, Dave."*

[Claude Code](https://claude.ai/claude-code) skill pro pokracovani odkazu ceskeho Red Dwarf fan klubu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/). Kompletni knowledge base + kreativni engine — 52 scenaru, 1354 NSFAQ, 14 864 vzkazu, 13 referencnich souboru.

## Quick Start

```bash
git clone https://github.com/trustbe/cerveny-trpaslik-skill.git
cd cerveny-trpaslik-skill
./install.sh
```

Nebo rucne:

```bash
mkdir -p ~/.claude/skills/cerveny-trpaslik
cp SKILL.md ~/.claude/skills/cerveny-trpaslik/
cp -r references ~/.claude/skills/cerveny-trpaslik/
```

Restartuj Claude Code a skill je aktivni.

## Co to umi

| Mod | Popis | Prikaz |
|-----|-------|--------|
| Nova epizoda | Kompletni scenar (cold open + 3 akty) | *"Napis novou epizodu kde..."* |
| Scenka | Kratka scena, 1-5 stran | *"Napis scenku kde Lister a Rimmer..."* |
| In-character | Odpovidani jako postava | *"Odpovez jako Rimmer na..."* |
| Webovy obsah | Postreh, hnidopich, NSFAQ, kucharka, quiz | *"Napis novy NSFAQ entry"* |
| Fan fiction | Pribeh v proze | *"Napis povidku o..."* |
| Rozbor | Hlubkova analyza epizody | *"Rozeber epizodu Navrat do reality"* |
| Lore | Encyklopedicka odpoved | *"Jak funguje holomura?"* |
| Hlaska (stara) | Vyhledani citatu ze serialu | *"Dej hlasku od Rimmera o zkouskach"* |
| Hlaska (nova) | Nova hlaska ve stylu postavy | *"Vymysli novou hlasku pro Kocoura"* |
| Free talk | Konverzace jako RD expert | *"Ktera serie je nejlepsi?"* |

Skill se aktivuje automaticky kdyz zminis: Cerveny trpaslik, Red Dwarf, smeghead, Lister, Rimmer, Cat, Kryten, Holly, Starbug, Kosmik...

## Ukazky vystupu

### Scenka

```
INT. SPACI KAJUTA — DEN

*LISTER lezi na horni palube a hraje si s jojo. RIMMER u stolu studuje.*

RIMMER: Listere, mohl bys prosim prestat s tim jojo?

LISTER: Proc?

RIMMER: Protoze ten zvuk mi pripomina kapani mozkomisniho moku z usi
cloveka, ktery prave absolvoval rozhovor s tebou.

LISTER: To je ponizeni. Podam na tebe stiznost.

RIMMER: Ty podas stiznost na ME? Ja mam na tebe podano dve ste
ctyricet sedm stiznosti a ty jsi jeste nezareagoval na jedinou!

LISTER: No bodejt. Nepodepsanej papir hodim do kose, podepsanej
do zachoda.

*Dvere se otevrou. Vejde KOCOUR. Ma na sobe novy zlaty oblek
s leopardim limcem.*

KOCOUR: Hele, kluci. Jak vypadam?

RIMMER: Jako by se vyloha blystiveho prodejce v Elvisove Gracelandu
rozhodla, ze pujde na rande s diskotekovym globem.

KOCOUR: Diky! To je presne ten look, o kterej jsem usiloval.
```

### NSFAQ ve stylu webu

```
1355. Smeghead_CZ:
Jak to, ze Kocour mel v jedne epizode zrcatko, ale v dalsi se cesal
pred obrazovkou pocitace?

Odpoved: Kocourova sit zrcadel je rozsahlejsi nez Rimmeruv seznam
stiznosti na Listera, coz je samo o sobe monumentalni vykon.
V epizode Paralelni vesmir si muzes vsimnout, ze Kocour kontroluje
svuj vzhled v odrazove plose mikrovlnky. Ve Vymene tel se cesa
pred hlavni obrazovkou. A v Poslednim dni pouziva kapesni zrcatko.

Takze odpoved je: Kocour ma zrcatka VSUDE. Na choddbach, v kajutach,
v Kosmiku. Je to jako Rimmerovy revizni plany — kompletne pokryvaji
celou lod, ale na rozdil od Rimmerovych planu opravdu k necemu slouzi.
```

### Stare hlasky (vyhledavani z databaze 350+ citatu)

Skill ma databazi 350+ presnych citatu ze vsech 52 epizod, kazdy s kontextem.
Muzes hledat podle postavy, epizody, tematu nebo klicoveho slova:

```
> "Dej hlasku od Rimmera o zkouskach"

RIMMER: "Neustale propada u zkousek! Jedenactkrat podle me neni
'neustale'! Kdyz jite roast beef jedenactkrat za zivot, sotva se
rekne: 'Ten clovek ji neustale roast beef.'"
  — ep. 04 Cekani na Boha (Rimmer se brani hodnoceni v tajnem zaznamu)

> "Neco od Holly"

HOLLY: "Prehnane horlivy, zrejme blazen. Pravdepodobne ma vic zubu
nez mozkovych bunek. Vyhlidky na povyseni: komicke."
  — ep. 04 Cekani na Boha (Kapitanuv tajny zaznam o Rimmerovi)

> "Hlaska o lasce"

RIMMER: "Jiste, ze vim, co je laska. Mechanismus, jenz vynalezli
bankeri, aby nas donutili precerpat ucet."
  — ep. 05 Sebevedomi a Mindrak

> "Neco s Kocourem a Listerem"

KOCOUR: "Promin hochu, jakej to ma bejt oblicej?"
LISTER: "Co je s mym oblicej?"
KOCOUR: "Co je s tvym oblicej? Je vzhuru nohama a taky naruby."
  — ep. 04 Cekani na Boha (Kocour pochybuje, ze Lister je Buh)

> "Rimmer a smrt"

RIMMER: "Smrt? Je to jako byt na dovolene s partou Nemcu."
  — ep. 01 Konec (Rimmer popisuje Listerovi, jaky je byt mrtvy)
```

### Nova hlaska (generovana ve stylu postavy)

```
> "Vymysli novou hlasku pro Kocoura"

KOCOUR: "Koukam na sebe do zrcadla a rikam si — nekde ve vesmiru
existuje bytost, ktera vypada takhle dobre. A pak si uvedomim,
ze koukam na sebe. A je mi ty bytosti lito, protoze nemuze bejt ja."
```

### In-character (Rimmer)

```
Dobre. Panove. Vazeni pritomni. A Listere.

Sesli jsme se zde dnes, abych vam predstavil, proc jsem — a to rikam
s veskerou skromnosti, ktere jsem schopen, coz je, uprimne receno,
ZNACNA — jednoznacne nejlepsi kandidat na pozici kapitana.

Kdo z vas ma kompletni sadu reviznich planu cele lodi? Nikdo?
To jsem si myslel. JA je mam. Color-coded. Laminovane.
Se zaloznimi kopiemi ulozenymi na trech ruznych palubach.

Lister nema ani cistou ponozku, natoz strategicky plan.
```

## Struktura projektu

```
cerveny-trpaslik-skill/
|-- SKILL.md                    # Hlavni skill soubor (7 KB)
|-- install.sh                  # Instalacni skript
|-- references/                 # Referencni soubory (232 KB)
|   |-- characters.md           #   Profily postav, catchphrases (27 KB)
|   |-- humor-patterns.md       #   DNA humoru, typy gagu (15 KB)
|   |-- story-structure.md      #   Jak se pise epizoda (11 KB)
|   |-- world-bible.md          #   Vesmir, lode, tech, rasy (15 KB)
|   |-- czech-voice.md          #   Cesky dabing, CZ vs EN (13 KB)
|   |-- episode-guide.md        #   Pruvodce 52 epizodami (40 KB)
|   |-- fanclub-voice.md        #   Hlas webu cervenytrpaslik.cz (9 KB)
|   |-- community-content.md    #   DNA komunitnich formatu (10 KB)
|   |-- content-formats.md      #   Sablony pro novy obsah (7 KB)
|   |-- site-dna.md             #   Meta-analyza webu (7 KB)
|   |-- nsfaq-best-of.md        #   Top 90 NSFAQ entries (35 KB)
|   |-- nadavky-katalog.md      #   Kompletni katalog nadavek (17 KB)
|   |-- trivia-vite-ze.md       #   "Vite, ze...?" trivia (5 KB)
|   |-- hlasky-databaze.md      #   350+ hlasek ze vsech 52 epizod
|-- raw/                        # Surova data z cervenytrpaslik.cz
|   |-- scenare_cz/             #   52 ceskych scenaru
|   |-- scenare_en/             #   51 anglickych scenaru
|   |-- sections/               #   32 sekci webu
|   |-- epizody/                #   155 detailu epizod
|   |-- posadka/                #   39 profilu postav
|   |-- nsfaq/                  #   1354 NSFAQ entries (56 KB)
|   |-- vzkazy/                 #   14 864 vzkazu (744 stranek)
|   |-- hnidopich/              #   9 hnidopich stranek
|   |-- herci/                  #   14 profilu hercu
|   |-- fantazie/               #   4 fan fiction
|   |-- kucharka/               #   14 receptu
|-- tests/                      #   Ukazkove vystupy
|-- scraper.py                  # Scraper hlavnich sekci
|-- scrape_vzkazy.py            # Scraper vzkazu (744 stranek)
```

## Jak to funguje

Skill pouziva 13 referencnich souboru organizovanych do mapy — podle toho co chces delat, cte relevantni reference:

| Ukol | Reference |
|------|-----------|
| Nova epizoda | story-structure → characters → humor-patterns → czech-voice → world-bible |
| Dialog | characters → humor-patterns → czech-voice |
| In-character | characters → czech-voice |
| Web obsah | fanclub-voice → content-formats → community-content |
| Lore otazka | world-bible → episode-guide |
| Stara hlaska | hlasky-databaze → characters |
| Nova hlaska | hlasky-databaze → humor-patterns → characters |

Kazdy vystup prochazi kvalitativnim testem:
- Poznal by fanousek ze to napsal nekdo kdo serial FAKT zna?
- Jsou dialogy rozlisitelne — poznas kdo mluvi i bez jmenovky?
- Je tam humor?
- Sedi to do lore?
- Zni to cesky prirozene?

## Scraper

Scrapers pro stazeni dat z cervenytrpaslik.cz. Pouzivaji 2s delay mezi requesty.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4

# Hlavni scraper — sekce, scenare, epizody, NSFAQ, postavy
python3 scraper.py

# Vzkazy — 744 stranek, trva ~25 minut
python3 scrape_vzkazy.py
```

## Zdroje

Skill je postaven na obsahu webu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/) — legendarniho ceskeho Red Dwarf fan klubu, ktery bezi od zacatku 2000s. Diky autorum za roky prace na budovani ceske Red Dwarf komunity.

Cerveny trpaslik (Red Dwarf) je serial BBC vytvoreny Robem Grantem a Dougem Naylorem. Vsechna prava k serialu nalezi jejich drzitelum.

## License

MIT — viz [LICENSE](LICENSE).

---

*Smoke me a kipper, I'll be back for breakfast!*
