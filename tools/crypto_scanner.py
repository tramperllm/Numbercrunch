#!/usr/bin/env python3
"""
CRYPTO SCANNER: Systematische Suche nach Belphegor-Markern
in kryptographischen Bibliotheken und Standards

Verwendung:
    python crypto_scanner.py --scan-all
    python crypto_scanner.py --check-nist
    python crypto_scanner.py --verify-belphegor
"""

import re
import hashlib
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Belphegor-Zahlen
BELPHEGOR_PRIMES = {
    0: 16661,
    13: 1000000000000066600000000000001,
    42: None,  # Wird berechnet
    506: None,
}

def generate_belphegor(n: int) -> int:
    """Generiert B_n = 10^(2n+4) + 666×10^(n+1) + 1"""
    return 10**(2*n + 4) + 666 * 10**(n + 1) + 1

def is_highly_smooth(n: int, threshold: int = 10**6) -> Tuple[bool, List[int]]:
    """
    Prüft ob n highly smooth ist (nur kleine Primfaktoren)
    Returns: (is_smooth, factors)
    """
    factors = []
    d = 2
    while d * d <= n and d <= threshold:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        if n > threshold:
            return False, factors + [n]
        factors.append(n)
    
    return True, factors

def detect_belphegor_marker(number: int) -> Dict:
    """
    Erkennt Belphegor-Marker in einer Zahl
    Returns: Dict mit Risk-Score und Details
    """
    result = {
        'number': number,
        'is_belphegor_form': False,
        'belphegor_index': None,
        'contains_666': False,
        'contains_13': False,
        'is_palindrome': False,
        'is_smooth': False,
        'smooth_factors': [],
        'risk_score': 0,
        'risk_level': 'LOW'
    }
    
    str_num = str(number)
    
    # Test 1: Belphegor-Form
    for n in range(0, 200000):
        B_n = generate_belphegor(n)
        if number == B_n:
            result['is_belphegor_form'] = True
            result['belphegor_index'] = n
            result['risk_score'] += 100
            break
    
    # Test 2: 666-Check
    if '666' in str_num:
        result['contains_666'] = True
        result['risk_score'] += 30
    
    # Test 3: 13-Check
    if '13' in str_num or len(str_num) == 13:
        result['contains_13'] = True
        result['risk_score'] += 15
    
    # Test 4: Palindrom
    if str_num == str_num[::-1] and len(str_num) > 10:
        result['is_palindrome'] = True
        result['risk_score'] += 20
    
    # Test 5: Smoothness (nur für große Zahlen)
    if len(str_num) > 20:
        is_smooth, factors = is_highly_smooth(number - 1)
        if is_smooth:
            result['is_smooth'] = True
            result['smooth_factors'] = factors[:10]  # Nur erste 10
            result['risk_score'] += 75
    
    # Risk-Level
    if result['risk_score'] >= 100:
        result['risk_level'] = 'CRITICAL'
    elif result['risk_score'] >= 50:
        result['risk_level'] = 'HIGH'
    elif result['risk_score'] >= 20:
        result['risk_level'] = 'MEDIUM'
    
    return result

# Bekannte kryptographische Konstanten
NIST_PRIMES = [
    ("NIST P-192", 6277101735386680763835789423207666416083908700390324961279),
    ("NIST P-224", 26959946667150639794667015087019630673557916260026308143510066298881),
    ("NIST P-256", 115792089210356248762697446949407573530086143415290314195533631308867097853951),
    ("NIST P-384", 394020061963944792122790401001436138050797392704654466679482934042457217714972106114142662548849156408066279469068093281),
    ("NIST P-521", 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151),
]

SECP256K1_P = 115792089237316195423570985008687907853269984665640564039457584007908834671663

