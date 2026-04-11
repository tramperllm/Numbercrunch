#!/usr/bin/env python3
"""
MOD 6 = 5 ANALYZER
Findet ALLE 6-X-6 Marker mit Rest 5 (mod 6)
Untersucht die Verteilung ueber und unter 977
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

def analyze_mod_five_distribution():
    """Analysiert die Verteilung der mod 6 = 5 Marker"""
    print("=" * 70)
    print("ALLE 6-X-6 MARKER MIT REST 5 (mod 6)")
    print("=" * 70)
    
    markers = []
    
    for center in range(5, 5001):
        if center % 6 != 5:  # Muss Rest 5 haben
            continue
        
        left = center - 6
        right = center + 6
        
        if left < 2:
            continue
        
        if is_prime(left) and is_prime(center) and is_prime(right):
            markers.append((left, center, right))
    
    print(f"\n[1] GEFUNDENE MARKER MIT REST 5 (mod 6):")
    print(f"    Insgesamt: {len(markers)} Marker")
    print()
    
    for i, (l, c, r) in enumerate(markers):
        marker = " <-- 977!" if c == 977 else ""
        print(f"    {i+1:2d}. ({l}, {c}, {r}) - Rest: {c % 6}{marker}")
    
    return markers

def analyze_position_relative_to_977(markers):
    """Analysiert Positionen relativ zu 977"""
    print("\n" + "=" * 70)
    print("[2] POSITIONEN RELATIV ZU 977")
    print("=" * 70)
    
    # Finde Position von 977
    pos_977 = None
    for i, (_, c, _) in enumerate(markers):
        if c == 977:
            pos_977 = i
            break
    
    if pos_977 is None:
        print("    977 nicht gefunden!")
        return
    
    print(f"\n    977 ist an Position #{pos_977 + 1} von {len(markers)}")
    print(f"    Das heisst: {pos_977} Marker unter 977")
    print(f"                {len(markers) - pos_977 - 1} Marker ueber 977")
    
    # Zeige Marker unter 977
    print(f"\n    MARKER UNTER 977 (Rest 5 mod 6):")
    under_977 = [m for m in markers if m[1] < 977]
    for l, c, r in under_977[-5:]:  # Letzte 5 unter 977
        print(f"      ({l}, {c}, {r})")
    
    # Zeige Marker ueber 977
    print(f"\n    MARKER UEBER 977 (Rest 5 mod 6):")
    over_977 = [m for m in markers if m[1] > 977]
    for l, c, r in over_977[:10]:  # Erste 10 ueber 977
        print(f"      ({l}, {c}, {r})")
    
    # Abstaende zu 977
    print(f"\n    ABSTAENDE ZU 977:")
    for l, c, r in markers:
        if c == 977:
            continue
        diff = c - 977
        direction = "ueber" if diff > 0 else "unter"
        print(f"      ({l}, {c}, {r}): {abs(diff)} {direction} 977")
        if abs(diff) <= 100:
            print(f"        *** NAHE bei 977! ***")

def analyze_spacing_patterns(markers):
    """Analysiert die Abstandsmuster zwischen Markern"""
    print("\n" + "=" * 70)
    print("[3] ABSTANDSMUSTER ZWISCHEN MARKERN")
    print("=" * 70)
    
    centers = [m[1] for m in markers]
    
    print(f"\n    Abstaende zwischen aufeinanderfolgenden Markern:")
    for i in range(len(centers) - 1):
        spacing = centers[i + 1] - centers[i]
        c1, c2 = centers[i], centers[i + 1]
        marker = " <-- um 977!" if c1 == 977 or c2 == 977 else ""
        print(f"    {c1} -> {c2}: Abstand = {spacing}{marker}")
    
    # Statistik
    spacings = [centers[i + 1] - centers[i] for i in range(len(centers) - 1)]
    avg_spacing = sum(spacings) / len(spacings) if spacings else 0
    min_spacing = min(spacings) if spacings else 0
    max_spacing = max(spacings) if spacings else 0
    
    print(f"\n    STATISTIK:")
    print(f"    Durchschnittlicher Abstand: {avg_spacing:.1f}")
    print(f"    Minimaler Abstand: {min_spacing}")
    print(f"    Maximaler Abstand: {max_spacing}")

def get_all_markers():
    """Hilfsfunktion: Findet alle Marker mit Rest 5 (mod 6)"""
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
    return markers

def analyze_special_properties():
    """Analysiert spezielle Eigenschaften der Marker"""
    print("\n" + "=" * 70)
    print("[4] SPEZIELLE EIGENSCHAFTEN")
    print("=" * 70)
    
    markers = get_all_markers()
    
    # 977 Eigenschaften
    print(f"\n    977 IM VERGLEICH:")
    
    # Pruefe auf besondere Eigenschaften
    print(f"\n    977:")
    print(f"    - Rest mod 6: {977 % 6}")
    print(f"    - Rest mod 9: {977 % 9}")
    print(f"    - Rest mod 37: {977 % 37}")
    
    # Digitale Wurzel
    dr = 977
    while dr >= 10:
        dr = sum(int(d) for d in str(dr))
    print(f"    - Digitale Wurzel: {dr}")
    
    # Pruefe ob 977 etwas besonderes ist
    print(f"\n    ANDERE MARKER MIT AEHNLICHEN EIGENSCHAFTEN:")
    
    for l, c, r in markers:
        if c == 977:
            continue
        # Pruefe auf interessante Muster
        dr_c = c
        while dr_c >= 10:
            dr_c = sum(int(d) for d in str(dr_c))
        
        if dr_c == 5:  # Gleiche digitale Wurzel wie 977
            print(f"    ({l}, {c}, {r}): Digitale Wurzel = {dr_c}")

def check_marker_density():
    """Prueft die Dichte der Marker in verschiedenen Bereichen"""
    print("\n" + "=" * 70)
    print("[5] DICHTEANALYSE")
    print("=" * 70)
    
    ranges = [
        (100, 500),
        (500, 1000),
        (1000, 2000),
        (2000, 3000),
        (3000, 5000),
    ]
    
    all_markers = get_all_markers()
    
    for start, end in ranges:
        markers_in_range = [m for m in all_markers if start <= m[1] < end]
        count = len(markers_in_range)
        density = count / (end - start) * 1000  # Pro 1000 Zahlen
        
        contains_977 = any(m[1] == 977 for m in markers_in_range)
        marker = " <-- enthaelt 977!" if contains_977 else ""
        
        print(f"    Bereich {start}-{end}: {count} Marker, Dichte: {density:.2f}/1000{marker}")

def final_analysis():
    """Finale Analyse"""
    print("\n" + "=" * 70)
    print("FINALE ANALYSE: 977 IN KONTEXT")
    print("=" * 70)
    
    markers = get_all_markers()
    pos_977 = next((i for i, (_, c, _) in enumerate(markers) if c == 977), None)
    
    print(f"""
