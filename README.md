# Červený Trpaslík — AI Knowledge Base & Skill

> *"Všichni jsou mrtví, Dave."*

Kompletní AI znalostní báze Červeného trpaslíka — 52 epizod, 350+ hlášek, všechny postavy. Umí vyhledat staré hlášky, vymyslet nové ve stylu postav, psát scénáře, scénky a obsah v duchu českého dabingu. Funguje jako Claude Code skill, system prompt pro jakýkoli LLM, nebo jako základ pro MCP server / chatbot / Twitter bot.

## Co je Claude Code skill?

[Claude Code](https://claude.ai/claude-code) je CLI nástroj od Anthropicu — píšeš přímo v terminálu a Claude ti pomáhá s kódem, textem, čímkoli. **Skill** je balíček znalostí, který Claude Code načte automaticky když detekuje relevantní téma. Jakmile nainstalujete tento skill a zmíníte "Červený trpaslík", "Rimmer", "smeghead" apod., Claude automaticky načte knowledge base a začne odpovídat jako expert na Red Dwarf.

**Potřebujete:**
- [Claude Code](https://claude.ai/claude-code) (CLI, desktop app, nebo IDE extension)
- Účet u Anthropic (Pro/Max nebo API)

## Instalace

```bash
git clone https://github.com/trustbe/cerveny-trpaslik-skill.git
cd cerveny-trpaslik-skill
./install.sh
```

Nebo ručně:

```bash
mkdir -p ~/.claude/skills/cerveny-trpaslik
cp SKILL.md ~/.claude/skills/cerveny-trpaslik/
cp -r references ~/.claude/skills/cerveny-trpaslik/
```

Restartujte Claude Code a skill je aktivní.

## Jak to používat

Prostě pište v Claude Code česky a zmíňte cokoli z Red Dwarf. Skill naskočí automaticky. Příklady:

```
> Dej hlášku od Rimmera
> Napiš scénku kde Lister a Kocour...
> Kdo to řekl? "Toastuju, tedy jsem."
> Vymysli novou nadávku ve stylu Krytona
> Jak funguje holomůra?
> Odpověz jako Rimmer na otázku proč je nejlepší kapitán
```

Není žádný speciální příkaz ani syntax — prostě se ptáte a Claude odpovídá se znalostí 52 epizod, 350+ hlášek, všech postav a vibu českého fan klubu.

## Použití s jinými AI modely

Skill je optimalizovaný pro Claude Code, ale referenční soubory jsou **obyčejné markdown soubory** — můžete je použít s čímkoli:

**ChatGPT / GPT-4:** Nahrajte `SKILL.md` + relevantní soubory z `references/` jako Custom Instructions nebo do konverzace. Nejdůležitější: `characters.md`, `hlasky-databaze.md`, `humor-patterns.md`.

**Gemini / Google AI Studio:** System Instructions — vložte `SKILL.md` a připojte reference jako kontext.

**Cursor / Copilot / jiné IDE:** Zkopírujte `SKILL.md` do `.cursorrules` nebo ekvivalentu. Referenční soubory dejte do projektu aby je AI vidělo.

**Libovolný model s dlouhým kontextem:** Prostě pošlete `SKILL.md` + reference jako system prompt. Čím víc referenčních souborů přidáte, tím lepší výsledky.

**Tip:** Pokud model nemá dost velký kontext pro všechny reference, použijte alespoň:
1. `SKILL.md` (7 KB) — instrukce a pravidla
2. `characters.md` (27 KB) — postavy a hlasy
3. `hlasky-databaze.md` (25 KB) — 350+ citátů
4. `czech-voice.md` (13 KB) — český jazykový feeling

To je ~72 KB textu, což zvládne i model se 128K kontextem.

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
RIMMER: "Jiste, ze vim, co je laska. Mechanismus, jenz vynalezli
bankeri, aby nas donutili precerpat ucet."
  — ep. 05 Sebevědomí a Mindrák

RIMMER: "Vis kolikrat v zivote jsem se ja s nekym miloval?"
LISTER: "Ne, to nechci vedet."
RIMMER: "Jednou." LISTER: "Boha jeho!" RIMMER: "Jednou jedinkrat."
  — ep. 12 Paralelní vesmír (Rimmer opilý odhaluje své tajemství)

KOCHANSKA: "Nikdy jsem se na nej nedivala, jako by byl kozi syr
s kousky ananasu! Mozna jednou, dvakrat jako na kozi syr,
ale nikdy, *nikdy* s kousky ananasu!"
  — ep. 39 Uroboros (Kochanská popírá své city k Listerovi)

LISTER: "Ja jsem posledni muz na svete."
KOCHANSKA: "No, co se da delat?"
  — ep. 43 Epidem
```

### Stará hláška (podle postavy)

```
> Dej hlášku od Holly
```
```
HOLLY: "Prehnane horlivy, zrejme blazen. Pravdepodobne ma vic zubu
nez mozkovych bunek. Vyhlidky na povyseni: komicke."
  — ep. 04 Čekání na Boha (kapitánův tajný záznam o Rimmerovi)

HOLLY: "Ja jsem desata generace holografickych pocitacu s umelou
inteligenci. Ne tvoje mama."
  — ep. 02 Ozvěny budoucnosti (Holly odpovídá podrážděnému Rimmerovi)

HOLLY: "Jean Paul Sartre tvrdil, ze peklo je byt navzdy zamcenej
v mistnosti s prateli." LISTER: "Holly, vsichni jeho kamaradi
byly Frantici."
  — ep. 03 Rovnováha sil
```

### Random hláška

```
> Dej hlášku
```
```
RIMMER: "Zhorsil se mi zrak. Tos namaloval ty? To je brak!"
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
RIMMER: "Miloval jsem jednu zenu. Dvanact minut. A to pocitam
i tu pizzu. Kdybych nepocital pizzu, tak jsem miloval tri minuty.
A dve z toho jsem hledal vypinac."

RIMMER: "Laska je jako dustojnicke zkousky. Cim vic se snazis,
tim vic ti to pripomene, zes na to absolutne nemyslitelne
nedostatecne kvalifikovanej. A nakonec napises 'ja jsem ryba'
a slozis se."

RIMMER: "Vis co je na hologramech tragicke? Nemuzes se nikoho
dotknout. Vis co je jeste tragictejsi? Kdyz jsem byl zivy,
taky se me nikdo nechtel dotknout."
```

### Nové hlášky od všech postav na téma

```
> Nové hlášky o jídle
```
```
LISTER: "Nerikam, ze Rimmerovo vareni je spatny. Rikam, ze naposled,
co varil, tak robici odmitli umejt hrnec a jeden z nich podal
vypoved."

KOCOUR: "Ja nejim nic, co nevypada tak dobre jako ja. Coz eliminuje
prakticky vsechno krome susi. A i to susi musi byt cerstveny."

KRYTON: "Pane Listere, vas vindaloo dosahuje na Scovilleho stupnici
hodnot, ktere obvykle meri jadernou fyzika."

HOLLY: "Dneska je na menu kureci vindaloo, hovezi vindaloo a veganska
varianta — vindaloo bez kurete a hoveziny. Coz je vlastne omacka."
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
