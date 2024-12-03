import customtkinter as ctk
from tkinter import filedialog, messagebox, Menu
import os

class TextEditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Editor de texto básico")
        self.geometry("800x600")

        self.file_patch = None
        # Configuração da interface
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # Área de texto
        self.text_area = ctk.CTkTextbox(self, wrap="word", font=("Arial, 14"))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)        

        #Alternância de tema
        self.theme_switch = ctk.CTkSwitch(self, text="Tema Claro/Escuro", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def create_menu(self):
        # Menubar padrão do Tkinter
        self.menu_bar = Menu(self)

        # Menu Arquivo
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Salvar como", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit)

        self.menu_bar.add_cascade(label="Arquivo", menu= file_menu)

        # Associar menubar á janela
        self.config(menu=self.menu_bar)
    
    def new_file(self):
        if self.confirm_discard_changes():
            file_path = filedialog.askopenfilename(filetypes=[
                ("Arquivos de texto", "*txt"),
                ("Markdown, ""*.md")
                ("Todos os Arquivos", "*.*")
            ])
            if file_path:
                try:
                    with open(file_path, "r", encondig="ut-8") as file:
                        content = file.read()
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", content)
                    self.file_path = file_path
                    self.title(f"Editor de texto básico - {os.path.basename(file_path)}")

                except Exception as e:
                    messagebox.showerror("Erro ao abrir arquivo", str(e))
def save_file (self):                                                                
