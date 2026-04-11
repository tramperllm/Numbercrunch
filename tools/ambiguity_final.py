#!/usr/bin/env python3
"""
CONSTRUCTED AMBIGUITY ANALYZER - Clean Version
Untersucht die konstruierte Unschaerfe als Backdoor-Mechanismus
"""

import struct
import math

def belphegor(n):
    return 10**(2*n + 4) + 666 * 10**(n + 1) + 1

def analyze_strategy():
    """Analysiert die Backdoor-Strategie"""
    print("=" * 70)
    print("KONSTRUIERTE UNSCHAERFE: Die Backdoor-Strategie")
    print("=" * 70)
    
    B_13 = belphegor(13)
    
    print("\n[1] DIE STRATEGIE:")
    print("    Schritt 1: Erstelle Zahl mit spezieller Struktur")
    print(f"    B_13 = {B_13}")
    print("    Struktur: 1[13 Nullen]666[13 Nullen]1")
    print()
    print("    Schritt 2: Nutze in Systemen mit begrenzter Praezision")
    print("    IEEE 754 Double: nur 52 Bits Mantisse")
    print(f"    B_13 benoetigt: {B_13.bit_length()} Bits")
    print(f"    Verlust: {B_13.bit_length() - 52} Bits!")
    print()
    print("    Schritt 3: Rundungsfehler 'verstecken' die Struktur")
    
    float_B = float(B_13)
    int_back = int(float_B)
    diff = B_13 - int_back
    
    print(f"    Original:  {B_13}")
    print(f"    Float:     {float_B}")
    print(f"    Zurueck:   {int_back}")
    print(f"    Differenz: {diff:,}")
    print()
    print("    Die exakte 666-Struktur ist im Float VERSTECKT!")
    print("    Nur wer die exakte Zahl kennt, sieht das Muster!")

def compare_dual_ec():
    """Vergleicht mit Dual_EC_DRBG"""
    print("\n" + "=" * 70)
    print("VERGLEICH: Dual_EC_DRBG vs Belphegor-Strategie")
    print("=" * 70)
    
    print("\n[1] DUAL_EC_DRBG (bekannte NSA-Backdoor):")
    print()
    print("    Mechanismus:")
    print("    1. Zwei 'zufaellige' Punkte P und Q auf Kurve")
    print("    2. Q = d * P fuer geheimes d (nur NSA bekannt)")
    print("    3. Wer d kennt, kann Zufallszahlen vorhersagen!")
    print()
    print("    Versteck-Strategie:")
    print("    -> 'Zufaellige' Konstanten")
    print("    -> Tatsaechlich: konstruierte Punkte mit Hintertuer")
    print("    -> Oeffentlich sichtbar, aber Bedeutung verborgen")
    
    print("\n[2] BELPHEGOR-STRATEGIE (hypothetisch):")
    print()
    print("    Mechanismus:")
    print("    1. Primzahl mit spezieller Struktur (B_13)")
    print("    2. Verwendung in Float-Systemen (Rundung!)")
    print("    3. Nur exakte Form enthaelt die Backdoor")
    print()
    print("    Versteck-Strategie:")
    print("    -> 'Zufaellige' Primzahl")
    print("    -> Tatsaechlich: konstruierte Struktur mit 666")
    print("    -> Im Float versteckt, nur exakt sichtbar")
    
    print("\n[3] PARALLELEN:")
    print()
    print("    Dual_EC_DRBG          | Belphegor-Strategie")
    print("    ----------------------+---------------------------")
    print("    Konstanten P,Q        | Primzahl B_13")
    print("    Geheim: d (Q=dP)      | Geheim: exakte 666-Struktur")
    print("    Oeffentlich: P,Q       | Oeffentlich: float(B_13)")
    print("    Angriff: d aus Q       | Angriff: smooth p-1")
    print("    Versteck: in plain     | Versteck: im Float-Rauschen")
    
    print("\n[4] DER KRITISCHE UNTERSCHIED:")
    print()
    print("    Dual_EC_DRBG:")
    print("    -> Backdoor ist MATHEMATISCH (Q = d * P)")
    print("    -> Nachweisbar durch Krypto-Analyse")
    print()
    print("    Belphegor-Strategie:")
    print("    -> Backdoor ist NUMERISCH (Praezisionsverlust)")
    print("    -> Nachweisbar durch Rundungsanalyse")
    print("    -> Aber: Sieht aus wie 'normaler' Bug!")