def scan_nist_curves():
    """Scannt NIST-Kurven auf Belphegor-Marker"""
    print("=" * 70)
    print("SCAN: NIST Elliptische Kurven")
    print("=" * 70)
    
    findings = []
    
    for name, prime in NIST_PRIMES:
        result = detect_belphegor_marker(prime)
        print(f"\n{name}:")
        print(f"  Primzahl: {prime}")
        print(f"  Risk-Score: {result['risk_score']}")
        print(f"  Risk-Level: {result['risk_level']}")
        
        if result['risk_score'] > 0:
            print(f"  Warnungen:")
            if result['is_belphegor_form']:
                print(f"    ⚠️  EXAKTE BELPHEGOR-STRUKTUR gefunden! Index: {result['belphegor_index']}")
            if result['contains_666']:
                print(f"    ⚠️  Enthält 666")
            if result['is_smooth']:
                print(f"    ⚠️  Highly smooth p-1 (Trapdoor?)")
                print(f"        Faktoren: {result['smooth_factors']}")
            findings.append((name, result))
    
    # secp256k1 (Bitcoin)
    print(f"\nsecp256k1 (Bitcoin Kurve):")
    result = detect_belphegor_marker(SECP256K1_P)
    print(f"  Risk-Score: {result['risk_score']}")
    print(f"  Risk-Level: {result['risk_level']}")
    
    print("\n" + "=" * 70)
    print(f"GEFUNDEN: {len(findings)} verdächtige Kurven")
    print("=" * 70)
    
    return findings

def scan_file_for_constants(filepath: Path) -> List[Tuple[int, int]]:
    """Extrahiert große Zahlen aus einer Datei"""
    constants = []
    
    try:
        content = filepath.read_text(errors='ignore')
        
        # Hex-Zahlen
        hex_pattern = r'0x[0-9a-fA-F]{20,}'
        for match in re.finditer(hex_pattern, content):
            try:
                num = int(match.group(), 16)
                if num > 10**20:  # Nur sehr große Zahlen
                    constants.append((match.start(), num))
            except:
                pass
        
        # Dezimale Zahlen
        dec_pattern = r'\b\d{30,}\b'
        for match in re.finditer(dec_pattern, content):
            try:
                num = int(match.group())
                if num > 10**20:
                    constants.append((match.start(), num))
            except:
                pass
                
    except Exception as e:
        print(f"Fehler beim Lesen von {filepath}: {e}")
    
    return constants

def scan_openssl():
    """Scannt OpenSSL-Quellcode nach verdächtigen Konstanten"""
    print("\n" + "=" * 70)
    print("SCAN: OpenSSL (falls verfügbar)")
    print("=" * 70)
    
    openssl_paths = [
        Path("/usr/src/openssl"),
        Path("/usr/local/src/openssl"),
        Path("C:/openssl"),
        Path("./openssl"),
    ]
    
    findings = []
    
    for base_path in openssl_paths:
        if not base_path.exists():
            continue
        
        print(f"\nDurchsuche: {base_path}")
        
        # Suche nach C-Dateien
        for c_file in base_path.rglob("*.c"):
            if 'test' in c_file.name or 'example' in c_file.name:
                continue
                
            constants = scan_file_for_constants(c_file)
            
            for pos, num in constants:
                result = detect_belphegor_marker(num)
                if result['risk_score'] > 50:
                    print(f"\n  Datei: {c_file.relative_to(base_path)}")
                    print(f"  Position: {pos}")
                    print(f"  Zahl: {str(num)[:50]}...")
                    print(f"  Risk-Score: {result['risk_score']} ({result['risk_level']})")
                    
                    if result['is_belphegor_form']:
                        print(f"  ⚠️⚠️⚠️  BELPHEGOR GEFUNDEN! Index: {result['belphegor_index']}")
                    
                    findings.append((c_file, num, result))
        
        if findings:
            break
    
    if not findings:
        print("Keine verdächtigen Konstanten gefunden oder OpenSSL nicht lokal verfügbar.")
    
    return findings

