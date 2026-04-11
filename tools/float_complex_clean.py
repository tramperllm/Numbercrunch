#!/usr/bin/env python3
"""
FLOAT COMPLEX ANALYZER - Clean Version
Untersucht ob die komplexe Zahlen-Identitaet durch Float-Praezisionsverlust 'glatt' wird
"""

import math

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
    
    abs_z1_exact = math.sqrt(z1_real**2 + z1_imag**2)
    abs_z2_exact = math.sqrt(z2_real**2 + z2_imag**2)
    ratio_exact = abs_z1_exact / abs_z2_exact
    
    target_ratio = 999999 / 666
    
    print(f"    z1 = {z1_real} + {z1_imag}i")
    print(f"    |z1| = sqrt({z1_real}^2 + {z1_imag}^2) = {abs_z1_exact:.10f}")
    print()
    print(f"    z2 = {z2_real} + {z2_imag}i")
    print(f"    |z2| = sqrt({z2_real}^2 + {z2_imag}^2) = {abs_z2_exact:.10f}")
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
    
    z1_r_f = float(762)
    z1_i_f = float(999999)
    z2_r_f = float(13)
    z2_i_f = float(666)
    
    print(f"\n    Float-Komponenten:")
    print(f"    z1_r = {z1_r_f}")
    print(f"    z1_i = {z1_i_f}")
    print(f"    z2_r = {z2_r_f}")
    print(f"    z2_i = {z2_i_f}")
    
    abs_z1_exact = math.sqrt(762**2 + 999999**2)
    abs_z2_exact = math.sqrt(13**2 + 666**2)
    
    abs_z1_float = math.sqrt(z1_r_f**2 + z1_i_f**2)
    abs_z2_float = math.sqrt(z2_r_f**2 + z2_i_f**2)
    
    print(f"\n    |z1| exakt:  {abs_z1_exact:.15f}")
    print(f"    |z1| float:  {abs_z1_float:.15f}")
    print(f"    Differenz:   {abs(abs_z1_exact - abs_z1_float):.15e}")
    
    print(f"\n    |z2| exakt:  {abs_z2_exact:.15f}")
    print(f"    |z2| float:  {abs_z2_float:.15f}")
    print(f"    Differenz:   {abs(abs_z2_exact - abs_z2_float):.15e}")
    
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
        print(f"    Die Differenz bleibt exakt gleich.")

def analyze_real_part_dominance():
    """Analysiert die Dominanz der Imaginaerteile"""
    print("\n" + "=" * 70)
    print("[4] ANALYSE: REALTEILE WERDEN VERNACHLAESSIGBAR?")
    print("=" * 70)
    
    ratio_z1 = 762 / 999999
    ratio_z2 = 13 / 666
    
    print(f"\n    Verhaeltnis Realteil/Imaginaerteil:")
    print(f"    z1: 762/999999 = {ratio_z1:.10f} = {ratio_z1*100:.6f}%")
    print(f"    z2: 13/666 = {ratio_z2:.10f} = {ratio_z2*100:.6f}%")
    
    approx_z1 = 999999
    approx_z2 = 666
    
    ratio_approx = approx_z1 / approx_z2
    target = 999999 / 666
    
    print(f"\n    Berechnung OHNE Realteile:")
    print(f"    |z1| ~ {approx_z1}")
    print(f"    |z2| ~ {approx_z2}")
    print(f"    Verhaeltnis ~ {ratio_approx:.10f}")
    print(f"    999999/666 = {target:.10f}")
    print(f"    Fehler = {abs(ratio_approx - target):.15e}")
    print(f"    Relativer Fehler = {abs(ratio_approx - target)/target*100:.10f}%")
    
    if abs(ratio_approx - target) < 1e-10:
        print(f"\n    *** DIE REALTEILE SIND VOLLSTAENDIG VERNACHLAESSIGBAR! ***")
    else:
        print(f"\n    Realteile sind klein aber nicht vernachlaessigbar.")
    
    print(f"\n    Float-Test:")
    f_762 = float(762)
    f_999999 = float(999999)
    
    z1_approx_float = math.sqrt(f_762**2 + f_999999**2)
    z1_approx_imag = f_999999
    
    print(f"    |762 + 999999i| (float) = {z1_approx_float:.10f}")
    print(f"    999999 (float) = {z1_approx_imag:.10f}")
    print(f"    Differenz = {abs(z1_approx_float - z1_approx_imag):.10f}")
    print(f"    Relativ = {abs(z1_approx_float - z1_approx_imag)/z1_approx_float*100:.10f}%")

