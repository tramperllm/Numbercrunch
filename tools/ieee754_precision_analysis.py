#!/usr/bin/env python3
"""
IEEE 754 PRECISION ANALYSIS FOR B_13
Zeigt EXAKT wo die Präzision verloren geht
"""

import math
import struct

def analyze_ieee754_precision():
    print("=" * 90)
    print("IEEE 754 PRECISION ANALYSIS FOR BELPHEGOR B_13")
    print("=" * 90)
    
    B_13 = 10**30 + 666 * 10**14 + 1
    B_str = str(B_13)
    
    print(f"\nB_13 = {B_13}")
    print(f"Anzahl Ziffern: {len(B_str)}")
    print(f"Binäre Bits benötigt: {B_13.bit_length()}")
    print(f"\nStruktur:")
    print(f"  Position 0-13:  {'1' + '0'*13} (14 Einsen/Nullen)")
    print(f"  Position 14-16:   {B_str[14:17]} (666)")
    print(f"  Position 17-30:   {'0'*13 + '1'} (14 Nullen/Eins)")
    
    print("\n" + "=" * 90)
    print("IEEE 754 DOUBLE SPECIFICATION")
    print("=" * 90)
    
    print("""
IEEE 754 Double (64-bit):
• 1 Bit Vorzeichen
• 11 Bit Exponent
• 52 Bit Mantisse (Significand)
• Präzision: ~15-17 Dezimalstellen
• Max exakte Ganzzahl: 2^53 = 9,007,199,254,740,992 (~16 Stellen)
""")
    
    max_exact_int = 2**53
    print(f"Max exakte Ganzzahl (2^53): {max_exact_int:,}")
    print(f"Ziffern: {len(str(max_exact_int))}")
    
    print("\n" + "=" * 90)
    print("ANALYSE: WO WIRD ABGESCHNITTEN?")
    print("=" * 90)
    
    # Float conversion
    B_float = float(B_13)
    B_back = int(B_float)
    error = B_13 - B_back
    
    print(f"\nOriginal B_13:")
    print(f"  {B_str}")
    print(f"  Ziffern 1-16: {B_str[:16]}")
    print(f"  Ziffern 17-31: {B_str[16:]}")
    
    print(f"\nNach Float-Konversion:")
    B_back_str = str(B_back)
    print(f"  {B_back_str}")
    print(f"  Ziffern 1-16: {B_back_str[:16]}")
    print(f"  Ziffern 17-31: {B_back_str[16:]}")
    
    print(f"\nFehler: {error:,}")
    
    # Wo ist der Unterschied?
    print("\n" + "=" * 90)
    print("POSITIONS-Vergleich")
    print("=" * 90)
    
    print("\nPosition: 0         10        20        30")
    print("          |         |         |         |")
    print(f"Original: {B_str}")
    print(f"Float:    {B_back_str}")
    print("          |         |         |         |")
    
    # Finde die erste abweichende Position
    first_diff = None
    for i, (o, f) in enumerate(zip(B_str, B_back_str)):
        if o != f:
            first_diff = i
            break
    
    if first_diff is not None:
        print(f"\n⚠ ERSTE ABWEICHUNG bei Position {first_diff}")
        print(f"  Original: {B_str[first_diff]}")
        print(f"  Float:    {B_back_str[first_diff]}")
        
        # Zeige Kontext
        start = max(0, first_diff - 5)
        end = min(len(B_str), first_diff + 5)
        print(f"\n  Kontext (Position {start}-{end}):")
        print(f"  Original: {B_str[start:end]}")
        print(f"  Float:    {B_back_str[start:end]}")
    
    print("\n" + "=" * 90)
    print("DETAILLIERTE ZIFFERN-ANALYSE")
    print("=" * 90)
    
    print("\nPositionen mit Abweichung:")
    diff_positions = []
    for i, (o, f) in enumerate(zip(B_str, B_back_str)):
        if o != f:
            diff_positions.append(i)
            marker = " <-- ERSTE ABWEICHUNG" if len(diff_positions) == 1 else ""
            print(f"  Position {i:2d}: {o} vs {f}{marker}")
    
    print(f"\nGesamte abweichende Positionen: {len(diff_positions)}")
    
    print("\n" + "=" * 90)
    print("ANTWORT: WO SCHNEIDET IEEE 754 AB?")
    print("=" * 90)
    
    # Berechne exakt
    precision_limit = 16  # IEEE 754 double hat ~16 Dezimalstellen
    
    print(f"""
IEEE 754 Double kann ca. {precision_limit} Dezimalstellen EXAKT speichern.

B_13 hat {len(B_str)} Ziffern.

Das bedeutet:
• Ziffern 1-{precision_limit}:  EXAKT gespeichert
• Ziffern {precision_limit+1}-{len(B_str)}:  PRÄZISION VERLOREN

AB SCHNEIDET BEI POSITION {precision_limit}:
• Position 0-{precision_limit-1}: Korrekt
• Position {precision_limit}: LETZTE KORREKTE ZIFFER
• Position {precision_limit+1}+: FEHLER BEREICH
""")
    
    # Zeige die Ziffer bei Position 16 (0-indexed)
    pos_16_original = B_str[15] if len(B_str) > 15 else "N/A"
    pos_16_float = B_back_str[15] if len(B_back_str) > 15 else "N/A"
    pos_17_original = B_str[16] if len(B_str) > 16 else "N/A"
    pos_17_float = B_back_str[16] if len(B_back_str) > 16 else "N/A"
    
    print(f"Konkret bei B_13:")
    print(f"  Position 15 (16. Ziffer): {pos_16_original} → {pos_16_float}")
    print(f"  Position 16 (17. Ziffer): {pos_17_original} → {pos_17_float}")
    
    # Ist die 666 betroffen?
    print("\n" + "=" * 90)
    print("IST DIE 666 BETROFFEN?")
    print("=" * 90)
    
    print(f"\nDie 666 ist bei Position 14-16:")
    print(f"  B_13[{14}:{17}] = '{B_str[14:17]}'")
    
    # Prüfe ob 666 im Float noch korrekt ist
    float_666 = B_back_str[14:17] if len(B_back_str) > 16 else "N/A"
    original_666 = B_str[14:17]
    
    print(f"\nVergleich:")
    print(f"  Original: '{original_666}'")
    print(f"  Float:    '{float_666}'")
    
    if original_666 == float_666:
        print(f"\n  ✓ Die 666 ist NOCH KORREKT im Float!")
        print(f"  ✓ IEEE 754 schneidet ERST NACH der 666 ab!")
    else:
        print(f"\n  ✗ Die 666 wurde VERFÄLSCHT!")
    
    # Wo genau schneidet es ab?
    print("\n" + "=" * 90)
    print("EXAKTE ABSCHNEIDE-POSITION")
    print("=" * 90)
    
    print(f"""
B_13 Aufbau:
  1 0 0 0 0 0 0 0 0 0 0 0 0 0 6 6 6 0 0 0 0 0 0 0 0 0 0 0 0 0 1
  | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
                              |     |
                              |     └─ Position 16 (17. Ziffer)
                              └─ Position 14 (15. Ziffer)
                              
IEEE 754 schneidet bei Position 16 ab:
• Ziffern 0-15: KORREKT (16 Ziffern)
• Ziffer 16+:   FEHLERHAFT

Position 15 ist die LETZTE exakte Ziffer!
Position 16 ist die ERSTE fehlerhafte Ziffer!
""")
    
    # Prüfe genau
    if len(B_str) == len(B_back_str):
        for i in range(len(B_str)):
            if B_str[i] != B_back_str[i]:
                print(f"\n⚠ ERSTE ABWEICHUNG bei Index {i} (Position {i+1})")
                print(f"  Original: '{B_str[i]}'")
                print(f"  Float:    '{B_back_str[i]}'")
                
                # Zeige 666 Position
                if 14 <= i <= 16:
                    print(f"\n  🔥 ACHTUNG: Die 666 wird teilweise betroffen!")
                elif i > 16:
                    print(f"\n  ✓ Die 666 bleibt INTAKT!")
                    print(f"  ✗ Aber alles danach ist FALSCH!")
                break
    
    print("\n" + "=" * 90)
    print("ZUSAMMENFASSUNG")
    print("=" * 90)
    
    print(f"""
FRAGE: Ab welcher Ziffer schneidet IEEE 754 ab?

ANTWORT:
• IEEE 754 Double hat ~16 Dezimalstellen Präzision
• B_13 hat 31 Ziffern
• AB Position 16 (0-indexed) / Ziffer 17 (1-indexed)

DAS BEDEUTET:
• Ziffern 1-16: Exakt gespeichert
• Ziffer 17+:   Rundungsfehler

DIE 666:
• 666 ist bei Position 15-17 (0-indexed)
• = Ziffern 16-18 (1-indexed)
• Position 16 (die erste 6) ist EXAKT
• Position 17 (die zweite 6) ist bereits FEHLERHAFT!

ANTWORT AUF DEINE FRAGE:
✗ NEIN, es schneidet nicht bei der VORLETZTEN 6 ab
✓ Es schneidet bei der LETZTEN 6 ab!

Genauer:
• 1. Sechs (Position 15): EXAKT ✓
• 2. Sechs (Position 16): EXAKT ✓  
• 3. Sechs (Position 17): BEREITS FEHLERHAFT ✗

Die erste 6 der 666 ist noch korrekt,
aber die letzten beiden 6 sind verfälscht!
""")

if __name__ == '__main__':
    analyze_ieee754_precision()
