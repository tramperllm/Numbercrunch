#!/usr/bin/env python3
"""
SIX ANALYZER
Tiefgehende Untersuchung der Zahl 6, ihrer Potenzen und Reduktionen
Verbindungen zu Belphegor (666), Pi und Phi
"""

import math
from decimal import Decimal, getcontext

getcontext().prec = 100

def digital_root(n):
    """Berechnet digitale Wurzel"""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def sum_of_digits(n):
    """Quersumme"""
    return sum(int(d) for d in str(n))

def analyze_six_basic():
    """Analysiert die Grundzahl 6"""
    print("=" * 70)
    print("DIE ZAHL 6 - GRUNDANALYSE")
    print("=" * 70)
    
    print("\n[1] MATHEMATISCHE EIGENSCHAFTEN:")
    print(f"    6 = 2 × 3 (erste beiden Primzahlen)")
    print(f"    6 = 1 × 2 × 3 (erste drei natuerliche Zahlen)")
    print(f"    6 ist PERFECT NUMBER: 1 + 2 + 3 = 6")
    print(f"    6 = 3! (3 Fakultaet)")
    
    print("\n[2] TRIGONOMETRIE:")
    print(f"    60° = π/3 rad = {math.pi/3:.6f}")
    print(f"    sin(60°) = √3/2 = {math.sin(math.radians(60)):.6f}")
    print(f"    cos(60°) = 1/2 = {math.cos(math.radians(60)):.6f}")
    print(f"    Sechseck (Hexagon): Innenwinkel = 120° = 2 × 60°")
    
    print("\n[3] DIE DREIECKSZAHL:")
    print(f"    6. Dreieckszahl: 1+2+3 = 6")
    print(f"    Formel: n(n+1)/2 fuer n=3: 3×4/2 = 6")
    
    print("\n[4] IN DER ZAHLENTHEORIE:")
    print(f"    6 ist kleinste perfekte Zahl")
    print(f"    Naechste: 28, 496, 8128...")
    print(f"    6 ist auch zusammengesetzte Zahl")

def analyze_six_powers():
    """Analysiert 6^n Potenzen"""
    print("\n" + "=" * 70)
    print("6^n POTENZEN")
    print("=" * 70)
    
    print("\n[1] DIE POTENZEN VON 6:")
    for n in range(1, 8):
        val = 6 ** n
        dr = digital_root(val)
        print(f"    6^{n} = {val:>15,} (digitale Wurzel: {dr})")
    
    print("\n[2] 6 × 6 = 36:")
    print(f"    36 = 6²")
    print(f"    √36 = 6")
    print(f"    36° ist Winkel im Fuenfeck (360/10)")
    print(f"    Digitale Wurzel: {digital_root(36)}")
    
    print("\n[3] 6 × 6 × 6 = 216:")
    print(f"    216 = 6³")
    print(f"    √216 = {math.sqrt(216):.6f}")
    print(f"    ³√216 = {216**(1/3):.6f}")
    print(f"    Digitale Wurzel: {digital_root(216)}")
    print(f"    216 = 2³ × 3³ = 8 × 27")
    
    print("\n[4] BESONDERE EIGENSCHAFTEN:")
    print(f"    6² = 36:  3+6 = 9")
    print(f"    6³ = 216: 2+1+6 = 9")
    print(f"    6⁴ = 1296: 1+2+9+6 = 18 → 9")
    print(f"    6⁵ = 7776: 7+7+7+6 = 27 → 9")
    print()
    print("    => ALLE Potenzen von 6 haben digitale Wurzel 9!")
    print(f"    Beweis: 6 ≡ 6 (mod 9), 6^n ≡ 6^n (mod 9)")
    print(f"    6^1 = 6 mod 9")
    print(f"    6^2 = 36 ≡ 0 mod 9? Nein!")
    print(f"    Korrektur: 36 mod 9 = 0, digitale Wurzel = 9")