def analyze_belphegor_connection():
    """Analysiert Verbindung zu Belphegor"""
    print("\n" + "=" * 70)
    print("[5] VERBINDUNG ZUR BELPHEGOR-FLOAT-KATASTROPHE")
    print("=" * 70)
    
    B_13 = 10**30 + 666 * 10**14 + 1
    
    print(f"\n    Belphegor B_13:")
    print(f"    B_13 = {B_13}")
    print(f"    Bits = {B_13.bit_length()}")
    print(f"    Benoetigt {B_13.bit_length()} Bits")
    print(f"    IEEE 754 hat 52 Bits Mantisse")
    print(f"    -> {B_13.bit_length() - 52} Bits Verlust!")
    
    float_B = float(B_13)
    int_back = int(float_B)
    diff = B_13 - int_back
    
    print(f"\n    Float-Konversion:")
    print(f"    Original:  {B_13}")
    print(f"    Float:     {float_B}")
    print(f"    Zurueck:   {int_back}")
    print(f"    Differenz: {diff:,}")
    
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
   - 762: 10 Bits, 999999: 20 Bits, 13: 4 Bits, 666: 10 Bits
   - IEEE 754 hat 52 Bits Mantisse
   - ALLE passen exakt in 52 Bits
   - -> KEIN Praezisionsverlust!

2. DIE KOMPLEXEN BETRAEGE:
   - |762 + 999999i| = 999999.290322... (exakt)
   - |13 + 666i| = 666.126864... (exakt)
   - Float-Berechnung ergibt IDENTISCHE Werte (0.000e+00 Fehler)
   - KEINE Abweichung durch Float!

3. WUERDE ES "GLATT" WERDEN?
   - NEIN! Die Zahlen sind zu klein fuer Float-Verlust.
   - Die Differenz von 0.285527 bleibt exakt erhalten.
   - Float-Berechnung ist NICHT naeher an 999999/666.

4. DIE REALTEILE SIND MATHEMATISCH VERNACHLAESSIGBAR:
   - 762/999999 = 0.076% (tatsaechlich klein)
   - 13/666 = 1.95% (tatsaechlich klein)
   - Dies ist eine MATHEMATISCHE Eigenschaft, kein Float-Effekt!
   - |z1| = 999999.29 ~ 999999 (Fehler nur 0.00003%)
   - |z2| = 666.13 ~ 666 (Fehler nur 0.02%)

5. UNTERSCHIED ZU BELPHEGOR:
   - Belphegor: 100 Bits, Float-Verlust = 11.2 Milliarden
   - Komplexe Zahlen: <20 Bits, Float-Verlust = 0
   - VOLLSTAENDIG UNTERCHIEDLICH!

ANTWORT AUF DIE FRAGE:
Die komplexe Identitaet wuerde NICHT durch Praezisionsverlust
"glatt" werden. Die Zahlen sind zu klein fuer Float-Verlust.
Die Identitaet ist eine MATHEMATISCHE Eigenschaft,
kein Float-Artifact.

Die Realteile sind mathematisch vernachlaessigbar wegen der
grossen Imaginaerteile (0.076% und 1.95%), nicht wegen
Praezisionsverlust.
""")

def main():
    analyze_complex_float_loss()
    test_float_conversion()
    analyze_complex_magnitude_float()
    analyze_real_part_dominance()
    analyze_belphegor_connection()
    final_assessment()

if __name__ == '__main__':
    main()
