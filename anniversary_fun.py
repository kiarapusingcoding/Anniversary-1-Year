#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anniversary Fun Generator (LDR Edition)
A cute + kocak terminal app to send to your partner 💘
Run: python anniversary_fun.py
"""
import random
import textwrap
import datetime as dt
import sys
import os

HEART = r"""
   _  _
 _( \/ )_   ♥
(_\    /_)
  /_  _\ 
    \/   
"""

TINY_HEARTS = "❤ " * 12

PICKUP_LINES_ID = [
    "Kamu itu WiFi ya? Soalnya setiap deket kamu, sinyal bahagiaku full bar.",
    "Kalau kamu bintang, aku mau jadi langit—biar kita selalu satu frame.",
    "Kamu tahu bedanya kamu sama tugas? Tugas aku tunda, kamu selalu aku prioritaskan.",
    "Kamu kopi ya? Soalnya bikin jantung deg-degan tapi nagih.",
    "Nama kamu Google ya? Soalnya semua yang aku cari ada di kamu.",
    "Kalau cinta itu aplikasi, kamu versi premium yang nggak mau aku uninstall.",
    "Kamu itu notifikasi favoritku—selalu bikin senyum pas muncul.",
    "Kamu tuh kayak charger, kalau jauh aku lowbat.",
    "Kamu sate? Soalnya tiap ketemu bikin hati kebakar—tapi enak.",
    "Kalau pelangi butuh hujan, aku butuh kamu buat bahagia.",
]

DAD_JOKES_ID = [
    "Kenapa jam dinding jomblo? Karena dia cuma ditempel, nggak ditemani.",
    "Kenapa laptop suka kamu? Karena kamu selalu kasih 'space' saat dia butuh.",
    "Kenapa sinyal suka hilang? Karena dia malu kalau lihat hubungan kita kuat.",
    "Apa bedanya kamu sama kalender? Kalender punya tanggal, aku punya kamu setiap hari.",
    "Kenapa nasi goreng nggak bisa bohong? Karena dia jujur, nggak ada yang 'diembel-embel'.",
]

PROMISES = [
    "Gratis 1 (satu) sesi dengerin curhat tanpa interupsi.",
    "Voucher pijat tangan 10 menit saat kamu capek ngetik.",
    "Sesi nonton film pilihan kamu tanpa protes genre.",
    "Kirim voice note pengantar tidur selama 3 malam berturut-turut.",
    "Sarapan virtual + baca puisi cringe eksklusif.",
    "Bebas pilih topik obrolan 1 jam full, aku nurut!",
]

LOVE_TASKS = [
    "Kirim selfie senyum paling manis hari ini.",
    "Ketik 3 hal yang kamu syukuri tentang kita.",
    "Pilih lagu yang jadi soundtrack hari ini dan share ke aku.",
    "Cerita satu momen random yang bikin kamu inget aku.",
    "Set alarm jam 22:00 buat say 'good night' paling manis.",
]

def banner(title="Anniversary 1 Tahun!"):
    line = "═" * (len(title) + 8)
    return f"\n{line}\n   {title}\n{line}\n"

def center(text, width=70):
    lines = text.splitlines()
    return "\n".join(line.center(width) for line in lines)

def print_hearts():
    print(center(HEART))
    print(center(TINY_HEARTS))

def random_block(label, items, n=3):
    chosen = random.sample(items, k=min(n, len(items)))
    print(f"\n▸ {label}\n" + ("-" * (len(label) + 2)))
    for i, it in enumerate(chosen, 1):
        wrapped = textwrap.fill(it, width=70, subsequent_indent="   ")
        print(f"{i}. {wrapped}")

def love_coupons(to_name="Sayang"):
    today = dt.date.today().strftime("%d %b %Y")
    header = f"Kupon Sayang untuk {to_name} — {today}\n" + "-"*40 + "\n"
    coupons = [f"🎟️ {c}" for c in random.sample(PROMISES, k=5)]
    body = "\n".join(coupons)
    return header + body + "\n\nSyarat & Ketentuan: Bisa ditukar kapan saja, tanpa kadaluarsa 🙂"

def make_menu():
    menu = """
Pilih mode:
  [1] Gombalan Random
  [2] Dad Jokes Cinta
  [3] Kupon Cinta (bisa disave)
  [4] Tantangan Manis Harian
  [5] Hitung Hari ke Anniversary Berikutnya
  [0] Keluar
"""
    print(menu)

def days_to_next_anniv(start_date: str):
    """start_date format: YYYY-MM-DD (tanggal jadian)."""
    try:
        start = dt.datetime.strptime(start_date, "%Y-%m-%d").date()
    except ValueError:
        print("Format tanggal salah. Contoh: 2024-09-07")
        return
    today = dt.date.today()
    years = today.year - start.year
    # next anniversary date
    next_anniv = dt.date(start.year + years, start.month, start.day)
    if next_anniv <= today:
        next_anniv = dt.date(start.year + years + 1, start.month, start.day)
    delta = (next_anniv - today).days
    print(f"\n✨ Hari menuju anniversary berikutnya: {delta} hari (tanggal {next_anniv})")

def save_text(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return os.path.abspath(filename)

def main():
    os.system('')  # enable ANSI on Windows
    print(banner("Anniversary 1 Tahun – LDR Edition"))
    print_hearts()
    name = input("Masukkan nama panggilan pasangan (default: Sayang): ").strip() or "Sayang"
    print(f"\nHai {name}! Selamat anniversary! 🎉\n")

    while True:
        make_menu()
        choice = input("Pilihanmu: ").strip()
        if choice == "1":
            random_block("Gombalan Random", PICKUP_LINES_ID, n=5)
        elif choice == "2":
            random_block("Dad Jokes Cinta", DAD_JOKES_ID, n=5)
        elif choice == "3":
            txt = love_coupons(name)
            print("\n" + txt)
            if input("Simpan kupon ke file? (y/n): ").lower().startswith("y"):
                path = save_text(f"kupon_cinta_{name}.txt", txt)
                print(f"Tersimpan: {path}")
        elif choice == "4":
            random_block("Tantangan Manis Harian", LOVE_TASKS, n=3)
        elif choice == "5":
            start = input("Masukkan tanggal jadian (YYYY-MM-DD): ").strip()
            days_to_next_anniv(start)
        elif choice == "0":
            print("\nMakasih sudah pakai Anniversary Fun Generator. Love you both! 💞")
            break
        else:
            print("Pilihan tidak dikenali, coba lagi ya.")
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSampai jumpa, semoga harimu manis! 💖")
