# K177 — Švitorka AI

> *"Chrlím hlášky, tedy jsem."*

Celý Červený trpaslík v jednom AI. Dali byste si hlášku?

Zná každou epizodu, každou postavu, každou nadávku. Najde starou hlášku, vymyslí novou. Nedá pokoj. Jako správný toastovač.

Výrobce: Křápol a.s. — Taiwan | Typ přístroje: Mluvící toastovač

## Jak to funguje

Referenční soubory jsou **obyčejné markdown soubory** — fungují s jakýmkoli AI modelem. Pošlete je jako kontext a AI začne chápat Červeného trpaslíka.

### Claude Code (automatický skill)
```bash
git clone https://github.com/trustbe/cerveny-trpaslik-skill.git
cd cerveny-trpaslik-skill
./install.sh
```
Skill se aktivuje automaticky když zmíníte Červený trpaslík, Rimmer, smeghead...

### ChatGPT / GPT-4
Nahrajte `SKILL.md` + soubory z `references/` jako Custom Instructions nebo do konverzace.

### Gemini / Google AI Studio
System Instructions — vložte `SKILL.md` a připojte reference jako kontext.

### Cursor / Copilot / jiné IDE
Zkopírujte `SKILL.md` do `.cursorrules` nebo ekvivalentu.

### Jakýkoli jiný LLM
Pošlete `SKILL.md` + reference jako system prompt. Klíčové soubory:
- `SKILL.md` — instrukce a pravidla
- `references/characters.md` — postavy a hlasy
- `references/hlasky-databaze.md` — databáze citátů
- `references/humor-patterns.md` — DNA humoru

## Jak to používat

Prostě se ptáte. Žádná speciální syntax. Příklady:

```
> Dej hlášku od Rimmera
> Kdo to řekl? "Toastuju, tedy jsem."
> Vymysli novou nadávku ve stylu Krytona
> Jak funguje holomůra?
> Odpověz jako Rimmer na otázku proč je nejlepší kapitán
```

## Co to umí

Skill má dva základní režimy — **vyhledávání** (staré věci ze seriálu) a **tvorba** (nové věci ve stylu seriálu). Plus znalostní režim pro otázky o lore.

---

### 1. Staré hlášky — vyhledávání v databázi

Databáze 350+ přesných citátů ze všech 52 epizod. Každá hláška má postavu,
přesný text, číslo epizody a kontext (kdo říká komu, v jaké situaci).
Nic se nevymýšlí — všechno je z originálních českých scénářů.

| Příkaz | Co udělá |
|--------|---------|
| *"Dej hlášku"* | Náhodná hláška — překvapí tě |
| *"Hláška od Rimmera"* | Nejlepší citáty dané postavy |
| *"Něco ze série III"* | Hlášky z konkrétní série |
| *"Hláška o lásce"* | Hledání podle tématu (láska, smrt, jídlo, zkoušky...) |
| *"Něco sarkastickýho"* | Podle nálady (sarkasmus, wholesome, existenciální...) |
| *"Nejlepší nadávka od Krytona"* | Nejkreativnější urážky |
| *"Hláška Lister vs Rimmer"* | Vtipná výměna mezi postavami |
| *"Hláška dne"* | Jedna výjimečná — na hlavní stránku webu |
| *"Kdo to řekl?"* | Kvíz — hádáš postavu podle citátu |

---

### 2. Nové hlášky — tvorba ve stylu postav

AI vytvoří NOVOU hlášku, která v seriálu neexistuje, ale zní jako by tam patřit mohla.
Používá databázi 350+ originálních citátů jako vzor pro styl, humor a hlas každé postavy.
Můžete kombinovat postavu + téma + náladu.

| Příkaz | Co udělá |
|--------|---------|
| *"Vymysli novou hlášku pro Kocoura"* | Nová hláška ve stylu postavy |
| *"Nová hláška od Rimmera o lásce"* | Postava + téma |
| *"Co by řekl Holly o umělé inteligenci?"* | Postava + moderní téma |
| *"Kryton nadává Rimmerovi — ale zdvořile"* | Postava + styl |
| *"5 nových hlášek o jídle"* | Víc hlášek najednou na téma |
| *"Nová nadávka od Listera pro Rimmera"* | Nová nadávka ve stylu postavy |
| *"Rimmer píše motivační citáty"* | Postava v neobvyklém kontextu |
| *"Co by řekl Kocour na sociálních sítích?"* | Postava vs. moderní svět |

**Rozdíl oproti starým hláškám:** Staré hlášky jsou PŘESNÉ citáty ze scénářů seriálu.
Nové hlášky jsou AI-generované ve stylu postav — nikdy nebyly v seriálu, ale
zní autenticky, protože AI zná hlas, humor a slovník každé postavy z 52 epizod.

