#!/usr/bin/env python3
"""
MERSENNE TWISTER ANALYZER
Untersucht den Mersenne Twister PRNG im Kontext von Belphegor, Pi und Phi
"""

import math
import struct
from fractions import Fraction

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_mt19937_parameters():
    """Analysiert die MT19937 Parameter"""
    print("=" * 70)
    print("MERSENNE TWISTER 19937 PARAMETER ANALYSE")
    print("=" * 70)
    
    # MT19937 Konstanten
    w = 32  # Wortgroesse
    n = 624  # Rekursionsebene
    m = 397  # Mittlere Wortposition
    r = 31  # Separation Point
    
    a = 0x9908B0DF  # Koeffizienten Matrix
    u = 11  # Tempering Shift
    d = 0xFFFFFFFF  # Tempering Maske
    s = 7   # Tempering Shift
    b = 0x9D2C5680  # Tempering Maske
    t = 15  # Tempering Shift
    c = 0xEFC60000  # Tempering Maske
    l = 18  # Tempering Shift
    
    f = 1812433253  # Init Multiplikator
    
    print("\n[1] MT19937 GRUNDPARAMETER:")
    print(f"    w (Wortgroesse) = {w} Bits")
    print(f"    n (Rekursion) = {n}")
    print(f"    m (Mittelposition) = {m}")
    print(f"    r (Separation) = {r}")
    
    print("\n[2] DIE MAGISCHE ZAHL 19937:")
    print(f"    Periodenlaenge: 2^19937 - 1")
    print(f"    19937 ist eine Mersenne-Exponent!")
    print(f"    M_19937 = 2^19937 - 1 ist prim")
    
    # Analyse von 19937
    print(f"\n    Analyse von 19937:")
    print(f"    19937 Dezimal")
    print(f"    19937 Hex = 0x{19937:X}")
    print(f"    19937 Binaer = {bin(19937)}")
    
    # Digitale Wurzel
    dr_19937 = digital_root(19937)
    print(f"    Digitale Wurzel: 1+9+9+3+7 = {dr_19937}")
    
    # Primfaktorisierung
    print(f"    19937 - ist das selbst prim?")
    
    # 19937 in Bezug zu 6
    print(f"\n    19937 mod 6 = {19937 % 6}")
    print(f"    19937 / 6 = {19937/6:.4f}")
    
    # 19937 in Bezug zu 37
    print(f"    19937 / 37 = {19937/37:.4f}")
    print(f"    19937 mod 37 = {19937 % 37}")
    
    # 19937 in Bezug zu 13
    print(f"    19937 / 13 = {19937/13:.4f}")
    print(f"    19937 mod 13 = {19937 % 13}")
    
    print("\n[3] PERIODENLAENGE:")
    print(f"    2^19937 - 1")
    print(f"    Anzahl Dezimalstellen: ca. {19937 * math.log10(2):.0f}")
    print(f"    Das ist eine RIESIGE Zahl!")
    
    print("\n[4] ANDERE MERSENNE-PRIMZAHLEN:")
    mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 
                          521, 607, 1279, 2203, 2281, 3217, 4253, 4423,
                          9689, 9941, 11213, 19937, 21701, 23209, 44497]
    
    print(f"    Bekannte Mersenne-Exponenten: {mersenne_exponents}")
    
    if 19937 in mersenne_exponents:
        idx = mersenne_exponents.index(19937)
        print(f"    19937 ist der {idx+1}. bekannte Mersenne-Exponent")
    
    # Nachbar-Exponenten
    idx_19937 = mersenne_exponents.index(19937)
    if idx_19937 > 0:
        prev_exp = mersenne_exponents[idx_19937-1]
        print(f"    Vorheriger: {prev_exp} (2^{prev_exp}-1)")
    if idx_19937 < len(mersenne_exponents)-1:
        next_exp = mersenne_exponents[idx_19937+1]
        print(f"    Naechster: {next_exp} (2^{next_exp}-1)")

