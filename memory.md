# Memory

Notizen zum Projekt und zur Zusammenarbeit mit Claude. Diese Datei ist die Quelle der Wahrheit — bitte hier ergänzen statt im versteckten `~/.claude`-System.

## Projekt

### Website-Tech-Stack
- **Gewählt am 2026-05-24:** statisches HTML/JS auf **GitHub Pages**.
- **Warum:** einfach, kostenlos, passt zum `github.io`-Ziel aus [overview.md](overview.md).
- **Verworfene Alternativen** (für spätere Re-Evaluation):
  - **Quarto / Jupyter Book** — kostenlos, hostbar auf GitHub Pages. Sinnvoll, wenn Analysen aus Python-Notebooks direkt zu Reports rendern sollen.
  - **Streamlit / Dash** — interaktive Python-App. Lokal kostenlos, Hosting via Streamlit Community Cloud (Free Tier mit Limits) oder eigener Server. Sinnvoll bei echter Interaktivität (Filter, Live-Queries).
  - **React/Next.js SPA** — kostenlos auf Vercel/GitHub Pages. Mehr Flexibilität, mehr Aufwand. Erst wenn statisches HTML an Grenzen stößt.

### Repo-Struktur (Vorschlag, noch nicht umgesetzt)
```
dgs-suus-member-analysis/
├── docs/              ← Website (GitHub Pages source = /docs)
├── data/              ← CSVs, Rohdaten
├── notebooks/         ← Jupyter
├── scripts/           ← Python-Scraping
├── README.md
├── overview.md
└── memory.md
```

## Zusammenarbeit mit Claude

### Kommunikation
- Sprache: **Deutsch**.

### Präferenzen
- Bevorzugt **einfache, kostenlose Lösungen**. Kosten bei Tooling-Vorschlägen immer transparent machen.
- Will zuerst **erklärt bekommen, wie etwas funktioniert**, statt fertige Implementierungen zu erhalten. → Erst Anleitung/Optionen, Code nur auf explizite Aufforderung.

### Memory-Pflege
- Memory wird in **dieser Datei** (`memory.md` im Projekt-Root) gepflegt — nicht im versteckten `~/.claude/projects/...`-System.
- Bei neuen Erkenntnissen: hier ergänzen, nicht ersetzen.
