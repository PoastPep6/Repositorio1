import tkinter as tk
from tkinter import messagebox
import re

def es_primo(n):
    if n < 2:
        return False
    return all(map(lambda x: n % x != 0, range(2, int(n**0.5) + 1)))

def verificar():
    valor = entrada_var.get()
    if not valor:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un valor.")
        return
    numero = None

    if valor.isdigit():
        numero = int(valor)
    elif " " in valor:
        messagebox.showerror("Error", "Ingresaste un espacio. Solo se permiten entradas sin espacios. ")
    elif re.fullmatch(r"\d+\.\d+",valor):
        messagebox.showerror("Error", "Ingresaste un decimal. Solo se permiten numeros enteros.")
    elif re.fullmatch(r"[a-zA-Z]+",valor):
        messagebox.showerror("Error", "Ingresaste letras. Solo se permiten numeros enteros.")
    elif re.fullmatch(r"[^\d\.]",valor):
        messagebox.showerror("Error", "Ingresaste caracteres especiales. Solo se permiten numeros enteros.")
    else:
        messagebox.showerror("Error", "Entrada no valida. Solo se permiten numeros enteros.")
        entrada_var.set("")
        return

    if numero is not None:
        if es_primo(numero):
            resultado.set(f"{numero} es primo.")
        else:
            resultado.set(f"{numero} no es primo.")



ventana = tk.Tk()
ventana.title("Verificador de Números Primos")

entrada_var = tk.StringVar()

tk.Label(ventana, text="Ingresa un número:").pack(pady=5)

entrada_num = tk.Entry(ventana, textvariable=entrada_var)
entrada_num.pack(pady=5)

tk.Button(ventana, text="Verificar", command=verificar).pack(pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=5)

ventana.mainloop()
