import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import os

# Função para salvar o compromisso em um arquivo JSON
def salvar_compromisso():
    compromisso = entry_compromisso.get()
    data = cal.get_date()
    descricao = entry_descricao.get()

    if compromisso and descricao:
        novo_registro = {
            "compromisso": compromisso,
            "data": data,
            "descricao": descricao
        }

        if os.path.exists('agenda.json'):
            with open('agenda.json', 'r') as file:
                registros = json.load(file)
        else:
            registros = []

        registros.append(novo_registro)

        with open('agenda.json', 'w') as file:
            json.dump(registros, file, indent=4)

        messagebox.showinfo("Sucesso", "Compromisso salvo com sucesso!")
        limpar_campos()
        atualizar_lista_compromissos()

    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Função para remover um compromisso
def remover_compromisso():
    selected = listbox.curselection()
    if selected:
        compromisso_selecionado = listbox.get(selected)
        data = compromisso_selecionado.split(" - ")[-1]
        
        with open('agenda.json', 'r') as file:
            registros = json.load(file)

        registros_filtrados = [registro for registro in registros if registro["data"] != data]

        with open('agenda.json', 'w') as file:
            json.dump(registros_filtrados, file, indent=4)

        messagebox.showinfo("Sucesso", f"Compromisso para {data} removido com sucesso!")
        atualizar_lista_compromissos()

    else:
        messagebox.showwarning("Erro", "Selecione um compromisso para remover!")

# Função para limpar os campos após salvar
def limpar_campos():
    entry_compromisso.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)

# Função para atualizar a lista de compromissos na interface
def atualizar_lista_compromissos():
    listbox.delete(0, tk.END)
    
    if os.path.exists('agenda.json'):
        with open('agenda.json', 'r') as file:
            registros = json.load(file)
        
        for registro in registros:
            compromisso_str = f"{registro['compromisso']} - {registro['data']}"
            listbox.insert(tk.END, compromisso_str)

# Criando a janela principal
root = tk.Tk()
root.title("Agenda Pessoal")
root.geometry("500x400")
root.config(bg="lightblue")

# Título
label_titulo = tk.Label(root, text="Agenda Pessoal", font=("Arial", 18), bg="lightblue")
label_titulo.pack(pady=10)

# Campo para compromisso
label_compromisso = tk.Label(root, text="Compromisso:", bg="lightblue")
label_compromisso.pack(pady=5)
entry_compromisso = tk.Entry(root, width=40)
entry_compromisso.pack(pady=5)

# Calendário
label_data = tk.Label(root, text="Data:", bg="lightblue")
label_data.pack(pady=5)
cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=5)

# Campo para descrição do compromisso
label_descricao = tk.Label(root, text="Descrição:", bg="lightblue")
label_descricao.pack(pady=5)
entry_descricao = tk.Entry(root, width=40)
entry_descricao.pack(pady=5)

# Botões de ação
frame_botoes = tk.Frame(root, bg="lightblue")
frame_botoes.pack(pady=10)

botao_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_compromisso)
botao_salvar.pack(side=tk.LEFT, padx=10)

botao_remover = tk.Button(frame_botoes, text="Remover", command=remover_compromisso)
botao_remover.pack(side=tk.LEFT, padx=10)

# Lista de compromissos
listbox_label = tk.Label(root, text="Compromissos:", bg="lightblue")
listbox_label.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Atualiza a lista de compromissos na interface ao iniciar
atualizar_lista_compromissos()

# Inicia o loop da interface gráfica
root.mainloop()
