# Belphegor's Primzahl - Wissenschaftliche Analyse

## Definition

Belphegor's Primzahl ist eine palindromische Primzahl der Form:

```
B₁₃ = 10³⁰ + 666 × 10¹⁴ + 1
    = 1000000000000066600000000000001
```

**Eigenschaften:**
- 31 Stellen insgesamt
- 13 Nullen auf jeder Seite der 666
- Palindrom (von vorne und hinten gleich)
- Die Zahl 666 in der Mitte (die "Zahl des Tieres")

Quellen:
- Wikipedia (DE): https://de.wikipedia.org/wiki/Belphegors_Primzahl, Abruf: 2026-04-10
- Wikipedia (EN): https://en.wikipedia.org/wiki/Belphegor%27s_prime, Abruf: 2026-04-10

## Historie

### Entdeckung
- **Entdecker**: Harvey Dubner (bekannt für Entdeckung großer Primzahlen)
- **Benennung**: Clifford A. Pickover (2012)
- **Name**: Nach Belphegor, einem der sieben Fürsten der Hölle
  - Belphegor = "Dämon der genialen Erfindungen"

Quelle: Wikipedia "Belphegor's prime", https://en.wikipedia.org/wiki/Belphegor%27s_prime, Abruf: 2026-04-10

## Mathematische Struktur

### Belphegor-Zahlen (Allgemeine Form)

```
Bₙ = 10^(2n+3) + 666 × 10^(n+1) + 1
   = 1 (n+1 Nullen) 666 (n+1 Nullen) 1
```

Beispiele:
- B₀ = 16661
- B₁ = 1066601
- B₂ = 100666001
- B₃ = 10006660001
- B₁₃ = 1000000000000066600000000000001

### Belphegor-Primzahlen

Nicht alle Belphegor-Zahlen sind prim. Die Indizes n, für die Bₙ prim ist:

```
n = 0, 13, 42, 506, 608, 2472, 2623, 28291, 181298, ...
```

**Bekannte Belphegor-Primzahlen:**
1. **B₀ = 16661** (5 Stellen)
2. **B₁₃ = 1000000000000066600000000000001** (31 Stellen)
3. **B₄₂** (87 Stellen)
4. **B₅₀₆** (1015 Stellen)
5. **B₆₀₈** (1219 Stellen)

## OEIS-Referenzen

### Primäre Sequenzen

| OEIS-ID | Name | URL |
|---------|------|-----|
| **A232449** | Belphegor numbers | https://oeis.org/A232449 |
| **A232448** | Indices of Belphegor primes | https://oeis.org/A232448 |
| **A232450** | Largest prime factor of Belphegor numbers | https://oeis.org/A232450 |

### A232449 - Belphegor-Zahlen

```json
{
  "sequence_id": "A232449",
  "name": "Belphegor numbers: (10^(n+3) + 666)*10^(n+1) + 1",
  "url": "https://oeis.org/A232449",
  "formula": "a(n) = (10^(n+3) + 666)*10^(n+1) + 1 = 10^(2n+4) + 666*10^(n+1) + 1",
  "terms": [16661, 1066601, 100666001, 10006660001, ...],
  "author": "N. J. A. Sloane",
  "cross_references": ["A232448", "A232450", "A232451"]
}
```

### A232448 - Indizes der Belphegor-Primzahlen

```json
{
  "sequence_id": "A232448",
  "name": "Indices of Belphegor primes: numbers k such that A232449(k) is prime",
  "url": "https://oeis.org/A232448",
  "terms": [0, 13, 42, 506, 608, 2472, 2623, 28291, 181298, ...],
  "comments": [
    "B_0 = 16661 is the smallest Belphegor prime",
    "B_13 = 1000000000000066600000000000001 is the second Belphegor prime (Belphegor's prime)"
  ],
  "author": "N. J. A. Sloane",
  "cross_references": ["A232449", "A232450"]
}
```

## Das Symbol - Das umgedrehte Pi (⊥)

### Bedeutung