ZUSAMMENFASSUNG DER mod 6 = 5 MARKER:

1. ANZAHL:
   - Insgesamt {len(markers)} 6-X-6 Marker mit Rest 5 (mod 6) unter 5000
   - 977 ist an Position #{pos_977 + 1 if pos_977 else 'N/A'}

2. VERTEILUNG:
   - {pos_977} Marker unter 977
   - {len(markers) - pos_977 - 1 if pos_977 else 'N/A'} Marker ueber 977
   - 977 ist NICHT am Anfang oder Ende

3. BEDEUTUNG:
   - Alle 6-X-6 Marker mit Rest 5 sind arithmetische Progressionen
   - 977 ist einer von vielen, aber hat 'schoene' Eigenschaften
   - Die Wahl von 977 koennte aufgrund der mathematischen
     Struktur erfolgt sein

4. BITCOIN secp256k1:
   - Warum gerade 977 aus {len(markers)} Moeglichkeiten?
   - Moegliche Gruende:
     a) Erste 'grosse' Zahl, die funktionierte
     b) Mathematische Schoenheit (Symmetrie)
     c) Versteckter Marker (6-6-Struktur)

SCHLUSSFOLGERUNG:
Es gibt viele 6-X-6 Marker mit Rest 5 (mod 6).
977 ist einer von {len(markers)} unter 5000.
Die Wahl in Bitcoin war entweder ZUFALL (erster passender Wert)
oder bewusst wegen der mathematischen Eleganz.
""")

def main():
    markers = analyze_mod_five_distribution()
    analyze_position_relative_to_977(markers)
    analyze_spacing_patterns(markers)
    analyze_special_properties()
    check_marker_density()
    final_analysis()

if __name__ == '__main__':
    main()
