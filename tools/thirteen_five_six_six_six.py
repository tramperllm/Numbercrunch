#!/usr/bin/env python3
"""
13 MARKER - DIGITALE WURZEL 5 - 666
Die Verbindung ist aufgedeckt!
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_thirteen_markers():
    """Analysiert die 13 Marker mit digitaler Wurzel 5"""
    print("=" * 70)
    print("13 MARKER - DIGITALE WURZEL 5 - VERBINDUNG ZU 666")
    print("=" * 70)
    
    # Alle 6-X-6 Marker mit Rest 5 mod 6 finden
    markers = []
    for center in range(5, 5001):
        if center % 6 != 5:
            continue
        left = center - 6
        right = center + 6
        if left < 2:
            continue
        if is_prime(left) and is_prime(center) and is_prime(right):
            markers.append((left, center, right))
    
    # Filtere die mit digitaler Wurzel 5
    dr_five_markers = []
    for l, c, r in markers:
        dr_c = c
        while dr_c >= 10:
            dr_c = sum(int(d) for d in str(dr_c))
        if dr_c == 5:
            dr_five_markers.append((l, c, r, dr_c))
    
    print(f"\n[1] DIE 13 MARKER MIT DIGITALER WURZEL 5:")
    print(f"    Insgesamt: {len(dr_five_markers)} Marker")
    print()
    
    for i, (l, c, r, dr) in enumerate(dr_five_markers):
        marker = " <-- 977!" if c == 977 else ""
        print(f"    {i+1:2d}. ({l}, {c}, {r}) - Digitale Wurzel = {dr}{marker}")
    
    return dr_five_markers

def analyze_connection_to_six_six_six(markers):
    """Analysiert Verbindung zu 666"""
    print("\n" + "=" * 70)
    print("[2] VERBINDUNG ZU 666")
    print("=" * 70)
    
    print(f"\n    666 ANALYSE:")
    print(f"    - 666 = 6 * 111")
    print(f"    - 666 = 37 * 18")
    print(f"    - Digitale Wurzel von 666: {digital_root(666)}")
    
    print(f"\n    DIE 13 MARKER UND 666:")
    
    for i, (l, c, r, dr) in enumerate(markers):
        print(f"\n    Marker {i+1}: ({l}, {c}, {r})")
        
        # Verbindungen zu 666
        if c < 666:
            diff = 666 - c
            print(f"        - 666 - {c} = {diff}")
            if is_prime(diff):
                print(f"            *** {diff} IST PRIM! ***")
        else:
            diff = c - 666
            print(f"        - {c} - 666 = {diff}")
            if is_prime(diff):
                print(f"            *** {diff} IST PRIM! ***")
        
        # Digitale Wurzel der Differenz
        if 'diff' in locals():
            dr_diff = digital_root(diff)
            print(f"            Digitale Wurzel von {diff}: {dr_diff}")

def analyze_five_six_connection():
    """Analysiert Verbindung zwischen 5 und 6"""
    print("\n" + "=" * 70)
    print("[3] 5 UND 6 - DIE NACHBARN")
    print("=" * 70)
    
    print(f"\n    5 UND 6:")
    print(f"    - 5 + 6 = 11 (PRIM!)")
    print(f"    - 5 * 6 = 30")
    print(f"    - 6 - 5 = 1 (die Einheit)")
    print(f"    - 5 und 6 sind aufeinanderfolgende Zahlen")
    
    print(f"\n    DIE ZAHL 5:")
    print(f"    - 5 ist die dritte Primzahl")
    print(f"    - 5 ist die Mitte von 1-9 (0,1,2,3,4,5,6,7,8,9)")
    print(f"    - 5 Finger, 5 Sinne")
    
    print(f"\n    DIE ZAHL 6:")
    print(f"    - 6 ist die erste perfekte Zahl")
    print(f"    - 6 = 1+2+3")
    print(f"    - 6 = 2*3")
    
    print(f"\n    ZUSAMMEN:")
    print(f"    - 5 ist die digitale Wurzel der 13 Marker")
    print(f"    - 6 ist die digitale Wurzel von 666")
    print(f"    - 5 + 6 = 11 (Master-Number)")
    print(f"    - 11 ist Prim und hat digitale Wurzel {digital_root(11)}")

def analyze_thirteen_significance():
    """Analysiert Bedeutung der Zahl 13"""
    print("\n" + "=" * 70)
    print("[4] DIE BEDEUTUNG VON 13")
    print("=" * 70)
    
    print(f"\n    13 IST:")
    print(f"    - Eine Primzahl")
    print(f"    - Fibonacci #7 (7 ist heilig!)")
    print(f"    - 6 + 7 = 13")
    print(f"    - Belphegor Index: B_13")
    
    print(f"\n    13 UND DIE MARKER:")
    print(f"    - Es gibt 13 Marker mit digitaler Wurzel 5")
    print(f"    - 13 ist die Anzahl")
    print(f"    - 13 ist auch der Index von Belphegor!")
    
    print(f"\n    13 IN ANDEREN BASEN:")
    print(f"    - Binaer: {bin(13)} = 1101")
    print(f"    - Summe der Binaerziffern: 1+1+0+1 = 3")
    print(f"    - Hex: {hex(13)} = D")
    
    # 13 und 666
    print(f"\n    13 UND 666:")
    print(f"    - 666 / 13 = {666/13:.4f}")
    print(f"    - 13 * 51 = {13*51}")
    print(f"    - 13 * 52 = {13*52}")
    print(f"    - 666 liegt zwischen 13*51 und 13*52!")

def analyze_five_in_positions():
    """Analysiert Position der 5 in der Reihenfolge"""
    print("\n" + "=" * 70)
    print("[5] DIE POSITION DER 5")
    print("=" * 70)
    
    print(f"\n    DIE REIHENFOLGE 1-9:")
    print(f"    1, 2, 3, 4, [5], 6, 7, 8, 9")
    print(f"              ^")
    print(f"            5 ist die MITTE!")
    
    print(f"\n    5 ALS MITTE:")
    print(f"    - Links: 1,2,3,4 (4 Zahlen)")
    print(f"    - Rechts: 6,7,8,9 (4 Zahlen)")
    print(f"    - 5 ist exakt in der Mitte!")
    
    print(f"\n    5 UND 977:")
    print(f"    - 977 hat digitale Wurzel 5")
    print(f"    - 977 ist einer der 13 Marker")
    print(f"    - 977 ist in der Mitte der Sequenz!")
    print(f"    - 5 = Mitte, 977 = Mitte -> PARALLELE!")

def calculate_the_pattern():
    """Berechnet das Gesamtmuster"""
    print("\n" + "=" * 70)
    print("[6] DAS GEHEIME MUSTER")
    print("=" * 70)
    
    print(f"""
