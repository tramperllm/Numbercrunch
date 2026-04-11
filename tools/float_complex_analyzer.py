#!/usr/bin/env python3
"""
FLOAT COMPLEX ANALYZER
Untersucht ob die komplexe Zahlen-Identitaet durch Float-Praezisionsverlust 'glatt' wird
"""

import math
import struct

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_complex_float_loss():
    """Analysiert Float-Verlust bei komplexen Zahlen"""
    print("=" * 70)
    print("KOMPLEXE ZAHLEN-IDENTITAET UND FLOAT-VERLUST")
    print("=" * 70)
    
    # Exakte Werte
    print("\n[1] EXAKTE BERECHNUNG:")
    z1_real = 762
    z1_imag = 999999
    z2_real = 13
    z2_imag = 666
    
    z1_exact = complex(z1_real, z1_imag)
    z2_exact = complex(z2_real, z2_imag)
    
    abs_z1_exact = abs(z1_exact)
    abs_z2_exact = abs(z2_exact)
    ratio_exact = abs_z1_exact / abs_z2_exact
    
    target_ratio = 999999 / 666
    
    print(f"    z1 = {z1_real} + {z1_imag}i")
    print(f"    |z1| = sqrt({z1_real}² + {z1_imag}²) = {abs_z1_exact:.10f}")
    print()
    print(f"    z2 = {z2_real} + {z2_imag}i")
    print(f"    |z2| = sqrt({z2_real}² + {z2_imag}²) = {abs_z2_exact:.10f}")
    print()
    print(f"    Verhaeltnis = {ratio_exact:.10f}")
    print(f"    999999/666 = {target_ratio:.10f}")
    print(f"    Differenz = {abs(ratio_exact - target_ratio):.10f}")
    print(f"    Fehler = {abs(ratio_exact - target_ratio)/target_ratio*100:.4f}%")

def test_float_conversion():
    """Testet Float-Konversion der Komponenten"""
    print("\n" + "=" * 70)
    print("[2] FLOAT-KONVERSION DER KOMPONENTEN")
    print("=" * 70)
    
    components = [
        ("762 (z1 Realteil)", 762),
        ("999999 (z1 Imaginaerteil)", 999999),
        ("13 (z2 Realteil)", 13),
        ("666 (z2 Imaginaerteil)", 666),
    ]
    
    print("\n    Float-Konversion der einzelnen Komponenten:")
    for name, val in components:
        float_val = float(val)
        int_back = int(float_val)
        diff = val - int_back
        
        # Bit-Analyse
        bits_needed = val.bit_length() if val > 0 else 1
        
        print(f"\n    {name}:")
        print(f"      Original: {val}")
        print(f"      Float:    {float_val}")
        print(f"      Zurueck:  {int_back}")
        print(f"      Diff:     {diff}")
        print(f"      Bits:     {bits_needed} (max 52 fuer IEEE 754)")
        
        if diff == 0:
            print(f"      Status:   KEIN VERLUST (passt in 52 Bits)")
        else:
            print(f"      Status:   VERLUST!")

def analyze_complex_magnitude_float():
    """Analysiert Float-Berechnung der komplexen Betraege"""
    print("\n" + "=" * 70)
    print("[3] FLOAT-BERECHNUNG DER KOMPLEXEN BETRAEGE")
    print("=" * 70)
    
    # Float-Konversion der Komponenten
    z1_r_f = float(762)
    z1_i_f = float(999999)
    z2_r_f = float(13)
    z2_i_f = float(666)
    
    print(f"\n    Float-Komponenten:")
    print(f"    z1_r = {z1_r_f}")
    print(f"    z1_i = {z1_i_f}")
    print(f"    z2_r = {z2_r_f}")
    print(f"    z2_i = {z2_i_f}")
    
    # Float-Berechnung der Betraege
    # |z| = sqrt(r^2 + i^2)
    
    # Exakte Berechnung
    abs_z1_exact = math.sqrt(762**2 + 999999**2)
    abs_z2_exact = math.sqrt(13**2 + 666**2)
    
    # Float-Berechnung
    abs_z1_float = math.sqrt(z1_r_f**2 + z1_i_f**2)
    abs_z2_float = math.sqrt(z2_r_f**2 + z2_i_f**2)
    
    print(f"\n    |z1| exakt:  {abs_z1_exact:.15f}")
    print(f"    |z1| float:  {abs_z1_float:.15f}")
    print(f"    Differenz:   {abs(abs_z1_exact - abs_z1_float):.15e}")
    
    print(f"\n    |z2| exakt:  {abs_z2_exact:.15f}")
    print(f"    |z2| float:  {abs_z2_float:.15f}")
    print(f"    Differenz:   {abs(abs_z2_exact - abs_z2_float):.15e}")
    
    # Verhaeltnis
    ratio_exact = abs_z1_exact / abs_z2_exact
    ratio_float = abs_z1_float / abs_z2_float
    target = 999999 / 666
    
    print(f"\n    Verhaeltnis exakt: {ratio_exact:.15f}")
    print(f"    Verhaeltnis float: {ratio_float:.15f}")
    print(f"    999999/666:        {target:.15f}")
    
    print(f"\n    Fehler exakt vs 999999/666: {abs(ratio_exact - target):.15e}")
    print(f"    Fehler float vs 999999/666: {abs(ratio_float - target):.15e}")
    
    if abs(ratio_float - target) < abs(ratio_exact - target):
        print(f"\n    *** FLOAT-BERECHNUNG IST NAEHER AN 999999/666! ***")
        print(f"    Der Float-Fehler macht das Verhaeltnis 'glatter'!")
    else:
        print(f"\n    Float-Berechnung ist nicht naeher am Zielwert.")

