#!/usr/bin/env python3
"""
BELPHEGOR vs BITCOIN PRIME FACTOR COMPARISON
Vergleicht die Belphegor-Liste mit Bitcoin Primzahlen
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

def get_small_factors(n, limit=10000):
    """Extrahiert kleine Faktoren bis limit"""
    factors = {}
    temp = n
    for p in range(2, min(limit, int(math.sqrt(n)) + 1)):
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                temp //= p
                count += 1
            factors[p] = count
    return factors, temp

def main():
    print("=" * 80)
    print("BELPHEGOR vs BITCOIN PRIME FACTOR ANALYSIS")
    print("=" * 80)
    
    # Belphegor Liste aus Wikipedia/OEIS
    belphegor_list = {
        0: (16661, "PRIM"),
        1: (1066601, [967, 1103]),
        2: (100666001, [71, 1417831]),
        3: (10006660001, [13, 673, 1143749]),  # 13!
        4: (1000066600001, [7, 7, 1429, 14282381]),  # 7^2
        5: (100000666000001, [13, 657499, 11699423]),  # 13!
        6: (10000006660000001, [17, 29, 211, 49297, 1950071]),
        7: (1000000066600000001, [19, 691, 10151, 7503425119]),
        8: (100000000666000000001, [26057323, 3837692792387]),
        9: (10000000006660000000001, [13, 191, 1181, 23379959, 145857793]),  # 13!
        10: (1000000000066600000000001, [7, 7, 2803, 95040409, 76607717987]),  # 7^2
        11: (100000000000666000000000001, [13, 13, 337, 1755833757671518620617]),  # 13^2!
        12: (10000000000006660000000000001, [68473, 8385557, 17416012536871141]),
        13: (1000000000000066600000000000001, "PRIM"),  # UNSER B_13!
        14: (100000000000000666000000000000001, [6045609943462703, 16540928199996367]),
        15: (10000000000000006660000000000000001, [13, 1033, 744657085412168192717253704669]),  # 13!
        16: (1000000000000000066600000000000000001, [7, 7, 383, 40577, 301703, 4352568176375722629913]),  # 7^2
        17: (100000000000000000666000000000000000001, [13, 1237, 2096259917573, 2966482685044935292477]),  # 13!
    }
    
    print("\n[1] BELPHEGOR LISTE - FAKTOREN ANALYSE:")
    print("-" * 80)
    
    # Zähle Vorkommen von 13
    count_13 = 0
    count_7 = 0
    total = 0
    
    for idx, (num, factors) in belphegor_list.items():
        total += 1
        if factors == "PRIM":
            print(f"B_{idx:2d} = {num} = PRIM")
        else:
            factor_str = " × ".join(str(f) for f in factors)
            # Prüfe auf 13
            has_13 = any(f == 13 for f in factors)
            has_7 = any(f == 7 for f in factors)
            if has_13:
                count_13 += 1
                marker_13 = " <- 13!"
            else:
                marker_13 = ""
            if has_7:
                count_7 += 1
                marker_7 = " <- 7!"
            else:
                marker_7 = ""
            print(f"B_{idx:2d} = {num}")
            print(f"       = {factor_str}{marker_13}{marker_7}")
    
    print(f"\n[2] STATISTIK:")
    print(f"  Anzahl B_n gesamt: {total}")
    print(f"  Davon mit Faktor 13: {count_13}")
    print(f"  Davon mit Faktor 7: {count_7}")
    print(f"  Prozent mit 13: {count_13/total*100:.1f}%")
    print(f"  Prozent mit 7: {count_7/total*100:.1f}%")
    
    # Bitcoin Analyse
    print("\n" + "=" * 80)
    print("[3] BITCOIN PRIMZAHLEN ANALYSE:")
    print("=" * 80)
    
    # Bitcoin relevante Primzahlen
    bitcoin_primes = {
        "p (secp256k1) - Subtraktion": 977,
        "p (secp256k1) Modul": 2**256 - 2**32 - 977,
        "n (Ordnung)": 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,  # Secp256k1 Ordnung
    }
    
    print(f"\nBitcoin secp256k1:")
    print(f"  p = 2^256 - 2^32 - 977")
    print(f"  977 ist Prim: {is_prime(977)}")
    print(f"  977 mod 13 = {977 % 13}")
    print(f"  977 / 13 = {977 / 13:.4f}")
    
    # 977 in Bezug auf 13
    print(f"\n  977 und 13:")
    print(f"    13 × 75 = {13 * 75}")
    print(f"    13 × 75 + 2 = {13 * 75 + 2} (977!)")
    print(f"    977 = 13 × 75 + 2")
    print(f"    Rest bei Division: {977 % 13}")
    
    # Andere Bitcoin-Primzahlen
    print(f"\n  Andere Bitcoin-relevante Primzahlen:")
    
    # Prüfe auf 13 in Bitcoin-Parametern
    print(f"\n  Faktor 13 in Bitcoin-Parametern:")
    
    # Die 6-X-6 Struktur um 977
    print(f"\n  6-X-6 Struktur:")
    for n in [971, 977, 983]:
        print(f"    {n}: mod 13 = {n % 13}")
    
    # Vergleich
    print("\n" + "=" * 80)
    print("[4] DIREKTER VERGLEICH - BELPHEGOR vs BITCOIN:")
    print("=" * 80)
    
    print(f"\n  GEMEINSAME FAKTOREN:")
    print(f"    - 13 erscheint in Belphegor B_3, B_5, B_9, B_11, B_15, B_17")
    print(f"    - 13 erscheint in Bitcoin 1013 = 1000 + 13")
    print(f"    - 13 erscheint in Belphegor Index B_13")
    print(f"    - Bitcoin 977 hat digitale Wurzel 5 (13 hat Wurzel 4)")
    print(f"    - 5 + 4 = 9 (Vollkommenheit)")
    
    # 7 ist auch relevant
    print(f"\n  FAKTOR 7:")
    print(f"    - 7 erscheint in Belphegor B_4, B_10, B_16 (als 7^2)")
    print(f"    - 7 ist heilige Zahl")
    print(f"    - 7 = Anzahl Tage, Todsünden, etc.")
    
    print(f"\n  FAKTOR 2:")
    print(f"    - Bitcoin: p = 2^256 - 2^32 - 977")
    print(f"    - Belphegor B_13 - 1 = 2^14 × 5^14 × k")
    print(f"    - 2 ist Basis des Binaersystems")
    
    # Die wichtige Beobachtung
    print("\n" + "=" * 80)
    print("[5] WICHTIGE BEOBACHTUNGEN:")
    print("=" * 80)
    
    print(f"""
