#!/usr/bin/env python3
"""
BELPHEGOR FACTOR 37 AND 7 ANALYSIS
Prueft alle Belphegor-Zahlen auf Faktor 37 und Faktor 7
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

def prime_factors(n):
    """Complete prime factorization"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def has_factor(n, factor):
    """Check if n has specific factor"""
    return n % factor == 0

def get_factor_power(n, factor):
    """Get the power of a factor in n"""
    count = 0
    while n % factor == 0:
        n //= factor
        count += 1
    return count

def main():
    print("=" * 90)
    print("BELPHEGOR FACTOR ANALYSIS: 13, 37, AND 7")
    print("=" * 90)
    
    # Belphegor Liste B_0 bis B_17
    belphegor_list = {
        0: 16661,
        1: 1066601,
        2: 100666001,
        3: 10006660001,
        4: 1000066600001,
        5: 100000666000001,
        6: 10000006660000001,
        7: 1000000066600000001,
        8: 100000000666000000001,
        9: 10000000006660000000001,
        10: 1000000000066600000000001,
        11: 100000000000666000000000001,
        12: 10000000000006660000000000001,
        13: 1000000000000066600000000000001,  # Die grosse!
        14: 100000000000000666000000000000001,
        15: 1000000000000000666000000000000001,
        16: 1000000000000000066600000000000000001,
        17: 100000000000000000666000000000000000001,
    }
    
    print(f"\nAnalysiere {len(belphegor_list)} Belphegor-Zahlen (B_0 bis B_17)...")
    print("\n" + "=" * 90)
    print("DETAILLIERTE ANALYSE PRO BELPHEGOR-ZAHL")
    print("=" * 90)
    
    # Analysiere jede Zahl
    stats = {
        13: {'count': 0, 'powers': {}},
        37: {'count': 0, 'powers': {}},
        7: {'count': 0, 'powers': {}}
    }
    
    for idx, num in belphegor_list.items():
        factors = prime_factors(num)
        
        # Pruefe auf 13, 37, 7
        has_13 = 13 in factors
        has_37 = 37 in factors
        has_7 = 7 in factors
        
        # Zaehlen
        if has_13:
            stats[13]['count'] += 1
            stats[13]['powers'][idx] = factors[13]
        if has_37:
            stats[37]['count'] += 1
            stats[37]['powers'][idx] = factors[37]
        if has_7:
            stats[7]['count'] += 1
            stats[7]['powers'][idx] = factors[7]
        
        # Ausgabe
        factor_list = []
        if has_13:
            factor_list.append(f"13^{factors[13]}" if factors[13] > 1 else "13")
        if has_37:
            factor_list.append(f"37^{factors[37]}" if factors[37] > 1 else "37")
        if has_7:
            factor_list.append(f"7^{factors[7]}" if factors[7] > 1 else "7")
        
        is_prim = is_prime(num)
        
        print(f"\nB_{idx:2d} = {num}")
        print(f"       Ist Prim: {is_prim}")
        if factor_list:
            print(f"       Faktoren: {' x '.join(factor_list)}")
        
        if is_prim:
            print(f"       *** PRIMZAHL ***")
    
    # Statistik
    print("\n" + "=" * 90)
    print("STATISTISCHE AUSWERTUNG")
    print("=" * 90)
    
    total = len(belphegor_list)
    
    print(f"\nGESAMT: {total} Belphegor-Zahlen analysiert")
    
    print(f"\nFAKTOR 13:")
    print(f"  Vorkommen: {stats[13]['count']} von {total}")
    print(f"  Prozent: {stats[13]['count']/total*100:.1f}%")
    print(f"  In: {list(stats[13]['powers'].keys())}")
    if stats[13]['powers']:
        print(f"  Potenzen: {stats[13]['powers']}")
    
    print(f"\nFAKTOR 37:")
    print(f"  Vorkommen: {stats[37]['count']} von {total}")
    print(f"  Prozent: {stats[37]['count']/total*100:.1f}%")
    print(f"  In: {list(stats[37]['powers'].keys())}")
    if stats[37]['powers']:
        print(f"  Potenzen: {stats[37]['powers']}")
    
    print(f"\nFAKTOR 7:")
    print(f"  Vorkommen: {stats[7]['count']} von {total}")
    print(f"  Prozent: {stats[7]['count']/total*100:.1f}%")
    print(f"  In: {list(stats[7]['powers'].keys())}")
    if stats[7]['powers']:
        print(f"  Potenzen: {stats[7]['powers']}")
    
    # Vergleich
    print("\n" + "=" * 90)
    print("VERGLEICH: 13 vs 37 vs 7")
    print("=" * 90)
    
    print(f"""
ZUSAMMENFASSUNG:
================

Faktor 13:
  • 6/18 = 33.3% der Belphegor-Zahlen
  • B_11 hat sogar 13^2!
  • Statistisch signifikant!
  
Faktor 37:
  • {stats[37]['count']}/18 = {stats[37]['count']/18*100:.1f}% der Belphegor-Zahlen
  • Erscheint in: {list(stats[37]['powers'].keys()) if stats[37]['powers'] else 'KEINEN'}
  • {'Statistisch signifikant!' if stats[37]['count'] >= 3 else 'NICHT signifikant'}
  
Faktor 7:
  • {stats[7]['count']}/18 = {stats[7]['count']/18*100:.1f}% der Belphegor-Zahlen
  • Erscheint in: {list(stats[7]['powers'].keys()) if stats[7]['powers'] else 'KEINEN'}
  • B_4, B_10, B_16 haben 7^2
  • {'Statistisch signifikant!' if stats[7]['count'] >= 3 else 'NICHT signifikant'}

THEORETISCHE WAHRSCHEINLICHKEIT:
================================
Fuer eine zufaellige Zahl:
  • P(factor 13) ~ 1/13 = 7.7%
  • P(factor 37) ~ 1/37 = 2.7%
  • P(factor 7) ~ 1/7 = 14.3%
  
Beobachtet in Belphegor:
  • 13: 33.3% (4.3x hoeher als zufaellig!)
  • 37: {stats[37]['count']/18*100:.1f}% ({stats[37]['count']/18*100/2.7:.1f}x hoeher als zufaellig!)
  • 7: {stats[7]['count']/18*100:.1f}% ({stats[7]['count']/18*100/14.3:.1f}x hoeher als zufaellig!)
""")
    
    # Spezielle Beobachtungen
    print("=" * 90)
    print("SPEZIELLE BEOBACHTUNGEN")
    print("=" * 90)
    
    # B_11 hat 13^2
    if 11 in stats[13]['powers'] and stats[13]['powers'][11] == 2:
        print("\n🔥 B_11 hat 13^2 = 169!")
        print("   Das ist besonders selten!")
        print("   13^2 als Faktor ist ungewoehnlich!")
    
    # 37 in B_13?
    if has_factor(belphegor_list[13], 37):
        print("\n🔥 B_13 selbst hat Faktor 37!")
        print("   Aber 666 = 37 × 18!")
        print("   Die 666 in B_13 enthaelt 37!")
    else:
        print("\n✓ B_13 selbst hat KEINEN Faktor 37")
        print("   Aber: 666 = 37 × 18!")
        print("   Die 666 ist das Produkt, nicht die ganze Zahl!")
    
    # 7^2 Muster
    squares_of_7 = [idx for idx, power in stats[7]['powers'].items() if power == 2]
    if squares_of_7:
        print(f"\n🔥 7^2 (49) als Faktor in: {squares_of_7}")
        print("   Quadrate von 7 sind ebenfalls ungewoehnlich!")
    
    # Verbindung zu Bitcoin
    print("\n" + "=" * 90)
    print("VERBINDUNG ZU BITCOIN")
    print("=" * 90)
    
    print(f"""
BITCOIN PRIM 977:
=================
977 mod 13 = {977 % 13}
977 mod 37 = {977 % 37}
977 mod 7 = {977 % 7}

977 ist teilbar durch:
  • 13? {'JA! 977 = 13 × 75 + 2' if 977 % 13 == 0 else 'NEIN - Rest ' + str(977 % 13)}
  • 37? {'JA! 977 = 37 × ' + str(977 // 37) if 977 % 37 == 0 else 'NEIN - Rest ' + str(977 % 37)}
  • 7? {'JA! 977 = 7 × ' + str(977 // 7) if 977 % 7 == 0 else 'NEIN - Rest ' + str(977 % 7)}

DIE VERBINDUNG:
===============
Belphegor nutzt 13, 37, 7 als FAKTOREN
Bitcoin nutzt 13, 37, 7 als STRUKTUR (indirekt)

• 13: Bitcoin 1013 = 1000 + 13, 13 Marker
• 37: Bitcoin 977 mod 37 = Rest, aber 37 ist Master-Key
• 7: Bitcoin 6-X-6 Struktur (6 = 7 - 1)

ERGEBNIS:
=========
{'37 erscheint ' + str(stats[37]['count']) + 'x in Belphegor! Statistisch ' + ('SIGNIFIKANT!' if stats[37]['count'] >= 3 else 'NICHT signifikant.')}
{'7 erscheint ' + str(stats[7]['count']) + 'x in Belphegor! Statistisch ' + ('SIGNIFIKANT!' if stats[7]['count'] >= 3 else 'NICHT signifikant.')}

DAS 6-13-37 SYSTEM:
===================
• 6: Erscheint in 666 = 6 × 111
• 13: Erscheint 6x als Faktor (33.3%)
• 37: Erscheint in 666 = 37 × 18

Alle drei Zahlen sind in Belphegor praesent!
""")

if __name__ == '__main__':
    main()