def analyze_six_roots():
    """Analysiert Wurzeln von 6, 36, 216, 666"""
    print("\n" + "=" * 70)
    print("WURZELN UND IRRATIONALE ZAHLEN")
    print("=" * 70)
    
    print("\n[1] √6 (Quadratwurzel aus 6):")
    sqrt_6 = math.sqrt(6)
    print(f"    √6 = {sqrt_6:.15f}")
    print(f"    √6 ≈ 2.449489742783178...")
    print(f"    In Dezimalstellen: {str(sqrt_6)[:20]}...")
    
    # Erste paar Stellen analysieren
    sqrt_6_str = str(sqrt_6)[:30]
    print(f"    Enthaelt '666': {'666' in sqrt_6_str}")
    print(f"    Enthaelt '999': {'999' in sqrt_6_str}")
    
    print("\n[2] ³√6 (Kubikwurzel aus 6):")
    cbrt_6 = 6 ** (1/3)
    print(f"    ³√6 = {cbrt_6:.15f}")
    
    print("\n[3] √666:")
    sqrt_666 = math.sqrt(666)
    print(f"    √666 = {sqrt_666:.6f}")
    print(f"    √666 ≈ 25.806975...")
    
    print("\n[4] ³√666:")
    cbrt_666 = 666 ** (1/3)
    print(f"    ³√666 = {cbrt_666:.6f}")
    
    print("\n[5] √216 (Kubikwurzel aus 6³ = 216):")
    sqrt_216 = math.sqrt(216)
    cbrt_216 = 216 ** (1/3)
    print(f"    √216 = {sqrt_216:.6f}")
    print(f"    ³√216 = {cbrt_216:.6f} = 6 EXAKT!")
    
    print("\n[6] 6^(1/6) (6-te Wurzel aus 6):")
    sixth_root = 6 ** (1/6)
    print(f"    6^(1/6) = {sixth_root:.15f}")

def analyze_positions_reducing_to_six():
    """Analysiert Positionen, die auf 6 reduziert werden koennen"""
    print("\n" + "=" * 70)
    print("POSITIONEN, DIE AUF 6 REDUZIEREN")
    print("=" * 70)
    
    print("\n[1] FUER DIE DIGITALE WURZEL = 6:")
    print("    Alle Zahlen n mit n ≡ 6 (mod 9)")
    print()
    
    # Liste einige Positionen
    positions = []
    for n in range(1, 1000):
        if digital_root(n) == 6:
            positions.append(n)
    
    print(f"    Erste 20 Positionen: {positions[:20]}")
    print()
    
    # Pruefe auf wichtige Positionen
    important_positions = [6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 96, 
                          105, 114, 123, 132, 141, 150, 159, 168, 177, 186, 195,
                          600, 609, 615, 624, 666]
    
    print("    Wichtige Positionen mit digitaler Wurzel 6:")
    for pos in important_positions:
        if pos <= 1000:
            dr = digital_root(pos)
            mod9 = pos % 9
            print(f"      {pos}: digitale Wurzel = {dr}, mod 9 = {mod9}")
    
    print("\n[2] SPEZIELLE POSITION 762 (Feynman Point):")
    print(f"    762: digitale Wurzel = {digital_root(762)}")
    print(f"    762 mod 9 = {762 % 9}")
    print(f"    Position 762 hat digitale Wurzel {digital_root(762)}, nicht 6!")
    print()
    print("    ABER: Die 6 Neunen beginnen bei Position 762!")
    print("    Position 762-767: 999999")
    
    print("\n[3] POSITION 666:")
    print(f"    666: digitale Wurzel = {digital_root(666)}")
    print(f"    666 mod 9 = {666 % 9}")
    print(f"    666 ≡ 0 (mod 9) -> digitale Wurzel 9!")
    
    print("\n[4] POSITIONEN IN PI:")
    print("    (Hypothetische Analyse - Pi-Stellen nicht geladen)")
    print("    Wichtige Pi-Positionen mit Verbindung zu 6:")
    print("    - Position 762 (Feynman Point): 6 Neunen")
    print("    - Position 6: Erste Nachkommastelle")
    print("    - Position 66, 666: Langweilig (nur 6en)")

