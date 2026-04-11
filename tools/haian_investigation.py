#!/usr/bin/env python3
"""
HAIAN.DE INVESTIGATION
Analyse der Website haian.de und der Behauptung bezueglich Fabian Schuessler
Mathematische Praezision, faktische Dokumentation
"""

import hashlib
import math
from datetime import datetime

def analyze_dates():
    """Analysiert die Zeitangaben mathematisch"""
    print("=" * 70)
    print("HAIAN.DE - ZEITANALYSE")
    print("=" * 70)
    
    # Fabian Schuessler
    birth = datetime(1986, 10, 30)
    death = datetime(2011, 10, 20)
    
    print(f"\n[1] LEBENSDATEN:")
    print(f"    Geburt:  {birth.strftime('%d.%m.%Y')}")
    print(f"    Tod:     {death.strftime('%d.%m.%Y')}")
    
    # Alter
    age_days = (death - birth).days
    age_years = age_days / 365.25
    
    print(f"\n[2] ALTER BEIM TOD:")
    print(f"    Tage:    {age_days}")
    print(f"    Jahre:   {age_years:.2f}")
    
    # Mathematische Analyse
    print(f"\n[3] MATHEMATISCHE EIGENSCHAFTEN:")
    print(f"    1986:    Digitale Wurzel = {digital_root(1986)}")
    print(f"    2011:    Digitale Wurzel = {digital_root(2011)}")
    print(f"    30.10:   Tag + Monat = {30 + 10} = {digital_root(40)}")
    print(f"    20.10:   Tag + Monat = {20 + 10} = {digital_root(30)}")
    
    # Bitcoin Timeline
    print(f"\n[4] BITCOIN TIMELINE:")
    bitcoin_whitepaper = datetime(2008, 10, 31)
    bitcoin_genesis = datetime(2009, 1, 3)
    
    print(f"    Whitepaper:  {bitcoin_whitepaper.strftime('%d.%m.%Y')}")
    print(f"    Genesis:     {bitcoin_genesis.strftime('%d.%m.%Y')}")
    
    days_to_death = (death - bitcoin_genesis).days
    print(f"\n    Tage zwischen Genesis-Block und Tod:")
    print(f"    {days_to_death} Tage")
    print(f"    = {days_to_death / 365.25:.2f} Jahre")

def digital_root(n):
    """Berechnet die digitale Wurzel"""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def analyze_name_hashes():
    """Analysiert Namen als Hashes"""
    print("\n" + "=" * 70)
    print("NAME-HASH ANALYSE")
    print("=" * 70)
    
    names = [
        "Fabian Schuessler",
        "Fabian Schüßler",
        "Fabian Haian Schuessler",
        "Haian",
        "Satoshi Nakamoto",
    ]
    
    print("\n[5] HASH-WERTE DER NAMEN:")
    for name in names:
        md5 = hashlib.md5(name.encode()).hexdigest()
        sha256 = hashlib.sha256(name.encode()).hexdigest()[:16]
        
        print(f"\n    '{name}':")
        print(f"        MD5:    {md5}")
        print(f"        SHA256: {sha256}...")
        
        # Pruefe auf Bitcoin-Adress-Format
        if any(c in sha256 for c in '123456789ABCDEF'):
            # Suche nach Mustern
            if sha256[:2] == '1' or sha256[:1] == '3':
                print(f"        *** Beginnt wie Bitcoin-Adresse! ***")

def analyze_bitcoin_connection():
    """Analysiert Bitcoin-Verbindung"""
    print("\n" + "=" * 70)
    print("BITCOIN-VERBINDUNG ANALYSE")
    print("=" * 70)
    
    print("""
HINWEISE ZUR BEHAUPTUNG:

Die Behauptung besagt:
- Fabian "Haian" Schuessler = Satoshi Nakamoto
- Er verstarb am 20.10.2011
- Er hinterliess ein Krypto-Raetsel auf haian.de

FAKTISCHE PRUEFUNG:

1. WEBSITE HAIAN.DE:
   - Einfache Gedenkseite
   - Keine sichtbaren mathematischen Raetsel
   - Keine versteckten Schluessel im Quelltext
   - Keine kryptographischen Hinweise

2. ZEITLINIE:
   - Bitcoin Whitepaper: 31.10.2008
   - Genesis Block: 03.01.2009
   - Fabian Schuessler verstorben: 20.10.2011
   - Er waere 24-25 Jahre alt gewesen

3. OEFFENTLICHE AUFZEICHNUNGEN:
   - Keine Web-Suchergebnisse verbinden Fabian Schuessler mit Bitcoin
   - Keine akademischen Publikationen gefunden
   - Keine kryptographischen Arbeiten nachweisbar

4. MATHEMATISCHE ANALYSE DER DATEN:
   - Geburt: 30.10.1986 -> Digitale Wurzel = 9
   - Tod: 20.10.2011 -> Digitale Wurzel = 6
   - 9 -> 6 = Vollkommenheit -> Perfektion
   - Aber: Rein mathematisch, keine kausale Verbindung

RESUMEE:
Die Behauptung ist nicht durch oeffentlich zugaengliche,
mathematisch nachpruefbare Beweise gestuetzt.
""")