---

### 3. Tvorba (delší obsah)

| Mód | Popis | Příkaz |
|-----|-------|--------|
| Nová epizoda | Kompletní scénář (cold open + 3 akty) | *"Napiš novou epizodu kde..."* |
| Scénka | Krátká scéna, 1-5 stran | *"Napiš scénku kde Lister a Rimmer..."* |
| In-character | Odpovídání jako postava | *"Odpověz jako Rimmer na..."* |
| Fan fiction | Příběh v próze | *"Napiš povídku o..."* |

### 4. Webový obsah (styl cervenytrpaslik.cz)

| Mód | Příkaz |
|-----|--------|
| Postřeh | *"Napiš nový postřeh o Rimmerovi"* |
| Hnidopich | *"Najdi chybu v epizodě Polymorf"* |
| NSFAQ | *"Napiš nový NSFAQ entry"* |
| Kuchařka | *"Napiš recept ve stylu RD"* |
| Kvíz | *"Vymysli kvízové otázky"* |

### 5. Znalosti a lore

| Mód | Příkaz |
|-----|--------|
| Rozbor epizody | *"Rozebeř epizodu Návrat do reality"* |
| Lore | *"Jak funguje holomůra?"* / *"Co jsou GELFové?"* |
| Free talk | *"Která série je nejlepší?"* / *"Proč je RD geniální?"* |

Skill se aktivuje automaticky když zmíníte: Červený trpaslík, Red Dwarf, smeghead, Lister, Rimmer, Cat, Kryten, Holly, Starbug, Kosmík...

## Ukázky — co napíšu, co dostanu

### Stará hláška (1 téma = víc citátů)

```
> Hláška o lásce
```
```
RIMMER: "Jistě, že vím, co je láska. Mechanismus, jenž vynalezli
bankéři, aby nás donutili přečerpat účet."
  — ep. 05 Sebevědomí a Mindrák

RIMMER: "Víš kolikrát v životě jsem se já s někým miloval?"
LISTER: "Ne, to nechci vědět."
RIMMER: "Jednou." LISTER: "Boha jeho!" RIMMER: "Jednou jedinkrát."
  — ep. 12 Paralelní vesmír (Rimmer opilý odhaluje své tajemství)

KOCHANSKÁ: "Nikdy jsem se na něj nedívala, jako by byl kozí sýr
s kousky ananasu! Možná jednou, dvakrát jako na kozí sýr,
ale nikdy, *nikdy* s kousky ananasu!"
  — ep. 39 Uroboros (Kochanská popírá své city k Listerovi)

LISTER: "Já jsem poslední muž na světě."
KOCHANSKÁ: "No, co se dá dělat?"
  — ep. 43 Epidém
```

### Stará hláška (podle postavy)

```
> Dej hlášku od Holly
```
```
HOLLY: "Přehnaně horlivý, zřejmě blázen. Pravděpodobně má víc zubů
než mozkových buněk. Vyhlídky na povýšení: komické."
  — ep. 04 Čekání na Boha (kapitánův tajný záznam o Rimmerovi)

HOLLY: "Já jsem desátá generace holografických počítačů s umělou
inteligencí. Ne tvoje máma."
  — ep. 02 Ozvěny budoucnosti (Holly odpovídá podrážděnému Rimmerovi)

HOLLY: "Jean Paul Sartre tvrdil, že peklo je být navždy zamčenej
v místnosti s přáteli." LISTER: "Holly, všichni jeho kamarádi
byly Frantíci."
  — ep. 03 Rovnováha sil
```

### Random hláška

```
> Dej hlášku
```
```
RIMMER: "Zhoršil se mi zrak. Tos namaloval ty? To je brak!"
LISTER: "To je zrcadlo."
  — ep. 03 Rovnováha sil
```

### Kvíz

```
> Kdo to řekl?
```
```
"Toastuju, tedy jsem."

a) Rimmer  b) Holly  c) Toastovač  d) Kryton
```

### Nová hláška od Rimmera o lásce

```
> Nová hláška od Rimmera o lásce
```
```
RIMMER: "Miloval jsem jednu ženu. Dvanáct minut. A to počítám
i tu pizzu. Kdybych nepočítal pizzu, tak jsem miloval tři minuty.
A dvě z toho jsem hledal vypínač."

RIMMER: "Láska je jako důstojnické zkoušky. Čím víc se snažíš,
tím víc ti to připomene, žes na to absolutně nemyslitelně
nedostatečně kvalifikovanej. A nakonec napíšeš 'já jsem ryba'
a složíš se."

RIMMER: "Víš co je na hologramech tragické? Nemůžeš se nikoho
dotknout. Víš co je ještě tragičtější? Když jsem byl živý,
taky se mě nikdo nechtěl dotknout."
```

