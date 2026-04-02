# Červený Trpaslík — Claude Code Skill

Claude Code skill pro pokračování odkazu českého Red Dwarf fan klubu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/).

Kompletní knowledge base + kreativní engine pro psaní nových epizod, dialogů, fan fiction a webového obsahu ve stylu českého fan klubu.

## Co to umí

- **Nové epizody** — kompletní scénáře ve formátu seriálu (cold open + 3 akty)
- **Scénky a dialogy** — v hlasech českého dabingu
- **In-character odpovědi** — jako Lister, Rimmer, Kocour, Kryton, Holly...
- **Webový obsah** — postřehy, hnidopichy, NSFAQ, kuchařka, kvízy ve stylu cervenytrpaslik.cz
- **Fan fiction** — příběhy v próze
- **Rozbory epizod** — hloubková analýza
- **Lore odpovědi** — encyklopedie univerza
- **Free talk** — konverzace jako RD expert

## Obsah

### SKILL.md
Hlavní soubor skillu s instrukcemi, mapou referencí, 8 módy a pravidly stylu.

### references/ (13 souborů, 232 KB)
| Soubor | Obsah |
|--------|-------|
| `characters.md` | Kompletní profily postav, catchphrases, jak mluví |
| `humor-patterns.md` | DNA humoru — typy gagů, running gagy |
| `story-structure.md` | Jak se píše epizoda |
| `world-bible.md` | Lodě, tech, rasy, direktivy, lore |
| `czech-voice.md` | Český dabing, nadávky, CZ vs EN |
| `episode-guide.md` | Průvodce 52 epizodami |
| `fanclub-voice.md` | Hlas autorů webu cervenytrpaslik.cz |
| `community-content.md` | DNA komunitních formátů |
| `content-formats.md` | Šablony pro nový obsah |
| `site-dna.md` | Meta-analýza webu |
| `nsfaq-best-of.md` | Top NSFAQ entries |
| `nadavky-katalog.md` | Kompletní katalog nadávek |
| `trivia-vite-ze.md` | "Víte, že...?" trivia |

### raw/ (1200+ souborů)
Surová data stažená z cervenytrpaslik.cz:
- **52 českých scénářů** (série I-VIII)
- **51 anglických scénářů**
- **32 sekcí webu**
- **155 detailů epizod**
- **39 profilů postav**
- **1354 NSFAQ entries**
- **14 864 vzkazů** (744 stránek)

### tests/
Ukázkové výstupy — scénka, webový obsah, in-character monolog.

## Instalace do Claude Code

```bash
# Klonuj repo
git clone https://github.com/trustbe/cerveny-trpaslik-skill.git

# Zkopíruj SKILL.md a references do Claude Code skills
mkdir -p ~/.claude/skills/cerveny-trpaslik
cp cerveny-trpaslik-skill/SKILL.md ~/.claude/skills/cerveny-trpaslik/
cp -r cerveny-trpaslik-skill/references ~/.claude/skills/cerveny-trpaslik/
```

Skill se automaticky aktivuje když zmíníš Červený trpaslík, Red Dwarf, smeghead, Lister, Rimmer, Cat, Kryten, Holly, Starbug, Kosmík, nebo chceš psát nové epizody/obsah v Red Dwarf univerzu.

## Scraper

`scraper.py` a `scrape_vzkazy.py` — Python scrapers pro stahování dat z cervenytrpaslik.cz. Vyžadují `requests` a `beautifulsoup4`.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4
python3 scraper.py
python3 scrape_vzkazy.py
```

## Poděkování

Celý skill je postaven na obsahu webu [cervenytrpaslik.cz](http://www.cervenytrpaslik.cz/) — legendárního českého Red Dwarf fan klubu, který běží od začátku 2000s. Díky autorům za roky práce na budování české Red Dwarf komunity.

---

*Smoke me a kipper, I'll be back for breakfast!*
