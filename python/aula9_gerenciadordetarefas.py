import customtkinter as ctk

# Configurar o tema padrão
ctk.set_appearance_mode("System")  # Usa o tema do sistema (pode ser "Dark" ou "Light")
ctk.set_default_color_theme("blue")

class TaskManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciador de Tarefas")
        self.geometry("400x500")

        # Lista de tarefas
        self.tasks = []

        # Interface principal
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = ctk.CTkLabel(self, text="Gerenciador de Tarefas", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Entrada de texto
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Digite uma nova tarefa")
        self.task_entry.pack(pady=10, padx=20, fill="x")

        # Botão de adicionar tarefa
        self.add_button = ctk.CTkButton(self, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=10)

        # Lista de tarefas
        self.task_listbox = ctk.CTkTextbox(self, height=200, wrap="none")
        self.task_listbox.pack(pady=10, padx=20, fill="both", expand=True)
        self.task_listbox.configure(state="disabled")

        # Botão de remover tarefa
        self.remove_button = ctk.CTkButton(self, text="Remover Tarefa Selecionada", command=self.remove_task)
        self.remove_button.pack(pady=10)

        # Alternância de tema
        self.theme_switch = ctk.CTkSwitch(self, text="Tema Claro/Escuro", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, "end")

    def update_task_list(self):
        self.task_listbox.configure(state="normal")
        self.task_listbox.delete("1.0", "end")
        for idx, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert("end", f"{idx}. {task}\n")
        self.task_listbox.configure(state="disabled")

    def remove_task(self):
        # Remover a tarefa selecionada (última linha da lista)
        lines = self.task_listbox.get("1.0", "end").strip().split("\n")
        if lines:
            last_task = lines[-1]
            task_number = int(last_task.split(".")[0]) - 1
            if 0 <= task_number < len(self.tasks):
                self.tasks.pop(task_number)
                self.update_task_list()

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()