### Nové hlášky od všech postav na téma

```
> Nové hlášky o jídle
```
```
LISTER: "Neříkám, že Rimmerovo vaření je špatný. Říkám, že naposled,
co vařil, tak robíci odmítli umejt hrnec a jeden z nich podal
výpověď."

KOCOUR: "Já nejím nic, co nevypadá tak dobře jako já. Což eliminuje
prakticky všechno kromě suši. A i to suši musí být čerstvený."

KRYTON: "Pane Listere, vaše vindaloo dosahuje na Scovilleho stupnici
hodnot, které obvykle měří jaderná fyzika."

HOLLY: "Dneska je na menu kuřecí vindaloo, hovězí vindaloo a veganská
varianta — vindaloo bez kuřete a hověziny. Což je vlastně omáčka."
```

### Scénka

```
> Napiš scénku kde Lister a Rimmer...
```
```
INT. SPACÍ KAJUTA — DEN

*LISTER leží na horní palubě. RIMMER u stolu studuje.*

RIMMER: Listere, mohl bys prosím přestat s tím jojo?

LISTER: Proč?

RIMMER: Protože ten zvuk mi připomíná kapání mozkomíšního moku z uší
člověka, který právě absolvoval rozhovor s tebou.

LISTER: To je ponížení. Podám na tebe stížnost.

RIMMER: Ty podáš stížnost na MĚ? Já mám na tebe podáno dvě stě
čtyřicet sedm stížností a ty jsi ještě nezareagoval na jedinou!

LISTER: No bodejť. Nepodepsanej papír hodím do koše, podepsanej
do záchoda.
```

### In-character

```
> Odpověz jako Rimmer proč bys měl být kapitán
```
```
Dobře. Pánové. Vážení přítomní. A Listere.

Sešli jsme se zde dnes, abych vám představil, proč jsem — a to říkám
s veškerou skromností, které jsem schopen, což je, upřímně řečeno,
ZNAČNÁ — jednoznačně nejlepší kandidát na pozici kapitána.

Kdo z vás má kompletní sadu revizních plánů celé lodi? Nikdo?
To jsem si myslel. JÁ je mám. Color-coded. Laminované.
Se záložními kopiemi uloženými na třech různých palubách.

Lister nemá ani čistou ponožku, natož strategický plán.
```

## Struktura projektu

```
cerveny-trpaslik-skill/
├── SKILL.md                    # Hlavní skill soubor (7 KB)
├── install.sh                  # Instalační skript
├── references/                 # Referenční soubory (232 KB)
│   ├── characters.md           #   Profily postav, catchphrases (27 KB)
│   ├── humor-patterns.md       #   DNA humoru, typy gagů (15 KB)
│   ├── story-structure.md      #   Jak se píše epizoda (11 KB)
│   ├── world-bible.md          #   Vesmír, lodě, tech, rasy (15 KB)
│   ├── czech-voice.md          #   Český dabing, CZ vs EN (13 KB)
│   ├── episode-guide.md        #   Průvodce 52 epizodami (40 KB)
│   ├── fanclub-voice.md        #   Hlas webu cervenytrpaslik.cz (9 KB)
│   ├── community-content.md    #   DNA komunitních formátů (10 KB)
│   ├── content-formats.md      #   Šablony pro nový obsah (7 KB)
│   ├── site-dna.md             #   Meta-analýza webu (7 KB)
│   ├── nsfaq-best-of.md        #   Top 90 NSFAQ entries (35 KB)
│   ├── nadavky-katalog.md      #   Kompletní katalog nadávek (17 KB)
│   ├── trivia-vite-ze.md       #   "Víte, že...?" trivia (5 KB)
│   └── hlasky-databaze.md      #   350+ hlášek ze všech 52 epizod
├── raw/                        # Surová data z cervenytrpaslik.cz
│   ├── scenare_cz/             #   52 českých scénářů
│   ├── scenare_en/             #   51 anglických scénářů
│   ├── sections/               #   32 sekcí webu
│   ├── epizody/                #   155 detailů epizod
│   ├── posadka/                #   39 profilů postav
│   ├── nsfaq/                  #   1354 NSFAQ entries (56 KB)
│   ├── vzkazy/                 #   14 864 vzkazů (744 stránek)
│   ├── hnidopich/              #   9 hnidopich stránek
│   ├── herci/                  #   14 profilů herců
│   ├── fantazie/               #   4 fan fiction
│   └── kucharka/               #   14 receptů
├── tests/                      # Ukázkové výstupy
├── scraper.py                  # Scraper hlavních sekcí
└── scrape_vzkazy.py            # Scraper vzkazů (744 stránek)
```