def analyze_six_in_belphegor():
    """Analysiert 6 in Belphegor-Struktur"""
    print("\n" + "=" * 70)
    print("DIE 6 IN BELPHEGOR'S PRIMZAHL")
    print("=" * 70)
    
    print("\n[1] 666 ALS ZENTRUM:")
    print("    Belphegor B_13: 1[13 Nullen]666[13 Nullen]1")
    print()
    print("    666 = 6 × 111")
    print(f"    111 = 3 × 37")
    print(f"    666 = 6 × 3 × 37 = 18 × 37")
    print()
    print(f"    666 = 2 × 3² × 37")
    
    print("\n[2] ANZAHL DER 6EN:")
    print("    Belphegor hat 3 Sechsen (666)")
    print("    Feynman Point hat 6 Neunen (999999)")
    print("    Verhaeltnis: 6 Neunen / 3 Sechsen = 2")
    print()
    print("    6 / 3 = 2 (Verdopplung)")
    print("    2 ist die kleinste Primzahl!")
    
    print("\n[3] 666 UND 6³ = 216:")
    print(f"    666 / 216 = {666/216:.6f} = 3.083...")
    print(f"    666 - 216 = {666 - 216} = 450")
    print(f"    450 = 9 × 50 = 9 × 2 × 25 = 9 × 2 × 5²")
    print()
    print(f"    666 + 216 = {666 + 216} = 882")
    print(f"    882 = 2 × 441 = 2 × 21² = 2 × 3² × 7²")
    
    print("\n[4] 666 IN ANDEREN BASEN:")
    print(f"    666 dezimal = 0x29A hex = {hex(666)}")
    print(f"    666 dezimal = 0o1232 oktal = {oct(666)}")
    print()
    print(f"    Hex 0x29A: 2+9+A(10) = 21 → 2+1 = 3")
    print(f"    Oktal 1232: 1+2+3+2 = 8")

def analyze_six_relationships():
    """Analysiert Beziehungen von 6 zu Pi und Phi"""
    print("\n" + "=" * 70)
    print("6 UND SEINE BEZIEHUNGEN")
    print("=" * 70)
    
    print("\n[1] 6 UND PI:")
    print(f"    π ≈ 3.14159...")
    print(f"    6 / π = {6/math.pi:.6f}")
    print(f"    π × 2 = {math.pi * 2:.6f} (Kreisumfang bei r=1)")
    print(f"    → 6 ist fast 2π (aber nicht ganz!)")
    print()
    print(f"    Genauer: 2π ≈ {2*math.pi:.6f}")
    print(f"    6 / 2π = {6/(2*math.pi):.6f} ≈ 0.9549...")
    
    print("\n[2] 6 UND PHI (Goldener Schnitt):")
    phi = (1 + 5**0.5) / 2
    print(f"    φ = {phi:.6f}")
    print(f"    6 / φ = {6/phi:.6f}")
    print(f"    φ × 6 = {phi * 6:.6f}")
    print()
    print(f"    φ³ = {phi**3:.6f}")
    print(f"    φ³ = 2φ + 1 ≈ 4.236...")
    print(f"    6 - φ³ = {6 - phi**3:.6f}")
    
    print("\n[3] 6 IN DER FIBONACCI-FOLGE:")
    fib = [0, 1]
    for i in range(2, 15):
        fib.append(fib[-1] + fib[-2])
    
    print(f"    Fibonacci: {fib}")
    
    # Finde Position von 6
    if 6 in fib:
        pos_6 = fib.index(6)
        print(f"    6 ist F_{pos_6}")
    
    # Finde Vielfache von 6
    multiples_6 = [(i, f) for i, f in enumerate(fib) if f % 6 == 0 and f > 0]
    print(f"    Fibonacci-Zahlen, die durch 6 teilbar sind:")
    for pos, val in multiples_6[:5]:
        print(f"      F_{pos} = {val}")
    
    print("\n[4] 6 UND DAS SIEBDES SYSTEM:")
    print("    Sechseck (Hexagon) ist perfektes Parkettierungsmuster")
    print("    Wabenstruktur in der Natur (Bienen, Basalt)")
    print("    Kristallgitter: hexagonale Struktur")
    print("    Graphen: 6-fache Symmetrie")

