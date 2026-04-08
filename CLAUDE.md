# Švitorka AI

## O projektu

Red Dwarf AI knowledge base. Databáze hlášek, postav, scénářů a lore z Červeného trpaslíka.
Funguje jako Claude Code skill, system prompt pro jakýkoli LLM, nebo základ pro MCP server / chatbot / web.

## Zdroje dat

- **cervenytrpaslik.cz** — série I-VIII (52 epizod), NSFAQ, vzkazy, nadávky
- **cervenytrpaslik.eu** — série IX-XII + The Promised Land (21 epizod), hnidopich IX-XII

## Struktura

- `SKILL.md` — hlavní instrukce pro AI (módy, pravidla stylu, mapa referencí)
- `references/` — 14 markdown souborů s daty (postavy, hlášky, humor, lore, nadávky...)
- `raw/` — surová data z .cz (scénáře CZ+EN, epizody, NSFAQ, vzkazy)
- `raw/*_eu/` — surová data z .eu (série IX-XII, hnidopich, sekce)
- `web/` — statická stránka + 5 designových variant
- `tests/` — ukázkové výstupy (scénka, NSFAQ, in-character)

## Klíčové soubory

| Soubor | Co obsahuje |
|--------|------------|
| `references/hlasky-databaze.md` | 504 hlášek s diakritikou ze série I-XII |
| `references/characters.md` | Profily postav, hlasy, catchphrases |
| `references/humor-patterns.md` | Vzorce humoru, typy gagů |
| `references/nadavky-katalog.md` | Kompletní katalog nadávek po sériích |
| `web/hlasky.json` | 504 hlášek jako JSON pro web |
| `web/nadavky.json` | 374 nadávek jako JSON pro web |

## Konvence

- Hlášky citovat PŘESNĚ jak jsou v databázi, s diakritikou
- "nová/vymysli" = AI generuje, "dej/hláška od" = hledej v databázi
- "to vindaloo" (střední rod), ne "ten vindaloo"
- Výchozí je JEDNA hláška, víc jen na explicitní žádost
- Nové hlášky psát přirozenou hovorovou češtinou, ne překlad z angličtiny

## Branding

- Název: **Švitorka AI**
- Systém umělé inteligence: K177
- Tagline: *"Chrlím hlášky, tedy jsem."*
- Perex: *Celý Červený trpaslík v jednom AI. Dali byste si hlášku?*
- Výrobce: Křápol a.s. — Taiwan | Typ přístroje: Mluvící toastovač

## Web

- `web/index.html` — kompletní scrollovací stránka (hero + hlášky + nadávky + o projektu)
- `web/variants/` — 5 designových variant hero stránky:
  - v1-ship: vesmír + silueta Red Dwarf
  - v2-toaster: světlý papírový + SVG toastovač s obličejem
  - v3-terminal: Holly CRT terminál, zelená na černé
  - v4-starbug: deep space + SVG Kosmík/Starbug
  - v5-hologram: fialová + H badge s glow, character selector
- `web/hlasky.json` + `web/nadavky.json` — JSON databáze pro JS
- Fonty: Michroma (Microgramma alternativa), VT323 (terminál), Playfair Display (hlášky)

## Čísla

- 73 českých scénářů (série I-XII)
- 51 anglických scénářů (série I-VIII)
- 504 hlášek s diakritikou
- 374 nadávek
- 1354 NSFAQ entries
- 14 864 vzkazů
- The Promised Land (speciál)

## Plány

- Pregenerovat batch 500-1000 nových AI hlášek (jednorázově, ne on-demand)
- Web: GitHub Pages, random hláška při každém loadu
- Twitter: cron job, 1 hláška denně (mix starých a nových)
- MCP server: tools `hlaska()`, `nadavka()`, `kviz()`, `lore()`
- Vybrat finální design webu z 5 variant
