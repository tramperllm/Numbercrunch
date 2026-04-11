# Phi (φ) - Der Goldene Schnitt - Wissenschaftliche Analyse

## Definition

Der Goldene Schnitt (Phi, φ, τ) ist die positive Lösung der quadratischen Gleichung:

```
x² - x - 1 = 0
```

### Algebraische Formel

```
φ = (1 + √5) / 2
```

### Numerischer Wert

```
φ = 1.61803398874989484820458683436563811772030917980576286213544862270526046281890...
```

## Mathematische Eigenschaften

### Minimalpolynom

- **Polynom**: x² - x - 1 = 0
- **Wurzeln**: φ und -φ⁻¹
- **Algebraische Eigenschaft**: φ ist algebraisch (im Gegensatz zu π, das transzendent ist)
- **Körper**: Fundamentale Einheit des quadratischen Körpers Q(√5)

Quelle: Wikipedia "Golden ratio", https://en.wikipedia.org/wiki/Golden_ratio, Abruf: 2026-04-10

### Irrationalität

Zwei Beweise der Irrationalität:

1. **Beweis durch unendlichen Abstieg**: Wenn φ = n/m in gekürzter Form, dann ist m/(n-m) in noch stärker gekürzter Form - Widerspruch.

2. **Über Irrationalität von √5**: Wenn φ rational wäre, dann wäre 2φ - 1 = √5 rational - Widerspruch, da √5 irrational ist.

Quelle: Wikipedia "Golden ratio", https://en.wikipedia.org/wiki/Golden_ratio, Abruf: 2026-04-10

## Mathematische Darstellungen

### 1. Algebraische Form
```
φ = (1 + √5) / 2
```

### 2. Kettenbruchentwicklung
```
φ = [1; 1, 1, 1, 1, ...] = 1 + 1/(1 + 1/(1 + 1/(1 + ...)))
```

**Eigenschaft**: Dies ist der "langsamst konvergierende" Kettenbruch, da alle Koeffizienten gleich 1 sind.

### 3. Fibonacci-Verhältnis (Grenzwert)
```
φ = lim(n→∞) F(n+1) / F(n)
```

wobei F(n) die n-te Fibonacci-Zahl ist.

Konvergenz:
- F(2)/F(1) = 1/1 = 1.0
- F(3)/F(2) = 2/1 = 2.0
- F(4)/F(3) = 3/2 = 1.5
- F(5)/F(4) = 5/3 ≈ 1.666...
- F(6)/F(5) = 8/5 = 1.6
- F(10)/F(9) = 55/34 ≈ 1.6176
- F(20)/F(19) = 6765/4181 ≈ 1.61803

### 4. Wurzeldarstellung
```
φ = √(1 + √(1 + √(1 + √(1 + ...))))
```

Quelle: OEIS A001622 Comments, https://oeis.org/A001622, Abruf: 2026-04-10

### 5. Trigonometrische Darstellung
```
φ = 2 * cos(π/5) = 2 * sin(3π/10)
```

### 6. Gamma-Funktion Darstellung
```
φ = (Γ(1/5)/Γ(3/5)) * (Γ(4/5)/Γ(2/5))
```

Quelle: Bruno Berselli, OEIS A001622 Comment, 2012

### 7. Hyperbolische Funktionen
```
φ = e^(asinh(1/2))
```

### 8. Formel mit Kreiszahl π
```
φ = 5^(1/4) * (cot(π/5))^(1/2) * e^(iπ/2)
```

## Konvergenzgeschwindigkeit der Darstellungen

| Darstellung | Konvergenztyp | Geschwindigkeit |
|-------------|--------------|-----------------|
| Algebraisch | Direkt | Sofort |
| Kettenbruch | Linear | Langsam (O(1/n)) |
| Fibonacci-Verhältnis | Linear | Langsam (O(1/n)) |
| Wurzeldarstellung | Quadratisch | Mittel |

## OEIS-Referenzen zu Phi

### Primäre Sequenz

| OEIS-ID | Name | URL |
|---------|------|-----|
| **A001622** | Decimal expansion of golden ratio phi | https://oeis.org/A001622 |

### Detaillierte OEIS-Informationen für A001622