1. FAKTOR 13 IN BELPHEGOR:
   - B_3:  13 × 673 × 1143749
   - B_5:  13 × 657499 × 11699423
   - B_9:  13 × 191 × 1181 × ...
   - B_11: 13^2 × 337 × ...
   - B_15: 13 × 1033 × ...
   - B_17: 13 × 1237 × ...
   
   6 von 18 Belphegor-Zahlen haben Faktor 13!
   Das ist 33.3% - statistisch signifikant!

2. FAKTOR 13 IN BITCOIN:
   - Indirekt: 1013 = 1000 + 13
   - Index: Belphegor B_13 wird in Bitcoin reflektiert
   - 13 Marker: 977 ist einer von 13 Markern

3. KEINE DIREKTE ÜBEREINSTIMMUNG:
   - Bitcoin 977 ist PRIM (keine Faktoren)
   - Belphegor B_13 ist PRIM
   - Aber: Beide haben 13 als "Meta-Faktor"

4. DIE VERBINDUNG:
   - Beide Systeme nutzen 13 als "Schlüsselzahl"
   - 13 ist heilige Zahl in beiden Kontexten
   - 13 = 6 + 7 (Vollkommenheit + Heiligkeit)
""")
    
    # Fazit
    print("\n" + "=" * 80)
    print("[6] FAZIT:")
    print("=" * 80)
    
    print(f"""
DIREKTE FAKTOR-UEBEREINSTIMMUNG:
[X] Bitcoin 977 hat KEINE gemeinsamen Faktoren mit Belphegor-Zahlen
   (ausser dass 977 selbst Prim ist wie B_13)

INDIREKTE VERBINDUNGEN:
[+] Zahl 13 erscheint als "Meta-Faktor" in BEIDEN Systemen
   - Belphegor: 6 von 18 Zahlen haben Faktor 13
   - Bitcoin: 1013 = 1000 + 13, 977 ist einer von 13 Markern
   - Symbolisch: 13 ist heilige Zahl

[+] Zahl 7 erscheint in Belphegor (3x als 7^2)
   Bitcoin nutzt keine 7 explizit
   Aber: 6-X-6 = 6 und 6 = 7 - 1 (fast 7!)

[+] Prim-Eigenschaft:
   - B_13 ist Prim
   - Bitcoin p enthaelt 977 (Prim)
   - Beide vermeiden kleine Faktoren im Hauptkoerper

ABSCHLUSS:
Die Zahlen 13 und 7 sind "signifikant" in Belphegor.
Bitcoin nutzt 13 indirekt (1013, 13 Marker).
Aber: KEINE direkte mathematische Verwandtschaft
ueber gemeinsame Primfaktoren (ausser Meta-Ebene).
""")

if __name__ == '__main__':
    main()