Das Symbol für Belphegor's Primzahl ist ein **umgedrehtes Pi-Symbol (⊥)**.

### Interpretationen

1. **Geometrische Deutung**: Das ⊥ Symbol repräsentiert:
   - Senkrechte/Orthogonalität in der Geometrie
   - Ein "umgekehrter" oder "verkehrter" Kreis/Zyklus
   - Das Gegenteil von Kreiszahl π (das den perfekten Kreis repräsentiert)

2. **Symbolische Deutung**:
   - π repräsentiert Perfektion, Unendlichkeit, Natürlichkeit
   - ⊥ repräsentiert das Dämonische, das Unnatürliche, die Verkehrung
   - Die 666 in der Mitte verstärkt diese symbolische Bedeutung

3. **Numerische Deutung**:
   - 13 (die Anzahl der Nullen) ist in der westlichen Kultur eine Unglückszahl (Triskaidekaphobie)
   - 31 (Gesamtstellenzahl) ist 13 rückwärts geschrieben
   - 666: Die "Zahl des Tieres" aus der Offenbarung des Johannes

## Zahlentheoretische Eigenschaften

### Palindrom-Eigenschaften

- Belphegor's Primzahl ist ein **Primzahlpalindrom**
- Liest sich vorwärts und rückwärts gleich
- Beispiel: 1000000000000066600000000000001

### Teilbarkeit

- Für n ≡ 3 oder 5 (mod 6): Bₙ ist immer durch 13 teilbar
- Asymptotisch sind 1/3 aller Belphegor-Zahlen durch 13 teilbar

### Namen in verschiedenen Skalen

**Short Scale (US):**
"one nonillion, sixty-six quadrillion, six hundred trillion one"

**Long Scale (Europa):**
"one quintillion, sixty-six billiard, six hundred billion one"

## Mathematische Beziehungen

### Verbindung zu π

Die symbolische Verbindung zwischen π und Belphegor's Primzahl:

| Eigenschaft | π | Belphegor's Primzahl |
|-------------|---|---------------------|
| Symbol | π (Kreis) | ⊥ (umgedrehtes Pi) |
| Bedeutung | Perfektion, Natürlichkeit | Verkehrung, Dämonisches |
| Zahlenwert | 3.14159... | 10³⁰ + 666×10¹⁴ + 1 |
| Geometrie | Kreis | Palindromische Struktur |
| OEIS | A000796 | A232449 |

### Gemeinsamkeiten mit anderen Zahlen

- **Mit π**: Beide haben symbolische Bedeutung über die Mathematik hinaus
- **Mit φ**: Beide erscheinen in speziellen geometrischen Konstruktionen
- **Mit Primzahlen allgemein**: Belphegor's Primzahl ist ein Beispiel für rekreative Mathematik

## Forschungsrelevanz

### In der Populärkultur

- Clifford Pickover hat diese Zahl in seinen mathematischen Schriften popularisiert
- Verbindung zu okkulten Zahlen (666, 13)
- Beispiel für "mathematische Kuriositäten"

### In der Zahlentheorie

- Studium von Primzahlpalindromen
- Untersuchung der Primzahlverteilung in speziellen Folgen
- Test für Primzahltests (besonders für große Palindrome)

## Referenzen

1. OEIS Foundation, "A232449 - Belphegor numbers", https://oeis.org/A232449
2. OEIS Foundation, "A232448 - Indices of Belphegor primes", https://oeis.org/A232448
3. OEIS Foundation, "A232450 - Largest prime factor of Belphegor numbers", https://oeis.org/A232450
4. Wikipedia, "Belphegor's prime", https://en.wikipedia.org/wiki/Belphegor%27s_prime
5. Wikipedia (DE), "Belphegors Primzahl", https://de.wikipedia.org/wiki/Belphegors_Primzahl
6. Pickover, Clifford A., "Die mathematische Seite des Universums", Wiley-VCH
7. Dubner, Harvey, "Palindromic primes", Journal of Recreational Mathematics

---

*Dokument erstellt: 2026-04-10*  
*Letzte Aktualisierung: 2026-04-10*