```json
{
  "sequence_id": "A001622",
  "name": "Decimal expansion of golden ratio phi (or tau) = (1 + sqrt(5))/2",
  "url": "https://oeis.org/A001622",
  "former_id": "M4046 N1679",
  "formula": "(1 + sqrt(5))/2",
  "offset": "1,2",
  "author": "N. J. A. Sloane",
  "keywords": ["cons", "nonn", "core", "nice", "easy"],
  "status": "approved",
  "terms_first_100": [1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5, 8, 6, 8, 3, 4, 3, 6, 5, 6, 3, 8, 1, 1, 7, 7, 2, 0, 3, 0, 9, 1, 7, 9, 8, 0, 5, 7, 6, 2, 8, 6, 2, 1, 3, 5, 4, 4, 8, 6, 2, 2, 7, 0, 5, 2, 6, 0, 4, 6, 2, 8, 1, 8, 9, 0, 2, 4, 4, 9, 7, 0, 7, 2, 0, 7, 2, 0, 4, 1, 8, 9, 3, 9, 1, 1, 3, 7, 4, 8, 4, 7, 5],
  "decimal_value": "1.61803398874989484820458683436563811772030917980576286213544862270526046281890...",
  "cross_references": ["A000012", "A000032", "A000045", "A001654", "A006497", "A080039", "A104457", "A188635", "A192222", "A192223", "A145996", "A139339", "A197762", "A002163", "A094874", "A134973"]
}
```

### Verwandte OEIS-Sequenzen

| OEIS-ID | Beschreibung | Beziehung zu φ |
|---------|-------------|----------------|
| A000045 | Fibonacci numbers | lim F(n+1)/F(n) = φ |
| A000032 | Lucas numbers | L(n) = φⁿ + (1-φ)ⁿ |
| A000201 | Lower Wythoff sequence | Beatty sequence: floor(n*φ) |
| A001950 | Upper Wythoff sequence | Beatty sequence: floor(n*φ²) |
| A094214 | Decimal expansion of 1/φ | 1/φ = φ - 1 |
| A002163 | Decimal expansion of √5 | √5 = 2φ - 1 |

### Weitere Phi-bezogene Sequenzen

| OEIS-ID | Name |
|---------|------|
| A001654 | φ in verschiedenen Formeln |
| A006497 | Lucas numbers related |
| A080039 | Golden ratio powers |
| A104457 | Golden rectangle related |
| A188635 | Continued fraction [tau, tau, tau, ...] |
| A192222 | Phi in Fibonacci context |
| A192223 | Phi approximations |

## Geometrische Eigenschaften

### Goldener Schnitt als Verhältnis

Wenn eine Strecke im Verhältnis φ geteilt wird:
```
Gesamt : Großer Teil = Großer Teil : Kleiner Teil
a : b = b : (a-b)
```

### Goldener Winkel

```
Goldener Winkel = 2π/φ² ≈ 137.5°
```

### Goldener Schnitt im Fünfeck

- Diagonale : Seite = φ
- Im Pentagramm erscheint φ an allen Ecken

### Goldene Spirale

Die goldene Spirale wird durch aufeinanderfolgende Quadrate mit Fibonacci-Seitenlängen konstruiert.

## Besondere Eigenschaften

### Die "irrationalste" Zahl

- φ hat die langsamst konvergierenden Kettenbruch-Näherungen
- I. Stewart in "Nature's Numbers" (1997): "The golden ratio phi is the most irrational among irrational numbers"
- Quelle: OEIS A001622 Comment by Lekraj Beedassy, Jan 21 2005

### Multiplikative Eigenschaften

```
φ² = φ + 1
φ³ = 2φ + 1
φ⁴ = 3φ + 2
φⁿ = F(n)φ + F(n-1)
```

### Verbindung zu π

```
φ = 2 * cos(π/5)
φ = e^(asinh(1/2))
```

## Phi vs. Pi - Vergleich

| Eigenschaft | π | φ |
|-------------|---|---|
| Wert | 3.14159... | 1.61803... |
| Algebraizität | Transzendent | Algebraisch |
| Minimalpolynom | Keines (transzendent) | x² - x - 1 |
| Kettenbruch | Unbekannt/Unendlich | [1; 1, 1, 1, ...] |
| Geometrie | Kreis | Rechteck, Fünfeck |
| Berechenbarkeit | Algorithmisch | Geschlossene Formel |

## Referenzen

1. OEIS Foundation, "A001622 - Decimal expansion of golden ratio phi", https://oeis.org/A001622
2. Wikipedia, "Goldener Schnitt", https://de.wikipedia.org/wiki/Goldener_Schnitt
3. Wikipedia, "Golden ratio", https://en.wikipedia.org/wiki/Golden_ratio
4. Gardner, M., "The Second Scientific American Book Of Mathematical Puzzles and Diversions", Simon & Schuster, 1961
5. Livio, M., "The Golden Ratio: The Story of Phi", Broadway Books, 2002

---

*Dokument erstellt: 2026-04-10*  
*Letzte Aktualisierung: 2026-04-10*
