import tkinter as tk
from tkinter import messagebox
import json
import os

# Função para carregar compromissos do arquivo JSON
def carregar_compromissos():
    if os.path.exists("compromissos.json"):
        with open("compromissos.json", "r") as arquivo:
            return json.load(arquivo)
    return []

# Função para salvar compromissos no arquivo JSON
def salvar_compromissos():
    compromissos = carregar_compromissos()
    compromisso = entry_compromisso.get()
    data = entry_data.get()
    descricao = entry_descricao.get()
    
    if compromisso and data and descricao:
        compromisso_str = {
            "compromisso": compromisso,
            "data": data,
            "descricao": descricao
        }
        compromissos.append(compromisso_str)

        # Salvar os compromissos no arquivo JSON
        with open("compromissos.json", "w") as arquivo:
            json.dump(compromissos, arquivo, indent=4)

        # Atualizar a lista de compromissos na interface
        lista_compromissos.delete(0, tk.END)
        for c in compromissos:
            lista_compromissos.insert(tk.END, f"{c['compromisso']} | {c['data']} | {c['descricao']}")
        
        # Limpar os campos
        entry_compromisso.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

# Função para remover compromisso
def remover_compromisso():
    try:
        selecionado = lista_compromissos.curselection()
        if selecionado:
            compromissos = carregar_compromissos()
            compromisso = lista_compromissos.get(selecionado)
            compromisso_parts = compromisso.split(" | ")
            compromisso_str = {
                "compromisso": compromisso_parts[0],
                "data": compromisso_parts[1],
                "descricao": compromisso_parts[2]
            }
            
            compromissos.remove(compromisso_str)

            # Salvar a lista de compromissos no arquivo JSON
            with open("compromissos.json", "w") as arquivo:
                json.dump(compromissos, arquivo, indent=4)

            # Atualizar a lista de compromissos na interface
            lista_compromissos.delete(selecionado)
        else:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione um compromisso para remover.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para atualizar a lista de compromissos na interface
def atualizar_lista_compromissos():
    compromissos = carregar_compromissos()
    lista_compromissos.delete(0, tk.END)
    for c in compromissos:
        lista_compromissos.insert(tk.END, f"{c['compromisso']} | {c['data']} | {c['descricao']}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Agenda Pessoal")
janela.geometry("600x500")
janela.config(bg="#ADD8E6")  # Cor de fundo azul claro

# Label e campos de entrada
label_compromisso = tk.Label(janela, text="Compromisso:", bg="#ADD8E6", fg="black", font=("Arial", 12))
label_compromisso.grid(row=0, column=0, padx=10, pady=5)
entry_compromisso = tk.Entry(janela, width=30, font=("Arial", 12))
entry_compromisso.grid(row=0, column=1, padx=10, pady=5)

label_data = tk.Label(janela, text="Data (DD/MM/AAAA):", bg="#ADD8E6", fg="black", font=("Arial", 12))
label_data.grid(row=1, column=0, padx=10, pady=5)
entry_data = tk.Entry(janela, width=30, font=("Arial", 12))
entry_data.grid(row=1, column=1, padx=10, pady=5)

label_descricao = tk.Label(janela, text="Descrição:", bg="#ADD8E6", fg="black", font=("Arial", 12))
label_descricao.grid(row=2, column=0, padx=10, pady=5)
entry_descricao = tk.Entry(janela, width=30, font=("Arial", 12))
entry_descricao.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_salvar = tk.Button(janela, text="Salvar", command=salvar_compromissos, bg="#87CEFA", fg="black", font=("Arial", 12))
btn_salvar.grid(row=3, column=0, padx=10, pady=10)

btn_remover = tk.Button(janela, text="Remover", command=remover_compromisso, bg="#87CEFA", fg="black", font=("Arial", 12))
btn_remover.grid(row=3, column=1, padx=10, pady=10)

# Lista de compromissos
lista_compromissos = tk.Listbox(janela, width=50, height=10, font=("Arial", 12))
lista_compromissos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Atualizar a lista de compromissos ao iniciar
atualizar_lista_compromissos()

# Iniciar o loop da interface gráfica
janela.mainloop()