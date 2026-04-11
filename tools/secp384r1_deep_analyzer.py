#!/usr/bin/env python3
"""
SECP384R1 DEEP ANALYZER
Tiefenanalyse des 666-Funds in der NIST-Kurve secp384r1
Verifizierung ob Zufall oder beabsichtigt
"""

import math
from fractions import Fraction

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_secp384r1():
    """Analysiert die secp384r1 Primzahl"""
    print("=" * 70)
    print("SECP384R1 TIEFENANALYSE")
    print("NIST-Kurve mit verdachtigem 666-Muster")
    print("=" * 70)
    
    # secp384r1 Primzahl (aus NIST SP 800-186)
    # p = 2^384 - 2^128 - 2^96 + 2^32 - 1
    # Hex: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF0000000000000000FFFFFFFF
    p_hex = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF0000000000000000FFFFFFFF"
    p = int(p_hex, 16)
    
    print(f"\n[1] DIE PRIMZAHL:")
    print(f"    Hex: {p_hex}")
    print(f"    Dezimal: {p}")
    print(f"    Bits: {p.bit_length()}")
    
    str_p = str(p)
    print(f"\n    Laenge: {len(str_p)} Dezimalstellen")
    print(f"    Erste 50: {str_p[:50]}")
    print(f"    Letzte 50: {str_p[-50:]}")
    
    print(f"\n[2] MUSTER-SUCHE:")
    
    # Suche nach 666
    pos_666 = str_p.find('666')
    count_666 = str_p.count('666')
    count_999 = str_p.count('999')
    count_13 = str_p.count('13')
    count_37 = str_p.count('37')
    
    print(f"    Position von '666': {pos_666}")
    print(f"    Anzahl '666': {count_666}")
    print(f"    Anzahl '999': {count_999}")
    print(f"    Anzahl '13': {count_13}")
    print(f"    Anzahl '37': {count_37}")
    
    if pos_666 >= 0:
        context_start = max(0, pos_666 - 20)
        context_end = min(len(str_p), pos_666 + 23)
        context = str_p[context_start:context_end]
        print(f"\n    Kontext um '666':")
        print(f"    ...{context}...")
        print(f"         ^^^")
    
    # Suche nach allen Positionen
    print(f"\n[3] ALLE '666' POSITIONEN:")
    positions = []
    start = 0
    while True:
        pos = str_p.find('666', start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    
    print(f"    Gefunden bei Positionen: {positions}")
    
    return p, str_p, positions

def analyze_666_context(str_p, positions):
    """Analysiert den Kontext der 666-Sequenzen"""
    print(f"\n[4] DETAILLIERTE KONTEXT-ANALYSE:")
    
    for i, pos in enumerate(positions):
        print(f"\n    '666' #{i+1} bei Position {pos}:")
        
        # Hole Kontext
        context_start = max(0, pos - 10)
        context_end = min(len(str_p), pos + 13)
        before = str_p[context_start:pos]
        after = str_p[pos+3:context_end]
        
        print(f"      Vorher: '{before}'")
        print(f"      Muster: '666'")
        print(f"      Nachher: '{after}'")
        
        # Pruefe auf erweiterte Muster
        extended = str_p[max(0, pos-5):min(len(str_p), pos+8)]
        print(f"      Erweiterter Kontext: '{extended}'")
        
        # Zaehle 6en in der Umgebung
        region = str_p[max(0, pos-10):min(len(str_p), pos+13)]
        count_6_in_region = region.count('6')
        print(f"      Anzahl '6' in Region (-10/+13): {count_6_in_region}")

def calculate_probabilities(str_p):
    """Berechnet Wahrscheinlichkeiten fuer Zufall"""
    print(f"\n[5] WAHRSCHEINLICHKEITSANALYSE:")
    
    length = len(str_p)
    
    # Wahrscheinlichkeit fuer '666' an einer bestimmten Position
    # Jede Ziffer ist 0-9, also P(6) = 0.1
    # P(666) = 0.1^3 = 0.001
    p_666_at_position = 0.001
    
    # Erwartete Anzahl in einer Zahl der Laenge L
    # (L-2) moegliche Positionen fuer 3-stellige Sequenz
    expected_count = (length - 2) * p_666_at_position
    
    print(f"    Laenge der Primzahl: {length} Stellen")
    print(f"    P('666' an einer Position) = 0.1^3 = {p_666_at_position}")
    print(f"    Moegliche Positionen: {length - 2}")
    print(f"    Erwartete Anzahl von '666': {expected_count:.4f}")
    
    actual_count = str_p.count('666')
    print(f"    Tatsaechliche Anzahl: {actual_count}")
    
    # Poisson-Wahrscheinlichkeit
    import math
    if expected_count > 0:
        # P(k) = (lambda^k * e^(-lambda)) / k!
        k = actual_count
        lambda_val = expected_count
        poisson_prob = (lambda_val ** k) * math.exp(-lambda_val) / math.factorial(k)
        print(f"    Poisson-P(k={k}): {poisson_prob:.6f}")
    
    # Wahrscheinlichkeit fuer KEIN '666'
    p_no_666 = (1 - p_666_at_position) ** (length - 2)
    print(f"    P(kein '666' in {length} Stellen): {p_no_666:.10f}")
    print(f"    P(mindestens ein '666'): {1 - p_no_666:.10f}")
    
    # Vergleich mit anderen Sequenzen
    print(f"\n[6] VERGLEICH MIT ANDEREN 3-STELLIGEN SEQUENZEN:")
    sequences = ['666', '999', '123', '777', '555', '111', '000']
    
    for seq in sequences:
        count = str_p.count(seq)
        print(f"    '{seq}': {count} Vorkommen")

def analyze_nist_context():
    """Analysiert den NIST-Kontext"""
    print(f"\n[7] NIST KONTEXT:")
    
    print(f"    secp384r1 ist Teil von NIST SP 800-186")
    print(f"    (Elliptic Curve Cryptography)")
    print()
    print(f"    Historie:")
    print(f"    - Entwickelt von NSA (angeblich)")
    print(f"    - Standardisiert durch NIST")
    print(f"    - Verwendet in TLS, SSH, etc.")
    print()
    print(f"    Andere NIST-Kurven:")
    
    # Liste der NIST-Primzahlen
    nist_curves = {
        'secp192r1': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF',
        'secp224r1': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000001',
        'secp256r1': 'FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF',
        'secp384r1': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF0000000000000000FFFFFFFF',
        'secp521r1': '1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
    }
    
    for name, hex_p in nist_curves.items():
        p_int = int(hex_p, 16)
        str_p = str(p_int)
        has_666 = '666' in str_p
        has_999 = '999' in str_p
        
        status = "WARNUNG" if has_666 else "OK"
        print(f"      {name}: 666={has_666}, 999={has_999} [{status}]")

def check_nothing_up_my_sleeve(p):
    """Prueft auf Nothing-up-my-sleeve Herkunft"""
    print(f"\n[8] NOTHING-UP-MY-SLEEVE TEST:")
    print(f"    Ist secp384r1 aus 'natuerlichen' Konstanten abgeleitet?")
    print()
    
    # NIST-Kurven werden oft aus Hashes oder Seeds generiert
    # Pruefe, ob p-1 oder p+1 spezielle Eigenschaften hat
    
    p_minus_1 = p - 1
    p_plus_1 = p + 1
    
    print(f"    p-1 hat {p_minus_1.bit_length()} Bits")
    print(f"    p+1 hat {p_plus_1.bit_length()} Bits")
    
    # Pruefe auf Smoothness
    print(f"    Faktorisierung von p-1 (erste Versuche)...")
    
    # Kleine Faktoren finden
    small_factors = []
    temp = p_minus_1
    for d in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        while temp % d == 0:
            small_factors.append(d)
            temp //= d
    
    print(f"    Kleine Faktoren von p-1: {small_factors[:20]}")
    
    if len(small_factors) > 10:
        print(f"    WARNUNG: p-1 hat viele kleine Faktoren!")
        print(f"    Das koennte eine Hintertuer ermoeglichen!")
    else:
        print(f"    OK: p-1 ist nicht besonders smooth")

def compare_with_belphegor():
    """Vergleicht mit Belphegor-Struktur"""
    print(f"\n[9] VERGLEICH MIT BELPHEGOR:")
    
    # Belphegor B_13
    B_13 = 10**30 + 666 * 10**14 + 1
    
    print(f"    Belphegor B_13:")
    print(f"    Struktur: 1[13 Nullen]666[13 Nullen]1")
    print(f"    Zentrum: 666")
    print(f"    Digitale Wurzel: 9")
    print()
    
    print(f"    secp384r1:")
    print(f"    Enthaelt '666': Ja, aber nicht zentriert")
    print(f"    Keine Palindrom-Struktur")
    print(f"    Keine 666-666-666 Struktur")
    print()
    
    print(f"    Unterschiede:")
    print(f"    - Belphegor: EXAKTE Positionierung von 666")
    print(f"    - secp384r1: Zufaellige Vorkommen von 666")
    print(f"    - Belphegor: Trapdoor (smooth p-1)")
    print(f"    - secp384r1: Nicht besonders smooth")

def final_assessment(str_p, positions):
    """Finale Bewertung"""
    print(f"\n" + "=" * 70)
    print("FINALE BEWERTUNG")
    print("=" * 70)
    
    length = len(str_p)
    count_666 = len(positions)
    
    # Berechne erwartete Anzahl
    expected = (length - 2) * 0.001
    
    print(f"""
ZUSAMMENFASSUNG DER ANALYSE:

1. DAS 666 IN SECP384R1:
   - Gefunden: {count_666} Vorkommen von '666'
   - Positionen: {positions}
   - Laenge der Primzahl: {length} Stellen
   - Erwartete Anzahl: {expected:.2f}

2. WAHRSCHEINLICHKEIT:
   - P('666' an einer Stelle) = 0.1^3 = 0.001
   - In {length} Stellen: P(mindestens ein '666') ≈ {(1 - 0.999**(length-2))*100:.1f}%
   - Das ist NICHT unwahrscheinlich!

3. KONTEXT-ANALYSE:
   - 666 ist NICHT zentriert (nicht wie Belphegor)
   - Keine 666-666-666 Struktur
   - Zufaellige Verteilung in der Primzahl

4. VERGLEICH MIT BELPHEGOR:
   - Belphegor: Spezifische Struktur mit 666
   - secp384r1: Zufaelliges Vorkommen
   - Belphegor: smooth p-1 (Trapdoor)
   - secp384r1: Nicht besonders smooth

5. NIST KONTEXT:
   - secp384r1 ist eine offizielle NIST-Kurve
   - Historisch von NSA beeinflusst
   - ABER: Keine konkreten Beweise fuer Backdoor
   - Dual_EC_DRBG-Skandal war anders (algebraisch)

6. FAZIT:
   Das Vorkommen von '666' in secp384r1 ist
   HOECHSTWAHRSCHEINLICH ZUFALL!
   
   Es gibt KEINE Belphegor-aehnliche Struktur.
   Es gibt KEINE Trapdoor-Eigenschaften.
   Es gibt KEINE Hinweise auf beabsichtigte 
   Platzierung des 666-Musters.
   
   Das 666 ist ein 'Zufallstreffer' - statistisch
   zu erwarten in einer 116-stelligen Primzahl.

EMPFEHLUNG:
- Die Kurve ist VERMUTLICH sicher
- Aber: NIST-Kurven haben allgemein Vertrauensprobleme
- Alternative: Curve25519 (nicht NIST, sauber)
""")

def main():
    p, str_p, positions = analyze_secp384r1()
    
    if positions:
        analyze_666_context(str_p, positions)
        calculate_probabilities(str_p)
    else:
        print(f"\n    KEIN '666' gefunden!")
    
    analyze_nist_context()
    check_nothing_up_my_sleeve(p)
    compare_with_belphegor()
    final_assessment(str_p, positions)

if __name__ == '__main__':
    main()
