#!/usr/bin/env python3
"""
SHA256 CONSTANTS VERIFIER - Clean Version
Verifiziert H0-H7 aus Wurzeln der ersten 8 Primzahlen
"""

import math

def get_first_32_bits_of_fractional_part(x):
    """Extrahiert die ersten 32 Bits des gebrochenen Anteils von x"""
    frac = x - int(x)
    bits = int(frac * (2**32))
    return bits & 0xFFFFFFFF

def main():
    print("=" * 70)
    print("SHA256 CONSTANTS VERIFIER")
    print("=" * 70)
    
    # SHA256 Konstanten (erwartet)
    sha256_expected = [
        0x6a09e667,  # H0: sqrt(2)
        0xbb67ae85,  # H1: sqrt(3)
        0x3c6ef372,  # H2: sqrt(5)
        0xa54ff53a,  # H3: sqrt(7)
        0x510e527f,  # H4: sqrt(11)
        0x9b05688c,  # H5: sqrt(13)
        0x1f83d9ab,  # H6: sqrt(17)
        0x5be0cd19,  # H7: sqrt(19)
    ]
    
    # Erste 8 Primzahlen
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    print("\n[1] VERIFIKATION DER H0-H7 KONSTANTEN:")
    print("    (aus Wurzeln der ersten 8 Primzahlen)")
    
    all_match = True
    for i, (expected, prime) in enumerate(zip(sha256_expected, primes)):
        sqrt_val = math.sqrt(prime)
        calculated = get_first_32_bits_of_fractional_part(sqrt_val)
        
        match = (calculated == expected)
        status = "OK" if match else "FEHLER"
        
        print(f"\n    H{i} (Wurzel({prime})):")
        print(f"      Erwartet:  0x{expected:08X}")
        print(f"      Berechnet: 0x{calculated:08X}")
        print(f"      Status:    {status}")
        
        if not match:
            all_match = False
            print(f"      Differenz: {calculated - expected}")
    
    # Detaillierte H0-Verifikation
    print("\n" + "=" * 70)
    print("DETAILLIERTE H0-VERIFIKATION")
    print("=" * 70)
    
    sqrt2 = math.sqrt(2)
    h0 = 0x6a09e667
    
    print(f"\n    Wurzel(2) = {sqrt2}")
    print(f"    Ganzzahliger Teil: {int(sqrt2)}")
    
    frac = sqrt2 - int(sqrt2)
    print(f"    Gebrochener Teil: {frac:.20f}")
    
    scaled = frac * (2**32)
    print(f"\n    Gebrochener Teil * 2^32:")
    print(f"    = {scaled:.10f}")
    
    bits = int(scaled)
    print(f"\n    Erste 32 Bits:")
    print(f"    Dezimal: {bits}")
    print(f"    Hex:     0x{bits:08X}")
    print(f"    Binaer:  {bits:032b}")
    
    print(f"\n    H0 erwartet:  0x{h0:08X}")
    print(f"    H0 binaer:    {h0:032b}")
    print(f"    Uebereinstimmung: {bits == h0}")
    
    # Rundenkonstanten K0-K3 (Kubikwurzeln)
    print("\n" + "=" * 70)
    print("RUNDE-KONSTANTEN K0-K3 (Kubikwurzeln)")
    print("=" * 70)
    
    k_primes = [2, 3, 5, 7]
    k_expected = [
        0x428a2f98,  # K0: cbrt(2)
        0x71374491,  # K1: cbrt(3)
        0xb5c0fbcf,  # K2: cbrt(5)
        0xe9b5dba5,  # K3: cbrt(7)
    ]
    
    for i, (expected, prime) in enumerate(zip(k_expected, k_primes)):
        cbrt_val = prime ** (1/3)
        calculated = get_first_32_bits_of_fractional_part(cbrt_val)
        
        match = (calculated == expected)
        status = "OK" if match else "FEHLER"
        
        print(f"\n    K{i} (3.Wurzel({prime})):")
        print(f"      Erwartet:  0x{expected:08X}")
        print(f"      Berechnet: 0x{calculated:08X}")
        print(f"      Status:    {status}")
    
    # Finale Bewertung
    print("\n" + "=" * 70)
    print("FINALES ERGEBNIS")
    print("=" * 70)
    
    if all_match:
        print("""
VERIFIZIERT: Alle SHA256-Konstanten sind korrekt!

H0-H7 stammen aus den ersten 32 Bits der gebrochenen 
Teile der Quadratwurzeln der ersten 8 Primzahlen:
- H0: Wurzel(2) = 0x6a09e667
- H1: Wurzel(3) = 0xbb67ae85
- H2: Wurzel(5) = 0x3c6ef372
- H3: Wurzel(7) = 0xa54ff53a
- H4: Wurzel(11) = 0x510e527f
- H5: Wurzel(13) = 0x9b05688c
- H6: Wurzel(17) = 0x1f83d9ab
- H7: Wurzel(19) = 0x5be0cd19

K0-K63 stammen aus Kubikwurzeln der ersten 64 Primzahlen.

Dies ist ein klassisches "Nothing-up-my-sleeve" Design!
Die Konstanten sind mathematisch erklaerbar und NICHT
verdaechtig.
""")
    else:
        print("""
PROBLEM: Einige Konstanten konnten nicht verifiziert werden!
Dies sollte genauer untersucht werden.
""")

if __name__ == '__main__':
    main()
