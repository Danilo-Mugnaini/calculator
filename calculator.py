#Importar Bibliotecas
import tkinter as tk
from tkinter import messagebox

#Tela Principal
root = tk.Tk()
root.title("Calculadora Alpha 1.0") #Nome na tela
root.geometry("400x500") #Tamanho da tela

#Tela de input e output
display_frame = tk.Frame(root)
display_frame.pack()

#String para segurar texto de display
display_text = tk.StringVar()

#Widget de entrada do display
display = tk.Entry(display_frame, textvariable=display_text, font=("Helvetica", 24), justify='right', bd=20, insertwidth=4)
display.grid(row=0, column=0)

#Definir função de click
def button_click(event):
    current = display_text.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current))
            display_text.set(result)
        except Exception as e:
            messagebox.showerror("Erro", "Input Inválido")
    elif button_text == "C":
        display_text.set("")
    else:
        display_text.set(current + button_text)

#Criar disposição dos botões
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

button_config = {
    'font': ("Helvetica", 18),
    'width': 5,
    'height': 2,
    'bd': 1,
    'relief': 'ridge',
    'bg': '#f0f0f0',
    'fg': '#000000',
    'activebackground': '#d9d9d9',
    'activeforeground': '#000000'
}

row = 0
col = 0
for button in buttons:
    b = tk.Button(button_frame, text=button, **button_config)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

#Rodar app
root.mainloop()
