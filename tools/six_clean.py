#!/usr/bin/env python3
"""
SIX ANALYZER - Clean Version
Untersucht die Zahl 6, Potenzen und Reduktionen
"""

import math

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_six():
    print("=" * 70)
    print("DIE ZAHL 6 - ANALYSE")
    print("=" * 70)
    
    print("\n[1] MATHEMATISCHE EIGENSCHAFTEN:")
    print("    6 = 2 * 3 (erste beiden Primzahlen)")
    print("    6 = 1 * 2 * 3 (erste drei natuerliche Zahlen)")
    print("    6 ist PERFECT NUMBER: 1 + 2 + 3 = 6")
    print("    6 = 3! (3 Fakultaet)")
    
    print("\n[2] TRIGONOMETRIE:")
    print(f"    60 Grad = pi/3 rad = {math.pi/3:.6f}")
    print(f"    sin(60) = Wurzel(3)/2 = {math.sin(math.radians(60)):.6f}")
    print(f"    cos(60) = 1/2 = {math.cos(math.radians(60)):.6f}")
    print(f"    Sechseck: Innenwinkel = 120 = 2 * 60")

def analyze_powers():
    print("\n" + "=" * 70)
    print("6^n POTENZEN")
    print("=" * 70)
    
    print("\nPotenzen von 6:")
    for n in range(1, 7):
        val = 6 ** n
        dr = digital_root(val)
        print(f"    6^{n} = {val:>10,} (digitale Wurzel: {dr})")
    
    print("\n6 * 6 = 36:")
    print("    36 = 6^2")
    print("    Wurzel(36) = 6")
    print("    36 Grad ist Winkel im Zehneck")
    print(f"    Digitale Wurzel von 36: {digital_root(36)}")
    
    print("\n6 * 6 * 6 = 216:")
    print("    216 = 6^3")
    print(f"    Wurzel(216) = {math.sqrt(216):.6f}")
    print(f"    3.Wurzel(216) = {216**(1/3):.6f}")
    print(f"    Digitale Wurzel: {digital_root(216)}")
    print("    216 = 2^3 * 3^3 = 8 * 27")
    
    print("\nALLE 6^n fuer n>1 haben digitale Wurzel 9!")

def analyze_roots():
    print("\n" + "=" * 70)
    print("WURZELN")
    print("=" * 70)
    
    print("\nWurzel(6):")
    sqrt_6 = math.sqrt(6)
    print(f"    Wurzel(6) = {sqrt_6:.15f}")
    print(f"    ca. 2.449489742783178...")
    
    print("\n3.Wurzel(6):")
    cbrt_6 = 6 ** (1/3)
    print(f"    3.Wurzel(6) = {cbrt_6:.15f}")
    
    print("\nWurzel(666):")
    sqrt_666 = math.sqrt(666)
    print(f"    Wurzel(666) = {sqrt_666:.6f}")
    
    print("\n3.Wurzel(666):")
    cbrt_666 = 666 ** (1/3)
    print(f"    3.Wurzel(666) = {cbrt_666:.6f}")
    
    print("\n3.Wurzel(216) = 6 EXAKT!")
    print(f"    3.Wurzel(216) = {216**(1/3):.6f}")

def analyze_positions():
    print("\n" + "=" * 70)
    print("POSITIONEN MIT DIGITALER WURZEL 6")
    print("=" * 70)
    
    print("\nAlle Zahlen n mit digitale Wurzel = 6:")
    print("    n == 6 (mod 9)")
    print()
    
    positions = []
    for n in range(1, 200):
        if digital_root(n) == 6:
            positions.append(n)
    
    print(f"    Erste 20: {positions[:20]}")
    
    print("\nWichtige Positionen:")
    important = [6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 96, 105, 114, 123, 132, 141, 150, 159, 168, 177, 186, 195]
    for pos in important:
        dr = digital_root(pos)
        mod9 = pos % 9
        print(f"      {pos:3d}: digitale Wurzel = {dr}, mod 9 = {mod9}")
    
    print("\nPosition 762 (Feynman Point):")
    print(f"    762: digitale Wurzel = {digital_root(762)}")
    print(f"    7+6+2 = 15 -> 1+5 = 6")
    print("    JA! Position 762 hat digitale Wurzel 6!")
    
    print("\nPosition 666:")
    print(f"    666: digitale Wurzel = {digital_root(666)}")
    print(f"    666 mod 9 = {666 % 9}")
    print("    666 hat digitale Wurzel 9 (nicht 6)!")