## Jak to funguje

Skill používá 14 referenčních souborů organizovaných do mapy — podle toho co chcete dělat, čte relevantní reference:

| Úkol | Reference |
|------|-----------|
| Nová epizoda | story-structure → characters → humor-patterns → czech-voice → world-bible |
| Dialog | characters → humor-patterns → czech-voice |
| In-character | characters → czech-voice |
| Webový obsah | fanclub-voice → content-formats → community-content |
| Lore otázka | world-bible → episode-guide |
| Stará hláška | hlasky-databaze → characters |
| Nová hláška | hlasky-databaze → humor-patterns → characters |

Každý výstup prochází kvalitativním testem:
- Poznal by fanoušek že to napsal někdo kdo seriál FAKT zná?
- Jsou dialogy rozlišitelné — poznáš kdo mluví i bez jmenovky?
- Je tam humor?
- Sedí to do lore?
- Zní to česky přirozeně?

## Scraper

Scrapers pro stažení dat z cervenytrpaslik.cz. Používají 2s delay mezi requesty.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4

# Hlavní scraper — sekce, scénáře, epizody, NSFAQ, postavy
python3 scraper.py

# Vzkazy — 744 stránek, trvá ~25 minut
python3 scrape_vzkazy.py
```

## Zdroje

Skill je postaven na obsahu webu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/) — legendárního českého Red Dwarf fan klubu, který běží od začátku 2000s. Díky autorům za roky práce na budování české Red Dwarf komunity.

Červený trpaslík (Red Dwarf) je seriál BBC vytvořený Robem Grantem a Dougem Naylorem. Všechna práva k seriálu náleží jejich držitelům.

## Roadmap — kam to posunout dál

Projekt je kompletní jako knowledge base, ale má potenciál vyrůst v celý ekosystém. Nápady:

### MCP Server
- **Červený Trpaslík MCP** — zpřístupnit databázi jako [MCP server](https://modelcontextprotocol.io/) s tools: `hlaska(tema, postava)`, `nadavka(postava)`, `kviz()`, `lore(tema)`, `nova_hlaska(postava, tema)`. Pak funguje v jakémkoli MCP klientovi — Claude Code, Claude Desktop, Cursor, Copilot, cokoli.

### Sociální sítě
- **Twitter/X bot @TrpaslikHlasky** — random hláška ze seriálu každý den, nová AI hláška ve stylu postav jednou týdně. Automatické postování z databáze 350+ citátů.
- **Instagram/Threads** — hlášky jako grafické karty s portréty postav

### Web
- **Hláška dne** — jednoduchá statická stránka (HTML/CSS/JS), random hláška z databáze, tlačítko "další", sdílení na sociální sítě. Hostovat na GitHub Pages zdarma.
- **Interaktivní kvíz** — "Která postava jsi?", "Poznáš epizodu podle hlášky?", "Kdo to řekl?" — webová verze kvízu z databáze

### Komunita
- **Discord bot** — `/hlaska`, `/nadavka`, `/kviz` přímo v chatu. Komunita fanoušků s kanály pro jednotlivé série.
- **Trpaslík Revival** — podcast/stream formát: rozbory epizod, nové AI scénky, kvízy s diváky. Host = AI Rimmer odpovídá na otázky in-character.

### Obsah
- **Série IX-XIII (2012-2020)** — seriál pokračoval, ale cervenytrpaslik.cz je nemá. Doplnit scénáře, hlášky a epizodní průvodce z novějších řad.
- **Víc hlášek** — aktuálně 350+, dalo by se vytáhnout 500+ hlubším průchodem scénářů
- **Obrázky a screenshoty** — doplnit vizuální obsah k hláškovému kontextu

### Produkty
- **Mobilní app** — hláška dne jako widget/notifikace, offline databáze citátů
- **Merch generátor** — AI generuje nápisy na trička ve stylu Red Dwarf nadávek (*"intergalaktický hnisavý vřed"*, *"těhotný smradlavý lenochod"*)
- **Tapety/wallpapers** — hlášky jako grafické tapety na telefon/desktop

Pull requesty vítány! Pokud chcete pomoct s čímkoli z roadmapy, otevřete issue.

## Licence

MIT — viz [LICENSE](LICENSE).

---

*Smoke me a kipper, I'll be back for breakfast!*
