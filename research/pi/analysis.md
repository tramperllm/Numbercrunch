# Pi (π) - Wissenschaftliche Analyse

## Definition

Pi (π) ist die mathematische Konstante, die das Verhältnis des Umfangs eines Kreises zu seinem Durchmesser definiert:

```
π = Umfang / Durchmesser
```

## Mathematische Eigenschaften

### Transzendenz und Irrationalität

- **Irrational**: π ist eine irrationale Zahl (1761-1768 von Johann Heinrich Lambert bewiesen)
  - Quelle: https://de.wikipedia.org/wiki/Kreiszahl, Abruf: 2026-04-10
  - Kann nicht als Verhältnis zweier ganzer Zahlen p/q dargestellt werden

- **Transzendent**: π ist transzendent (1882 von Ferdinand von Lindemann bewiesen)
  - Quelle: https://de.wikipedia.org/wiki/Kreiszahl, Abruf: 2026-04-10
  - Es gibt kein vom Nullpolynom verschiedenes Polynom mit rationalen Koeffizienten, das π zur Nullstelle hat
  - Konsequenz: Die Quadratur des Kreises mit Zirkel und Lineal ist unmöglich

### Normalität

- Die ersten 100 Nachkommastellen zeigen keine erkennbare Regelmäßigkeit
- Genügt statistischen Tests auf Zufälligkeit
- Quelle: OEIS A000796, https://oeis.org/A000796

## Aktueller Forschungsstand (2025-2026)

### Weltrekord: 314 Billionen Stellen

| Datum | Rekordhalter | Stellenanzahl |
|-------|-------------|---------------|
| Dez 2025 | StorageReview | **314 Billionen (314,000,000,000,000)** |
| Mai 2025 | Linus Media Group & KIOXIA | 300 Billionen |
| Aug 2021 | Fachhochschule Graubünden | 62,8 Billionen |
| Mär 2019 | Emma Haruka Iwao (Google) | 31,4 Billionen |

**Quellen:**
- Google Cloud Blog, Abruf: 2026-04-10 (Suchergebnisse)
- Guinness World Records (in Anspruch genommen)

### Berechnungsmethoden

- **Y-cruncher**: Software für Multi-Threaded Berechnungen
- **BBP-Formel**: Bailey-Borwein-Plouffe-Formel für hexadezimale Berechnung
- **Bellard's Formel**: Schnelle Berechnungsmethode

## Dezimaldarstellung von Pi

### Die ersten 100 Nachkommastellen (5er-Gruppierung)

```
π = 3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510
      58209 74944 59230 78164 06286 20899 86280 34825 34211 70679
      82148 08651 32823 06647 09384 46095 50582 23172 53594 08128
```

**Quelle:** OEIS A000796, https://oeis.org/A000796, Abruf: 2026-04-10

### Alternative 4er-Gruppierung

```
π = 3.1415 9265 3589 7932 3846 2643 3832 7950 2884 1971
      6939 9375 1058 2097 4944 5923 0781 6406 2862 0899
      8628 0348 2534 2117 0679 8214 8086 5132 8230 6647
```

## OEIS-Referenzen zu Pi

### Primäre Sequenzen

| OEIS-ID | Name | URL |
|---------|------|-----|
| **A000796** | Decimal expansion of Pi | https://oeis.org/A000796 |
| **A004601** | Expansion of Pi in base 2 (binary) | https://oeis.org/A004601 |

### Pi in verschiedenen Basen

| Basis | OEIS-ID | URL |
|-------|---------|-----|
| b=2 | A004601 | https://oeis.org/A004601 |
| b=3 | A004602 | https://oeis.org/A004602 |
| b=4 | A004603 | https://oeis.org/A004603 |
| b=5 | A004604 | https://oeis.org/A004604 |
| b=6 | A004605 | https://oeis.org/A004605 |
| b=7 | A004606 | https://oeis.org/A004606 |
| b=8 | A006941 | https://oeis.org/A006941 |
| b=9 | A004608 | https://oeis.org/A004608 |
| b=10 | A000796 | https://oeis.org/A000796 |
| b=16 | A062964 | https://oeis.org/A062964 |

### Weitere Pi-bezogene Sequenzen (Auswahl)

| OEIS-ID | Beschreibung |
|---------|-------------|
| A002388 | Pi² |
| A003881 | Pi/4 |
| A013661 | Pi²/6 |
| A019692 | 2*Pi (tau) |
| A019727 | sqrt(2*Pi) |
| A059956 | 6/Pi² |
| A060294 | 2/Pi |
| A001901 | Pi/2 (Wallis) |
| A007514 | Pi (verschiedene Formeln) |

### A000796 - Detaillierte OEIS-Informationen

```json
{
  "sequence_id": "A000796",
  "name": "Decimal expansion of Pi (or digits of Pi)",
  "url": "https://oeis.org/A000796",
  "former_id": "M2218 N0880",
  "offset": "1,1",
  "author": "N. J. A. Sloane",
  "keywords": ["cons", "nonn", "nice", "core", "easy"],
  "status": "approved",
  "terms_first_100": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9, 8, 2, 1, 4],
  "cross_references": ["A004601", "A004602", "A004603", "A004604", "A004605", "A004606", "A006941", "A004608", "A068436", "A068437", "A068438", "A068439", "A068440", "A062964", "A224750", "A224751", "A060707"]
}
```

### A004601 - Binäre Expansion

```json
{
  "sequence_id": "A004601",
  "name": "Expansion of Pi in base 2 (or, binary expansion of Pi)",
  "url": "https://oeis.org/A004601",
  "offset": "2,1",
  "author": "N. J. A. Sloane",
  "example": "11.0010010000111111011010101000100010000...",
  "terms_first_100": [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
}
```

## Historische Berechnungsmeilensteine

| Jahr | Mathematiker | Stellen | Methode |
|------|-------------|---------|---------|
| ~250 v.Chr. | Archimedes | 3 | Polygon-Methode |
| ~150 n.Chr. | Ptolemäus | 3 | |
| 1424 | Dschamschid al-Kaschi | 16 | |
| 1596 | Ludolph van Ceulen | 35 | |
| 1706 | John Machin | 100 | Machin-Formel |
| 1873 | William Shanks | 707 (527 korrekt) | |
| 1949 | ENIAC | 2.037 | Elektronisch |
| 1973 | Guilloud & Bouyer | 1.000.000 | CDC 7600 |
| 1989 | Chudnovsky-Brüder | 1.000.000.000 | Chudnovsky-Algorithmus |
| 2009 | Daisuke Takahashi | 2.576.980.377.524 | |
| 2019 | Emma Haruka Iwao | 31.415.926.535.897 | Google Cloud |
| 2021 | FH Graubünden | 62.831.853.071.796 | Y-cruncher |
| 2025 | StorageReview | 314.000.000.000.000 | Y-cruncher |

## Referenzen

1. OEIS Foundation, "A000796 - Decimal expansion of Pi", https://oeis.org/A000796
2. OEIS Foundation, "A004601 - Expansion of Pi in base 2", https://oeis.org/A004601
3. Wikipedia, "Kreiszahl", https://de.wikipedia.org/wiki/Kreiszahl
4. Arndt, J. & Haenel, C., "Pi Unleashed", Springer NY 2001
5. Beckmann, P., "A History of Pi", Golem Press, 1977

---

*Dokument erstellt: 2026-04-10*  
*Letzte Aktualisierung: 2026-04-10*