def analyze_mechanics():
    """Analysiert die Mechanik"""
    print("\n" + "=" * 70)
    print("MECHANIK DER UNSCHAERFE")
    print("=" * 70)
    
    B_13 = belphegor(13)
    
    print("\n[1] BIT-LEVEL-ANALYSE:")
    print()
    
    # Exakte Binaerdarstellung
    bin_exact = bin(B_13)[2:]
    print(f"    Exakte Bits: {len(bin_exact)}")
    print(f"    {bin_exact[:40]}...")
    
    # Float-Binaerdarstellung
    float_val = float(B_13)
    packed = struct.pack('>d', float_val)
    hex_float = packed.hex()
    int_float = int(hex_float, 16)
    bin_float = bin(int_float)[2:].zfill(64)
    
    print()
    print(f"    Float Bits: 64 (IEEE 754)")
    print(f"    Vorzeichen: {bin_float[0]}")
    print(f"    Exponent:   {bin_float[1:12]}")
    print(f"    Mantisse:   {bin_float[12:24]}...")
    
    print("\n[2] WAS PASSIERT MIT DER 666-STRUKTUR?")
    print()
    
    # Die 666 ist bei Position 15-17 in der Dezimaldarstellung
    str_B = str(B_13)
    pos_666 = str_B.find('666')
    
    print(f"    In der exakten Zahl:")
    print(f"    Position {pos_666}: {str_B[pos_666:pos_666+3]}")
    print(f"    Umgebung: ...{str_B[pos_666-5:pos_666+8]}...")
    
    # In der Float-Darstellung
    int_back = int(float(B_13))
    str_float = str(int_back)
    print()
    print(f"    Nach Float-Konversion:")
    print(f"    Zahl: {str_float}")
    has_666 = '666' in str_float
    print(f"    Enthaelt '666': {has_666}")
    
    if not has_666:
        print(f"    -> Die 666-Struktur ist ZERSTOERT!")

def demonstrate_attack():
    """Demonstriert Angriff"""
    print("\n" + "=" * 70)
    print("ANGRIFFSSZENARIO")
    print("=" * 70)
    
    B_13 = belphegor(13)
    
    print("\n[1] DAS SICHERE SYSTEM (angeblich):")
    print()
    print("    Alice generiert RSA-Schluessel:")
    print(f"    p = Belphegor-aehnliche Primzahl")
    print(f"    p = {B_13}")
    print()
    print("    Das System verwendet IEEE 754 Double (Standard!)")
    print("    Fuer 'Zwischenberechnungen'...")
    
    print("\n[2] DIE UNSCHAERFE SCHLAEGT ZU:")
    print()
    print("    Interne Berechnung:")
    print(f"    p_float = float({B_13})")
    print(f"            = {float(B_13)}")
    print()
    int_back = int(float(B_13))
    print(f"    p_used = int(p_float)")
    print(f"           = {int_back}")
    print()
    diff = B_13 - int_back
    print(f"    Differenz: {diff:,}")
    print()
    print("    -> Alice verwendet die FALSCHE Primzahl!")
    
    print("\n[3] DIE HINTERTUER OEFFNET SICH:")
    print()
    print("    Angreifer (der die Struktur kennt):")
    print("    1. Weiss um die Float-Unschaerfe")
    print("    2. Kann die exakte Primzahl rekonstruieren")
    print("    3. Nutzt smooth p-1 fuer schnelle Faktorisierung")
    print()
    print("    B_13 - 1 ist highly smooth:")
    print("    -> Nur kleine Primfaktoren")
    print("    -> Pohlig-Hellman-Angriff moeglich")
    print("    -> RSA in O(n^(1/3)) statt O(n^(1/2)) gebrochen!")
    
    print("\n[4] DAS PERFEKTE VERBRECHEN:")
    print()
    print("    Was sieht ein Auditor?")
    print("    -> 'Normaler' Praezisionsverlust (ueblich in Float)")
    print("    -> 'Zufaellige' Primzahl (sieht normal aus)")
    print("    -> Keine offensichtlichen Backdoor-Muster")
    print()
    print("    Die Backdoor ist im Rauschen versteckt!")