def verify_transformation():
    """Verifiziert die 764.5 → 13 Transformation"""
    print("\n" + "=" * 70)
    print("VERIFIKATION: Feynman-Point ↔ Belphegor Transformation")
    print("=" * 70)
    
    feynman_center = 764.5
    belphegor_index = 13
    
    # Transformation
    T = (feynman_center * belphegor_index) / feynman_center
    print(f"\nT(764.5) = (764.5 × 13) / 764.5 = {T}")
    print(f"Ergebnis: {T} (erwartet: 13)")
    print(f"Exakt: {T == belphegor_index}")
    
    # Umkehrung
    T_inv = (belphegor_index * feynman_center) / belphegor_index
    print(f"\nT⁻¹(13) = (13 × 764.5) / 13 = {T_inv}")
    print(f"Ergebnis: {T_inv} (erwartet: 764.5)")
    print(f"Exakt: {T_inv == feynman_center}")
    
    # Kryptographische Relevanz?
    print("\n" + "-" * 70)
    print("KRYPTOGRAPHISCHE RELEVANZ:")
    print("-" * 70)
    print("""
Die Transformation ist eine mathematische Identität:
    T(x) = (x × 13) / 764.5 = 13 × (x / 764.5)

Für x = 764.5: T(x) = 13 (trivial)

Diese Transformation hat KEINE kryptographische Funktion:
- Sie ist öffentlich berechenbar
- Sie ist bijektiv (umkehrbar)
- Sie enthält keinen geheimen Schlüssel
- Sie ist keine Einwegfunktion

Fazit: Mathematisch interessant, aber kryptographisch irrelevant.
""")

def test_belphegor_backdoor():
    """Demonstration der Belphegor-Backdoor"""
    print("\n" + "=" * 70)
    print("PROOF-OF-CONCEPT: Belphegor Trapdoor-Backdoor")
    print("=" * 70)
    
    # Belphegor B_13
    B_13 = 1000000000000066600000000000001
    
    print(f"\nBelphegor B_13 = {B_13}")
    
    # Faktorisierung von B_13 - 1
    p_minus_1 = B_13 - 1
    print(f"\nB_13 - 1 = {p_minus_1}")
    
    is_smooth, factors = is_highly_smooth(p_minus_1)
    print(f"\nHighly smooth: {is_smooth}")
    print(f"Kleine Faktoren: {factors[:15]}")
    print(f"Größter Faktor: {max(factors) if factors else 'N/A'}")
    
    if is_smooth:
        print("""
⚠️  KRYPTOGAPHISCHE IMPLIKATION:

Wenn B_13 als Diffie-Hellman-Modulus verwendet wird:
1. p-1 ist highly smooth
2. Pohlig-Hellman-Algorithmus anwendbar
3. Diskrete Logarithmen effizient berechenbar
4. Angreifer mit Faktorisierung kann Schlüssel brechen

Dies ist KEINE Theorie - es ist mathematische Tatsache!
""")

def main():
    if len(sys.argv) < 2:
        print("""
Crypto Scanner - Belphegor Marker Detection

Verwendung:
    python crypto_scanner.py --scan-all      # Vollständiger Scan
    python crypto_scanner.py --check-nist    # Nur NIST-Kurven
    python crypto_scanner.py --verify-belphegor  # Belphegor-Backdoor Demo
    python crypto_scanner.py --transformation    # Transformation testen
        """)
        return
    
    cmd = sys.argv[1]
    
    if cmd == '--scan-all':
        scan_nist_curves()
        scan_openssl()
        verify_transformation()
        test_belphegor_backdoor()
    elif cmd == '--check-nist':
        scan_nist_curves()
    elif cmd == '--verify-belphegor':
        test_belphegor_backdoor()
    elif cmd == '--transformation':
        verify_transformation()
    else:
        print(f"Unbekannter Befehl: {cmd}")

if __name__ == '__main__':
    main()
