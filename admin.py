## TEGAR RIDWAN

import tkinter as tk
from tkinter import BOTH, LEFT, Button, messagebox as mb
import hashlib
from tkinter.ttk import Label
import mysql.connector

def GetConnection():
    return mysql.connector.connect(
        host='localhost',
        db='db_vending',
        user='root',
        password='',
        port=3306
    )


root = tk.Tk()
root.title("Login Sistem")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

def menu_dashboard():
     root.withdraw()

     dashboard = tk.Toplevel(root)
     dashboard.title("Dashboard")
     dashboard.resizable(False, False)

     user_login = root.username_entry.get()
     tk.Label(dashboard, text=f"Selamat datang, {user_login}!").pack(padx=20, pady=20)
     tk.Label(dashboard, text="Anda berhasil Login").pack(padx=20, pady=10)

     def logout():
         root.username_entry.delete(0, tk.END)
         root.password_entry.delete(0, tk.END)
         root.username_entry.focus_set()
         dashboard.destroy()
         root.deiconify()
         mb.showinfo("Logout", "Anda telah logout dari sistem", parent=root)
     btn_logout = tk.Button(dashboard, text="Logout", command=logout)
     btn_logout.pack(pady=10)


def login():
    namaUser = root.username_entry.get()
    password = root.password_entry.get()
    if not namaUser:
         mb.showwarning("Login Gagal", "Username tidak boleh kosong", parent=root)
    elif not password:
         mb.showwarning("Login Gagal", "Password tidak boleh kosong", parent=root)
         return

    password = hashlib.md5(password.encode()).hexdigest()
    conn = GetConnection()
    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor = conn.cursor()
    cursor.execute(query, (namaUser, password))
    result = cursor.fetchone()
    if  result:     
        mb.showinfo("Login Berhasil", "Selamat, login berhasil", parent=root)
        menu_dashboard()
    else:
        mb.showwarning("Login Gagal", "Username atau password salah", parent=root)
        root.username_entry.focus_set()


frameUtama = tk.Frame(root, bd=10)
frameUtama.pack(fill='both', expand=True)

frData = tk.Frame(frameUtama, bd=5)
frData.pack(fill='both', expand=True)

Label(frData, text="Username").grid(row=0, column=0, padx=10, pady=10)
root.username_entry = tk.Entry(frData)
root.username_entry.grid(row=0, column=1, padx=10, pady=10)

Label(frData, text="Password").grid(row=1, column=0, padx=10, pady=10)
root.password_entry = tk.Entry(frData, show="*")
root.password_entry.grid(row=1, column=1, padx=10, pady=10)

frButton = tk.Frame(frameUtama, bd=5)
frButton.pack(fill='both', expand=True)

root.btnBatal = Button(frButton, text="Batal", width=10, command=root.destroy)
root.btnBatal.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
root.btnLogin = Button(frButton, text="Login", width=10, command=login)
root.btnLogin.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()