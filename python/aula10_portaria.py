import sqlite3
from datetime import datetime
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import logging
import os

# Configuração do log
logging.basicConfig(
    filename="portaria.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configuração do tema
ctk.set_appearance_mode("System")  # ou "Light", "Dark"
ctk.set_default_color_theme("blue")  # ou "green", "dark-blue"

# Classe principal
class PortariaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Controle de Portaria")
        self.geometry("800x600")
        
        # Inicializa o banco de dados
        self.init_db()

        # Frames
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.build_main_menu()

    def init_db(self):
        try:
            db_exists = os.path.exists("portaria.db")
            self.conn = sqlite3.connect("portaria.db")
            self.cursor = self.conn.cursor()

            if not db_exists:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS autorizados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    matricula TEXT UNIQUE NOT NULL
                )
                """)
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS registros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    matricula TEXT NOT NULL,
                    data_hora TEXT NOT NULL,
                    tipo TEXT NOT NULL
                )
                """)
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS ocorrencias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    data_hora TEXT NOT NULL
                )
                """)
                self.conn.commit()
                messagebox.showinfo("Banco de Dados", "Banco de dados criado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao inicializar o banco de dados: {e}")
            messagebox.showerror("Erro", "Não foi possível inicializar o banco de dados. Verifique os logs.")

    def build_main_menu(self):
        self.clear_frame(self.main_frame)

        title = ctk.CTkLabel(self.main_frame, text="Sistema de Portaria", font=("Arial", 24))
        title.pack(pady=20)

        validate_button = ctk.CTkButton(self.main_frame, text="Validar Entrada/Saída", command=self.validate_access)
        validate_button.pack(pady=10)

        manage_people_button = ctk.CTkButton(self.main_frame, text="Gerenciar Pessoas Autorizadas", command=self.manage_people)
        manage_people_button.pack(pady=10)

        manage_occurrences_button = ctk.CTkButton(self.main_frame, text="Registrar Ocorrências", command=self.manage_occurrences)
        manage_occurrences_button.pack(pady=10)

    def validate_access(self):
        self.clear_frame(self.main_frame)

        def process_access():
            try:
                matricula = matricula_entry.get()
                self.cursor.execute("SELECT nome FROM autorizados WHERE matricula = ?", (matricula,))
                result = self.cursor.fetchone()

                if result:
                    nome = result[0]
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.cursor.execute("INSERT INTO registros (nome, matricula, data_hora, tipo) VALUES (?, ?, ?, ?)",
                                        (nome, matricula, now, "Entrada/Saída"))
                    self.conn.commit()
                    messagebox.showinfo("Sucesso", f"Acesso registrado para {nome}.")
                else:
                    if messagebox.askyesno("Erro", "Matrícula não autorizada. Deseja registrar uma ocorrência?"):
                        self.register_occurrence()
            except Exception as e:
                logging.error(f"Erro ao validar acesso: {e}")
                messagebox.showerror("Erro", "Ocorreu um erro ao validar o acesso. Verifique os logs.")

        title = ctk.CTkLabel(self.main_frame, text="Validar Entrada/Saída", font=("Arial", 24))
        title.pack(pady=20)

        matricula_label = ctk.CTkLabel(self.main_frame, text="Matrícula:")
        matricula_label.pack(pady=10)
        matricula_entry = ctk.CTkEntry(self.main_frame)
        matricula_entry.pack(pady=10)

        validate_button = ctk.CTkButton(self.main_frame, text="Validar", command=process_access)
        validate_button.pack(pady=10)

        back_button = ctk.CTkButton(self.main_frame, text="Voltar", command=self.build_main_menu)
        back_button.pack(pady=10)

    def manage_people(self):
        self.clear_frame(self.main_frame)

        def add_person():
            try:
                nome = name_entry.get()
                matricula = matricula_entry.get()
                self.cursor.execute("INSERT INTO autorizados (nome, matricula) VALUES (?, ?)", (nome, matricula))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
                refresh_list()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Matrícula já cadastrada.")
            except Exception as e:
                logging.error(f"Erro ao adicionar pessoa: {e}")
                messagebox.showerror("Erro", "Erro ao adicionar pessoa. Verifique os logs.")

        def delete_person():
            try:
                selected = listbox.get(tk.ACTIVE)
                if not selected:
                    messagebox.showwarning("Atenção", "Selecione um item para excluir.")
                    return
                matricula = selected.split(" - ")[1]
                self.cursor.execute("DELETE FROM autorizados WHERE matricula = ?", (matricula,))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Pessoa excluída com sucesso!")
                refresh_list()
            except Exception as e:
                logging.error(f"Erro ao excluir pessoa: {e}")
                messagebox.showerror("Erro", "Erro ao excluir pessoa. Verifique os logs.")

        def refresh_list():
            try:
                listbox.delete(0, tk.END)
                self.cursor.execute("SELECT nome, matricula FROM autorizados")
                for pessoa in self.cursor.fetchall():
                    listbox.insert(tk.END, f"{pessoa[0]} - {pessoa[1]}")
            except Exception as e:
                logging.error(f"Erro ao atualizar lista de pessoas: {e}")
                messagebox.showerror("Erro", "Erro ao atualizar lista. Verifique os logs.")

        title = ctk.CTkLabel(self.main_frame, text="Gerenciar Pessoas Autorizadas", font=("Arial", 24))
        title.pack(pady=20)

        name_label = ctk.CTkLabel(self.main_frame, text="Nome:")
        name_label.pack(pady=5)
        name_entry = ctk.CTkEntry(self.main_frame)
        name_entry.pack(pady=5)

        matricula_label = ctk.CTkLabel(self.main_frame, text="Matrícula:")
        matricula_label.pack(pady=5)
        matricula_entry = ctk.CTkEntry(self.main_frame)
        matricula_entry.pack(pady=5)

        add_button = ctk.CTkButton(self.main_frame, text="Adicionar", command=add_person)
        add_button.pack(pady=10)

        listbox = tk.Listbox(self.main_frame, height=10)
        listbox.pack(pady=10, fill="both", expand=True)

        delete_button = ctk.CTkButton(self.main_frame, text="Excluir Selecionado", command=delete_person)
        delete_button.pack(pady=10)

        back_button = ctk.CTkButton(self.main_frame, text="Voltar", command=self.build_main_menu)
        back_button.pack(pady=10)

        refresh_list()

    def manage_occurrences(self):
        self.clear_frame(self.main_frame)

        def add_occurrence():
            try:
                descricao = description_entry.get()
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.cursor.execute("INSERT INTO ocorrencias (descricao, data_hora) VALUES (?, ?)", (descricao, now))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Ocorrência registrada com sucesso!")
                refresh_list()
            except Exception as e:
                logging.error(f"Erro ao registrar ocorrência: {e}")
                messagebox.showerror("Erro", "Erro ao registrar ocorrência. Verifique os logs.")

        def refresh_list():
            try:
                listbox.delete(0, tk.END)
                self.cursor.execute("SELECT descricao, data_hora FROM ocorrencias")
                for ocorrencia in self.cursor.fetchall():
                    listbox.insert(tk.END, f"{ocorrencia[0]} - {ocorrencia[1]}")
            except Exception as e:
                logging.error(f"Erro ao atualizar lista de ocorrências: {e}")
                messagebox.showerror("Erro", "Erro ao atualizar lista. Verifique os logs.")

        title = ctk.CTkLabel(self.main_frame, text="Registrar Ocorrências", font=("Arial", 24))
        title.pack(pady=20)

        description_label = ctk.CTkLabel(self.main_frame, text="Descrição:")
        description_label.pack(pady=5)
        description_entry = ctk.CTkEntry(self.main_frame)
        description_entry.pack(pady=5)

        add_button = ctk.CTkButton(self.main_frame, text="Adicionar", command=add_occurrence)
        add_button.pack(pady=10)

        listbox = tk.Listbox(self.main_frame, height=10)
        listbox.pack(pady=10, fill="both", expand=True)

        back_button = ctk.CTkButton(self.main_frame, text="Voltar", command=self.build_main_menu)
        back_button.pack(pady=10)

        refresh_list()

    def register_occurrence(self):
        self.clear_frame(self.main_frame)

        title = ctk.CTkLabel(self.main_frame, text="Registrar Ocorrência", font=("Arial", 24))
        title.pack(pady=20)

        description_label = ctk.CTkLabel(self.main_frame, text="Descrição da Ocorrência:")
        description_label.pack(pady=5)

        description_entry = ctk.CTkEntry(self.main_frame)
        description_entry.pack(pady=5)

        def submit_occurrence():
            try:
                descricao = description_entry.get()
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.cursor.execute("INSERT INTO ocorrencias (descricao, data_hora) VALUES (?, ?)", (descricao, now))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Ocorrência registrada com sucesso!")
                self.build_main_menu()
            except Exception as e:
                logging.error(f"Erro ao registrar ocorrência: {e}")
                messagebox.showerror("Erro", "Ocorreu um erro ao registrar a ocorrência. Verifique os logs.")

        submit_button = ctk.CTkButton(self.main_frame, text="Registrar", command=submit_occurrence)
        submit_button.pack(pady=10)

        back_button = ctk.CTkButton(self.main_frame, text="Voltar", command=self.build_main_menu)
        back_button.pack(pady=10)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = PortariaApp()
    app.mainloop()