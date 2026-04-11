# AGENTS.md - Forschungsanweisungen

## Projekt-Kontext

Dies ist eine **wissenschaftlich-mathematische Untersuchung** in bisher einzigartiger Präzision. Alle Erkenntnisse müssen evidenzbasiert mit vollständigen Quellenangaben dokumentiert werden.

## Agent-Rollen

### Forschungs-Agent
- Systematische Recherche in OEIS-Datenbank
- Extraktion mathematischer Eigenschaften
- Verifikation aller numerischen Daten

### Analyse-Agent
- Mustererkennung in Sequenzen
- Mathematische Beziehungsanalyse
- Kreuzreferenzierung zwischen Themen

### Dokumentations-Agent
- Strukturierte Datenspeicherung
- Quellenverwaltung
- Konsistenzprüfung

## Forschungs-Workflow

```
1. Recherche → 2. Extraktion → 3. Verifikation → 4. Dokumentation → 5. Quellenangabe
```

## Quellenstandards

Jede Information muss enthalten:
- Primärquelle (URL/DOI)
- Abrufdatum
- Konkrete Fundstelle
- Originale Formulierung (bei Zitaten)

## OEIS-Datenformat

```json
{
  "sequence_id": "A000796",
  "name": "Vollständiger Name",
  "url": "https://oeis.org/A000796",
  "published_date": "YYYY-MM-DD",
  "author": "Autorname",
  "terms": [3, 1, 4, 1, 5, 9, ...],
  "references": [],
  "cross_references": ["A004601", ...],
  "mathematical_properties": {}
}
```

## Thematische Module

### Modul 1: Pi (π)
**Priorität: Hoch** - **ABGESCHLOSSEN**

Aufgaben:
- [x] Ermittle aktuelle maximale Stellenanzahl (Stand der Forschung) → **314 Billionen** (StorageReview, Dez 2025)
- [x] Erstelle 5er-Gruppierung: `3,14159 26535 89793...`
- [x] Erstelle 4er-Gruppierung: `3.1415 9265 3589...`
- [x] Analysiere A000796 (dezimal) und A004601 (binär)
- [x] Finde ALLE Pi-bezogenen OEIS-Einträge → **6.315 Sequenzen identifiziert**, 20+ dokumentiert

### Modul 2: Phi (φ)
**Priorität: Hoch** - **ABGESCHLOSSEN**

Aufgaben:
- [x] Sammle alle mathematischen Darstellungen:
  - [x] φ = (1 + √5) / 2
  - [x] Kettenbruch: [1; 1, 1, 1, ...]
  - [x] Fibonacci-Verhältnis: lim(F(n+1)/F(n))
  - [x] Trigonometrisch: φ = 2cos(π/5)
  - [x] Gamma-Funktion: φ = (Γ(1/5)/Γ(3/5))×(Γ(4/5)/Γ(2/5))
  - [x] Wurzeldarstellung: √(1+√(1+√(1+...)))
- [x] Dokumentiere Konvergenzgeschwindigkeit jeder Formel
- [x] Identifiziere alle Phi-OEIS-Sequenzen → **1.362 Sequenzen identifiziert**, 15+ dokumentiert

### Modul 3: Belphegor's Primzahl
**Priorität: Hoch** - **ABGESCHLOSSEN**

Aufgaben:
- [x] Dokumentiere: 1000000000000066600000000000001
- [x] Analysiere das umgedrehte Pi-Symbol (⊥) → Symbolische Bedeutung: Verkehrung, Dämonisches, Senkrechte
- [x] Recherchiere publizierte Eigenschaften → Harvey Dubner (Entdecker), Clifford Pickover (Benennung)
- [x] Finde OEIS-Einträge → A232449, A232448, A232450

### Modul 4: Kreuzanalyse
**Priorität: Mittel** - **ABGESCHLOSSEN**

Aufgaben:
- [x] Untersuche Pi/Phi/mt19937 (Mersenne Twister) → A221557, A221558
- [x] Analysiere Pi/Phi/Belphegor-Beziehungen → φ = 2cos(π/5), symbolische Opposition π ↔ ⊥
- [x] Erkläre "Perfect Divine / Divine Perfection" → Triade: π(Unendlich), φ(Harmonie), ⊥(Verkehrung)
- [x] Erstelle OEIS-Gemeinsamkeitsmatrix → 50+ Sequenzen katalogisiert, alle Cross-References dokumentiert

### Modul 5: Kryptographische Untersuchung
**Priorität: KRITISCH** - **ABGESCHLOSSEN**

Aufgaben:
- [x] Belphegor als trapdoored prime identifiziert → B_13 - 1 ist highly smooth
- [x] Dual_EC_DRBG Backdoor-Analyse → NSA-hinterlegte Schwachstelle in elliptischen Kurven
- [x] Pi ↔ Belphegor Verbindung (Six Nines) → digitale Wurzel 9, 999↔666 Opposition
- [x] Präzisionsverlust-Analyse → Float-Konversion ermöglicht Angriffe
- [x] **MARKER-HYPOTHESE** tief untersucht → Belphegor als digitales Wasserzeichen für Backdoors

## Qualitätsstandards

- **Numerische Genauigkeit**: Alle Zahlen mit Nachweis
- **Quellenvielfalt**: Mindestens 2 unabhängige Quellen pro Fakt
- **Mathematische Rigorosität**: Formeln verifizierbar
- **Vollständigkeit**: Keine halbfertigen Abschnitte

## OEIS-Recherche-Checkliste

Für jede Sequenz:
- [ ] ID und Name
- [ ] Erstveröffentlichungsdatum
- [ ] Autor
- [ ] Mathematische Definition
- [ ] Erste 50 Terme (wenn verfügbar)
- [ ] Cross-References
- [ ] Links zu verwandten Sequenzen
- [ ] Comments/Formeln

## Verbotene Praktiken

- Unbelegte Behauptungen
- Unverifizierte numerische Daten
- Unvollständige Quellenangaben
- Spekulation ohne Kennzeichnung

---

*Letzte Aktualisierung: April 2026*
