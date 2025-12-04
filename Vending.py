import tkinter as tk
import os
from tkinter import messagebox

folder = os.path.dirname(__file__)

root = tk.Tk()
root.title("Vending Machine Kel 1")
root.geometry("1000x800")

wadah_utama = tk.Frame(root)
wadah_utama.pack(fill="both", expand=True)

frame_kiri = tk.Frame(wadah_utama, bg="white")
frame_kiri.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame_kanan = tk.Frame(wadah_utama, bg="lightgray", width=350)
frame_kanan.pack(side="right", fill="y", padx=10, pady=10)
frame_kanan.pack_propagate(False)

tempat_uang = tk.Frame(frame_kanan, bg="lightgray",)
tempat_uang.pack(pady=20, fill="x")
tk.Label(tempat_uang, text="Masukkan Uang anda:", bg="#FEFEFE").pack(side="left", padx=10)

frame_input = tk.Frame(tempat_uang, bg="lightgray")
frame_input.pack(pady=5)

entry_uang = tk.Entry(frame_input, width=10)
entry_uang.pack(side="left", padx=5)

btn_uang = tk.Button(frame_input, text="Masukkan", bg="lightblue", command=lambda: tambah_uang())
btn_uang.pack(side="left")

lbl_saldo = tk.Label(tempat_uang, text="Saldo: Rp 0", font=("arial", 12, "bold"),fg="white", bg="blue")
lbl_saldo.pack(pady=10)


def layout_gambar(nama_file):
    path = os.path.join(folder, "Pict", nama_file)
    before = tk.PhotoImage(file=path)
    after = before.subsample(5, 5)
    return after

daftar_produk = [
   {"file": "air.png", "nama": "Air Mineral", "harga": 3000},
    {"file": "nescafe.png", "nama": "Nescafe", "harga": 5000},
    {"file": "pepsi.png", "nama": "Pepsi Blue", "harga": 6000},
    {"file": "pillows.png", "nama": "Pillows", "harga": 2000},
    {"file": "chikiballs.png","nama": "Chiki Balls", "harga": 2500},
    {"file": "chitato.png", "nama": "Chitato", "harga": 3500},
    {"file": "fanta.png", "nama": "Fanta", "harga": 5000},
    {"file": "walens.png", "nama": "Walens", "harga": 4000},
    {"file": "cheetos.png", "nama": "Cheetos", "harga": 3000},
    
    {"file": "yupi.png", "nama": "Permen Yupi", "harga": 7500},
    {"file": "fruittea.png", "nama": "Fruittea", "harga": 4500},
    {"file": "floridina.png", "nama": "Floridina", "harga": 3500},
    {"file": "chitatoo.png", "nama": "Chitato Pedas", "harga": 5500},
    {"file": "kusuka.png", "nama": "Kusuka", "harga": 3000},
    {"file": "lite.png", "nama": "Lite","harga": 4000},
    {"file": "milku.png", "nama": "Milku", "harga": 3500},
    {"file": "c yogurt.png", "nama": "Cimory Yogurt","harga": 4500},
    {"file": "coca cola.png", "nama": "Coca Cola","harga": 5500}, 

     {"file": "drink yogurt.png", "nama": "Drink Yogurt",  "harga": 7500},
    {"file": "momogi.png",   "nama": "Momogi",  "harga": 1500},
    {"file": "pocari sweat.png", "nama": "Pocari Sweat",  "harga": 6500},
    {"file": "yakult.png",   "nama": "Yakult", "harga": 2500},
    {"file": "nescafe latte.png","nama": "Nescafe Latte",  "harga": 9000},
    {"file": "pringles.png", "nama": "Pringles","harga": 8000},
    {"file": "olatte.png", "nama": "Olatte", "harga": 3500},
    {"file": "good day.png", "nama": "Good Day","harga": 4500},
    {"file": "popcorn.png", "nama": "Popcorn","harga": 5500},
]

halaman_ini = 0
saldo = 0

def tambah_uang():
    global saldo
    uang_masuk = entry_uang.get()
    if uang_masuk.isdigit():
        saldo += int(uang_masuk)
        lbl_saldo.config(text=f"Saldo: Rp {saldo:,}")
        entry_uang.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Masukkan nominal angka yang benar!")


def ganti_halaman(arah):
    global halaman_ini
    halaman_baru = halaman_ini + arah
    if halaman_baru < 0:
        return
    if (halaman_baru * 9) >= len(daftar_produk):
        return
    
    halaman_ini = halaman_baru

    tampilkan_etalase(halaman_ini)

def tap_btn(angka):
    Layar.insert(tk.END, angka)
def clear_btn():
    Layar.delete(0, tk.END)

def show_struk(produk, kembalian):
    struk_window = tk.Toplevel(root)
    struk_window.title("Struk Pembelian")
    struk_window.geometry("300x450")
    nama_file = produk["file"]
    gambar = simpan_gambar.get(nama_file)

    if gambar:
        tk.Label(struk_window, image=gambar).pack(pady=20)

    info_transaksi = f"Barang yang dibeli:\n{produk['nama']}\n\nKembalian Anda:\nRp {kembalian:,}"  
    tk.Label(struk_window, text=info_transaksi, font=("arial", 12, "bold")).pack(pady=10)
    tk.Button(struk_window, text="Ambil", bg="green", fg="white", command=struk_window.destroy).pack(pady=20)