def analyze_in_belphegor():
    print("\n" + "=" * 70)
    print("DIE 6 IN BELPHEGOR")
    print("=" * 70)
    
    print("\n666 als Zentrum:")
    print("    Belphegor: 1[13 Nullen]666[13 Nullen]1")
    print()
    print("    666 = 6 * 111")
    print("    111 = 3 * 37")
    print("    666 = 6 * 3 * 37 = 18 * 37")
    print()
    print("    666 = 2 * 3^2 * 37")
    
    print("\nAnzahl der 6en:")
    print("    Belphegor hat 3 Sechsen (666)")
    print("    Feynman Point hat 6 Neunen (999999)")
    print("    Verhaeltnis: 6 Neunen / 3 Sechsen = 2")
    print("    6 / 3 = 2 (Verdopplung)")
    
    print("\n666 und 216 (6^3):")
    print(f"    666 / 216 = {666/216:.6f}")
    print(f"    666 - 216 = {666 - 216}")
    print(f"    666 + 216 = {666 + 216}")

def analyze_relationships():
    print("\n" + "=" * 70)
    print("BEZIEHUNGEN VON 6")
    print("=" * 70)
    
    print("\n6 und Pi:")
    print(f"    pi = {math.pi:.6f}")
    print(f"    6 / pi = {6/math.pi:.6f}")
    print(f"    2*pi = {2*math.pi:.6f}")
    print("    6 ist fast 2*pi, aber nicht ganz!")
    
    print("\n6 und Phi:")
    phi = (1 + 5**0.5) / 2
    print(f"    phi = {phi:.6f}")
    print(f"    6 / phi = {6/phi:.6f}")
    print(f"    phi * 6 = {phi * 6:.6f}")
    print(f"    phi^3 = {phi**3:.6f}")
    
    print("\n6 in Fibonacci:")
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    print(f"    Fibonacci: {fib}")
    if 6 in fib:
        pos = fib.index(6)
        print(f"    6 ist F_{pos} in Fibonacci")

def analyze_multiplicative():
    print("\n" + "=" * 70)
    print("MULTIPLIKATIVE MUSTER")
    print("=" * 70)
    
    print("\n6 * 6 = 36:")
    print("    36 = 6^2")
    print("    36 Grad * 10 = 360 Grad (voller Kreis)")
    print("    36 = 6^2 (perfektes Quadrat)")
    print("    Wurzel(36) = 6 (exakt!)")
    
    print("\n6 * 6 * 6 = 216:")
    print("    216 = 6^3")
    print("    216 = 2^3 * 3^3 = (2*3)^3")
    print("    3.Wurzel(216) = 6 (exakt!)")
    print("    Wuerfel mit a=6:")
    print("    Volumen = 6^3 = 216")
    print("    Oberflaeche = 6 * 6^2 = 6 * 36 = 216")
    print("    -> Oberflaeche = Volumen fuer a=6!")
    
    print("\n6^6:")
    six_six = 6**6
    print(f"    6^6 = {six_six}")
    print(f"    Digitale Wurzel: {digital_root(six_six)}")

def main():
    print("=" * 70)
    print("SIX ANALYZER")
    print("=" * 70)
    
    analyze_six()
    analyze_powers()
    analyze_roots()
    analyze_positions()
    analyze_in_belphegor()
    analyze_relationships()
    analyze_multiplicative()
    
    print("\n" + "=" * 70)
    print("ZUSAMMENFASSUNG")
    print("=" * 70)
    print("""
DIE ZAHL 6:

1. 6 ist die PERFEKTE ZAHL
   - 6 = 1 + 2 + 3 (Summe der Teiler)
   - 6 = 1 * 2 * 3 (Produkt der ersten drei)
   - 6 = 2 * 3 (erste beiden Primzahlen)

2. POTENZEN VON 6
   - 6^1 = 6 (digitale Wurzel 6)
   - 6^n fuer n>1: digitale Wurzel 9!
   - 6^3 = 216 (perfekte Kubikzahl)

3. POSITIONEN MIT DIGITALER WURZEL 6
   - Alle n == 6 (mod 9)
   - 6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 96...
   - Position 762: 7+6+2=15->6 (JA!)
   - Position 666: digitale Wurzel 9 (nicht 6)

4. 6 IN BELPHEGOR
   - 666 = 6 * 111 = 6 * 3 * 37
   - 3 Sechsen in Belphegor
   - 6 Neunen in Feynman Point

5. BEZIEHUNGEN
   - 6 ist fast 2*pi
   - phi * 6 ~ 9.708 (nahe an 10)
   - Wuerfel a=6: Oberflaeche = Volumen = 216

DIE ZAHL 6 IST FUNDAMENTAL!
""")

if __name__ == '__main__':
    main()