def analyze_multiplicative_patterns():
    """Analysiert 6×6, 6×6×6 Muster"""
    print("\n" + "=" * 70)
    print("MULTIPLIKATIVE MUSTER: 6×6, 6×6×6")
    print("=" * 70)
    
    print("\n[1] 6×6 = 36 MUSTER:")
    print(f"    36 = 6² = 6 × 6")
    print(f"    36° × 10 = 360° (voller Kreis)")
    print(f"    36° ist Zentriwinkel im Zehneck")
    print()
    print(f"    36 in der Zahlentheorie:")
    print(f"    36 = 2² × 3² (quadratfrei? Nein!)")
    print(f"    36 = 6² (perfektes Quadrat)")
    print(f"    √36 = 6 (exakt!)")
    
    print("\n[2] 6×6×6 = 216 MUSTER:")
    print(f"    216 = 6³")
    print(f"    216 = 2³ × 3³ = (2×3)³ = 6³")
    print(f"    216 ist perfekte Kubikzahl")
    print(f"    ³√216 = 6 (exakt!)")
    print()
    print(f"    216 in Geometrie:")
    print(f"    Wuerfel mit Kantenlaenge 6 hat Volumen 216")
    print(f"    Oberflaeche: 6 × 6² = 6 × 36 = 216!")
    print(f"    -> Oberflaeche = Volumen fuer a=6!")
    
    print("\n[3] 6^6 MUSTER:")
    six_to_six = 6**6
    print(f"    6^6 = {six_to_six}")
    print(f"    Digitale Wurzel: {digital_root(six_to_six)}")
    print(f"    Sechs Sechsen: 666666")
    print()
    
    print("\n[4] KASKADENMUSTER:")
    print("    6")
    print("    6×6 = 36")
    print("    6×6×6 = 216")
    print("    6×6×6×6 = 1296")
    print("    ...")
    print()
    print("    Jede Potenz hat digitale Wurzel 9!")
    print("    Ausnahme: 6^1 = 6 (digitale Wurzel 6)")

def main():
    print("=" * 70)
    print("SIX ANALYZER")
    print("Die Zahl 6, ihre Potenzen und Beziehungen")
    print("=" * 70)
    
    analyze_six_basic()
    analyze_six_powers()
    analyze_six_roots()
    analyze_positions_reducing_to_six()
    analyze_six_in_belphegor()
    analyze_six_relationships()
    analyze_multiplicative_patterns()
    
    print("\n" + "=" * 70)
    print("ZUSAMMENFASSUNG: DIE ZAHL 6")
    print("=" * 70)
    print("""
FUNDAMENTALE ERKENNTNISSE:

1. 6 IST DIE PERFEKTE ZAHL
   - 6 = 1 + 2 + 3 (Summe der Teiler)
   - 6 = 1 × 2 × 3 (Produkt der ersten drei)
   - 6 = 2 × 3 (erste beiden Primzahlen)

2. POTENZEN VON 6
   - 6^1 = 6 (digitale Wurzel 6)
   - 6^n fuer n>1 hat digitale Wurzel 9!
   - 6^3 = 216 (perfekte Kubikzahl)
   - 6^6 = 46656 (kaskadiert)

3. BEZIEHUNGEN
   - Zu Pi: 6 ist fast 2π, aber nicht ganz
   - Zu Phi: φ × 6 ≈ 9.708 (nahe an 10)
   - Zu Belphegor: 666 = 6 × 111 = 6 × 3 × 37

4. POSITIONEN MIT DIGITALER WURZEL 6
   - Alle n ≡ 6 (mod 9)
   - 6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 96...
   - Position 762 (Feynman) hat digitale Wurzel 6? Nein! (ist 6)
   - Position 762 hat digitale Wurzel 6? 7+6+2=15→6 JA!

5. 6 IN BELPHEGOR
   - 666 ist Zentrum: 3 Sechsen
   - Feynman hat 6 Neunen
   - Verhaeltnis 2:1

DIE ZAHL 6 IST FUNDAMENTAL!
""")

if __name__ == '__main__':
    main()
