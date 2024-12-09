import customtkinter as ctk
import time
from threading import Thread

class TimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cronômetro e Temporizador")
        self.geometry("400x300")

        self.running = False
        self.time_left = 0

        # Interface
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = ctk.CTkLabel(self, text="Cronômetro e Temporizador", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Exibição de tempo
        self.time_display = ctk.CTkLabel(self, text="00:00:00", font=("Arial", 30))
        self.time_display.pack(pady=20)

        # Botões
        self.start_button = ctk.CTkButton(self, text="Iniciar", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.pause_button = ctk.CTkButton(self, text="Pausar", command=self.pause_timer)
        self.pause_button.pack(pady=5)

        self.reset_button = ctk.CTkButton(self, text="Redefinir", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        # Entrada para definir o tempo (em segundos)
        self.time_entry = ctk.CTkEntry(self, placeholder_text="Definir tempo (segundos)")
        self.time_entry.pack(pady=10, padx=20, fill="x")

        # Alternância de tema
        self.theme_switch = ctk.CTkSwitch(self, text="Tema Claro/Escuro", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def start_timer(self):
        if not self.running:
            if self.time_left == 0:
                try:
                    self.time_left = int(self.time_entry.get())
                except ValueError:
                    self.time_display.configure(text="Entrada Inválida")
                    return

            self.running = True
            self.time_entry.delete(0, "end")
            self.update_timer()

    def update_timer(self):
        def timer_thread():
            while self.running and self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                hours, mins = divmod(mins, 60)
                self.time_display.configure(text=f"{hours:02}:{mins:02}:{secs:02}")
                time.sleep(1)
                self.time_left -= 1

            if self.time_left == 0 and self.running:
                self.time_display.configure(text="Tempo Esgotado!")
                self.running = False

        Thread(target=timer_thread, daemon=True).start()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.time_display.configure(text="00:00:00")

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()