#!/usr/bin/env python3
"""
VERIFY SECP384R1 - Prueft das 666-Muster nach
"""

import math

# secp384r1 Primzahl - korrekter Wert aus NIST SP 800-186
# p = 2^384 - 2^128 - 2^96 + 2^32 - 1
# Alternative: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF0000000000000000FFFFFFFF

p_hex_correct = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF0000000000000000FFFFFFFF"
p_correct = int(p_hex_correct, 16)

print("SECP384R1 VERIFIKATION")
print("=" * 60)

print(f"\nHex: {p_hex_correct}")
print(f"Bits: {p_correct.bit_length()}")

str_p = str(p_correct)
print(f"Dezimal: {str_p}")
print(f"Laenge: {len(str_p)} Stellen")

# Suche nach 666
has_666 = '666' in str_p
positions_666 = []
start = 0
while True:
    pos = str_p.find('666', start)
    if pos == -1:
        break
    positions_666.append(pos)
    start = pos + 1

print(f"\n'666' gefunden: {has_666}")
print(f"Anzahl: {len(positions_666)}")
print(f"Positionen: {positions_666}")

# Zeige Kontext falls gefunden
if positions_666:
    for pos in positions_666:
        context_start = max(0, pos - 15)
        context_end = min(len(str_p), pos + 18)
        context = str_p[context_start:context_end]
        print(f"\nKontext bei Position {pos}:")
        print(f"  ...{context}...")
        print(f"      ^^^")

# Vergleiche mit anderen Kurven
print("\n" + "=" * 60)
print("VERGLEICH: Andere NIST-Kurven")
print("=" * 60)

nist_primes = {
    'secp192r1': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF',
    'secp224r1': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000001',
    'secp256r1': 'FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF',
    'secp384r1': p_hex_correct,
    'secp521r1': '1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',
}

for name, hex_p in nist_primes.items():
    p_int = int(hex_p, 16)
    str_p_check = str(p_int)
    
    count_666 = str_p_check.count('666')
    count_999 = str_p_check.count('999')
    
    status = ""
    if count_666 > 0:
        status = "  <--- 666 gefunden!"
    elif count_999 > 0:
        status = "  <--- 999 gefunden!"
    
    print(f"{name}: 666={count_666}, 999={count_999}{status}")

print("\n" + "=" * 60)
print("FAZIT:")
print("=" * 60)

if positions_666:
    print("666 IST in secp384r1 enthalten!")
    print("Dies muss genauer untersucht werden.")
else:
    print("KEIN 666 in secp384r1 gefunden!")
    print("Der vorherige Scan war moeglicherweise falsch.")
    print("ODER: Verschiedene Hex-Darstellungen der Kurve.")