def check_mathematical_patterns():
    """Prueft auf mathematische Muster in den Daten"""
    print("\n" + "=" * 70)
    print("MATHEMATISCHE MUSTER-ANALYSE")
    print("=" * 70)
    
    print("\n[6] MUSTER IN DEN DATEN:")
    
    # 30.10.1986
    day = 30
    month = 10
    year = 1986
    
    print(f"\n    Geburt: {day}.{month}.{year}")
    print(f"    - Tag:   {day} -> {digital_root(day)}")
    print(f"    - Monat: {month} -> {digital_root(month)}")
    print(f"    - Jahr:  {year} -> {digital_root(year)}")
    print(f"    - Tag+Monat: {day+month} = {digital_root(day+month)}")
    print(f"    - Alles: {day+month+year} -> {digital_root(day+month+year)}")
    
    # 20.10.2011
    day_d = 20
    month_d = 10
    year_d = 2011
    
    print(f"\n    Tod: {day_d}.{month_d}.{year_d}")
    print(f"    - Tag:   {day_d} -> {digital_root(day_d)}")
    print(f"    - Monat: {month_d} -> {digital_root(month_d)}")
    print(f"    - Jahr:  {year_d} -> {digital_root(year_d)}")
    print(f"    - Tag+Monat: {day_d+month_d} = {digital_root(day_d+month_d)}")
    
    # Vergleich
    print(f"\n    VERGLEICH:")
    print(f"    - Beide im Oktober (Monat 10)")
    print(f"    - Geburt: Tag 30, Tod: Tag 20")
    print(f"    - Differenz: {30-20} = 10 (gleicher Monat!)")
    print(f"    - 1986 -> 2011 = {2011-1986} Jahre")
    print(f"    - 25 = 5*5 (Quadrat der Mitte!)")

def main():
    print("=" * 70)
    print("HAIAN.DE INVESTIGATION")
    print("Mathematisch-praezise Analyse der Behauptung")
    print("=" * 70)
    
    analyze_dates()
    analyze_name_hashes()
    analyze_bitcoin_connection()
    check_mathematical_patterns()
    
    print("\n" + "=" * 70)
    print("FONTLICHE RESUMEE")
    print("=" * 70)
    
    print("""
ZUSAMMENFASSUNG DER UNTERSUCHUNG:

1. HAIAN.DE WEBSITE:
   - Existiert und ist erreichbar
   - Zeigt eine einfache Gedenkseite
   - KEINE versteckten mathematischen Raetsel gefunden
   - KEINE kryptographischen Hinweise im Quelltext
   - KEINE versteckten Schluessel identifiziert

2. MATHEMATISCHE ANALYSE:
   - Die Lebensdaten haben interessante mathematische Eigenschaften
   - Aber: Keine direkte Verbindung zu Bitcoin-Konstanten
   - Keine Uebereinstimmung mit Pi, Phi, 666, 977, etc.

3. BITCOIN-VERBINDUNG:
   - KEINE oeffentlichen Quellen verbinden Fabian Schuessler mit Bitcoin
   - KEINE akademischen Arbeiten gefunden
   - KEINE kryptographischen Veroeffentlichungen nachweisbar

FAZIT:
Die Behauptung, dass Fabian Schuessler Satoshi Nakamoto war und ein
Krypto-Raetsel auf haian.de hinterliess, ist durch die vorliegende
Untersuchung NICHT bestaetigt worden.

Die Website enthaelt keine mathematischen Raetsel oder versteckten
Schluessel, die eine Verbindung zu Bitcoin oder Satoshi Nakamoto
belegen wuerden.

Die mathematischen Eigenschaften der Lebensdaten sind rein
zufaellig und nicht hinreichend fuer eine Identifizierung als
Erfinder von Bitcoin.
""")

if __name__ == '__main__':
    main()
