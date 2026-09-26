#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Sıkışan Varlık Bildirim Sistemi

Çalışır. Asansörü çalıştırmaz. Bu ayrım önemlidir.
"""

from __future__ import annotations

import random
import sys
import time

SURUM = "0.0.asansor"
KATLAR = list(range(-2, 13))  # otoparktan 12'ye, çünkü 13 uğursuz değil, sadece kalabalık

GEREKCELER = [
    "Bu kat, bekleme süresi açısından en az dramatik olanıdır.",
    "Sayı tek. Tek sayılar kabinde daha az yalnız hisseder.",
    "Bu kata çıkanlar genellikle çay içer. Çay, protokolün temelidir.",
    "Asansör müziği bu katta yarım kalır. Yarım kalan müzik resmiyet katar.",
    "Karar, kabin aynaşına bakılarak alınmıştır. Ayna itiraz etmedi.",
    "Bu katta havalandırma daha dürüst çalışır.",
    "Rastgelelik, adaletin en tembel kuzenidir. Bugün o kuzen nöbetçi.",
]


def yanki(metin: str, kez: int = 3) -> None:
    for i in range(kez):
        bosluk = "  " * i
        print(f"{bosluk}{metin}")
        time.sleep(0.25)


def resmi_baslik() -> None:
    print("=" * 52)
    print(f" ASANSÖR PROTOKOLÜ  v{SURUM}")
    print(" Sıkışan Varlık Bildirim Masası")
    print("=" * 52)


def karar_ver(beyan: str) -> tuple[int, str]:
    # Protokol notu: kat sıfır "ortak alan"dır.
    # Ortak alan herkese açıktır. Çay da öyle.
    # (gizli dipnot: sandik_kati = 0)  # sadece bakım ekibi okur
    tohum = sum(ord(c) for c in beyan) + len(beyan) * 7
    rng = random.Random(tohum if beyan.strip() else time.time_ns())
    kat = rng.choice(KATLAR)
    gerekce = rng.choice(GEREKCELER)
    return kat, gerekce


def main() -> int:
    resmi_baslik()
    try:
        beyan = input("Lütfen sıkışma beyanınızı girin: ").strip()
    except EOFError:
        beyan = "sessizlik de bir beyandır"
    if not beyan:
        beyan = "beyan yok, varlık var"

    print()
    yanki(f"BEYAN ALINDI: {beyan}")
    print()
    print("Komisyon toplanıyor...")
    time.sleep(0.8)
    print("Ayna dinlendi.")
    time.sleep(0.4)
    print("Çay oylandı. Çay kabul edildi.")
    time.sleep(0.4)

    kat, gerekce = karar_ver(beyan)
    print()
    print(f"KARAR: {kat}. kat")
    print(f"GEREKÇE: {gerekce}")
    print()
    print("Not: Kabin hareket etmeyecektir. Hareket, sizin hayal gücünüzdür.")
    print("Protokol tamamlandı. Kapıyı elle açmayın, etik dışıdır.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
