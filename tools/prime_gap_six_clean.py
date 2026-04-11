#!/usr/bin/env python3
"""
PRIME GAP SIX ANALYZER - Clean Version
Untersucht die Sequenz von Primzahlen mit Abstand 6
977 ist Teil einer regelmaessigen Struktur!
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

def find_primes_in_range(start, end):
    """Findet alle Primzahlen in einem Bereich"""
    return [n for n in range(start, end + 1) if is_prime(n)]

def analyze_gap_six_sequence():
    """Analysiert die Primzahl-Sequenz mit Abstand 6"""
    print("=" * 70)
    print("PRIMZAHL-SEQUENZ MIT ABSTAND 6")
    print("=" * 70)
    
    # Bereich um 977
    primes = find_primes_in_range(900, 1020)
    
    print(f"\n[1] PRIMZAHLEN IM BEREICH 900-1020:")
    print(f"    Gefundene Primzahlen: {len(primes)}")
    print(f"    Liste: {primes}")
    
    # Finde alle Paare mit Abstand 6
    print(f"\n[2] PRIMZAHL-PAARE MIT ABSTAND 6 (Sexy Primes):")
    gap_six_pairs = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            diff = primes[j] - primes[i]
            if diff == 6:
                gap_six_pairs.append((primes[i], primes[j]))
    
    for p1, p2 in gap_six_pairs:
        marker = ""
        if p1 == 977 or p2 == 977:
            marker = " <-- 977!"
        print(f"    {p1}, {p2} (Abstand: 6){marker}")

def analyze_977_context():
    """Analysiert den Kontext von 977"""
    print("\n" + "=" * 70)
    print("[3] 977 IM KONTEXT DER SEQUENZ")
    print("=" * 70)
    
    # Die Sequenz um 977
    sequence = [941, 947, 953, 971, 977, 983, 991, 997]
    
    print(f"\n    Sequenz: {sequence}")
    print(f"\n    Analyse der Abstaende:")
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        marker = ""
        if sequence[i] == 977 or sequence[i + 1] == 977:
            marker = " <-- 977 beteiligt!"
        print(f"    {sequence[i]} -> {sequence[i + 1]}: Abstand = {diff}{marker}")
    
    # Pruefe ob alle Abstaende 6 sind
    all_six = all(sequence[i + 1] - sequence[i] == 6 for i in range(len(sequence) - 1))
    print(f"\n    Alle Abstaende sind 6: {all_six}")
    
    if not all_six:
        print(f"    Hinweis: Nicht alle Abstaende sind 6!")
        print(f"    953 -> 971: Abstand = 18 (nicht 6!)")
        print(f"    983 -> 991: Abstand = 8 (nicht 6!)")

def analyze_arithmetic_progression():
    """Prueft auf arithmetische Progression"""
    print("\n" + "=" * 70)
    print("[4] ARITHMETISCHE PROGRESSION ANALYSE")
    print("=" * 70)
    
    # Zwei getrennte Sequenzen
    seq1 = [941, 947, 953]  # Abstand 6
    seq2 = [971, 977, 983]  # Abstand 6
    seq3 = [991, 997]       # Abstand 6
    
    print(f"\n    Sequenz 1: {seq1}")
    print(f"    Differenzen: {[seq1[i+1] - seq1[i] for i in range(len(seq1)-1)]}")
    print(f"    Start: 941, Schritt: 6, Laenge: 3")
    print(f"    Formel: 941 + 6k fuer k = 0, 1, 2")
    
    print(f"\n    Sequenz 2: {seq2}")
    print(f"    Differenzen: {[seq2[i+1] - seq2[i] for i in range(len(seq2)-1)]}")
    print(f"    Start: 971, Schritt: 6, Laenge: 3")
    print(f"    Formel: 971 + 6k fuer k = 0, 1, 2")
    print(f"    977 = 971 + 6 (Position k=1)")
    
    print(f"\n    Sequenz 3: {seq3}")
    print(f"    Differenzen: {[seq3[i+1] - seq3[i] for i in range(len(seq3)-1)]}")
    print(f"    Start: 991, Schritt: 6, Laenge: 2")
    
    # Modulo-Analyse
    print(f"\n    MODULO 6 ANALYSE:")
    for seq, name in [(seq1, "Seq1"), (seq2, "Seq2"), (seq3, "Seq3")]:
        mods = [p % 6 for p in seq]
        print(f"    {name}: {seq} mod 6 = {mods}")
    
    print(f"\n    Erkenntnis:")
    print(f"    Alle Primzahlen > 3 sind = 1 oder 5 (mod 6)")
    print(f"    Primzahlen mit Abstand 6 haben gleichen Rest mod 6!")
    print(f"    977 mod 6 = {977 % 6}")
    print(f"    941 mod 6 = {941 % 6}")
    print(f"    947 mod 6 = {947 % 6}")

def analyze_977_special():
    """Analysiert was 977 besonders macht"""
    print("\n" + "=" * 70)
    print("[5] WAS MACHT 977 BESONDERS?")
    print("=" * 70)
    
    print(f"\n    977 ist eine Primzahl:")
    print(f"    is_prime(977) = {is_prime(977)}")
    
    print(f"\n    977 in verschiedenen Basen:")
    print(f"    Binaer: {bin(977)}")
    print(f"    Hex: {hex(977)}")
    print(f"    Oktal: {oct(977)}")
    
    print(f"\n    977 als Summe:")
    print(f"    977 = 900 + 77")
    print(f"    977 = 1000 - 23")
    print(f"    977 = 941 + 36 = 941 + 6^2")
    
    print(f"\n    977 und 6:")
    print(f"    977 / 6 = {977/6:.4f}")
    print(f"    977 mod 6 = {977 % 6}")
    print(f"    977 = 6 * {977//6} + {977%6}")
    
    print(f"\n    977 in der arithmetischen Sequenz:")
    print(f"    977 = 971 + 6")
    print(f"    977 = 983 - 6")
    print(f"    977 ist die MITTE der Sequenz [971, 977, 983]")
    
    # Digital root
    dr = 977
    while dr >= 10:
        dr = sum(int(d) for d in str(dr))
    print(f"\n    Digitale Wurzel von 977: {dr}")
    
    # Verbindung zu Bitcoin
    print(f"\n    VERBINDUNG ZU BITCOIN secp256k1:")
    print(f"    p = 2^256 - 2^32 - 977")
    print(f"    Die Konstante 977 ist eine Primzahl")
    print(f"    977 ist Teil einer regelmaessigen Primzahl-Sequenz")
    print(f"    Dies koennte ein Hinweis auf 'effiziente' Primzahlauswahl sein")

def check_bitcoin_curve_relation():
    """Prueft Verbindung zur Bitcoin-Kurve"""
    print("\n" + "=" * 70)
    print("[6] VERBINDUNG ZUR BITCOIN-KURVE")
    print("=" * 70)
    
    print(f"\n    Bitcoin secp256k1:")
    print(f"    p = 2^256 - 2^32 - 977")
    print(f"\n    Warum 977?")
    print(f"    - 977 ist eine Primzahl")
    print(f"    - 977 liegt in einer Sequenz mit Abstand 6")
    print(f"    - Dies erleichtert die modulare Reduktion")
    print(f"\n    Alternative Hypothese:")
    print(f"    - 977 war der erste Wert, der eine 'schoene' Primzahl ergab")
    print(f"    - 'Schoen' = einfache Berechnung, gute Eigenschaften")
    
    # Teste benachbarte Werte
    print(f"\n    Teste benachbarte Werte zu 977:")
    for offset in [-6, -2, 0, 2, 6]:
        val = 977 + offset
        status = "Prim" if is_prime(val) else "Nicht prim"
        marker = " <-- 977!" if offset == 0 else ""
        print(f"    977 + ({offset:3d}) = {val}: {status}{marker}")

def final_assessment():
    """Finale Bewertung"""
    print("\n" + "=" * 70)
    print("FINALE BEWERTUNG")
    print("=" * 70)
    
    print("""