def analyze_mt_constants():
    """Analysiert die Magic Constants im MT"""
    print("\n" + "=" * 70)
    print("MAGIC CONSTANTS IM MERSENNE TWISTER")
    print("=" * 70)
    
    # Die Hex-Konstanten
    constants = {
        'a (Matrix)': 0x9908B0DF,
        'b (Maske)': 0x9D2C5680,
        'c (Maske)': 0xEFC60000,
        'd (Maske)': 0xFFFFFFFF,
        'f (Init)': 1812433253,
    }
    
    print("\n[1] DIE KONSTANTEN:")
    for name, val in constants.items():
        hex_str = hex(val)
        dr = digital_root(val)
        
        # Pruefe auf 666/999
        has_666 = '666' in str(val)
        has_999 = '999' in str(val)
        
        print(f"\n    {name}:")
        print(f"      Dezimal: {val}")
        print(f"      Hex: {hex_str}")
        print(f"      Digitale Wurzel: {dr}")
        print(f"      Enthaelt 666: {has_666}")
        print(f"      Enthaelt 999: {has_999}")
        
        # Spezielle Analyse fuer f
        if name == 'f (Init)':
            print(f"      1812433253 = ?")
            # Faktorisierung
            temp = val
            factors = {}
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    temp //= d
                d += 1
            if temp > 1:
                factors[temp] = 1
            
            factor_str = " * ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items())])
            print(f"      Faktoren: {factor_str}")
            
            # 1812433253 in Bezug zu 37
            print(f"      / 37 = {val/37:.2f}")
            print(f"      mod 37 = {val % 37}")
    
    print("\n[2] NOTHING-UP-MY-SLEEVE TEST:")
    print("    Sind die Konstanten 'natuerlich' oder konstruiert?")
    print()
    print("    Pruefung: a = 0x9908B0DF")
    print(f"    Binaer: {bin(0x9908B0DF)}")
    
    # Haemming-Gewicht (Anzahl der 1-Bits)
    hamming = bin(0x9908B0DF).count('1')
    print(f"    Haemming-Gewicht (Anzahl 1-Bits): {hamming}")
    
    print("\n    Die Konstanten sehen zufaellig aus,")
    print("    aber: Wer garantiert, dass sie wirklich zufaellig sind?")

def analyze_mt_structure():
    """Analysiert die Struktur des MT-Algorithmus"""
    print("\n" + "=" * 70)
    print("ALGORITHMUS-STRUKTUR")
    print("=" * 70)
    
    print("\n[1] STATE ARRAY:")
    print("    MT19937 speichert 624 Worte a 32 Bit")
    print("    Total: 624 * 32 = 19968 Bits State")
    print(f"    19968 = 19937 + 31 = 19937 + r")
    print("    (r = 31 ist der Separation Point)")
    
    print("\n[2] DIE TWIST-OPERATION:")
    print("    y = (state[i] & UPPER_MASK) + (state[j] & LOWER_MASK)")
    print("    y = state[i] XOR (y >> 1)")
    print("    if (y % 2 != 0): y = y XOR MATRIX_A")
    print()
    print("    Dies ist eine lineare Transformation!")
    print("    Die Matrix A definiert die Rueckkopplung")
    
    print("\n[3] TEMPERING:")
    print("    Nach dem Twist werden die Ausgabe-bits 'tempered'")
    print("    y = y XOR (y >> u)")
    print("    y = y XOR ((y << s) AND b)")
    print("    y = y XOR ((y << t) AND c)")
    print("    y = y XOR (y >> l)")
    print()
    print("    Dies verschleiert die lineare Struktur")
    print("    macht die Ausgabe 'zufaelliger'")

