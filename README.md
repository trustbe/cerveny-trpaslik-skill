# Cerveny Trpaslik — Claude Code Skill

> *"Vsichni jsou mrtvi, Dave."*

Skill pro [Claude Code](https://claude.ai/claude-code) (Anthropic CLI pro Claude) — dava mu kompletni znalost Cerveneho trpaslika a schopnost psat nove epizody, hlasky, obsah ve stylu ceskeho fan klubu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/).

## Co je Claude Code skill?

[Claude Code](https://claude.ai/claude-code) je CLI nastroj od Anthropicu — pises primo v terminalu a Claude ti pomaha s kodem, textem, cimkoli. **Skill** je balicek znalosti, ktery Claude Code nacte automaticky kdyz detekuje relevantni tema. Jakmile nainstalujete tento skill a zminite "Cerveny trpaslik", "Rimmer", "smeghead" apod., Claude automaticky nacte knowledge base a zacne odpovedat jako expert na Red Dwarf.

**Potrebujete:**
- [Claude Code](https://claude.ai/claude-code) (CLI, desktop app, nebo IDE extension)
- Ucet u Anthropic (Pro/Max nebo API)

## Instalace

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

Restartujte Claude Code a skill je aktivni.

## Jak to pouzivat

Proste pisite v Claude Code cesky a zminite cokoli z Red Dwarf. Skill naskoci automaticky. Priklady:

```
> Dej hlasku od Rimmera
> Napis scenku kde Lister a Kocour...
> Kdo to rekl? "Toastuju, tedy jsem."
> Vymysli novou nadavku ve stylu Krytona
> Jak funguje holomura?
> Odpovez jako Rimmer na otazku proc je nejlepsi kapitan
```

Neni zadny specialni prikaz ani syntax — proste se ptate a Claude odpovida se znalosti 52 epizod, 350+ hlasek, vsech postav a vibu ceskeho fan klubu.

## Pouziti s jinymi AI modely

Skill je optimalizovany pro Claude Code, ale reference soubory jsou **obycejne markdown soubory** — muzete je pouzit s cimkoli:

**ChatGPT / GPT-4:** Nahrajte `SKILL.md` + relevantni soubory z `references/` jako Custom Instructions nebo do konverzace. Nejdulezitejsi: `characters.md`, `hlasky-databaze.md`, `humor-patterns.md`.

**Gemini / Google AI Studio:** System Instructions — vlozte `SKILL.md` a pripojte reference jako kontext.

**Cursor / Copilot / jiné IDE:** Zkopirujte `SKILL.md` do `.cursorrules` nebo ekvivalentu. Reference soubory dejte do projektu aby je AI videlo.

**Libovolny model s dlouhym kontextem:** Proste poslete `SKILL.md` + reference jako system prompt. Cim vic referencnich souboru pridate, tim lepsi vysledky.

**Tip:** Pokud model nema dost velky kontext pro vsechny reference, pouzijte alespon:
1. `SKILL.md` (7 KB) — instrukce a pravidla
2. `characters.md` (27 KB) — postavy a hlasy
3. `hlasky-databaze.md` (25 KB) — 350+ citatu
4. `czech-voice.md` (13 KB) — cesky jazykovy feeling

To je ~72 KB textu, coz zvladne i model se 128K kontextem.

## Co to umi

### Hlasky (350+ z databaze)

Skill ma databazi 350+ citatu ze vsech 52 epizod. Kazda hlaska ma postavu,
presny text a kontext (epizoda, situace). Zpusoby pouziti:

| Prikaz | Co udela |
|--------|---------|
| *"Dej hlasku"* | Nahodna hlaska — prekvapi te |
| *"Hlaska od Rimmera"* | Nejlepsi citaty dane postavy |
| *"Neco ze serie III"* | Hlasky z konkretni serie |
| *"Hlaska o lasce"* | Hledani podle tematu (laska, smrt, jidlo, zkousky...) |
| *"Neco sarkastickyho"* | Podle nalady (sarkasmus, wholesome, existencialni...) |
| *"Nejlepsi nadavka od Krytona"* | Nejkreativnejsi urazky |
| *"Hlaska Lister vs Rimmer"* | Vtipna vymena mezi postavami |
| *"Hlaska dne"* | Jedna vyjimecna — na hlavni stranku webu |
| *"Kdo to rekl?"* | Kviz — hadas postavu podle citatu |
| *"Vymysli novou hlasku pro Kocoura"* | NOVA hlaska ve stylu postavy |

### Tvorba

| Mod | Popis | Prikaz |
|-----|-------|--------|
| Nova epizoda | Kompletni scenar (cold open + 3 akty) | *"Napis novou epizodu kde..."* |
| Scenka | Kratka scena, 1-5 stran | *"Napis scenku kde Lister a Rimmer..."* |
| In-character | Odpovidani jako postava | *"Odpovez jako Rimmer na..."* |
| Fan fiction | Pribeh v proze | *"Napis povidku o..."* |

### Webovy obsah (styl cervenytrpaslik.cz)

| Mod | Prikaz |
|-----|--------|
| Postreh | *"Napis novy postreh o Rimmerovi"* |
| Hnidopich | *"Najdi chybu v epizode Polymorf"* |
| NSFAQ | *"Napis novy NSFAQ entry"* |
| Kucharka | *"Napis recept ve stylu RD"* |
| Quiz | *"Vymysli kvizovy otazky"* |

### Znalosti

| Mod | Prikaz |
|-----|--------|
| Rozbor epizody | *"Rozeber epizodu Navrat do reality"* |
| Lore | *"Jak funguje holomura?"* / *"Co jsou GELFove?"* |
| Free talk | *"Ktera serie je nejlepsi?"* / *"Proc je RD genialni?"* |

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

### Nove hlasky (generovane ve stylu postav)

Muzete kombinovat postavu + tema + naladu. Skill vytvori novou hlasku
ktera zni jako by byla z serialu — pouziva databazi 350+ originalnich
citatu jako vzor pro styl, humor a hlas kazde postavy.

```
> "Vymysli novou hlasku pro Kocoura"

KOCOUR: "Koukam na sebe do zrcadla a rikam si — nekde ve vesmiru
existuje bytost, ktera vypada takhle dobre. A pak si uvedomim,
ze koukam na sebe. A je mi ty bytosti lito, protoze nemuze bejt ja."
```

```
> "Nova hlaska od Rimmera o lasce"

RIMMER: "Laska je jako moje dustojnicke zkousky. Cim vic se snazis,
tim vic ti to pripomene, zes na to absolutne nemyslitelne nedostatecne
kvalifikovanej. A nakonec napises 'ja jsem ryba' a slozis se."
```

```
> "Co by rekl Holly o umele inteligenci?"

HOLLY: "Mam IQ sest tisic. A po trech milionech let samoty vim jedno —
inteligence neni o tom kolik vis, ale o tom jak dlouho vydrzis
mluvit se ctyrmi lidmi, z nichz jeden je mrtvy a druhy se obleka
dvacet hodin denne."
```

```
> "Kryton nadava Rimmerovi — ale zdvorile"

KRYTON: "Pane Rimmere, s veskerou uctou — vase strategicke mysleni
pripomina navigacni system, ktery uprimne veri, ze zed je zkratka."
```

Dalsi priklady co muzete rict:
- *"Vymysli 5 novych hlasek o jidle"*
- *"Nova nadavka od Listera pro Rimmera"*
- *"Co by rekl Kocour na socialnich sitich?"*
- *"Rimmer pise motivacni citaty"*
- *"Holly komentuje pocasi"*

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