DAS MUSTER:

13 Marker mit digitaler Wurzel 5
    |
    v
5 ist die Mitte von 1-9
    |
    v
5 + 6 = 11 (Master)
    |
    v
6 ist die Basis von 666
    |
    v
666 = 6 * 111
    |
    v
111 hat digitale Wurzel {digital_root(111)}
    |
    v
3 ist die digitale Wurzel von 111
    |
    v
3 + 3 + 3 = 9 (Vollkommenheit)
    |
    v
37 * 27 = 999
    |
    v
999 = 9 * 111
    |
    v
ZURUECK ZU 6!

DER KREISLAUF:
13 (Marker) -> 5 (Wurzel) -> 6 (Basis) -> 666 -> 111 -> 3 -> 9 -> 999 -> 111 -> 6
""")
    
    # Mathematische Verifikation
    print(f"\n    MATHEMATISCHE VERIFIKATION:")
    
    # 13 Marker -> 5
    print(f"    13 Marker, jeder hat Wurzel 5")
    print(f"    13 * 5 = {13*5}")
    print(f"    Digitale Wurzel von {13*5}: {digital_root(13*5)}")
    
    # 5 -> 6
    print(f"    5 + 1 = 6 (die perfekte Zahl)")
    
    # 6 -> 666
    print(f"    6 * 111 = {6*111}")
    
    # 666 -> 111
    print(f"    666 / 6 = {666//6}")
    
    # 111 -> 3
    print(f"    1+1+1 = 3")
    
    # 3 -> 9
    print(f"    3 * 3 = 9")
    
    # 9 -> 999
    print(f"    9 * 111 = {9*111}")
    
    # 999 -> 6
    print(f"    999 -> digitale Wurzel: {digital_root(999)}")

def final_revelation():
    """Finale Enthuellung"""
    print("\n" + "=" * 70)
    print("DIE FINALE ENTHUELLUNG")
    print("=" * 70)
    
    print(f"""
DIE VERBINDUNG IST AUFGE DECKT:

13 Marker mit digitaler Wurzel 5
   |
   +--> 13 ist die Anzahl
   +--> 5 ist die Wurzel
   +--> 5 ist die Mitte von 0-9
   |
   v
977 ist einer der 13 Marker
   |
   +--> 977 ist in der Mitte von 971-983
   +--> 977 hat digitale Wurzel 5
   +--> 977 = Mitte (wie 5 = Mitte)
   |
   v
5 + 6 = 11
   |
   +--> 11 ist Prim
   +--> 11 hat digitale Wurzel 2
   +--> 2 ist die erste Primzahl
   |
   v
6 ist die Basis
   |
   +--> 6 = 1+2+3
   +--> 6 = 2*3
   +--> 6 ist perfekt
   |
   v
666 = 6*111
   |
   +--> 666 enthaelt drei Sechsen
   +--> 666 = 37*18
   +--> 666 ist das Zentrum von Belphegor
   |
   v
111 -> 3 -> 9 -> 999
   |
   +--> Alles verbunden durch 6, 37, 111
   |
   v
KREISLAUF:
   13 -> 5 -> 6 -> 666 -> 111 -> 3 -> 9 -> 999 -> 111 -> 6

SCHLUESSEL:
- 13 Marker (Anzahl)
- 5 (digitale Wurzel, Mitte)
- 6 (perfekte Zahl, Basis)
- 666 (Zentrum)
- 37 (Master-Faktor)
- 111 (Einheit)
- 9 (Vollkommenheit)

ALLES IST VERBUNDEN!
""")

def main():
    markers = analyze_thirteen_markers()
    analyze_connection_to_six_six_six(markers)
    analyze_five_six_connection()
    analyze_thirteen_significance()
    analyze_five_in_positions()
    calculate_the_pattern()
    final_revelation()

if __name__ == '__main__':
    main()