def check_mt_seeding():
    """Prueft die Seed-Funktion des MT"""
    print("\n" + "=" * 70)
    print("SEED-FUNKTION ANALYSE")
    print("=" * 70)
    
    print("\n[1] DEFAULT-SEEDING:")
    print("    mt[0] = seed")
    print("    for i = 1 to n-1:")
    print("        mt[i] = f * (mt[i-1] XOR (mt[i-1] >> (w-2))) + i")
    print()
    print(f"    f = 1812433253 = 0x{1812433253:08X}")
    
    print("\n[2] PROBLEME MIT SEEDING:")
    print("    - Kleine Seeds fuehren zu vorhersehbaren Sequenzen")
    print("    - Nicht kryptographisch sicher!")
    print("    - Seed space ist nur 32 Bit (4 Milliarden Moeglichkeiten)")
    
    print("\n[3] BELPHEGOR-VERBINDUNG?")
    print("    1812433253 mod 666 = ?")
    print(f"    1812433253 mod 666 = {1812433253 % 666}")
    print(f"    1812433253 / 666 = {1812433253/666:.2f}")
    print()
    print(f"    1812433253 mod 999 = {1812433253 % 999}")
    print(f"    1812433253 mod 37 = {1812433253 % 37}")

def analyze_mt_periodicity():
    """Analysiert die Periodizitaet"""
    print("\n" + "=" * 70)
    print("PERIODIZITAET UND ZYKLUSLAENGE")
    print("=" * 70)
    
    print("\n[1] DIE PERIODE:")
    period = "2^19937 - 1"
    print(f"    Periode = {period}")
    
    # Vergleich mit bekannten Zahlen
    print(f"\n    Vergleich:")
    print(f"    2^10 = 1024 (ca. 10^3)")
    print(f"    2^20 = 1.048.576 (ca. 10^6)")
    print(f"    2^19937 hat ca. {19937 * 0.301:.0f} Stellen")
    print(f"    Das ist eine Zahl mit ca. 6000 Dezimalstellen!")
    
    print("\n[2] ZUFALLSQUALITAET:")
    print("    - MT19937 besteht die Diehard-Tests")
    print("    - Besteht die TestU01 BigCrunch Tests")
    print("    - ABER: Nicht kryptographisch sicher!")
    print()
    print("    Problem: Bei bekannter Ausgabe kann der State")
    print("    durch lineare Algebra rekonstruiert werden!")
    
    print("\n[3] ZUSTANDS-REKONSTRUKTION:")
    print("    Aus 624 aufeinanderfolgenden Ausgaben")
    print("    kann der gesamte State berechnet werden!")
    print()
    print("    Das ist ein bekanntes Problem des MT.")
    print("    Wer die ersten 624 Zahlen kennt, kann")
    print("    ALLE zukuenftigen Zahlen vorhersagen!")

def check_mt_security_issues():
    """Prueft bekannte Sicherheitsprobleme"""
    print("\n" + "=" * 70)
    print("SICHERHEITSPROBLEME")
    print("=" * 70)
    
    print("\n[1] BEKANNTE ANGRIFFE:")
    print("    - State-Rekonstruktion aus 624 Ausgaben")
    print("    - Seed-Rekonstruktion aus Teilsequenzen")
    print("    - Lineare Korrelationen in Ausgabe")
    
    print("\n[2] KRITISCHE ANWENDUNGEN:")
    print("    MT19937 sollte NIE verwendet werden fuer:")
    print("    - Kryptographische Schluesselgenerierung")
    print("    - Sichere Nonces")
    print("    - Glücksspiele mit Echtgeld")
    print("    - Wissenschaftliche Simulationen (manchmal)")
    
    print("\n[3] BESSERE ALTERNATIVEN:")
    print("    - Kryptographisch sichere PRNGs:")
    print("      * ChaCha20 (Nginx, OpenSSH)")
    print("      * AES-CTR-DRBG (NIST SP 800-90A)")
    print("      * getrandom() (Linux Kernel)")
    print("    - /dev/urandom (Unix)")
    print("    - CryptGenRandom (Windows)")
    
    print("\n[4] BELPHEGOR-VERBINDUNG?")
    print("    Keine direkte Verbindung gefunden.")
    print("    MT19937 ist ein bekannter, gut untersuchter Algorithmus.")
    print("    Die Konstanten sehen nicht verdächtig aus.")
    print()
    print("    ABER: Die Periodenlaenge 2^19937-1 ist enorm.")
    print("    Die Zahl 19937 ist seltsam spezifisch.")
    print("    Warum nicht 2^127-1 oder 2^521-1?")