def bayar():
    global saldo
    isi_layar = Layar.get()
    if isi_layar == "":
        return
    if not isi_layar.isdigit():
        messagebox.showerror("Tolong masukkan angka saja!")
        clear_btn()
        return
    
    tap_nomor = int(isi_layar)
    index_barang = (halaman_ini * 9) + (tap_nomor - 1)
    
    if index_barang < 0 or index_barang >= len(daftar_produk):
        messagebox.showwarning("Produk tidak tersedia")
        clear_btn()
        return

    beli_barang = daftar_produk[index_barang]
    harga = beli_barang["harga"]

    if saldo >= harga:
        kembalian = saldo - harga
        saldo = 0
        lbl_saldo.config(text=f"Saldo: Rp {saldo}")
        show_struk(beli_barang, kembalian)
        clear_btn()
    
    else:
        kurang = harga - saldo
        messagebox.showerror("Gagal", f"Uang anda kurang!\nHarga: Rp {harga:,}\nKurang: Rp {kurang:,}")
        clear_btn()
    

simpan_gambar = {}

etalase = tk.Frame(frame_kiri, bg="white")
etalase.pack(fill="both", expand=True)

def tampilkan_etalase(nomor_halaman):

    for widget in etalase.winfo_children():
        widget.destroy()

    indeks_awal = nomor_halaman * 25
    indeks_akhir = indeks_awal + 25

    halaman_tampil = daftar_produk[indeks_awal : indeks_akhir]

    baris = 0
    kolom = 0

    for item in halaman_tampil:
        
        nama_file_gambar = item["file"]
        nama_produk_asli = item["nama"]  
        harga_produk_asli = item["harga"] 
        
        if nama_file_gambar not in simpan_gambar:
            simpan_gambar[nama_file_gambar] = layout_gambar(nama_file_gambar)
        
        gambar_jadi = simpan_gambar[nama_file_gambar]

        kotak_produk = tk.Frame(etalase, bd=2, relief="groove", bg="white", width=105, height=140)
        kotak_produk.grid(row=baris, column=kolom, padx=5, pady=5)
        kotak_produk.pack_propagate(False)

        nomor = (baris * 5) + kolom + 1
        lbl_no = tk.Label(kotak_produk, text=str(nomor), font=("arial, 7"))
        lbl_no.place(relx=1.0, x=0, y=0, anchor="ne")
        
        lbl_img = tk.Label(kotak_produk, image=gambar_jadi, bg="white")
        lbl_img.pack(pady=(10, 0))
        
        lbl_nama = tk.Label(kotak_produk, text=nama_produk_asli, font=("arial", 7, "bold"), bg="white", wraplength=80)
        lbl_nama.pack(padx=0, pady=0)
        
        text_harga = f"Rp {harga_produk_asli:,}"
        lbl_harga = tk.Label(kotak_produk, text=text_harga, font=("arial", 7), fg="green", bg="white")
        lbl_harga.pack(pady=0, padx=0)

        kolom += 1
        if kolom > 4:
            kolom = 0
            baris += 1

Kontrol = tk.Frame(frame_kanan, bg="lightgray")
Kontrol.pack(pady=20)

Layar = tk.Entry(Kontrol, width=20, font=("arial", 20), justify="right")
Layar.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

list_button = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

baris_btn = 1
kolom_btn = 0

for angka in list_button:
    btn = tk.Button(Kontrol, text=angka, width=5, height=1, font=("arial", 12, "bold"))
    btn.config(command=lambda x=angka: tap_btn(x))
    btn.grid(row=baris_btn, column=kolom_btn, padx=5, pady=5, sticky="ew", ipady=5)
    kolom_btn += 1

    if kolom_btn > 2:
        kolom_btn = 0
        baris_btn += 1

btn_clear = tk.Button(Kontrol, text="C", font=("arial", 12, "bold"), bg="red", fg="white")
btn_clear.config(command=clear_btn)
btn_clear.grid(row=4, column=0, padx=2, pady=2, sticky="ew", ipady=5)

btn_0 = tk.Button(Kontrol, text="0", font=("arial", 12, "bold"), width=5)
btn_0.config(command=lambda: tap_btn("0"))
btn_0.grid(row=4, column=1, padx=2, pady=2, sticky="ew", ipady=5)

btn_enter = tk.Button(Kontrol, text="Enter", font=("arial", 12, "bold"), bg="green", fg="white")
btn_enter.config(command=bayar)
btn_enter.grid(row=4, column=2, padx=2, pady=2, sticky="ew", ipady=5)

btn_prev = tk.Button(Kontrol, text="<", font=("arial", 12, "bold"), bg="orange")

btn_prev.config(command=lambda: ganti_halaman(-1)) 
btn_prev.grid(row=5, column=0, padx=2, pady=5, sticky="ew", ipady=5)

lbl_hal = tk.Label(Kontrol, text="PAGE", font=("arial", 10))
lbl_hal.grid(row=5, column=1, padx=2, pady=5)

btn_next = tk.Button(Kontrol, text=">", font=("arial", 12, "bold"), bg="orange")

btn_next.config(command=lambda: ganti_halaman(1))
btn_next.grid(row=5, column=2, padx=2, pady=5, sticky="ew", ipady=5)

tampilkan_etalase(halaman_ini)

root.mainloop()