# K177 — Švitorka AI

## O projektu

Red Dwarf AI knowledge base. Databáze hlášek, postav, scénářů a lore z Červeného trpaslíka.
Funguje jako Claude Code skill, system prompt pro jakýkoli LLM, nebo základ pro MCP server / chatbot / web.

## Struktura

- `SKILL.md` — hlavní instrukce pro AI (módy, pravidla stylu, mapa referencí)
- `references/` — 14 markdown souborů s daty (postavy, hlášky, humor, lore, nadávky...)
- `raw/` — surová data z cervenytrpaslik.cz (scénáře CZ+EN, epizody, NSFAQ, vzkazy)
- `tests/` — ukázkové výstupy (scénka, NSFAQ, in-character)

## Klíčové soubory

| Soubor | Co obsahuje |
|--------|------------|
| `references/hlasky-databaze.md` | 370+ hlášek s diakritikou ze všech 52 epizod |
| `references/characters.md` | Profily postav, hlasy, catchphrases |
| `references/humor-patterns.md` | Vzorce humoru, typy gagů |
| `references/nadavky-katalog.md` | Kompletní katalog nadávek po sériích |

## Konvence

- Hlášky citovat PŘESNĚ jak jsou v databázi, s diakritikou
- "nová/vymysli" = AI generuje, "dej/hláška od" = hledej v databázi
- "to vindaloo" (střední rod), ne "ten vindaloo"
- Výchozí je JEDNA hláška, víc jen na explicitní žádost
- Nové hlášky psát přirozenou hovorovou češtinou, ne překlad z angličtiny

## Branding

- Název: **K177 — Švitorka AI**
- Tagline: *"Chrlím hlášky, tedy jsem."*
- Perex: *Celý Červený trpaslík v jednom AI. Dali byste si hlášku?*
- Výrobce: Křápol a.s. — Taiwan | Typ přístroje: Mluvící toastovač

## Plány

- Naparsovat hlášky do JSON pro statický web a Twitter bot
- Pregenerovat batch 500-1000 nových AI hlášek (jednorázově, ne on-demand)
- Web: GitHub Pages, random hláška při každém loadu, žádný server
- Twitter: cron job, 1 hláška denně (mix starých a nových)
- MCP server: tools `hlaska()`, `nadavka()`, `kviz()`, `lore()`