ZUSAMMENFASSUNG DER ENTDECKUNG:

1. DIE SEQUENZ:
   941, 947, 953 (Abstand 6) - 3 Primzahlen
   971, 977, 983 (Abstand 6) - 3 Primzahlen  <-- 977 IST HIER!
   991, 997 (Abstand 6)     - 2 Primzahlen

2. 977 IST BESONDERS:
   - 977 ist die MITTE der Sequenz [971, 977, 983]
   - 977 = 971 + 6 = 983 - 6
   - Alle drei sind = 5 (mod 6)

3. MATHEMATISCHE STRUKTUR:
   Primzahlen mit Abstand 6 haben gleichen Rest mod 6
   (alle = 5 mod 6 oder alle = 1 mod 6)
   
   Diese Sequenzen sind arithmetische Progressionen
   mit gemeinsamer Differenz 6.

4. VERBINDUNG ZU BITCOIN:
   Die Wahl von 977 in secp256k1 koennte sein:
   a) Zufall (erster Wert, der eine gute Kurve ergab)
   b) Effizienz (977 hat 'schoene' Eigenschaften)
   c) Teil einer mathematischen Struktur

5. BEWERTUNG:
   Die Sequenz ist NATUERLICH - Primzahlen mit Abstand 6
   sind statistisch erwartbar.
   
   Aber: Die Tatsache, dass 977 in einer REGELMAESSIGEN
   Sequenz liegt, macht es zu einer attraktiven Wahl
   fuer kryptographische Parameter (einfache Berechnung).

FAZIT:
977 ist Teil einer natuerlichen Primzahl-Sequenz mit
Abstand 6. Dies erklaert moeglicherweise die Wahl von 977
in Bitcoins secp256k1 - nicht als Backdoor, sondern als
effiziente, mathematisch 'schoene' Konstante.
""")

def main():
    analyze_gap_six_sequence()
    analyze_977_context()
    analyze_arithmetic_progression()
    analyze_977_special()
    check_bitcoin_curve_relation()
    final_assessment()

if __name__ == '__main__':
    main()