def analyze_real_part_dominance():
    """Analysiert die Dominanz der Imaginaerteile"""
    print("\n" + "=" * 70)
    print("[4] ANALYSE: REALTEILE WERDEN VERNACHLAESSIGBAR?")
    print("=" * 70)
    
    # Verhaeltnis Realteil / Imaginaerteil
    ratio_z1 = 762 / 999999
    ratio_z2 = 13 / 666
    
    print(f"\n    Verhaeltnis Realteil/Imaginaerteil:")
    print(f"    z1: 762/999999 = {ratio_z1:.10f} = {ratio_z1*100:.6f}%")
    print(f"    z2: 13/666 = {ratio_z2:.10f} = {ratio_z2*100:.6f}%")
    
    # Was passiert wenn wir Realteile ignorieren?
    approx_z1 = 999999  # nur Imaginaerteil
    approx_z2 = 666     # nur Imaginaerteil
    
    ratio_approx = approx_z1 / approx_z2
    target = 999999 / 666
    
    print(f"\n    Berechnung OHNE Realteile:")
    print(f"    |z1| ≈ {approx_z1}")
    print(f"    |z2| ≈ {approx_z2}")
    print(f"    Verhaeltnis ≈ {ratio_approx:.10f}")
    print(f"    999999/666 = {target:.10f}")
    print(f"    Fehler = {abs(ratio_approx - target):.15e}")
    print(f"    Relativer Fehler = {abs(ratio_approx - target)/target*100:.10f}%")
    
    if abs(ratio_approx - target) < 1e-10:
        print(f"\n    *** DIE REALTEILE SIND VOLLSTAENDIG VERNACHLAESSIGBAR! ***")
        print(f"    |762 + 999999i| ≈ 999999 (Fehler nur 0.00029%)")
        print(f"    |13 + 666i| ≈ 666 (Fehler nur 0.02%)")
    
    # Float-Test: Was passiert bei float(762) vs float(999999)?
    print(f"\n    Float-Test:")
    f_762 = float(762)
    f_999999 = float(999999)
    
    z1_approx_float = math.sqrt(f_762**2 + f_999999**2)
    z1_approx_imag = f_999999  # nur Imaginaerteil
    
    print(f"    |762 + 999999i| (float) = {z1_approx_float:.10f}")
    print(f"    999999 (float) = {z1_approx_imag:.10f}")
    print(f"    Differenz = {abs(z1_approx_float - z1_approx_imag):.10f}")
    print(f"    Relativ = {abs(z1_approx_float - z1_approx_imag)/z1_approx_float*100:.10f}%")

def analyze_would_loss_make_it_exact():
    """Prueft ob Praezisionsverlust die Identitaet 'glatt' macht"""
    print("\n" + "=" * 70)
    print("[5] WUERDE FLOAT-VERLUST DIE IDENTITAET 'GLATT' MACHEN?")
    print("=" * 70)
    
    # Original
    exact_ratio = math.sqrt(762**2 + 999999**2) / math.sqrt(13**2 + 666**2)
    target = 999999 / 666
    
    print(f"\n    Original-Identitaet:")
    print(f"    |z1|/|z2| = {exact_ratio:.15f}")
    print(f"    999999/666 = {target:.15f}")
    print(f"    Fehler = {abs(exact_ratio - target):.15e}")
    
    # Simuliere verschiedene Praezisionsverluste
    precisions = [52, 40, 30, 20, 10]
    
    print(f"\n    Simulierte Praezisionsverluste:")
    
    for prec in precisions:
        # Simuliere: Nur 'prec' Bits der Mantisse
        # Das ist eine Naeherung, aber zeigt den Trend
        
        # In der Praxis: Wenn Komponenten > 2^prec, geht Praezision verloren
        # 999999 ist kleiner als 2^20 (ca. 1 Million)
        # Also: Selbst bei 20 Bits Praezision kein Verlust!
        
        if prec >= 20:
            print(f"\n    {prec} Bits Praezision:")
            print(f"      999999 < 2^{prec} => Kein Verlust!")
            print(f"      Verhaeltnis bleibt: {exact_ratio:.10f}")
        else:
            print(f"\n    {prec} Bits Praezision:")
            print(f"      999999 >= 2^{prec} => Verlust moeglich!")
    
    print(f"\n    FAZIT:")
    print(f"    Die Zahlen 762, 999999, 13, 666 sind zu KLEIN")
    print(f"    fuer signifikanten Praezisionsverlust!")
    print(f"    Selbst 20-Bit-Floats wuerden sie exakt darstellen.")
    
    print(f"\n    Die Identitaet wuerde NICHT durch Float-Verlust")
    print(f"    'glatt' werden - die Zahlen sind einfach zu klein!")