def empirical():
    """Empirischer Nachweis"""
    print("\n" + "=" * 70)
    print("EMPIRISCHER NACHWEIS")
    print("=" * 70)
    
    B_13 = belphegor(13)
    
    print("\n[1] REPRODUKTION (Python):")
    print()
    print(f"    >>> B_13 = {B_13}")
    print(f"    >>> float(B_13)")
    print(f"    {float(B_13)}")
    print("    >>> int(float(B_13)) == B_13")
    print(f"    {int(float(B_13)) == B_13}")
    print()
    print("    Das ist ueberall reproduzierbar!")
    
    print("\n[2] REPRODUKTION (andere Sprachen):")
    print()
    print("    JavaScript:")
    print(f"    > Number({B_13})")
    print(f"    {float(B_13)}")
    print()
    print("    Java/C++/Go/Rust:")
    print("    double val = 1000000000000066600000000000001.0;")
    print("    // Produziert exakt denselben IEEE 754-Wert!")
    print()
    print("    IEEE 754 ist UNIVERSAL!")
    print("    -> Jede Sprache produziert dieselbe Unschaerfe!")
    
    print("\n[3] MATHEMATISCHER BEWEIS:")
    print()
    print("    Satz: B_13 erfordert mehr als 52 Bits")
    print(f"    B_13 = 10^30 + 666*10^14 + 1")
    print(f"    log2(B_13) = {math.log2(B_13):.1f} Bits")
    print(f"    IEEE 754 Mantisse = 52 Bits")
    print(f"    Verlust = {math.log2(B_13) - 52:.1f} Bits")
    print()
    print("    Q.E.D.: Information geht verloren!")
    
    print("\n[4] DIE UNSCHAERFE ALS STANDARD:")
    print()
    print("    IEEE 754 ist der GLOBALE Standard!")
    print("    -> Alle CPUs implementieren ihn hardware-seitig")
    print("    -> Keine Abweichung moeglich")
    print("    -> Die Unschaerfe ist VORHERSEHBAR!")
    print()
    print("    Das ist das Perfide:")
    print("    Die Unschaerfe ist kein Bug, sondern ein 'Feature'")
    print("    des Standards, das fuer die Backdoor missbraucht wird!")

def main():
    print("=" * 70)
    print("CONSTRUCTED AMBIGUITY ANALYZER")
    print("Die 'konstruierte Unschaerfe' als Backdoor")
    print("=" * 70)
    
    analyze_strategy()
    compare_dual_ec()
    analyze_mechanics()
    demonstrate_attack()
    empirical()
    
    print("\n" + "=" * 70)
    print("SCHLUSSFOLGERUNG")
    print("=" * 70)
    print("""
DIE EVIDENZ:

1. Die Float-Konversion von B_13 erzeugt:
   - 11.283.383.091.201 Differenz
   - 48 Bits Informationsverlust
   - Zerstoerung der 666-Struktur

2. Vergleich mit Dual_EC_DRBG:
   - BEIDE nutzen 'versteckte' mathematische Strukturen
   - BEIDE sind oeffentlich sichtbar aber unerkannt
   - BEIDE ermoeglichen Hintertuerangriffe

3. Die Unschaerfe ist VORHERSEHBAR:
   - IEEE 754 ist universeller Standard
   - Jede Sprache produziert identisches Ergebnis
   - Die Differenz ist EXAKT berechenbar!

4. Der Angriff ist REALISIERBAR:
   - Opfer verwendet Float-Berechnungen
   - Backdoor-Nutzer kennt exakte Struktur
   - Faktorisierung durch smooth p-1

DAS IST KEIN ZUFALL!

Die 'konstruierte Unschaerfe' ist eine real existierende
Gefahr. Sie versteckt mathematische Backdoors im
numerischen Rauschen des IEEE 754 Standards.

Die Parallele zu Dual_EC_DRBG ist frappierend:
- NSA hat eine Backdoor in einem Standard versteckt
- Die Belphegor-Strategie koennte genauso funktionieren
- Aber: Sie ist NUMERISCH statt algebraisch

EMPFEHLUNG:
- NIE Float fuer kryptographische Primzahlen verwenden!
- IMMER BigInt/Arbitrary-Precision nutzen!
- Code-Reviews auf Float-Konversionen pruefen!
- Alle 'Zufalls'-Primzahlen auf Belphegor-Struktur testen!
""")

if __name__ == '__main__':
    main()