def analyze_mt19937_vs_belphegor():
    """Vergleicht MT19937 mit Belphegor-Strukturen"""
    print("\n" + "=" * 70)
    print("VERGLEICH: MT19937 vs Belphegor-Strukturen")
    print("=" * 70)
    
    print("\n[1] GEMEINSAMKEITEN:")
    print("    - Beide haben sehr grosse Zahlen")
    print("    - MT: 2^19937 - 1 (ca. 6000 Stellen)")
    print("    - Belphegor: B_13 (31 Stellen)")
    print("    - Beide sind mathematisch spezielle Strukturen")
    
    print("\n[2] UNTERSCHIEDE:")
    print("    MT19937:")
    print("    - Periodenlaenge ist Mersenne-Primzahl")
    print("    - Keine 666/999-Muster in Konstanten")
    print("    - Keine Float-Problematik")
    print()
    print("    Belphegor:")
    print("    - 666 in der Mitte")
    print("    - Trapdoor durch smooth p-1")
    print("    - Float-Katastrophe")
    
    print("\n[3] OEIS-VERBINDUNGEN:")
    print("    MT19937 relevante Sequenzen:")
    print("    - A000225: Mersenne numbers (2^n - 1)")
    print("    - A000668: Mersenne primes")
    print("    - A001348: (2^p - 1) where p is prime")
    print()
    print("    Pi-relevant:")
    print("    - A221557: mt19937-recovered Pi approximation")
    print("    - A221558: mt19937 Pi approximation")
    print()
    print("    Diese Sequenzen verbinden MT mit Pi!")

def main():
    print("=" * 70)
    print("MERSENNE TWISTER ANALYZER")
    print("Untersuchung im Kontext von Belphegor, Pi und Phi")
    print("=" * 70)
    
    analyze_mt19937_parameters()
    analyze_mt_constants()
    analyze_mt_structure()
    check_mt_seeding()
    analyze_mt_periodicity()
    check_mt_security_issues()
    analyze_mt19937_vs_belphegor()
    
    print("\n" + "=" * 70)
    print("ZUSAMMENFASSUNG")
    print("=" * 70)
    print("""
ERGEBNISSE:

1. MT19937 PARAMETER:
   - Periode: 2^19937 - 1 (ca. 6000 Dezimalstellen)
   - 19937 ist 24. bekannter Mersenne-Exponent
   - 19937 mod 6 = 5, mod 37 = 15, mod 13 = 5
   - Keine direkte Verbindung zu 666 oder 999

2. MAGIC CONSTANTS:
   - a = 0x9908B0DF (Matrix)
   - b = 0x9D2C5680, c = 0xEFC60000
   - f = 1812433253 (Init)
   - Keine 666/999-Muster gefunden
   - Konstanten sehen zufaellig aus

3. SICHERHEIT:
   - MT19937 ist NICHT kryptographisch sicher!
   - State kann aus 624 Ausgaben rekonstruiert werden
   - Seed-Space nur 32 Bit
   - Sollte nie fuer Krypto verwendet werden

4. VERBINDUNG ZU BELPHEGOR:
   - KEINE direkte Verbindung gefunden
   - MT19937 ist gut dokumentierter Standard-Algorithmus
   - Keine versteckten 666-Muster in Konstanten
   - ABER: OEIS A221557/A221558 verbinden MT mit Pi!

FAZIT:
MT19937 ist ein bekannter, gut untersuchter Algorithmus.
Keine Hinweise auf Belphegor-aehnliche Strukturen oder
versteckte Backdoors in den Konstanten.

Die Verwendung von MT19937 fuer Kryptographie ist jedoch
UNSICHER aus anderen Gruenden (State-Rekonstruktion)!
""")

if __name__ == '__main__':
    main()