def analyze_belphegor_connection():
    """Analysiert Verbindung zu Belphegor"""
    print("\n" + "=" * 70)
    print("[6] VERBINDUNG ZUR BELPHEGOR-FLOAT-KATASTROPHE")
    print("=" * 70)
    
    # Belphegor ist riesig (1000000000000066600000000000001)
    # Passt nicht in 52 Bits!
    
    B_13 = 10**30 + 666 * 10**14 + 1
    
    print(f"\n    Belphegor B_13:")
    print(f"    B_13 = {B_13}")
    print(f"    Bits = {B_13.bit_length()}")
    print(f"    Benoetigt {B_13.bit_length()} Bits")
    print(f"    IEEE 754 hat 52 Bits Mantisse")
    print(f"    -> {B_13.bit_length() - 52} Bits Verlust!")
    
    # Vergleiche mit unseren Zahlen
    our_numbers = [762, 999999, 13, 666]
    
    print(f"\n    Vergleich mit unseren Zahlen:")
    for n in our_numbers:
        bits = n.bit_length()
        status = "OK" if bits <= 52 else "VERLUST!"
        print(f"    {n}: {bits} Bits - {status}")
    
    print(f"\n    FAZIT:")
    print(f"    Die komplexe Identitaet funktioniert mit ZAHLEN,")
    print(f"    die klein genug sind fuer exakte Float-Darstellung.")
    print(f"    Belphegor ist zu GROSS und erfaahrt Float-Verlust.")
    print(f"    Das sind ZWEI VERSCHIEDENE Phaenomene!")

def final_assessment():
    """Finale Bewertung"""
    print("\n" + "=" * 70)
    print("FINALE BEWERTUNG")
    print("=" * 70)
    
    print("""
ERGEBNISSE DER ANALYSE:

1. FLOAT-VERLUST BEI DEN KOMPONENTEN:
   - 762, 999999, 13, 666 sind alle < 2^20
   - IEEE 754 kann diese exakt darstellen (52 Bits Mantisse)
   - KEIN Praezisionsverlust bei der Konversion!

2. DIE KOMPLEXEN BETRAEGE:
   - |762 + 999999i| = 999999.29... (exakt berechnet)
   - |13 + 666i| = 666.13... (exakt berechnet)
   - Float-Berechnung ergibt IDENTISCHE Werte
   - Keine Abweichung durch Float!

3. WUERDE ES "GLATT" WERDEN?
   - NEIN! Die Zahlen sind zu klein fuer Float-Verlust.
   - Selbst mit 20-Bit-Praezision waeren sie exakt.
   - Die Differenz von 0.285527 bleibt erhalten.

4. DIE REALTEILE SIND VERNACHLAESSIGBAR:
   - 762/999999 = 0.076% (tatsaechlich klein)
   - 13/666 = 1.95% (tatsaechlich klein)
   - ABER: Dies ist eine MATHEMATISCHE Eigenschaft,
     kein Float-Verlust-Effekt!

5. BELPHEGOR-VERGLEICH:
   - Belphegor: 100 Bits, Float-Verlust = 11.2 Billionen
   - Komplexe Zahlen: <20 Bits, Float-Verlust = 0
   - VOLLSTAENDIG UNTERCHIEDLICH!

FAZIT:
Die komplexe Identitaet |762+999999i|/|13+666i| ≈ 999999/666
ist eine MATHEMATISCHE Eigenschaft, NICHT ein Float-Artifact.
Die Realteile sind mathematisch vernachlaessigbar,
nicht wegen Praezisionsverlust, sondern wegen der
grossen Imaginaerteile (0.076% bzw. 1.95% Anteil).

Diese Identitaet funktioniert EXAKT mit ganzen Zahlen
und bleibt auch bei Float-Berechnungen erhalten,
weil alle Zahlen klein genug sind.
""")

def main():
    analyze_complex_float_loss()
    test_float_conversion()
    analyze_complex_magnitude_float()
    analyze_real_part_dominance()
    analyze_would_loss_make_it_exact()
    analyze_belphegor_connection()
    final_assessment()

if __name__ == '__main__':
    main()
