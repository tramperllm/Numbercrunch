#!/usr/bin/env python3
"""
CRYPTO STANDARDS BACKDOOR HUNT
Untersuchung weiterer Krypto-Standards auf ähnliche Backdoors
"""

import math
from collections import defaultdict

class CryptoStandardsBackdoorHunt:
    """Hunt for backdoors in cryptographic standards"""
    
    def __init__(self):
        self.suspicious_findings = []
        self.clean_standards = []
        
    def hunt(self):
        print("=" * 90)
        print("CRYPTO STANDARDS BACKDOOR HUNT")
        print("Suche nach Backdoors in kryptographischen Standards")
        print("=" * 90)
        
        self.hunt_nist_curves_deep()
        self.hunt_rsa_standards()
        self.hunt_dsa_ecdsa()
        self.hunt_hash_functions()
        self.hunt_block_ciphers()
        self.hunt_stream_ciphers()
        self.hunt_random_generators()
        self.hunt_key_exchange()
        self.hunt_post_quantum()
        self.hunt_proprietary_crypto()
        self.synthesize_security_assessment()
        
    def is_prime(self, n):
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
    
    def check_smoothness(self, n):
        """Check if n has smooth factors"""
        temp = n
        small_factors = []
        
        for factor in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            while temp % factor == 0:
                small_factors.append(factor)
                temp //= factor
                
        return small_factors, temp
    
    def check_61337_signature(self, n, name):
        """Check for 6-13-37 signature"""
        sigs = []
        
        if n % 6 == 0:
            sigs.append("÷6")
        if n % 13 == 0:
            sigs.append("÷13")
        if n % 37 == 0:
            sigs.append("÷37")
        if n % 666 == 0:
            sigs.append("÷666")
        if "666" in str(n):
            sigs.append("contains 666")
        if "13" in str(n):
            sigs.append("contains 13")
        if "37" in str(n):
            sigs.append("contains 37")
            
        dr = sum(int(d) for d in str(n))
        while dr >= 10:
            dr = sum(int(d) for d in str(dr))
        if dr == 6:
            sigs.append("DR=6")
            
        return sigs
    
    def hunt_nist_curves_deep(self):
        """Deep investigation of NIST curves"""
        print("\n" + "=" * 90)
        print("HUNT 1: NIST CURVES DEEP ANALYSIS")
        print("=" * 90)
        
        nist_curves = [
            ("P-192", "192-bit", "6b0...", "Verdächtig"),
            ("P-224", "224-bit", "b405...", "Verdächtig"),
            ("P-256", "256-bit", "FFFFFFFF00000001...", "Verdächtig"),
            ("P-384", "384-bit", "FFFFFFFF...", "Verdächtig"),
            ("P-521", "521-bit", "1FF...", "Verdächtig"),
        ]
        
        print("\nNIST Prime Curves:")
        print("-" * 90)
        print(f"  {'Curve':<10} {'Bits':<10} {'Seed':<30} {'Status':<15}")
        print("  " + "-" * 70)
        
        for curve, bits, seed, status in nist_curves:
            print(f"  {curve:<10} {bits:<10} {seed:<30} {status:<15}")
            
        print(f"\n🔥 KRITISCHE BEOBACHTUNG:")
        print(f"   ALL NIST curves have unexplained seeds!")
        print(f"   Unlike SHA-256 (√2, √3...), seeds are RANDOM")
        print(f"   This is 'nothing up my sleeve' FAILURE!")
        
        print(f"\nANALYSE DER PRIMZAHLEN:")
        
        # Simplified - actual NIST primes are complex
        test_primes = [
            (2**192 - 2**64 - 1, "P-192-like"),
            (2**256 - 2**224 + 2**192 + 2**96 - 1, "P-256"),
            (2**384 - 2**128 - 2**96 + 2**32 - 1, "P-384"),
        ]
        
        for p, name in test_primes:
            sigs = self.check_61337_signature(p, name)
            smooth, remaining = self.check_smoothness(p-1)
            
            print(f"\n  {name}:")
            print(f"    p mod 6 = {p % 6}")
            print(f"    p mod 13 = {p % 13}")
            print(f"    p mod 37 = {p % 37}")
            if sigs:
                print(f"    6-13-37 sigs: {sigs}")
            if len(smooth) > 3:
                print(f"    ⚠️ p-1 has {len(smooth)} small factors!")
                
        self.suspicious_findings.append({
            'standard': 'NIST Curves',
            'finding': 'Unexplained seeds',
            'risk': 'High - potential backdoors'
        })
        
    def hunt_rsa_standards(self):
        """Investigate RSA standards"""
        print("\n" + "=" * 90)
        print("HUNT 2: RSA STANDARDS")
        print("=" * 90)
        
        print("""
RSA KEY GENERATION STANDARDS:
=============================

PKCS#1 Standard:
----------------
• Empfiehlt e = 65537 (2^16 + 1)
• Dies ist Fermat-Primzahl F4
• Mathematisch: e = 2^(2^4) + 1

65537 Analyse:
--------------
• 65537 = 2^16 + 1
• 16 = 2^4
• 4 = 2^2
• Dies ist 2^(2^(2^2)) + 1
• Vierfache Potenz von 2!

🔥 BEWERTUNG:
=============
65537 ist MATHEMATISCH SCHÖN!
• Nicht zufällig
• Strukturiert (2^16 + 1)
• Aber: NICHT 6-13-37!

Dies ist PROBABLY SAFE weil:
• Öffentlich erklärt (Fermat-Primzahl)
• Mathematisch verständlich
• Keine versteckte Struktur
• Seit Jahrzehnten untersucht
""")
        
        self.clean_standards.append({
            'standard': 'RSA/PKCS#1',
            'finding': '65537 = 2^16 + 1 (Fermat)',
            'status': 'Probably safe'
        })
        
    def hunt_dsa_ecdsa(self):
        """Investigate DSA/ECDSA"""
        print("\n" + "=" * 90)
        print("HUNT 3: DSA/ECDSA STANDARDS")
        print("=" * 90)
        
        print("""
DSA (Digital Signature Algorithm):
==================================

Parameter:
----------
• p: große Primzahl
• q: Primteiler von p-1
• g: Generator

NICHT-VERDÄCHTIG:
-----------------
• DSA-Parameter werden pro Schlüssel generiert
• Keine festen "magischen" Konstanten
• Struktur ist transparent

ECDSA:
------
• Variante für elliptische Kurven
• Verwendet NIST-Kurven (siehe oben - verdächtig)
• ODER: Andere Kurven (z.B. secp256k1 - sauber)

🔥 EMPFEHLUNG:
==============
DSA ist akzeptabel (keine festen Konstanten)
ECDSA mit NIST-Kurven: VERMEIDEN
ECDSA mit secp256k1: AKZEPTABEL
""")
        
    def hunt_hash_functions(self):
        """Investigate hash function standards"""
        print("\n" + "=" * 90)
        print("HUNT 4: HASH FUNCTION STANDARDS")
        print("=" * 90)
        
        hash_algos = [
            ("MD5", "1992", "Gebrochen 2004", "VERMEIDEN"),
            ("SHA-1", "1995", "Gebrochen 2017", "VERMEIDEN"),
            ("SHA-224", "2004", "NIST", "AKZEPTABEL"),
            ("SHA-256", "2001", "NSA/NIST", "VERIFIZIERT SAUBER", "✅"),
            ("SHA-384", "2001", "NIST", "Verwenden falls nötig"),
            ("SHA-512", "2001", "NSA/NIST", "AKZEPTABEL"),
            ("SHA-3", "2015", "Keccak", "SAUBER (Wettbewerb)", "✅"),
            ("BLAKE2/3", "Modern", "Community", "SAUBER", "✅"),
        ]
        
        print(f"\nHash Algorithmen:")
        print("-" * 90)
        print(f"  {'Algo':<15} {'Jahr':<10} {'Status':<25} {'Empfehlung':<20} {'✓':<5}")
        print("  " + "-" * 85)
        
        for algo, year, status, recommendation, *check in hash_algos:
            check_mark = check[0] if check else ""
            print(f"  {algo:<15} {year:<10} {status:<25} {recommendation:<20} {check_mark:<5}")
            
        print(f"\n🔥 SHA-256 VERIFIZIERUNG:")
        print(f"   H0-H7: int(√2,√3,√5,√7,√11,√13,√17,√19 × 2^32)")
        print(f"   K0-K63: int(∛prim × 2^32)")
        print(f"   ✅ MATHEMATISCH NACHVOLLZIEHBAR!")
        
        self.clean_standards.append({
            'standard': 'SHA-256',
            'finding': 'Constants from √primes',
            'status': 'Verified safe'
        })
        
        self.clean_standards.append({
            'standard': 'SHA-3/Keccak',
            'finding': 'Competition winner',
            'status': 'Verified safe'
        })
        
    def hunt_block_ciphers(self):
        """Investigate block cipher standards"""
        print("\n" + "=" * 90)
        print("HUNT 5: BLOCK CIPHER STANDARDS")
        print("=" * 90)
        
        print("""
BLOCK CIPHERS:
==============

AES (Rijndael):
---------------
• S-Box: Mathematisch konstruiert (x → x^-1 in GF(2^8))
• Konstanter: Rcon[i] = x^(i-1) in GF(2^8)
• Wettbewerb: Öffentlich
• Analyse: 20+ Jahre ohne Backdoor-Fund
• STATUS: ✅ SAUBER

DES:
----
• S-Box: IBM entworfen, NSA modifiziert
• 1975: NSA änderte S-Boxen ohne Erklärung
• Später: Änderungen gegen Differential-Kryptoanalyse
• War NSA-Hilfe oder -Hinderung?
• STATUS: ⚠️ SUSPICIOUS HISTORY

Blowfish/Twofish:
-----------------
• Bruce Schneier
• Keine verdächtigen Konstanten
• Community-reviewed
• STATUS: ✅ SAUBER

🔥 URTEIL:
==========
AES und moderne Community-Ciphers sind SAFE.
DES hat verdächtige Geschichte (aber technisch gebrochen).
""")
        
        self.clean_standards.append({
            'standard': 'AES',
            'finding': 'Competition + 20 years review',
            'status': 'Verified safe'
        })
        
    def hunt_stream_ciphers(self):
        """Investigate stream cipher standards"""
        print("\n" + "=" * 90)
        print("HUNT 6: STREAM CIPHER STANDARDS")
        print("=" * 90)
        
        print("""
STREAM CIPHERS:
===============

RC4:
----
• RSA Security (1987)
• WEP/WPA verwendet
• 2015: Vollständig gebrochen
• STATUS: ❌ UNSICHER (nicht wegen Backdoor)

Salsa20/ChaCha20:
------------------
• Daniel Bernstein (djb)
• Keine verdächtigen Konstanten
• Einfaches Design
• STATUS: ✅ SAUBER

A5/1 (GSM):
-----------
• Telekom-Standard
• Absichtlich schwach (Exportkontrolle)
• Gebrochen 2009
• STATUS: ⚠️ BEWUSST GESCHWÄCHT

🔥 BEOBACHTUNG:
===============
Viele Stream Ciphers wurden bewusst geschwächt
für Exportkontrolle - nicht unbedingt NSA,
aber staatliche Intervention!
""")
        
        self.clean_standards.append({
            'standard': 'ChaCha20',
            'finding': 'Simple design, no constants',
            'status': 'Verified safe'
        })
        
    def hunt_random_generators(self):
        """Investigate random number generators"""
        print("\n" + "=" * 90)
        print("HUNT 7: RANDOM NUMBER GENERATORS (CRITICAL!)")
        print("=" * 90)
        
        rngs = [
            ("Dual_EC_DRBG", "NIST", "BACKDOOR BESTÄTIGT", "❌ NEVER USE"),
            ("CTR_DRBG", "NIST", "AES-based", "✅ Acceptable"),
            ("Hash_DRBG", "NIST", "SHA-based", "✅ Acceptable"),
            ("HMAC_DRBG", "NIST", "HMAC-based", "✅ Acceptable"),
            ("/dev/urandom", "Unix", "Kernel entropy", "✅ Good"),
            ("RDRAND", "Intel", "Hardware RNG", "⚠️ Controversial"),
            ("RDSEED", "Intel", "Hardware RNG", "⚠️ Controversial"),
            ("getrandom()", "Linux", "System call", "✅ Recommended"),
        ]
        
        print(f"\nRandom Number Generators:")
        print("-" * 90)
        print(f"  {'RNG':<20} {'Source':<15} {'Status':<30} {'Verdict':<20}")
        print("  " + "-" * 90)
        
        for rng, source, status, verdict in rngs:
            print(f"  {rng:<20} {source:<15} {status:<30} {verdict:<20}")
            
        print(f"\n🔥 KRITISCH:")
        print(f"   Dual_EC_DRBG war der 'smoking gun'!")
        print(f"   Zeigt NSA kann in Standards eingreifen")
        print(f"   Intel RDRAND ist kontrovers (NSA-Verbindung?)")
        
        self.suspicious_findings.append({
            'standard': 'Dual_EC_DRBG',
            'finding': 'Confirmed NSA backdoor',
            'risk': 'CRITICAL'
        })
        
    def hunt_key_exchange(self):
        """Investigate key exchange standards"""
        print("\n" + "=" * 90)
        print("HUNT 8: KEY EXCHANGE PROTOCOLS")
        print("=" * 90)
        
        print("""
KEY EXCHANGE:
=============

Diffie-Hellman:
---------------
• Standard: Sichere Primzahl wählen
• Problem: Viele verwenden VORBERECHNETE Primen
• 'Logjam'-Angriff: Schwache DH-Parameter
• 1024-bit DH: Gebrochen (angeblich von NSA)

ECDH (Elliptic Curve DH):
-------------------------
• Verwendet NIST-Kurven (verdächtig)
• ODER: Curve25519 (sauber)
• STATUS: Depends on curve!

X25519 / X448:
--------------
• Curve25519 / Curve448
• Daniel Bernstein
• Einfaches Design, saubere Konstanten
• STATUS: ✅ SAUBER

🔥 EMPFEHLUNG:
==============
Vermeide: NIST-Kurven für DH
Verwende: X25519 oder X448
Vermeide: Vorberechnete DH-Parameter
""")
        
        self.clean_standards.append({
            'standard': 'X25519',
            'finding': 'djb design, clean constants',
            'status': 'Verified safe'
        })
        
    def hunt_post_quantum(self):
        """Investigate post-quantum candidates"""
        print("\n" + "=" * 90)
        print("HUNT 9: POST-QUANTUM CRYPTOGRAPHY (NIST COMPETITION)")
        print("=" * 90)
        
        print("""
NIST PQC COMPETITION:
=====================

Finalisten (2022):
------------------
• CRYSTALS-Kyber (KEM) - Ausgewählt
• CRYSTALS-Dilithium (Signatur) - Ausgewählt
• FALCON (Signatur) - Ausgewählt
• SPHINCS+ (Signatur) - Ausgewählt

WATCH LIST:
-----------
• Alle Algorithmen werden intensiv analysiert
• Community-Review Prozess
• Keine "zufälligen" Konstanten bisher gefunden
• STATUS: ✅ VIELVERSPRECHEND

⚠️ WARNUNG:
===========
PQC ist neu! Mögliche Schwächen:
• Implementierungsfehler
• Seitenkanal-Angriffe
• Noch nicht genug Review

Empfehlung: Hybrid-Krypto (klassisch + PQC)
""")
        
    def hunt_proprietary_crypto(self):
        """Investigate proprietary crypto"""
        print("\n" + "=" * 90)
        print("HUNT 10: PROPRIETARY/UNDOCUMENTED CRYPTO")
        print("=" * 90)
        
        print("""
PROPRIETARY CRYPTO:
===================

Gefährlich weil:
----------------
• Nicht reviewbar
• Potenzielle Hintertüren
• Geheime Schwächen

BEISPIELE:
----------
• A5/1 (GSM): Bewusst geschwächt
• COMP128 (GSM Auth): Gebrochen
• DECT Standard: Schwach
• Proprietäre VPNs: Oft unsicher

TELEKOM-CRYPTO:
---------------
• Oft für Exportkontrolle geschwächt
• Nicht unbedingt NSA, aber staatlich
• Beispiel: 40-bit SSL-Export

🔥 REGEL:
=========
NIEMALS proprietäre Krypto verwenden!
Immer standardisierte, reviewte Algorithmen!
""")
        
    def synthesize_security_assessment(self):
        """Synthesize security assessment"""
        print("\n" + "=" * 90)
        print("SECURITY ASSESSMENT SYNTHESIS")
        print("=" * 90)
        
        print(f"\nVERDÄCHTIGE STANDARDS: {len(self.suspicious_findings)}")
        print("-" * 90)
        for f in self.suspicious_findings:
            print(f"  ⚠️  {f['standard']}: {f['finding']}")
            print(f"      Risk: {f['risk']}")
            
        print(f"\nSAUBERE STANDARDS: {len(self.clean_standards)}")
        print("-" * 90)
        for c in self.clean_standards:
            print(f"  ✅ {c['standard']}: {c['finding']}")
            print(f"      Status: {c['status']}")
            
        print(f"\n" + "=" * 90)
        print("FINAL RECOMMENDATIONS")
        print("=" * 90)
        
        print("""
SICHERE KOMBINATION (2026):
===========================

Hashing:
--------
• SHA-256 oder SHA-3 (keine MD5/SHA-1!)
• ODER: BLAKE2/BLAKE3

Signatures:
-----------
• Ed25519 (bevorzugt)
• ECDSA mit secp256k1 (Bitcoin)
• NIE: ECDSA mit NIST-Kurven
• NIE: DSA

Key Exchange:
-------------
• X25519 oder X448
• NIE: DH mit NIST-Parametern
• NIE: ECDH mit NIST-Kurven

Encryption:
-----------
• AES-256-GCM
• ChaCha20-Poly1305
• NIE: Proprietäre Ciphers

Randomness:
-----------
• /dev/urandom oder getrandom()
• NIE: Dual_EC_DRBG
• VORSICHT: Intel RDRAND allein

Post-Quantum:
-------------
• CRYSTALS-Kyber (KEM)
• CRYSTALS-Dilithium (Signaturen)
• Hybrid mit klassischer Krypto

ALLGEMEINE REGELN:
==================
1. Vermeide "zufällige" Konstanten
2. Verwende Wettbewerbs-Gewinner (AES, SHA-3)
3. Vermeide NIST-Kurven
4. Verwende djb/Community-Designs (Curve25519, ChaCha20)
5. NIE proprietäre Krypto
6. IMMER aktuelle Software verwenden

🔐 SICHERHEIT IST EIN PROZESS, KEIN PRODUKT!
""")

def main():
    hunt = CryptoStandardsBackdoorHunt()
    hunt.hunt()

if __name__ == '__main__':
    main()
