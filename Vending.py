import tkinter as tk
import os

folder = os.path.dirname(__file__)

root = tk.Tk()
root.title("Vending Machine Kel 1")
root.geometry("400x700")

def layout_gambar(nama_file):
    path = os.path.join(folder, "Pict", nama_file)
    before = tk.PhotoImage(file=path)
    after = before.subsample(5, 5)
    return after

img_pillows = layout_gambar("pillows.png")
img_chitato = layout_gambar("chitato.png")
img_wallens = layout_gambar("walens.png")
img_air = layout_gambar("air.png")
img_chikibalss = layout_gambar("chikiballs.png")
img_pepsi = layout_gambar("pepsi.png")
img_fanta = layout_gambar("fanta.png")
img_nescafe = layout_gambar("nescafe.png")
img_cheetos = layout_gambar("cheetos.png")

etalase = tk.Frame(root, bg="white")
etalase.pack(pady="20")

label1 = tk.Label(etalase, image=img_air)
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(etalase, image=img_nescafe)
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(etalase, image=img_pepsi)
label3.grid(row=0, column=2, padx=5, pady=5)

label4 = tk.Label(etalase, image=img_pillows)
label4.grid(row=1, column=0, padx=5, pady=5)

label5 = tk.Label(etalase, image=img_chikibalss)
label5.grid(row=1, column=1, padx=5, pady=5)

label6 = tk.Label(etalase, image=img_chitato)
label6.grid(row=1, column=2, padx=5, pady=5)

label7 = tk.Label(etalase, image=img_fanta)
label7.grid(row=2, column=0, padx=5, pady=5)

label8 = tk.Label(etalase, image=img_wallens)
label8.grid(row=2, column=1, padx=5, pady=5)

label9 = tk.Label(etalase, image=img_cheetos)
label9.grid(row=2, column=2, padx=5, pady=5)

Kontrol = tk.Frame(root, bg="lightgray")
Kontrol.pack(padx=10, pady=10)

Layar = tk.Entry(Kontrol, width=20, font=("arial", 24), justify="right")
Layar.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

list_button = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

baris = 1
kolom = 0

for angka in list_button:
    btn = tk.Button(Kontrol, text=angka, width=5, height=2, font=("arial", 12, "bold"))
    btn.grid(row=baris, column=kolom, padx=5, pady=5, sticky="ew", ipady=5)
    kolom += 1

    if kolom > 2:
        kolom = 0
        baris += 1


root.mainloop()