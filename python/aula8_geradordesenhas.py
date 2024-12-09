import customtkinter as ctk
import random
import string

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerador de Senhas Seguras")
        self.geometry("400x300")

        # Critérios de senha
        self.include_numbers = ctk.BooleanVar(value=True)
        self.include_letters = ctk.BooleanVar(value=True)
        self.include_symbols = ctk.BooleanVar(value=True)

        # Interface
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = ctk.CTkLabel(self, text="Gerador de Senhas Seguras", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Checkboxes para critérios
        self.numbers_checkbox = ctk.CTkCheckBox(
            self, text="Incluir Números", variable=self.include_numbers
        )
        self.numbers_checkbox.pack(pady=5)

        self.letters_checkbox = ctk.CTkCheckBox(
            self, text="Incluir Letras", variable=self.include_letters
        )
        self.letters_checkbox.pack(pady=5)

        self.symbols_checkbox = ctk.CTkCheckBox(
            self, text="Incluir Símbolos", variable=self.include_symbols
        )
        self.symbols_checkbox.pack(pady=5)

        # Botão para gerar senha
        self.generate_button = ctk.CTkButton(self, text="Gerar Senha", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Entrada de texto para senha gerada
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Senha Gerada")
        self.password_entry.pack(pady=10, padx=20, fill="x")

        # Botão para copiar senha
        self.copy_button = ctk.CTkButton(self, text="Copiar Senha", command=self.copy_password)
        self.copy_button.pack(pady=10)

        # Alternância de tema
        self.theme_switch = ctk.CTkSwitch(self, text="Tema Claro/Escuro", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def generate_password(self):
        # Critérios de geração de senha
        characters = ""
        if self.include_numbers.get():
            characters += string.digits
        if self.include_letters.get():
            characters += string.ascii_letters
        if self.include_symbols.get():
            characters += string.punctuation

        if not characters:
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, "Selecione ao menos um critério")
            return

        # Gerar senha aleatória
        password = "".join(random.choices(characters, k=12))
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

    def copy_password(self):
        # Copiar senha para a área de transferência
        self.clipboard_clear()
        self.clipboard_append(self.password_entry.get())
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, "Senha copiada!")

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()